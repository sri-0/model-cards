---
id: qwen/qwen3-coder-next
name: Qwen3 Coder Next
owned_by: qwen
type: llm
description: Qwen3 Coder Next is Qwen's February 2026 open-weight (Apache-2.0) coding-agent model built on the hybrid Gated DeltaNet and MoE Qwen3-Next-80B-A3B base, with 80B total and 3B active parameters and a native 262,144-token context.
aliases: [Qwen/Qwen3-Coder-Next, "qwen3-coder-next:latest"]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: true
license: Apache-2.0
release_date: "2026-02-03"
pricing:
  input: 0.12
  output: 0.8
  cache_read: 0.07
benchmarks:
  intelligence_index: 9.2
  coding_index: 36.2
  agentic_index: 0.9
  omniscience_index: -62.4
  humanitys_last_exam: 10.1
  gpqa_diamond: 73.7
  scicode: 36.2
  terminal_bench_hard: 18.2
  terminal_bench_4: 0
  long_context_reasoning: 47
  ifbench: 35.2
  tau2_bench: 79.5
  output_tokens_per_second: 66
  time_to_first_token_seconds: 1.16
benchmark_variant: Qwen3 Coder Next
sources:
  - https://openrouter.ai/qwen/qwen3-coder-next
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-coder-next
  - https://huggingface.co/Qwen/Qwen3-Coder-Next
  - https://github.com/QwenLM/Qwen3-Coder
  - https://ollama.com/library/qwen3-coder-next
retrieved: "2026-10-16"
---

# Qwen3 Coder Next

## Overview
Qwen3-Coder-Next is built on Qwen3-Next-80B-A3B-Base and trained for coding agents and local development. The release date here is Artificial Analysis' 2026-02-03; the Hugging Face repository was created on 2026-01-30 and OpenRouter lists 2026-02-04. The Hugging Face card gives 80B total and 3B activated parameters (79B non-embedding), 48 layers arranged as 12 blocks of three Gated DeltaNet plus MoE layers followed by one gated attention plus MoE layer, 512 experts with 10 active and one shared, and a native context of 262,144 tokens. It runs only in non-thinking mode. Serving needs sglang 0.5.8 or vllm 0.15.0 or newer; Qwen's examples serve the full 256K context with tensor parallel over four GPUs. Recommended sampling is temperature 1.0, top_p 0.95, top_k 40. Ollama's qwen3-coder-next library has only a latest tag. The Qwen3.5 to Qwen3.8 generations, which have their own cards, are newer.

## Strengths
- Qwen says it matches models with 10 to 20 times more active parameters and recovers from execution failures; its benchmark charts are images, so no figures are quoted.
- Artificial Analysis (Qwen3 Coder Next): tau2-bench 79.5%, Coding Index 36.2, GPQA Diamond 73.7%, long-context reasoning 47%, Terminal-Bench Hard 18.2%.
- Works with Claude Code, Qwen Code, Qoder, Kilo, Trae and Cline scaffolds.
- 66 output tokens per second and 1.16 s to first token in Artificial Analysis' measurements.

## Limitations
- Artificial Analysis Intelligence Index 9.2, Agentic Index 0.9, Terminal-Bench 4.0 0%, Omniscience -62.4 and IFBench 35.2%.
- No thinking mode, text input only, and no published knowledge cutoff.
- Needs recent vLLM or SGLang builds with the hybrid-attention kernels.

## Good for
- Always-on local coding agents where active compute must stay small.
- Multi-step tool-using tasks in CLI and IDE scaffolds.
- Teams wanting an Apache 2.0 coding model with 256K context.
