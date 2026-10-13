---
id: meta-llama/llama-4-maverick
name: Llama 4 Maverick
owned_by: meta
type: llm
description: Llama 4 Maverick is Meta's open-weight mixture-of-experts multimodal model with 17B active and about 400B total parameters, released in April 2025.
aliases: [Llama-4-Maverick-17B-128E-Instruct-FP8, meta/llama-4-maverick-17b-128e-instruct-maas, meta-llama/Llama-4-Maverick-17B-128E-Instruct, meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8]
context_length: 1048576
max_output_tokens: 16384
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Llama4
open_weights: true
license: Llama 4 Community License
release_date: "2025-04-05"
knowledge_cutoff: "2024-08"
pricing:
  input: 0.1875
  output: 0.6525
  cache_read: 0.05
benchmarks:
  intelligence_index: 10
  coding_index: 16.3
  agentic_index: 0.6
  omniscience_index: -41.9
  humanitys_last_exam: 4.9
  gpqa_diamond: 67.1
  scicode: 31.7
  terminal_bench_hard: 6.8
  terminal_bench_4: 0
  long_context_reasoning: 50
  ifbench: 43
  tau2_bench: 17.8
  mmmu_pro: 62.1
  output_tokens_per_second: 43.1
  time_to_first_token_seconds: 1.09
benchmark_variant: Llama 4 Maverick
sources:
  - https://openrouter.ai/meta-llama/llama-4-maverick
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/llama-4-maverick
  - https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Llama 4 Maverick

## Overview
Llama 4 Maverick uses 128 experts with 17B parameters active per forward pass (about 400B in total). It takes multilingual text and images, uses early fusion for native multimodality, and outputs text and code in 12 supported languages. Meta trained it on about 22 trillion tokens with an August 2024 knowledge cutoff and released it on April 5, 2025 under the Llama 4 Community License. It is instruction-tuned and has no reasoning mode.

## Strengths
- Image understanding and general multimodal chat. Artificial Analysis (Llama 4 Maverick) reports 62.1% on MMMU Pro and 67.1% on GPQA Diamond.
- 1,048,576-token context window on OpenRouter.
- Low hosted price: $0.1875 input and $0.6525 output per million tokens on OpenRouter.
- Open weights, including an FP8 checkpoint on Hugging Face.

## Limitations
- Artificial Analysis gives it 10 on the Intelligence Index (estimated), below average for open non-reasoning models of its size.
- Weak for agents: agentic index 0.6, tau2-bench 17.8%, Terminal-Bench 4 at 0%.
- Omniscience index of -41.9, so check factual answers.
- All ~400B parameters must be stored, so serving needs far more memory than the 17B active count suggests.
- 43.1 output tokens per second, slower than average per Artificial Analysis.

## Good for
- Image and text question answering, captioning and visual document reading.
- Multilingual assistants.
- Long-document tasks that do not need deep reasoning.
