---
id: meta-llama/llama-3.1-8b-instruct
name: Llama 3.1 8B Instruct
owned_by: meta
type: llm
description: Llama 3.1 8B Instruct is Meta's small open-weight, text-only instruction-tuned model from July 2024.
aliases: [meta/llama-3.1-8b-instruct-maas, "llama3.1:8b", meta-llama/Llama-3.1-8B-Instruct, meta-llama/Meta-Llama-3.1-8B-Instruct]
context_length: 131072
max_output_tokens: 117964
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Llama3
  instruct_type: llama3
open_weights: true
license: Llama 3.1 Community License
release_date: "2024-07-23"
knowledge_cutoff: "2023-12"
pricing:
  input: 0.05
  output: 0.08
  cache_read: 0.025
benchmarks:
  intelligence_index: 6.9
  coding_index: 5.4
  omniscience_index: -30.9
  humanitys_last_exam: 5.3
  gpqa_diamond: 25.9
  terminal_bench_hard: 0.8
  long_context_reasoning: 18
  ifbench: 28.6
  tau2_bench: 16.4
  output_tokens_per_second: 141.1
  time_to_first_token_seconds: 0.86
benchmark_variant: Llama 3.1 Instruct 8B
sources:
  - https://openrouter.ai/meta-llama/llama-3.1-8b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/llama-3-1-instruct-8b
  - https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
  - https://ollama.com/library/llama3.1
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Llama 3.1 8B Instruct

## Overview
Llama 3.1 8B Instruct is the 8B member of Meta's Llama 3.1 family, released on July 23, 2024. It takes text and returns text, with a 131,072-token context window on OpenRouter and a December 2023 knowledge cutoff. It is released under the Llama 3.1 Community License, and use is subject to Meta's Acceptable Use Policy. OpenRouter's description for this id describes the 405B model, so it is not used here.

## Strengths
- Small and cheap: $0.05 input and $0.08 output per million tokens on OpenRouter.
- Fast: Artificial Analysis (Llama 3.1 Instruct 8B) measures 141.1 output tokens per second and 0.86 s to first token.
- Small enough to run on modest local hardware; packaged as the Ollama tag `llama3.1:8b`.
- Tool calling and structured outputs are supported by providers on OpenRouter.

## Limitations
- Low capability by current standards: Intelligence Index 6.9 (estimated), GPQA Diamond 25.9%, tau2-bench 16.4%.
- Weak use of long inputs: 18% on Artificial Analysis' long-context reasoning test.
- Omniscience index of -30.9; verify factual answers.
- Old knowledge (December 2023), no image input and no reasoning mode.

## Good for
- High-volume, low-cost classification, routing and extraction.
- Short summaries and simple rewriting.
- Lightweight local assistants where speed matters more than depth.
