---
id: qwen/qwen-mt-image-2.0
name: Qwen-MT-Image-2.0
owned_by: qwen
type: image
description: "Qwen-MT-Image-2.0 is Alibaba hosted image translation engine on Model Studio that translates text in images from 55 source languages while replicating the original layout and typography."
architecture:
  input_modalities: [image]
  output_modalities: [image]
open_weights: false
license: proprietary
release_date: "2026-08-28"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-MT-Image-2.0

## Overview
Qwen-MT-Image-2.0 (Model Studio id `qwen-mt-image-2.0`) is an image translation model released on 2026-08-28; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes an advanced image translation engine that supports 55 source languages and replicates the original layout and typography closely, with custom terminology and sensitive-word filtering for professional image localisation. Model Studio publishes no separate model page for it, so limits such as image size and output formats are not documented here. It is billed per output image: $0.0006 per image in Singapore, with 100 free images, and $0.000565 in China (Beijing).

## Strengths
- 55 source languages, five times Qwen-MT-Image.
- Very low per-image price.

## Limitations
- No model page with limits or formats.

## Good for
- Localising screenshots, posters and product images.
