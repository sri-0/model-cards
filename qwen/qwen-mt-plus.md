---
id: qwen/qwen-mt-plus
name: Qwen-MT-Plus
owned_by: qwen
type: llm
description: "Qwen-MT-Plus is Alibaba flagship hosted Qwen translation model on Model Studio, upgraded to the Qwen3 architecture, translating 92 languages with terminology control, format preservation and domain adaptation."
context_length: 16384
max_output_tokens: 8192
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-07-22"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-mt-plus
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/machine-translation
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-MT-Plus

## Overview
Qwen-MT-Plus (Model Studio id `qwen-mt-plus`) is the flagship of the Qwen-MT translation models, released on 2025-07-22 in China (Beijing) and 2025-07-24 internationally; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio says it is fully upgraded to the Qwen3 architecture, supports 92 languages, and is stronger than traditional machine translation on context, terminology control and format preservation, especially in specialised domains. It has a 16,384-token context with 8,192 input and 8,192 output tokens, and no thinking, function calling or structured output; Model Studio's text generation page lists it under translation models. Prices per million tokens are $2.46 input and $7.37 output in Singapore, and $0.259 and $0.775 in China (Beijing), Germany (Frankfurt) and US (Virginia).

## Strengths
- Terminology and format control for professional translation.
- 92 languages.

## Limitations
- Short 8,192-token input.
- Singapore price is about 9.5 times the other regions.

## Good for
- Legal, technical and product translation with glossaries.
