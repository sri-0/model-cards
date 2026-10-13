---
id: google/gemma-3-12b-it
name: Gemma 3 12B
owned_by: google
type: llm
description: Gemma 3 12B is the mid-sized model in Google's March 2025 Gemma 3 family, an open-weight model with text and image input released under the Gemma Terms of Use.
aliases: [gemma-3-12b-it, google.gemma-3-12b-it]
context_length: 131072
max_output_tokens: 16384
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
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
  input: 0.05
  output: 0.15
benchmarks:
  intelligence_index: 3.8
  coding_index: 5.8
  agentic_index: 0.1
  omniscience_index: -77.1
  humanitys_last_exam: 4.2
  gpqa_diamond: 34.9
  scicode: 16.4
  terminal_bench_hard: 0.8
  terminal_bench_4: 0
  long_context_reasoning: 8.3
  ifbench: 36.7
  tau2_bench: 10.8
  mmmu_pro: 37.5
benchmark_variant: Gemma 3 12B Instruct
sources:
  - https://openrouter.ai/google/gemma-3-12b-it
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gemma-3-12b
  - https://huggingface.co/google/gemma-3-12b-it
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Gemma 3 12B

## Overview
Gemma 3 12B Instruct was released on 2025-03-12 and is the second largest Gemma 3 model after Gemma 3 27B. Gemma 3 added vision-language input with text output, a 128K context window (131,072 tokens on OpenRouter), support for over 140 languages, structured outputs and function calling. It has no reasoning mode, and its knowledge cutoff is August 2024. The weights are under the Gemma Terms of Use. Gemma 4 (April 2026) is the newer generation.

## Strengths
- Small enough for modest local hardware while still accepting images.
- Tool calling and structured outputs are available through providers on OpenRouter.
- Very cheap on OpenRouter: $0.05 input and $0.15 output per million tokens.
- Artificial Analysis (Gemma 3 12B Instruct) reports 36.7% on IFBench and 37.5% on MMMU Pro.

## Limitations
- Low current scores: Intelligence Index 3.8, coding index 5.8, GPQA Diamond 34.9%.
- Weak long-context use: 8.3% on long-context reasoning despite the 128K window.
- Omniscience index of -77.1; do not rely on it for factual recall.
- Verbose for its class: 26M tokens to run the Intelligence Index against a median of 18M.
- OpenRouter caps output at 16,384 tokens.

## Good for
- Lightweight image captioning and visual question answering.
- Classification, extraction and short multilingual replies.
- Existing Gemma 3 pipelines.
