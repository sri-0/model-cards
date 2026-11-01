---
id: mistralai/mixtral-8x7b-instruct-v0.1
name: Mixtral 8x7B Instruct
owned_by: mistralai
type: llm
description: Mixtral 8x7B Instruct is Mistral AI's first open sparse mixture-of-experts model, with 46.7B total and 12.9B active parameters, a 32K context window and an Apache-2.0 licence, released in December 2023.
aliases: [mistralai/Mixtral-8x7B-Instruct-v0.1, open-mixtral-8x7b, mistral-small-2312, "mistral.mixtral-8x7b-instruct-v0:1", mixtral-8x7b-instruct, "mixtral:8x7b"]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2023-12-11"
benchmarks:
  gpqa_diamond: 29.2
  humanitys_last_exam: 4.7
  output_tokens_per_second: 25.2
  time_to_first_token_seconds: 1.04
benchmark_variant: Mixtral 8x7B Instruct
sources:
  - https://artificialanalysis.ai/models/mixtral-8x7b-instruct
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mixtral-8x7b-0-1
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/mixtral-of-experts
  - https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1
  - https://huggingface.co/api/models/mistralai/Mixtral-8x7B-Instruct-v0.1
  - https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1/raw/main/config.json
  - https://openrouter.ai/api/v1/models
  - https://ollama.com/library/mixtral
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mixtral 8x7B Instruct

## Overview
Mixtral 8x7B Instruct was released on 2023-12-11. OpenRouter does not list it (it lists only the 8x22B), so the id follows the Hugging Face repo mistralai/Mixtral-8x7B-Instruct-v0.1. It is a sparse mixture-of-experts model with eight experts and two active per token, 46.7B total and 12.9B active parameters, so it runs at the speed and cost of a 12.9B model, with a 32K context window and support for English, French, Italian, German and Spanish. Mistral's API first served it as mistral-small in beta, then as open-mixtral-8x7b (alias mistral-small-2312) from February 2024; Mistral's docs list it as deprecated on 2024-11-30 and retired on 2025-03-30, with Mistral Small 4 as the replacement, so there is no current vendor price. Mistral's docs give about 94 GB of GPU memory at bf16 and about 13 GB at fp4. The Hugging Face card warns that the [INST] instruction format must be strictly respected.

## Strengths
- Mistral reports an MT-Bench score of 8.30 for the instruct model and says the base matches or outperforms GPT-3.5 on most standard benchmarks and Llama 2 70B with 6x faster inference.
- Apache 2.0 licence and a small active parameter count.
- Artificial Analysis measured 25.2 output tokens per second and 1.04 s to first token.

## Limitations
- No moderation mechanisms; the Hugging Face card calls the instruct checkpoint a quick demonstration of fine-tuning the base model.
- Artificial Analysis (Mixtral 8x7B Instruct): 29.2% on GPQA Diamond and 4.7% on Humanity's Last Exam.
- No function calling in the Hugging Face card (v1 tokenizer), no image input, no reasoning mode and a 2023 training vintage.
- Retired from Mistral's API.

## Good for
- Legacy self-hosted deployments and Bedrock integrations pinned to it.
- Research on mixture-of-experts models under a permissive licence.
- Low-cost chat in its five languages.
