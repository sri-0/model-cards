---
id: meta-llama/llama-4-scout
name: Llama 4 Scout
owned_by: meta
type: llm
description: Llama 4 Scout is Meta's open-weight mixture-of-experts multimodal model with 17B active of 109B total parameters and a 10M-token design context.
aliases: [Llama-4-Scout-17B-16E-Instruct-FP8, meta/llama-4-scout-17b-16e-instruct-maas, meta-llama/Llama-4-Scout-17B-16E-Instruct]
context_length: 1310720
max_output_tokens: 117964
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Llama4
open_weights: true
license: Llama 4 Community License
release_date: "2025-04-05"
knowledge_cutoff: "2024-08"
pricing:
  input: 0.18
  output: 0.59
benchmarks:
  intelligence_index: 8.1
  coding_index: 8.2
  agentic_index: 0.5
  omniscience_index: -52.1
  humanitys_last_exam: 3.8
  gpqa_diamond: 58.7
  scicode: 21.3
  terminal_bench_hard: 1.5
  terminal_bench_4: 0
  long_context_reasoning: 27.7
  ifbench: 39.5
  tau2_bench: 15.5
  mmmu_pro: 52.9
  output_tokens_per_second: 67.2
  time_to_first_token_seconds: 0.87
benchmark_variant: Llama 4 Scout
sources:
  - https://openrouter.ai/meta-llama/llama-4-scout
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/llama-4-scout
  - https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Llama 4 Scout

## Overview
Llama 4 Scout uses 16 experts and activates 17B of its 109B parameters per token. It takes text and images, outputs text and code in 12 supported languages, and was trained on about 40 trillion tokens with data up to August 2024. Meta specifies a 10 million token context; providers on OpenRouter expose 1,310,720 tokens. It was released on April 5, 2025 under the Llama 4 Community License and has no reasoning mode.

## Strengths
- Built for efficiency and local or commercial deployment; much smaller in total than Llama 4 Maverick.
- Very long context window.
- Quick responses: Artificial Analysis (Llama 4 Scout) measures 67.2 output tokens per second and 0.87 s to first token.
- Handles images: 52.9% on MMMU Pro.
- Cheap on OpenRouter: $0.18 input and $0.59 output per million tokens.

## Limitations
- Low general scores: Intelligence Index 8.1 (estimated), GPQA Diamond 58.7%.
- A long window is not reliable long-context reasoning: 27.7% on Artificial Analysis' long-context reasoning test.
- Poor fit for agents: agentic index 0.5, tau2-bench 15.5%.
- Omniscience index of -52.1, so verify facts.

## Good for
- Multilingual chat, image captioning and image understanding.
- Ingesting long documents or logs for search and summarisation.
- Deployments with tight hardware budgets that still want multimodal input.
