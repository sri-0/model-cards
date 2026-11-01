---
id: qwen/qwen-mt-turbo
name: Qwen-MT-Turbo
owned_by: qwen
type: llm
description: "Qwen-MT-Turbo is an earlier hosted Qwen3-MT translation model on Model Studio, translating 92 languages with terminology intervention, format preservation and domain-specific translation."
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-07-22"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-MT-Turbo

## Overview
Status: Model Studio's current pricing page no longer lists qwen-mt-turbo; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. Qwen-MT-Turbo (Model Studio id `qwen-mt-turbo`) was released on 2025-07-22 in China (Beijing) and 2025-07-24 internationally as part of Qwen3-MT, alongside Qwen-MT-Plus; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes a translation-specialised model that provides high-quality, rapid translation across 92 languages at a cost-effective price, with terminology intervention, format preservation and domain-specific translation. It was priced at $0.16 input and $0.49 output per million tokens in Singapore, the same as the later Qwen-MT-Flash.

## Strengths
- 92 languages at a low price.

## Limitations
- No longer listed for sale on Model Studio.
- Context limits are not given in the archived pages.

## Good for
- Interpreting older translation integrations; Qwen-MT-Flash has the same price.
