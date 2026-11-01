---
id: qwen/qwen-image-2.0-pro
name: Qwen-Image-2.0-Pro
owned_by: qwen
type: image
description: "Qwen-Image-2.0-Pro is the full tier of Alibaba's hosted Qwen-Image-2.0 series, one model for image generation and editing with the series' strongest text rendering, 1,000-token prompts and the most lifelike textures."
aliases: [qwen-image-2.0-pro-2026-06-22, qwen-image-2.0-pro-2026-04-22, qwen-image-2.0-pro-2026-03-03, dashscope/qwen-image-2.0-pro]
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

# Qwen-Image-2.0-Pro

## Overview
Qwen-Image-2.0-Pro (Model Studio id `qwen-image-2.0-pro`) is the full-featured tier of the hosted Qwen-Image-2.0 series; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio lists three dated snapshots: 2026-03-03 (released that day), 2026-04-22 (released 2026-04-23 together with the stable id) and 2026-06-22 (released 2026-06-25). The current pricing page does not say which snapshot the stable id resolves to; an April 2026 archive mapped it to 2026-03-03. Model Studio describes it as combining generation and editing, with the 2.0 series' strongest text rendering from prompts of up to 1,000 tokens, its most lifelike textures, detailed photorealistic scenes and stronger semantic adherence. The image page lists up to six outputs per call and up to 2048x2048 resolution. It is priced at $0.075 per output image in Singapore and $0.071676 in China (Beijing).

## Strengths
- Artificial Analysis image arena (Qwen Image 2.0 Pro (2026-04-22)): Elo 1030 for text-to-image and 1058 for editing.
- Several pinned snapshots for reproducible output.

## Limitations
- Below Qwen-Image-2.1 and 3.0 on AA's arenas, at a higher per-image price than Qwen-Image-3.0-Pro at 1K ($0.04).
- Closed weights.

## Good for
- Integrations that need a fixed 2.0-series snapshot.
- Text-heavy posters and edits on Model Studio.
