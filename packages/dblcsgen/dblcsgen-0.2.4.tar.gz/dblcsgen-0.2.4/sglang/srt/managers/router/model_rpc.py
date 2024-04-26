import asyncio
import logging
import multiprocessing
import time
import warnings
from concurrent.futures import ThreadPoolExecutor
from typing import List

import rpyc
import torch
from rpyc.utils.classic import obtain
from rpyc.utils.server import ThreadedServer
from sglang.srt.constrained.fsm_cache import FSMCache
from sglang.srt.constrained.jump_forward import JumpForwardCache
from sglang.srt.hf_transformers_utils import get_processor, get_tokenizer
from sglang.srt.managers.io_struct import (
    BatchTokenIDOut,
    FlushCacheReq,
    TokenizedGenerateReqInput,
)
from sglang.srt.managers.router.infer_batch import Batch, ForwardMode, Req
from sglang.srt.managers.router.model_runner import ModelRunner
from sglang.srt.managers.router.radix_cache import RadixCache
from sglang.srt.managers.router.scheduler import Scheduler
from sglang.srt.model_config import ModelConfig
from sglang.srt.server_args import PortArgs, ServerArgs
from sglang.srt.utils import (
    get_exception_traceback,
    get_int_token_logit_bias,
    is_multimodal_model,
    set_random_seed,
)
from vllm.logger import _default_handler as vllm_default_handler

logger = logging.getLogger("model_rpc")


class ModelRpcServer:
    def __init__(
        self,
        tp_rank: int,
        server_args: ServerArgs,
        port_args: PortArgs,
    ):
        server_args, port_args = [obtain(x) for x in [server_args, port_args]]

        # Copy arguments
        self.tp_rank = tp_rank
        self.tp_size = server_args.tp_size
        self.schedule_heuristic = server_args.schedule_heuristic
        self.disable_regex_jump_forward = server_args.disable_regex_jump_forward
        vllm_default_handler.setLevel(
            level=getattr(logging, server_args.log_level.upper())
        )

        # Init model and tokenizer
        self.model_config = ModelConfig(
            server_args.model_path,
            server_args.trust_remote_code,
            context_length=server_args.context_length,
        )

        # for model end global settings
        server_args_dict = {
            "enable_flashinfer": server_args.enable_flashinfer,
            "attention_reduce_in_fp32": server_args.attention_reduce_in_fp32,
        }

        self.model_runner = ModelRunner(
            model_config=self.model_config,
            mem_fraction_static=server_args.mem_fraction_static,
            tp_rank=tp_rank,
            tp_size=server_args.tp_size,
            nccl_port=port_args.nccl_port,
            load_format=server_args.load_format,
            trust_remote_code=server_args.trust_remote_code,
            server_args_dict=server_args_dict,
        )
        if is_multimodal_model(server_args.model_path):
            self.processor = get_processor(
                server_args.tokenizer_path,
                tokenizer_mode=server_args.tokenizer_mode,
                trust_remote_code=server_args.trust_remote_code,
            )
            self.tokenizer = self.processor.tokenizer
        else:
            self.tokenizer = get_tokenizer(
                server_args.tokenizer_path,
                tokenizer_mode=server_args.tokenizer_mode,
                trust_remote_code=server_args.trust_remote_code,
            )
        self.max_total_num_token = self.model_runner.max_total_num_token
        self.max_num_running_seq = self.max_total_num_token // 2
        self.max_prefill_num_token = max(
            self.model_config.context_len,
            (
                self.max_total_num_token // 6
                if server_args.max_prefill_num_token is None
                else server_args.max_prefill_num_token
            ),
        )
        self.int_token_logit_bias = torch.tensor(
            get_int_token_logit_bias(self.tokenizer, self.model_config.vocab_size)
        )
        set_random_seed(server_args.random_seed)
        logger.info(
            f"Rank {self.tp_rank}: "
            f"max_total_num_token={self.max_total_num_token}, "
            f"max_prefill_num_token={self.max_prefill_num_token}, "
            f"context_len={self.model_config.context_len}, "
        )
        logger.info(server_args.get_optional_modes_logging())

        # Init cache
        self.tree_cache = RadixCache(server_args.disable_radix_cache)
        self.tree_cache_metrics = {"total": 0, "hit": 0}
        self.scheduler = Scheduler(
            self.schedule_heuristic,
            self.max_num_running_seq,
            self.max_prefill_num_token,
            self.max_total_num_token,
            self.tree_cache,
        )
        self.req_to_token_pool = self.model_runner.req_to_token_pool
        self.token_to_kv_pool = self.model_runner.token_to_kv_pool

        # Init running status
        self.forward_queue: List[Req] = []
        self.running_batch: Batch = None
        self.out_pyobjs = []
        self.decode_forward_ct = 0
        self.stream_interval = server_args.stream_interval

        # Init the FSM cache for constrained generation
        self.regex_fsm_cache = FSMCache(
            server_args.tokenizer_path,
            {
                "tokenizer_mode": server_args.tokenizer_mode,
                "trust_remote_code": server_args.trust_remote_code,
            },
        )
        self.jump_forward_cache = JumpForwardCache()

        # Init new token estimation
        self.new_token_ratio = min(0.4 * server_args.schedule_conservativeness, 1.0)
        self.min_new_token_ratio = min(0.2 * server_args.schedule_conservativeness, 1.0)
        self.new_token_ratio_step = (0.0001, 0.05)  # (down, up)

    def flush_cache(self):
        if len(self.forward_queue) == 0 and (
            self.running_batch is None or len(self.running_batch.reqs) == 0
        ):
            self.tree_cache.reset()
            self.tree_cache_metrics = {"total": 0, "hit": 0}
            self.regex_fsm_cache.reset()
            self.req_to_token_pool.clear()
            self.token_to_kv_pool.clear()
            torch.cuda.empty_cache()
            logger.info("Cache flushed successfully!")
        else:
            warnings.warn(
                "Cache not flushed because there are pending requests. "
                f"#queue-req: {len(self.forward_queue)}, "
                f"#running-req: {0 if self.running_batch is None else len(self.running_batch.reqs)}"
            )

    def exposed_step(self, recv_reqs):
        if self.tp_size != 1:
            recv_reqs = obtain(recv_reqs)

        try:
            # Recv requests
            for recv_req in recv_reqs:
                if isinstance(recv_req, TokenizedGenerateReqInput):
                    self.handle_generate_request(recv_req)
                elif isinstance(recv_req, FlushCacheReq):
                    self.flush_cache()
                else:
                    raise ValueError(f"Invalid request: {recv_req}")

            # Forward
            self.forward_step()
        except Exception:
            logger.error("Exception in ModelRpcClient:\n" + get_exception_traceback())

        # Return results
        ret = self.out_pyobjs
        self.out_pyobjs = []
        return ret

    @torch.inference_mode()
    def forward_step(self):
        new_batch = self.get_new_fill_batch()

        if new_batch is not None:
            # Run new fill batch
            self.forward_fill_batch(new_batch)

            if not new_batch.is_empty():
                if self.running_batch is None:
                    self.running_batch = new_batch
                else:
                    self.running_batch.merge(new_batch)
        else:
            # Run decode batch
            if self.running_batch is not None:
                # Run a few decode batches continuously for reducing overhead
                for _ in range(10):
                    self.forward_decode_batch(self.running_batch)

                    if self.running_batch.is_empty():
                        self.running_batch = None
                        break

                    if self.out_pyobjs and self.running_batch.reqs[0].stream:
                        break

                    if self.running_batch is not None and self.tp_rank == 0:
                        if self.decode_forward_ct % 40 == 0:
                            num_used = self.max_total_num_token - (
                                self.token_to_kv_pool.available_size()
                                + self.tree_cache.evictable_size()
                            )
                            logger.info(
                                f"#running-req: {len(self.running_batch.reqs)}, "
                                f"#token: {num_used}, "
                                f"token usage: {num_used / self.max_total_num_token:.2f}, "
                                f"#queue-req: {len(self.forward_queue)}"
                            )
            else:
                # check the available size
                available_size = (
                    self.token_to_kv_pool.available_size()
                    + self.tree_cache.evictable_size()
                )
                if available_size != self.max_total_num_token:
                    warnings.warn(
                        "Warning: "
                        f"available_size={available_size}, max_total_num_token={self.max_total_num_token}\n"
                        "KV cache pool leak detected!"
                    )

    def handle_generate_request(
        self,
        recv_req: TokenizedGenerateReqInput,
    ):
        req = Req(recv_req.rid, recv_req.input_text, recv_req.input_ids)
        req.pixel_values = recv_req.pixel_values
        if req.pixel_values is not None:
            req.pad_value = [
                (recv_req.image_hash) % self.model_config.vocab_size,
                (recv_req.image_hash >> 16) % self.model_config.vocab_size,
                (recv_req.image_hash >> 32) % self.model_config.vocab_size,
                (recv_req.image_hash >> 64) % self.model_config.vocab_size,
            ]
            req.image_size = recv_req.image_size
            req.input_ids, req.image_offset = self.model_runner.model.pad_input_ids(
                req.input_ids, req.pad_value, req.pixel_values.shape, req.image_size
            )
        req.sampling_params = recv_req.sampling_params
        req.return_logprob = recv_req.return_logprob
        req.logprob_start_len = recv_req.logprob_start_len
        req.top_logprobs_num = recv_req.top_logprobs_num
        req.stream = recv_req.stream
        req.tokenizer = self.tokenizer

        # Init regex fsm
        if req.sampling_params.regex is not None:
            req.regex_fsm = self.regex_fsm_cache.query(req.sampling_params.regex)
            if not self.disable_regex_jump_forward:
                req.jump_forward_map = self.jump_forward_cache.query(
                    req.sampling_params.regex
                )

        # Truncate long prompts
        req.input_ids = req.input_ids[: self.model_config.context_len - 1]
        req.sampling_params.max_new_tokens = min(
            req.sampling_params.max_new_tokens,
            self.model_config.context_len - 1 - len(req.input_ids),
            self.max_total_num_token - 128 - len(req.input_ids),
        )
        self.forward_queue.append(req)

    def get_new_fill_batch(self):
        if (
            self.running_batch is not None
            and len(self.running_batch.reqs) > self.max_num_running_seq
        ):
            return None

        for req in self.forward_queue:
            prefix_indices, last_node = self.tree_cache.match_prefix(req.input_ids)
            if req.return_logprob:
                prefix_indices = prefix_indices[: req.logprob_start_len]
            req.extend_input_len = len(req.input_ids) - len(prefix_indices)
            req.prefix_indices = prefix_indices
            req.last_node = last_node

        # Get priority queue
        self.forward_queue = self.scheduler.get_priority_queue(self.forward_queue)

        # Add requests if there is available space
        can_run_list = []
        new_batch_total_tokens = 0
        new_batch_input_tokens = 0

        available_size = (
            self.token_to_kv_pool.available_size() + self.tree_cache.evictable_size()
        )
        if self.running_batch:
            available_size -= sum(
                [
                    (r.max_new_tokens() - len(r.output_ids)) * self.new_token_ratio
                    for r in self.running_batch.reqs
                ]
            )

        for req in self.forward_queue:
            if req.return_logprob:
                # Need at least two tokens to compute normalized logprob
                if req.extend_input_len < 2:
                    delta = 2 - req.extend_input_len
                    req.extend_input_len += delta
                    req.prefix_indices = req.prefix_indices[:-delta]
                    if req.image_offset is not None:
                        req.image_offset += delta
            if req.extend_input_len == 0 and req.max_new_tokens() > 0:
                # Need at least one token to compute logits
                req.extend_input_len = 1
                req.prefix_indices = req.prefix_indices[:-1]
                if req.image_offset is not None:
                    req.image_offset += 1

            if (
                req.extend_input_len + req.max_new_tokens() + new_batch_total_tokens
                < available_size
                and req.extend_input_len + new_batch_input_tokens
                < self.max_prefill_num_token
            ):
                delta = self.tree_cache.inc_ref_counter(req.last_node)
                available_size += delta

                if not (
                    req.extend_input_len + req.max_new_tokens() + new_batch_total_tokens
                    < available_size
                ):
                    # Undo the insertion
                    delta = self.tree_cache.dec_ref_counter(req.last_node)
                    available_size += delta
                    break
                else:
                    # Add this request to the running batch
                    self.token_to_kv_pool.add_refs(req.prefix_indices)
                    can_run_list.append(req)
                    new_batch_total_tokens += (
                        req.extend_input_len + req.max_new_tokens()
                    )
                    new_batch_input_tokens += req.extend_input_len
            else:
                break
        if len(can_run_list) == 0:
            return None

        if self.tp_rank == 0:
            running_req = (
                0 if self.running_batch is None else len(self.running_batch.reqs)
            )
            hit_tokens = sum(len(x.prefix_indices) for x in can_run_list)
            self.tree_cache_metrics["total"] += (
                hit_tokens + new_batch_input_tokens
            ) / 10**9
            self.tree_cache_metrics["hit"] += hit_tokens / 10**9
            tree_cache_hit_rate = (
                self.tree_cache_metrics["hit"] / self.tree_cache_metrics["total"]
            )
            logger.info(
                f"new fill batch. #seq: {len(can_run_list)}. "
                f"#cached_token: {hit_tokens}. "
                f"#new_token: {new_batch_input_tokens}. "
                f"#remaining_req: {len(self.forward_queue) - len(can_run_list)}. "
                f"#running_req: {running_req}. "
                f"tree_cache_hit_rate: {100.0 * tree_cache_hit_rate:.2f}%."
            )
            logger.debug(
                f"fsm_cache_hit_rate: {100.0 * self.regex_fsm_cache.get_cache_hit_rate():.2f}%. "
                f"fsm_cache_avg_init_time: {self.regex_fsm_cache.get_avg_init_time():.2f}s. "
                f"ff_cache_hit_rate: {100.0 * self.jump_forward_cache.get_cache_hit_rate():.2f}%. "
                f"ff_cache_avg_init_time: {self.jump_forward_cache.get_avg_init_time():.2f}s. "
            )

        new_batch = Batch.init_new(
            can_run_list,
            self.req_to_token_pool,
            self.token_to_kv_pool,
            self.tree_cache,
        )
        self.forward_queue = [x for x in self.forward_queue if x not in can_run_list]
        return new_batch

    def forward_fill_batch(self, batch: Batch):
        # Build batch tensors
        batch.prepare_for_extend(
            self.model_config.vocab_size, self.int_token_logit_bias
        )

        prefill_token_logprobs = None
        if batch.extend_num_tokens != 0:
            # Forward
            logits, (
                prefill_token_logprobs,
                prefill_top_logprobs,
                decode_top_logprobs,
                normalized_prompt_logprobs,
                last_logprobs,
            ) = self.model_runner.forward(batch, ForwardMode.EXTEND)
            if prefill_token_logprobs is not None:
                prefill_token_logprobs = prefill_token_logprobs.cpu().tolist()
                normalized_prompt_logprobs = normalized_prompt_logprobs.cpu().tolist()

            next_token_ids, _ = batch.sample(logits)
            next_token_ids = next_token_ids.cpu().tolist()
        else:
            next_token_ids = [self.tokenizer.eos_token_id] * len(batch.reqs)
            (
                logits,
                prefill_token_logprobs,
                normalized_prompt_logprobs,
                last_logprobs,
            ) = (None,) * 4

        # Only batch transfer the selected logprobs of the next token to CPU to reduce overhead.
        reqs = batch.reqs
        last_token_logprobs = None
        if last_logprobs is not None:
            last_token_logprobs = (
                last_logprobs[torch.arange(len(reqs)), next_token_ids].cpu().tolist()
            )

        # Check finish condition
        pt = 0
        for i, req in enumerate(reqs):
            req.completion_tokens_wo_jump_forward += 1
            req.output_ids = [next_token_ids[i]]
            req.check_finished()

            if prefill_token_logprobs is not None:
                # If logprob_start_len > 0, then first logprob_start_len prompt tokens will be ignored.
                req.prefill_token_logprobs = list(
                    zip(
                        prefill_token_logprobs[pt : pt + req.extend_input_len - 1],
                        req.input_ids[-req.extend_input_len + 1 :],
                    )
                )
                if req.logprob_start_len == 0:
                    req.prefill_token_logprobs = [
                        (None, req.input_ids[0])
                    ] + req.prefill_token_logprobs
                req.decode_token_logprobs = [
                    (last_token_logprobs[i], next_token_ids[i])
                ]
                req.prefill_top_logprobs = prefill_top_logprobs[i]
                if req.logprob_start_len == 0:
                    req.prefill_top_logprobs = [None] + req.prefill_top_logprobs
                req.decode_top_logprobs = [decode_top_logprobs[i]]
                req.normalized_prompt_logprob = normalized_prompt_logprobs[i]
                pt += req.extend_input_len

        self.handle_finished_requests(batch)

    def forward_decode_batch(self, batch: Batch):
        # check if decode out of memory
        if not batch.check_decode_mem():
            old_ratio = self.new_token_ratio
            self.new_token_ratio = min(old_ratio + self.new_token_ratio_step[1], 1.0)

            retracted_reqs = batch.retract_decode()
            logger.info(
                "decode out of memory happened, "
                f"#retracted_reqs: {len(retracted_reqs)}, "
                f"#new_token_ratio: {old_ratio:.4f} -> {self.new_token_ratio:.4f}"
            )
            self.forward_queue.extend(retracted_reqs)
        else:
            self.new_token_ratio = max(
                self.new_token_ratio - self.new_token_ratio_step[0],
                self.min_new_token_ratio,
            )

        if not self.disable_regex_jump_forward:
            # check for jump-forward
            jump_forward_reqs = batch.check_for_jump_forward()

            # check for image jump-forward
            for req in jump_forward_reqs:
                if req.pixel_values is not None:
                    (
                        req.input_ids,
                        req.image_offset,
                    ) = self.model_runner.model.pad_input_ids(
                        req.input_ids,
                        req.pad_value,
                        req.pixel_values.shape,
                        req.image_size,
                    )

            self.forward_queue.extend(jump_forward_reqs)
            if batch.is_empty():
                return

        # Update batch tensors
        self.decode_forward_ct = (self.decode_forward_ct + 1) % (1 << 30)
        batch.prepare_for_decode()

        # Forward
        logits, (_, _, decode_top_logprobs, _, last_logprobs) = (
            self.model_runner.forward(batch, ForwardMode.DECODE)
        )
        next_token_ids, _ = batch.sample(logits)
        next_token_ids = next_token_ids.cpu().tolist()

        # Only batch transfer the selected logprobs of the next token to CPU to reduce overhead.
        reqs = batch.reqs
        new_token_logprobs = None
        if last_logprobs is not None:
            new_token_logprobs = last_logprobs[
                torch.arange(len(reqs)), next_token_ids
            ].tolist()

        # Check finish condition
        for i, (req, next_token_id) in enumerate(zip(reqs, next_token_ids)):
            req.completion_tokens_wo_jump_forward += 1
            req.output_ids.append(next_token_id)
            req.check_finished()

            if new_token_logprobs is not None:
                req.decode_token_logprobs.append((new_token_logprobs[i], next_token_id))
                req.decode_top_logprobs.append(decode_top_logprobs[i])

        self.handle_finished_requests(batch)

    def handle_finished_requests(self, batch: Batch):
        output_rids = []
        output_tokens = []
        output_and_jump_forward_strs = []
        output_hit_stop_str = []
        output_skip_special_tokens = []
        output_meta_info = []
        output_finished = []
        finished_indices = []
        unfinished_indices = []
        for i, req in enumerate(batch.reqs):
            if req.finished:
                finished_indices.append(i)
            else:
                unfinished_indices.append(i)

            if req.finished or (
                (
                    req.stream
                    and (
                        self.decode_forward_ct % self.stream_interval == 0
                        or len(req.output_ids) == 1
                    )
                )
            ):
                output_rids.append(req.rid)
                output_tokens.append(req.output_ids)
                output_and_jump_forward_strs.append(req.output_and_jump_forward_str)
                output_hit_stop_str.append(req.hit_stop_str)
                output_skip_special_tokens.append(
                    req.sampling_params.skip_special_tokens
                )

                meta_info = {
                    "prompt_tokens": req.prompt_tokens,
                    "completion_tokens": len(req.input_ids)
                    + len(req.output_ids)
                    - req.prompt_tokens,
                    "completion_tokens_wo_jump_forward": req.completion_tokens_wo_jump_forward,
                }
                if req.return_logprob:
                    (
                        meta_info["prefill_token_logprobs"],
                        meta_info["decode_token_logprobs"],
                        meta_info["prefill_top_logprobs"],
                        meta_info["decode_top_logprobs"],
                        meta_info["normalized_prompt_logprob"],
                    ) = (
                        req.prefill_token_logprobs,
                        req.decode_token_logprobs,
                        req.prefill_top_logprobs,
                        req.decode_top_logprobs,
                        req.normalized_prompt_logprob,
                    )
                output_meta_info.append(meta_info)
                output_finished.append(req.finished)

        # Send to detokenizer
        if output_rids:
            self.out_pyobjs.append(
                BatchTokenIDOut(
                    output_rids,
                    output_tokens,
                    output_and_jump_forward_strs,
                    output_hit_stop_str,
                    output_skip_special_tokens,
                    output_meta_info,
                    output_finished,
                )
            )

        # Remove finished reqs
        if finished_indices:
            # Update radix cache
            req_pool_indices_cpu = batch.req_pool_indices.cpu().tolist()
            for i in finished_indices:
                req = batch.reqs[i]
                req_pool_idx = req_pool_indices_cpu[i]
                token_ids = tuple(req.input_ids + req.output_ids)
                seq_len = len(token_ids) - 1
                indices = self.req_to_token_pool.req_to_token[req_pool_idx, :seq_len]
                prefix_len = self.tree_cache.insert(
                    token_ids[:seq_len], indices.clone()
                )

                self.token_to_kv_pool.free(indices[:prefix_len])
                self.req_to_token_pool.free(req_pool_idx)
                self.tree_cache.dec_ref_counter(req.last_node)

            # Update batch tensors
            if unfinished_indices:
                batch.filter_batch(unfinished_indices)
            else:
                batch.reqs = []


class ModelRpcService(rpyc.Service):
    exposed_ModelRpcServer = ModelRpcServer


class ModelRpcClient:
    def __init__(self, server_args: ServerArgs, port_args: PortArgs):
        tp_size = server_args.tp_size

        if tp_size == 1:
            # Init model
            self.model_server = ModelRpcService().exposed_ModelRpcServer(
                0, server_args, port_args
            )

            # Wrap functions
            def async_wrap(f):
                async def _func(*args, **kwargs):
                    return f(*args, **kwargs)

                return _func

            self.step = async_wrap(self.model_server.exposed_step)
        else:
            with ThreadPoolExecutor(tp_size) as executor:
                # Launch model processes
                rets = executor.map(start_model_process, port_args.model_rpc_ports)
                self.remote_services = [x[0] for x in rets]
                self.procs = [x[1] for x in rets]

                # Init model
                def init_model(i):
                    return self.remote_services[i].ModelRpcServer(
                        i, server_args, port_args
                    )

                self.model_servers = executor.map(init_model, range(tp_size))

            # Wrap functions
            def async_wrap(func_name):
                fs = [rpyc.async_(getattr(m, func_name)) for m in self.model_servers]

                async def _func(*args, **kwargs):
                    tasks = [f(*args, **kwargs) for f in fs]
                    await asyncio.gather(*[asyncio.to_thread(t.wait) for t in tasks])
                    return obtain(tasks[0].value)

                return _func

            self.step = async_wrap("step")


def _init_service(port):
    t = ThreadedServer(
        ModelRpcService(),
        port=port,
        protocol_config={"allow_pickle": True, "sync_request_timeout": 1800},
    )
    t.start()


def start_model_process(port):
    proc = multiprocessing.Process(target=_init_service, args=(port,))
    proc.start()
    time.sleep(1)

    repeat_count = 0
    while repeat_count < 20:
        try:
            con = rpyc.connect(
                "localhost",
                port,
                config={"allow_pickle": True, "sync_request_timeout": 1800},
            )
            break
        except ConnectionRefusedError:
            time.sleep(1)
        repeat_count += 1
    if repeat_count == 20:
        raise RuntimeError("init rpc env error!")

    assert proc.is_alive()
    return con.root, proc
