---
id: meta-llama/llama-guard-4-12b
name: Llama Guard 4 12B
owned_by: meta
type: llm
description: Llama Guard 4 12B is Meta's open-weight multimodal safety classifier that labels prompts and responses as safe or unsafe and names the violated hazard categories.
aliases: [meta-llama/Llama-Guard-4-12B]
context_length: 163840
max_output_tokens: 16384
capabilities: [vision]
supported_parameters: [frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p]
architecture:
  input_modalities: [image, text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Llama 4 Community License
knowledge_cutoff: "2024-08"
pricing:
  input: 0.18
  output: 0.18
sources:
  - https://openrouter.ai/meta-llama/llama-guard-4-12b
  - https://openrouter.ai/api/v1/models
  - https://huggingface.co/meta-llama/Llama-Guard-4-12B
retrieved: "2026-10-14"
---

# Llama Guard 4 12B

## Overview
Llama Guard 4 is derived from Llama 4 Scout and fine-tuned for content safety classification. It is not a chat model. It classifies LLM inputs (prompt classification) and LLM responses (response classification) and generates text saying whether the content is safe or unsafe; if unsafe, it lists the categories violated. Meta aligned it to the standardized MLCommons hazards taxonomy. It has about 12B parameters, a 163,840-token context on OpenRouter, and is released under the Llama 4 Community License.

## Strengths
- Covers both sides of a conversation: user prompts and model outputs.
- Handles mixed text-and-image prompts, including multiple images.
- Moderates English and multiple other supported languages.
- Open weights, so it can run next to a self-hosted model. It is also part of Meta's Llama Moderations API.
- Cheap on OpenRouter: $0.18 per million input and output tokens.

## Limitations
- Only classifies. No tool calling, reasoning or general generation.
- Categories follow the MLCommons hazards taxonomy; other policies need separate handling.
- No Artificial Analysis benchmarks, since it is not a general model.

## Good for
- Input and output moderation in front of chat or agent models.
- Screening image-and-text prompts before they reach a multimodal model.
- Logging safety categories for review.
