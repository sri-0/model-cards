---
id: google/gemma-3-4b-it
name: Gemma 3 4B
owned_by: google
type: llm
description: Gemma 3 4B is a small model in Google's March 2025 Gemma 3 family, an open-weight model with text and image input released under the Gemma Terms of Use.
aliases: [gemma-3-4b-it, google.gemma-3-4b-it]
context_length: 131072
max_output_tokens: 16384
capabilities: [vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p]
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
  output: 0.1
benchmarks:
  intelligence_index: 4.8
  coding_index: 2.7
  omniscience_index: -82.9
  humanitys_last_exam: 5.3
  gpqa_diamond: 29.1
  terminal_bench_hard: 0.8
  long_context_reasoning: 6.7
  ifbench: 28.3
  tau2_bench: 5
  mmmu_pro: 29.9
benchmark_variant: Gemma 3 4B Instruct
sources:
  - https://openrouter.ai/google/gemma-3-4b-it
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gemma-3-4b
  - https://huggingface.co/google/gemma-3-4b-it
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Gemma 3 4B

## Overview
Gemma 3 4B Instruct was released on 2025-03-12. Like the rest of Gemma 3 it takes text and images, returns text, has a 128K context window (131,072 tokens on OpenRouter), and supports over 140 languages. Its knowledge cutoff is August 2024 and it has no reasoning mode. The weights are under the Gemma Terms of Use. Gemma 4 E4B and E2B are the newer small Gemma models.

## Strengths
- Small footprint, suited to local and edge hardware.
- Image input at this size: Artificial Analysis (Gemma 3 4B Instruct) reports 29.9% on MMMU Pro.
- Structured outputs are available through providers on OpenRouter.
- Very cheap on OpenRouter: $0.05 input and $0.10 output per million tokens.

## Limitations
- Low scores: Intelligence Index 4.8 (estimated), coding index 2.7, GPQA Diamond 29.1%, tau2-bench 5%.
- Long-context reasoning of 6.7%, so long inputs are handled poorly.
- Omniscience index of -82.9; do not rely on it for factual recall.
- OpenRouter does not list tool calling for this model, although OpenRouter's Gemma 3 family description mentions function calling.
- OpenRouter caps output at 16,384 tokens.

## Good for
- Simple classification, tagging and extraction.
- Basic image captioning on small devices.
- Existing Gemma 3 deployments with tight memory limits.
