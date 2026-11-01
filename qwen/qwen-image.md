---
id: qwen/qwen-image
name: Qwen-Image
owned_by: qwen
type: image
description: "Qwen-Image is the Qwen team's original August 2025 Apache-2.0 open-weight 20B MMDiT text-to-image model, known for complex text rendering, especially in Chinese; Model Studio also served it as qwen-image."
aliases: [Qwen/Qwen-Image, qwen-image-plus]
architecture:
  input_modalities: [text]
  output_modalities: [image]
open_weights: true
license: Apache-2.0
release_date: "2025-08-04"
sources:
  - https://huggingface.co/Qwen/Qwen-Image
  - https://huggingface.co/api/models/Qwen/Qwen-Image
  - https://github.com/QwenLM/Qwen-Image
  - https://arxiv.org/abs/2508.02324
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://artificialanalysis.ai/image/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Image

## Overview
Qwen-Image was released on 2025-08-04 as open weights under Apache 2.0, with technical report arXiv 2508.02324. OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen-Image, which matches Model Studio's `qwen-image` id. Model Studio describes `qwen-image` in the words of Qwen's announcement, as the first Qwen image generation foundation model, and priced it at $0.035 per image; its stable `qwen-image-plus` was "currently equivalent to qwen-image" at $0.03 per image (the dated qwen-image-plus-2026-01-09 is a different, Max-derived model with its own card). Model Studio's current pricing page no longer lists either id; an archived copy from 2026-10-07 still did. Qwen describes Qwen-Image as a 20B MMDiT model with strong general generation and exceptional text rendering, especially for Chinese. It loads with Diffusers (`QwenImagePipeline`); the example uses 50 steps, a true CFG scale of 4.0, a "positive magic" suffix and presets from 1328x1328. ComfyUI added native support on 2025-08-05, and community LoRAs followed.

## Strengths
- Complex Chinese and English text rendering in posters and signage.
- Apache 2.0 licence that allows commercial use.

## Limitations
- Artificial Analysis text-to-image Elo 903, far below later Qwen image models (Qwen-Image-3.0-Pro 1095).
- Superseded by Qwen-Image-2512 for realism and text rendering.
- Text-to-image only in this checkpoint; editing is Qwen-Image-Edit.

## Good for
- Reproducing work built on the original Qwen-Image or its LoRAs.
- Self-hosted text-heavy graphics where licence terms matter.
