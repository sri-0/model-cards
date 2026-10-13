---
id: google/gemma-4-31b-it
name: Gemma 4 31B
owned_by: google
type: llm
description: Gemma 4 31B is Google DeepMind's 30.7B-parameter dense open-weight multimodal model, released under Apache 2.0 with a configurable thinking mode.
aliases: [gemma-4-31b-it, gemini/gemma-4-31b-it, google/gemma-4-31B-it]
context_length: 262144
max_output_tokens: 16384
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
  output: 0.34
  cache_read: 0.05
benchmarks:
  intelligence_index: 14.7
  coding_index: 43.4
  agentic_index: 4.2
  omniscience_index: -47.9
  humanitys_last_exam: 23.6
  gpqa_diamond: 85.7
  scicode: 45.5
  terminal_bench_hard: 36.4
  terminal_bench_4: 0
  long_context_reasoning: 69.7
  ifbench: 75.6
  tau2_bench: 59.9
  mmmu_pro: 73.4
  output_tokens_per_second: 35.1
  time_to_first_token_seconds: 1.03
benchmark_variant: Gemma 4 31B (Reasoning)
sources:
  - https://openrouter.ai/google/gemma-4-31b-it
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gemma-4-31b
  - https://huggingface.co/google/gemma-4-31B-it
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Gemma 4 31B

## Overview
Gemma 4 31B Instruct is the largest dense model in the Gemma 4 family, released on 2026-04-02 under Apache 2.0. It takes text and images (OpenRouter and Artificial Analysis also list video) and returns text. It has a 256K context window (262,144 tokens on OpenRouter), native function calling, native system-role support, a configurable thinking mode and support for over 140 languages. Its 60 layers mix local sliding-window and global attention.

## Strengths
- Strong for its size on knowledge and instruction following. Artificial Analysis (Gemma 4 31B, Reasoning variant): GPQA Diamond 85.7%, IFBench 75.6%, MMMU Pro 73.4%, long-context reasoning 69.7%, coding index 43.4, Intelligence Index 14.7.
- Artificial Analysis rates its intelligence among the leading open-weight models of similar size.
- Low hosted price: $0.09 input and $0.34 output per million tokens on OpenRouter.
- Fully open weights under a permissive licence, suitable for offline deployment.

## Limitations
- Slow per Artificial Analysis: 35.1 output tokens per second.
- OpenRouter providers cap output at 16,384 tokens.
- No audio input (audio is limited to E2B, E4B and 12B).
- Weak on long agentic runs: agentic index 4.2 and 0% on Terminal-Bench 4.
- Omniscience index of -47.9; verify factual answers.

## Good for
- Local coding help, reasoning and document understanding on a workstation GPU.
- Image and document question answering.
- Multilingual assistants that need a permissively licensed model.
