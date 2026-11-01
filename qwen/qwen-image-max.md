---
id: qwen/qwen-image-max
name: Qwen-Image-Max
owned_by: qwen
type: image
description: "Qwen-Image-Max is a hosted Model Studio text-to-image model from December 2025 that reduces the AI-generated look of the Plus series, with more lifelike skin and natural textures and better text rendering."
aliases: [qwen-image-max-2025-12-30]
architecture:
  input_modalities: [text]
  output_modalities: [image]
open_weights: false
license: proprietary
release_date: "2025-12-30"
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

# Qwen-Image-Max

## Overview
Status: Model Studio's current pricing and image-generation pages no longer list qwen-image-max; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. Qwen-Image-Max (Model Studio id `qwen-image-max`, documented as currently equivalent to the `qwen-image-max-2025-12-30` snapshot) was released on 2025-12-30 as the Max tier above the Plus series; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio says that, compared with the Plus series, it greatly reduces the "AI-like" feel of generated images, renders more lifelike material textures for people and finer natural textures, and produces more visually appealing text. The later qwen-image-plus-2026-01-09 snapshot is a distilled, faster variant of it. It was priced at $0.075 per image in Singapore and $0.071677 in China (Beijing), billed on output only.

## Strengths
- Realistic portraits and natural detail compared with earlier Qwen image models, per Model Studio.
- Strong text rendering.

## Limitations
- No longer listed for sale on Model Studio.
- Artificial Analysis publishes no arena score for it.
- Text-to-image only; editing used the separate Qwen-Image-Edit-Max.

## Good for
- Interpreting older integrations that used qwen-image-max.
- Comparing with the newer Qwen-Image-2.0 and 3.0 models.
