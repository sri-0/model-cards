---
id: qwen/qwen3.5-35b-a3b
name: Qwen3.5 35B A3B
owned_by: qwen
type: llm
description: "Qwen3.5 35B A3B is Alibaba's open-weight (Apache-2.0) vision-language mixture-of-experts model with 35B total and 3B active parameters, Gated DeltaNet attention, thinking mode and a 262,144-token native context; the hosted Qwen3.5 Flash is its production version."
aliases: [Qwen/Qwen3.5-35B-A3B, qwen3.5-35b-a3b, "qwen3.5:35b"]
context_length: 262144
max_output_tokens: 16384
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2026-02-24"
pricing:
  input: 0.15
  output: 1
  cache_read: 0.05
benchmarks:
  intelligence_index: 19.3
  omniscience_index: -48.1
  humanitys_last_exam: 21
  gpqa_diamond: 84.5
  terminal_bench_hard: 26.5
  long_context_reasoning: 72
  ifbench: 72.5
  tau2_bench: 89.2
  mmmu_pro: 72.7
  output_tokens_per_second: 147.4
  time_to_first_token_seconds: 2.09
benchmark_variant: Qwen3.5 35B A3B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3.5-35b-a3b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-5-35b-a3b
  - https://huggingface.co/Qwen/Qwen3.5-35B-A3B
  - https://github.com/QwenLM/Qwen3.5
  - https://ollama.com/library/qwen3.5
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
retrieved: "2026-10-16"
---

# Qwen3.5 35B A3B

## Overview
Qwen3.5-35B-A3B was released on 2026-02-24. It is a vision-language mixture-of-experts model with 35B total and 3B activated parameters: 40 layers alternating three Gated DeltaNet blocks with one gated attention block, each followed by a 256-expert MoE layer that activates 8 routed experts plus 1 shared. Qwen names the hosted Qwen3.5 Flash as the production version of this model, with a 1M-token default context and built-in tools (see qwen/qwen3.5-flash-02-23). OpenRouter describes its performance as comparable to Qwen3.5-27B. Native context is 262,144 tokens (1,010,000 with YaRN); OpenRouter lists 262,144 with a 16,384-token output limit. Thinking is on by default. Weights are Apache-2.0; Ollama serves `qwen3.5:35b` (22 GB) and Model Studio serves `qwen3.5-35b-a3b` under its legacy models at $0.25 input and $2 output per million tokens.

## Strengths
- Qwen reports SWE-bench Verified 69.2, Terminal Bench 2 40.5, TAU2-Bench 81.2, GPQA Diamond 84.2, MMMU-Pro 75.1, OCRBench 91.0 and AndroidWorld 71.1.
- Fast: 147.4 tokens per second and 2.09 s to first token in Artificial Analysis' test.
- Artificial Analysis (Qwen3.5 35B A3B, Reasoning): tau2-bench 89.2%, GPQA Diamond 84.5%, MMMU-Pro 72.7%, long-context reasoning 72%.

## Limitations
- AA Intelligence Index 19.3, Omniscience -48.1, Terminal-Bench Hard 26.5%, Humanity's Last Exam 21%.
- OpenRouter's listed endpoint caps output at 16,384 tokens, which is short for long thinking traces.
- Only 3B parameters are active per token, but all 35B must be loaded; keep at least 128K tokens of context.

## Good for
- High-throughput multimodal agents and batch document processing.
- Local inference where a 22 GB download is acceptable.
- Workloads that will later move to the hosted Qwen3.5 Flash.
