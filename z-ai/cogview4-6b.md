---
id: z-ai/cogview4-6b
name: CogView4-6B
owned_by: z-ai
type: image
description: CogView4-6B is Z.ai's 6B open-weight (Apache-2.0) text-to-image diffusion model with a bilingual GLM-4 text encoder, able to render Chinese text and take prompts of any length; Z.ai serves it as CogView-4.
aliases: [cogView-4-250304, zai-org/CogView4-6B]
architecture:
  input_modalities: [text]
  output_modalities: [image]
open_weights: true
license: Apache-2.0
release_date: "2025-03-04"
sources:
  - https://huggingface.co/zai-org/CogView4-6B
  - https://huggingface.co/api/models/zai-org/CogView4-6B
  - https://github.com/zai-org/CogView4
  - https://docs.z.ai/guides/image/cogview-4
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.z.ai/api-reference/image/generate-image
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# CogView4-6B

## Overview
CogView-4 is Z.ai's first open-source text-to-image model; the 6B diffusers version was released on 2025-03-04. It replaces the English-only T5 encoder of earlier CogView models with the bilingual GLM-4-9B encoder and was trained on Chinese and English image-text pairs, which lets it follow Chinese prompts and draw Chinese characters in images. Training mixed captions of any length with images of any resolution, so prompts have no fixed length and output can be any size from 512 to 2048 px per side, divisible by 32 and at most 2^21 pixels. Z.ai's API serves it as `cogView-4-250304` at $0.01 per image, listed under "other pricing", while the image API reference names only GLM-Image in its model enum. OpenRouter does not list it; the id follows the Hugging Face repo. Weights are Apache-2.0.

## Strengths
- Z.ai reports 85.13 overall on DPG-Bench, first among open text-to-image models at release, ahead of SD3-Medium, Flux.1-dev and DALL-E 3 in its table.
- 0.73 on GenEval, per the same report.
- Fits on a 13-14 GB GPU with CPU offload and a 4-bit text encoder, or about 20 GB with offload alone.

## Limitations
- Without offload it needs 33-39 GB of GPU memory at batch size 4.
- FP16 overflows to black images; use BF16 or FP32.
- Z.ai's model overview now lists GLM-Image, not CogView-4, as its image generation model.
- Text-to-image only in this checkpoint.

## Good for
- Self-hosted bilingual image generation under a permissive licence.
- Product, food, poster and illustration images with short Chinese or English captions.
