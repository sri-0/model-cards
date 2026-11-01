---
id: mistralai/mistral-nemo
name: Mistral Nemo
owned_by: mistralai
type: llm
description: Mistral NeMo is a 12B Apache-2.0 open-weight multilingual model built by Mistral AI with NVIDIA, with a 128K context window and the Tekken tokenizer, released in July 2024.
aliases: [open-mistral-nemo, open-mistral-nemo-2407, mistral/open-mistral-nemo, mistralai/Mistral-Nemo-Instruct-2407, nvidia/Mistral-NeMo-12B-Instruct, "mistral-nemo@2407", azure_ai/mistral-nemo, "mistral-nemo:12b"]
context_length: 131072
max_output_tokens: 16384
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Apache-2.0
release_date: "2024-07-18"
knowledge_cutoff: "2024-04"
pricing:
  input: 0.029
  output: 0.03
sources:
  - https://openrouter.ai/mistralai/mistral-nemo
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models/mistralai/mistral-nemo/endpoints
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mistral-nemo-12b-24-07
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/mistral-nemo
  - https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407
  - https://huggingface.co/api/models/mistralai/Mistral-Nemo-Instruct-2407
  - https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407/raw/main/config.json
  - https://ollama.com/library/mistral-nemo
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mistral Nemo

## Overview
Mistral NeMo (API id open-mistral-nemo, dated open-mistral-nemo-2407) was released on 2024-07-18, trained jointly by Mistral AI and NVIDIA. It is a dense 12B transformer (40 layers, 131,072 positions in config.json) with a 128K context window, offered as a drop-in replacement for Mistral 7B. It uses the Tekken tokenizer, based on Tiktoken with a 131,072-token vocabulary, which Mistral says is about 30% more efficient than SentencePiece on source code, Chinese, Italian, French, German, Spanish and Russian, 2x on Korean and 3x on Arabic. Mistral names English, French, German, Spanish, Italian, Portuguese, Chinese, Japanese, Korean, Arabic and Hindi as its strong languages. Mistral says quantisation-aware training lets FP8 inference run without performance loss. Weights are on Hugging Face (mistralai/Mistral-Nemo-Instruct-2407) under Apache 2.0, and NVIDIA ships it as a NIM microservice. Mistral's docs give a deprecation date of 2026-05-22 and a retirement date of 2026-07-31, with Ministral 3 8B as the replacement. Artificial Analysis has no page for it.

## Strengths
- The Hugging Face card reports 68.0% on MMLU (5-shot), 83.5% on HellaSwag and 73.8% on TriviaQA, with multilingual MMLU from 59.0% to 64.6% across eight languages.
- Very cheap on OpenRouter: $0.029 input and $0.03 output per million tokens.
- Function calling and JSON output.
- Apache 2.0 licence and base weights for fine-tuning.

## Limitations
- No moderation mechanisms; the Hugging Face card calls the instruct checkpoint a quick demonstration of fine-tuning the base model.
- Past its retirement date on Mistral's API. No image input and no reasoning mode.
- Needs a lower temperature than earlier Mistral models; the card recommends 0.3.
- No independent Artificial Analysis results. Top-provider output limit of 16,384 tokens on OpenRouter.

## Good for
- Small self-hosted multilingual assistants and FP8 deployments.
- Replacing Mistral 7B deployments without changing the serving stack.
- Fine-tuning from the Apache-2.0 base model.
