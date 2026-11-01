---
id: qwen/qvq-plus
name: QVQ-Plus
owned_by: qwen
type: llm
description: "QVQ-Plus is the Plus tier of Alibaba hosted Qwen QVQ visual reasoning model on Model Studio, offered in China (Beijing), taking images and producing chain-of-thought answers."
aliases: [qvq-plus-latest, qvq-plus-2025-05-15, qvq-plus-0515]
capabilities: [reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-06-03"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# QVQ-Plus

## Overview
Status: Model Studio's current pricing page no longer lists qvq-plus; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. QVQ-Plus (Model Studio id `qvq-plus`, with `qvq-plus-latest` and the `qvq-plus-2025-05-15` snapshot, also `qvq-plus-0515`) was released on 2025-06-03 for China (Beijing); no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes the Plus version of the QVQ visual reasoning model, which takes visual input and outputs a chain of thought, with improved maths, programming, visual analysis, creative and general abilities. Model Studio positions QVQ-Max above it for complex tasks. It was priced at $0.287 input and $0.717 output per million tokens. The archived pages that list it give no separate context limits.

## Strengths
- Lower-cost visual reasoning than QVQ-Max.

## Limitations
- No longer listed for sale on Model Studio.
- China (Beijing) only; limits not documented.

## Good for
- Interpreting older visual reasoning integrations.
