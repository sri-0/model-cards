---
id: qwen/qwen3.8-2.4t-a95b
name: Qwen3.8 2.4T A95B
owned_by: qwen
type: llm
description: "Qwen3.8 2.4T A95B is the open-weight (Qwen3.8-Max License) text-only mixture-of-experts model behind Alibaba's hosted Qwen3.8 Max, with 2.4T total and 95B active parameters, mandatory thinking with reasoning_effort control and a 262,144-token native context."
aliases: [Qwen/Qwen3.8-2.4T-A95B, qwen3.8-2.4t-a95b]
context_length: 1048576
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: true
license: Qwen3.8-Max License
release_date: "2026-08-12"
pricing:
  input: 2
  output: 6
  cache_read: 0.25
benchmarks:
  intelligence_index: 39.9
  coding_index: 71.9
  agentic_index: 50.1
  omniscience_index: 4.3
  humanitys_last_exam: 42.4
  gpqa_diamond: 93.5
  scicode: 54.1
  terminal_bench_4: 11.1
  long_context_reasoning: 80.3
  output_tokens_per_second: 39.1
  time_to_first_token_seconds: 2.94
benchmark_variant: Qwen3.8 2.4T A95B
sources:
  - https://openrouter.ai/qwen/qwen3.8-2.4t-a95b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-8-2-4t-a95b
  - https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - https://github.com/QwenLM/Qwen3.8
  - https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/main/LICENSE
  - https://www.qwencloud.com/models/qwen3.8-2.4t-a95b
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
retrieved: "2026-10-16"
---

# Qwen3.8 2.4T A95B

## Overview
Qwen3.8-2.4T-A95B was released on 2026-08-12 as the first open Qwen-Max-class model; it is the open-weight variant of the hosted Qwen3.8 Max (see qwen/qwen3.8-max-0902). It is a text-only sparse mixture-of-experts model with 2.4T total and 95B activated parameters: 92 layers alternating three Gated DeltaNet blocks with one gated attention block, with 512-expert MoE layers (10 routed plus 1 shared active). Thinking cannot be disabled; `reasoning_effort` accepts xhigh (default), medium and low, and `preserve_thinking` is on by default. The hosted Qwen3.8 Max adds vision input, a non-thinking mode and built-in tools. Native context is 262,144 tokens (1,010,000 with YaRN); OpenRouter lists 1,048,576 with a 131,072-token output limit. Weights are compatible with vLLM, SGLang and TokenSpeed. The Qwen3.8-Max License is permissive but requires model-name attribution above 100,000,000 monthly active users or US$20,000,000 monthly revenue, and a separate licence for model-as-a-service or AI work assistant businesses above US$50,000,000 annual revenue. Qwen Cloud and Model Studio serve `qwen3.8-2.4t-a95b` at $2 input and $6 output per million tokens.

## Strengths
- Qwen reports Terminal Bench 2.1 86.6, SWE-bench Pro 67.7, PaperBench 93.0, CoWorkBench 74.8, GPQA Diamond 92.6, IFBench 82.8 and MRCR v2 256K 92.9.
- Artificial Analysis (Qwen3.8 2.4T A95B): Intelligence Index 39.9, Coding Index 71.9, Agentic Index 50.1, GPQA Diamond 93.5%, Humanity's Last Exam 42.4%, SciCode 54.1%, Omniscience 4.3.

## Limitations
- Text only, and thinking cannot be switched off.
- Terminal-Bench 4.0 11.1%; 39.1 tokens per second and 2.94 s to first token in AA's test.
- 2.4T parameters need a multi-node GPU cluster; the licence adds attribution and revenue conditions.

## Good for
- Self-hosted frontier-class coding, research and agent workloads.
- Long-context professional work in legal, finance and health domains.
- Running Qwen3.8 Max quality on your own hardware.
