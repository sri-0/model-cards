---
id: qwen/qwen-mt-image
name: Qwen-MT-Image
owned_by: qwen
type: image
description: "Qwen-MT-Image is a hosted Model Studio image translation model that translates text in images across 11 languages while preserving layout, with terminology, sensitive-word filtering and product detection."
architecture:
  input_modalities: [image]
  output_modalities: [image]
open_weights: false
license: proprietary
release_date: "2025-08-22"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-mt-image
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-MT-Image

## Overview
Qwen-MT-Image (Model Studio id `qwen-mt-image`) is an image translation model released on 2025-08-22; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio says it translates images across 11 languages, such as Chinese, English and Japanese, into target languages while accurately preserving layout and content, and supports custom terminology, sensitive-word filtering and product detection for image localisation. It takes an image and returns an image, with no function calling or structured output, at 60 requests per minute in China (Beijing). The current pricing page lists it only for China (Beijing), at $0.000431 per output image. Qwen-MT-Image-2.0 (qwen/qwen-mt-image-2.0) expands the language range.

## Strengths
- Keeps the original layout while replacing text.
- Terminology and sensitive-word controls.

## Limitations
- 11 languages.
- China (Beijing) only on the current pricing page.

## Good for
- Localising product images for e-commerce.
