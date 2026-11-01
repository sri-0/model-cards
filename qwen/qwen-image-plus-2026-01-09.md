---
id: qwen/qwen-image-plus-2026-01-09
name: Qwen-Image-Plus 2026-01-09
owned_by: qwen
type: image
description: "Qwen-Image-Plus 2026-01-09 is a hosted Model Studio snapshot that distils and accelerates Qwen-Image-Max for faster high-quality text-to-image generation with strong text rendering."
architecture:
  input_modalities: [text]
  output_modalities: [image]
open_weights: false
license: proprietary
release_date: "2026-01-09"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://artificialanalysis.ai/image/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Image-Plus 2026-01-09

## Overview
Status: Model Studio's current pricing and image-generation pages no longer list this snapshot; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. `qwen-image-plus-2026-01-09` is a dated Model Studio text-to-image snapshot released on 2026-01-09; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes it as a distilled and accelerated variant of Qwen-Image-Max that generates high-quality images faster, with the Qwen series' strength in complex text rendering. It is a separate card because the undated `qwen-image-plus` id was documented as "currently equivalent to qwen-image", the original August 2025 model (see qwen/qwen-image). Both Plus ids were priced at $0.03 per image in Singapore and $0.028671 in China (Beijing), billed on output only, against $0.075 for Qwen-Image-Max.

## Strengths
- Artificial Analysis text-to-image Elo 952 (as Qwen Image Plus 2601), above the original Qwen-Image at 903.
- Less than half the per-image price of Qwen-Image-Max.

## Limitations
- No longer listed for sale on Model Studio.
- Far below Qwen-Image-2.0 and later models on AA's arena.
- Closed weights.

## Good for
- Interpreting older Model Studio integrations that pinned this snapshot.
- Comparing distilled and full Max-series quality.
