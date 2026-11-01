---
id: minimax/image-01
name: MiniMax Image-01
owned_by: minimax
type: image
description: MiniMax Image-01 is MiniMax's text-to-image and character-reference image model, generating up to nine images per request at preset ratios or custom sizes up to 2048 px for $0.0035 per image.
aliases: [image-01]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
open_weights: false
license: proprietary
release_date: "2025-02-15"
sources:
  - https://platform.minimax.io/docs/faq/models
  - https://platform.minimax.io/docs/release-notes/models
  - https://platform.minimax.io/docs/release-notes/apis
  - https://platform.minimax.io/docs/guides/image-generation
  - https://platform.minimax.io/docs/api-reference/image-generation-t2i
  - https://platform.minimax.io/docs/api-reference/image-generation-i2i
  - https://platform.minimax.io/docs/pricing/overview
  - https://platform.minimax.io/docs/guides/rate-limits
  - https://openrouter.ai/api/v1/models?output_modalities=image
  - https://artificialanalysis.ai/image/leaderboard/text-to-image
retrieved: "2026-11-01"
---

# MiniMax Image-01

## Overview
Image-01 was released on 2025-02-15 and is MiniMax's only image model with a published price. OpenRouter does not list it; the id is MiniMax's API id under the `minimax/` prefix. Both modes use `POST /v1/image_generation`: text-to-image from a prompt of up to 1,500 characters, and image-to-image, where one `subject_reference` portrait (type `character`) carries a person's likeness into new scenes. Eight aspect ratios map to fixed sizes from 1024x1024 (1:1) to 1344x576 (21:9); since 2025-04-25, `width` and `height` can instead be set from 512 to 2048 px in multiples of 8. A request returns one to nine images as URLs that expire after 24 hours or as Base64, with an optional seed for reproducible output and an optional prompt optimiser that is off by default. Pay-as-you-go price is $0.0035 per image, with a default limit of 10 requests per minute. MiniMax also lists `image-01-live`, a separate model that only the image-to-image request accepts and that ignores custom width and height.

## Strengths
- A very low price per image.
- Character reference keeps a face consistent across images without fine-tuning.
- Custom resolutions and up to nine images per call.

## Limitations
- One reference image per request, and only portraits (`character`) are supported as subjects.
- No inpainting, masking or multi-image editing is documented.
- Not on Artificial Analysis's AA-Image-T2I v2.1 leaderboard (read 2026-11-01), so there is no independent quality score.
- MiniMax publishes no architecture, training details or benchmark results.

## Good for
- Cheap bulk illustration, thumbnails and concept art.
- Series of images that must keep the same character.
