---
id: qwen/qwen-image-edit
name: Qwen-Image-Edit
owned_by: qwen
type: image
description: "Qwen-Image-Edit is the Qwen team's original August 2025 Apache-2.0 open-weight image-editing model built on the 20B Qwen-Image, with semantic and appearance editing and precise bilingual text editing; Model Studio also served it as qwen-image-edit."
aliases: [Qwen/Qwen-Image-Edit]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
open_weights: true
license: Apache-2.0
release_date: "2025-08-18"
sources:
  - https://huggingface.co/Qwen/Qwen-Image-Edit
  - https://huggingface.co/api/models/Qwen/Qwen-Image-Edit
  - https://github.com/QwenLM/Qwen-Image
  - https://arxiv.org/abs/2508.02324
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://artificialanalysis.ai/image/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Image-Edit

## Overview
Qwen-Image-Edit was open-sourced on 2025-08-18 under Apache 2.0 (Hugging Face repo created 2025-08-17). OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen-Image-Edit, which matches Model Studio's `qwen-image-edit` id. Model Studio describes `qwen-image-edit` as the first Qwen image editing model, extending Qwen-Image's text rendering to editing with bilingual text editing, and priced it at $0.045 per image in Singapore; its current pricing page no longer lists it, though an archived copy from 2026-10-07 did. Built on the 20B Qwen-Image, the model feeds the input image both to Qwen2.5-VL for semantic control and to the VAE encoder for appearance control. That supports low-level appearance edits (adding, removing or changing elements while the rest stays fixed) and high-level semantic edits such as IP creation, object rotation and style transfer, plus adding, deleting or changing Chinese and English text while keeping font, size and style. It loads with Diffusers (`QwenImageEditPipeline`, 50 steps, true CFG 4.0). Qwen advised updating Diffusers on 2025-08-19 after performance misalignments.

## Strengths
- Precise in-image text edits in Chinese and English.
- Apache 2.0 licence.

## Limitations
- Artificial Analysis image-editing Elo 889, the lowest of the Qwen editors AA lists.
- Single input image; multi-image editing arrived with Qwen-Image-Edit-2509.

## Good for
- Reproducing work built on the August 2025 editor.
- Simple text and object edits on self-hosted GPUs.
