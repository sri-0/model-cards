---
id: qwen/qwen-image-2.0
name: Qwen-Image-2.0
owned_by: qwen
type: image
description: "Qwen-Image-2.0 is the accelerated tier of Alibaba's hosted Qwen-Image-2.0 series, one model for image generation and editing with 1,000-token prompts, improved text rendering and realistic textures."
aliases: [qwen-image-2.0-2026-03-03, dashscope/qwen-image-2.0]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
open_weights: false
license: proprietary
release_date: "2026-03-03"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/image-model
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://artificialanalysis.ai/image/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Image-2.0

## Overview
Qwen-Image-2.0 (Model Studio id `qwen-image-2.0`, with snapshot `qwen-image-2.0-2026-03-03`) was released on 2026-03-03 as the accelerated version of the Qwen-Image-2.0 series; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio says the series combines image generation and image editing in one model, with stronger text rendering from prompts of up to 1,000 tokens, more realistic textures, finely detailed photorealistic scenes and better semantic adherence, and that the accelerated version balances performance and quality. Model Studio's image page lists up to six outputs per call and resolutions up to 2048x2048 for both generation and editing. It is still on Model Studio's pricing page at $0.035 per output image in Singapore and $0.028671 in China (Beijing).

## Strengths
- Artificial Analysis image arena (Qwen Image 2.0 (2026-03-03)): Elo 990 for text-to-image and 966 for editing.
- About half the per-image price of Qwen-Image-2.0-Pro.

## Limitations
- Well below Qwen-Image-2.0-Pro (1030 and 1058) and the 2.1 and 3.0 models on AA's arenas.
- Closed weights.

## Good for
- Low-cost hosted generation and editing with readable text.
- Existing integrations pinned to the Qwen-Image-2.0 series.
