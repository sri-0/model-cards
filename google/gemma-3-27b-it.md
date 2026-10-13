---
id: google/gemma-3-27b-it
name: Gemma 3 27B
owned_by: google
type: llm
description: Gemma 3 27B is the largest model in Google's March 2025 Gemma 3 family, an open-weight model with text and image input released under the Gemma Terms of Use.
aliases: [gemma-3-27b-it, gemini/gemma-3-27b-it]
context_length: 131072
max_output_tokens: 117964
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Gemini
  instruct_type: gemma
open_weights: true
license: Gemma Terms of Use
release_date: "2025-03-12"
knowledge_cutoff: "2024-08"
pricing:
  input: 0.08
  output: 0.45
  cache_read: 0.04
benchmarks:
  intelligence_index: 4.9
  coding_index: 10.1
  agentic_index: 0.1
  omniscience_index: -67.2
  humanitys_last_exam: 4.4
  gpqa_diamond: 42.8
  scicode: 23.3
  terminal_bench_hard: 3.8
  terminal_bench_4: 0
  long_context_reasoning: 7.3
  ifbench: 31.8
  tau2_bench: 10.5
  mmmu_pro: 48
benchmark_variant: Gemma 3 27B Instruct
sources:
  - https://openrouter.ai/google/gemma-3-27b-it
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gemma-3-27b
  - https://huggingface.co/google/gemma-3-27b-it
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Gemma 3 27B

## Overview
Gemma 3 27B Instruct was released on 2025-03-12. Gemma 3 added vision-language input with text output, a 128K context window (131,072 tokens on OpenRouter), support for over 140 languages, structured outputs and function calling. It has no reasoning mode. Its knowledge cutoff is August 2024. The weights are under the Gemma Terms of Use, not Apache 2.0 as used for Gemma 4, which is the newer generation (April 2026).

## Strengths
- Uses the established Gemma instruction format (`instruct_type: gemma` on OpenRouter).
- Image understanding: Artificial Analysis (Gemma 3 27B Instruct) reports 48% on MMMU Pro and 42.8% on GPQA Diamond.
- Concise output: 11M tokens to run the Intelligence Index against a median of 18M.
- Cheap on OpenRouter: $0.08 input and $0.45 output per million tokens, with up to 117,964 output tokens.

## Limitations
- Low current scores: Intelligence Index 4.9, coding index 10.1, agentic index 0.1.
- Poor use of its long window: 7.3% on Artificial Analysis' long-context reasoning test.
- Omniscience index of -67.2; verify factual answers.
- Licence is the Gemma Terms of Use; check its conditions before redistribution.
- Superseded by the Gemma 4 family.

## Good for
- Existing Gemma 3 deployments.
- Simple multilingual chat, image captioning and extraction.
- Short-context tasks on a single GPU where newer models are not yet approved.
