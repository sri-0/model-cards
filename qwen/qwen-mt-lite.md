---
id: qwen/qwen-mt-lite
name: Qwen-MT-Lite
owned_by: qwen
type: llm
description: "Qwen-MT-Lite is Alibaba lowest-cost hosted Qwen translation model on Model Studio, translating 32 languages with terminology intervention, format preservation and domain-specific translation."
aliases: [qwen-mt-lite-us]
context_length: 16384
max_output_tokens: 8192
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-11-19"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-mt-lite
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/machine-translation
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-MT-Lite

## Overview
Qwen-MT-Lite (Model Studio id `qwen-mt-lite`, with a `qwen-mt-lite-us` id for US deployment) is the smallest Qwen-MT translation model, released on 2025-11-19; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes high-quality, rapid translation across 32 languages at a cost-effective price, with terminology intervention, format preservation and domain-specific translation. It has a 16,384-token context with 8,192 input and 8,192 output tokens and no function calling, structured output or caching, and is available in China (Beijing), Singapore, Germany (Frankfurt) and US (Virginia). The price is $0.12 input and $0.36 output per million tokens in Singapore.

## Strengths
- Lowest Qwen-MT price.

## Limitations
- 32 languages, against 92 for Plus and Flash.
- Short 8,192-token input.

## Good for
- Cheap translation between major languages.
