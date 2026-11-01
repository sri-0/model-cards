---
id: qwen/qwen-mt-flash
name: Qwen-MT-Flash
owned_by: qwen
type: llm
description: "Qwen-MT-Flash is Alibaba fast, low-cost hosted Qwen translation model on Model Studio, upgraded to the Qwen3 architecture, translating 92 languages with terminology intervention and format preservation."
context_length: 16384
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-11-06"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/machine-translation
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-MT-Flash

## Overview
Qwen-MT-Flash (Model Studio id `qwen-mt-flash`) is the speed- and cost-focused Qwen-MT translation model, released on 2025-11-06 in China (Beijing) and 2025-11-11 in other regions; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio says it is fully upgraded to the Qwen3 architecture for better performance and translation quality, translates 92 languages quickly and cheaply, and supports terminology intervention, format preservation and domain-specific adaptation, balancing speed, quality and cost. Model Studio's text generation page lists it under translation models with a 16K context and no thinking, function calling or structured output. The price is $0.16 input and $0.49 output per million tokens in Singapore.

## Strengths
- Low price for 92-language translation.
- Glossary and format support.

## Limitations
- 16K context.
- No published quality comparison with Qwen-MT-Plus.

## Good for
- High-volume app, chat and catalogue translation.
