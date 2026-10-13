---
id: google/gemma-4-26b-a4b-it
name: Gemma 4 26B A4B
owned_by: google
type: llm
description: Gemma 4 26B A4B is Google DeepMind's open-weight (Apache-2.0) mixture-of-experts multimodal model with 25.2B total and 3.8B active parameters.
aliases: [gemma-4-26b-a4b-it, gemini/gemma-4-26b-a4b-it, google/gemma-4-26B-A4B-it]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [image, text, video]
  output_modalities: [text]
  tokenizer: Gemma
open_weights: true
license: Apache-2.0
release_date: "2026-04-02"
pricing:
  input: 0.09
  output: 0.3
  cache_read: 0.05
benchmarks:
  intelligence_index: 16.7
  coding_index: 39.3
  agentic_index: 2.9
  omniscience_index: -50.8
  humanitys_last_exam: 19.3
  gpqa_diamond: 79.2
  scicode: 40
  terminal_bench_hard: 13.6
  long_context_reasoning: 65.7
  ifbench: 72.4
  tau2_bench: 43.6
  mmmu_pro: 69.2
  output_tokens_per_second: 73.4
  time_to_first_token_seconds: 0.98
benchmark_variant: Gemma 4 26B A4B (Reasoning)
sources:
  - https://openrouter.ai/google/gemma-4-26b-a4b-it
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gemma-4-26b-a4b
  - https://huggingface.co/google/gemma-4-26B-A4B-it
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Gemma 4 26B A4B

## Overview
Gemma 4 26B A4B Instruct is the mixture-of-experts member of the Gemma 4 family, released on 2026-04-02 under Apache 2.0. It has 128 experts plus one shared expert, with 8 active per token, so only 3.8B of 25.2B parameters run per token. It takes text, images and video (up to 60 s at 1 fps per OpenRouter) and returns text. It has a 256K context window, native function calling, structured output and a configurable thinking mode.

## Strengths
- Low compute per token for its quality. Artificial Analysis (Gemma 4 26B A4B, Reasoning variant) gives it 16.7 on the Intelligence Index (estimated), above the dense Gemma 4 31B's 14.7.
- Good knowledge and instruction following: GPQA Diamond 79.2%, IFBench 72.4%, MMMU Pro 69.2%, long-context reasoning 65.7%.
- Responsive: 0.98 s to first token and 73.4 output tokens per second.
- Long outputs: OpenRouter lists up to 235,929 output tokens.
- Cheap on OpenRouter: $0.09 input and $0.30 output per million tokens.

## Limitations
- All 25.2B parameters must still be held in memory.
- No audio input.
- Weak on agentic benchmarks: agentic index 2.9, Terminal-Bench Hard 13.6%.
- Omniscience index of -50.8; verify factual answers.

## Good for
- Local assistants where throughput and latency matter.
- Coding help and document or image understanding on consumer GPUs and workstations.
- Video frame analysis within the 60-second limit.
