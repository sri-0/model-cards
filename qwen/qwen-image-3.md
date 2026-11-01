---
id: qwen/qwen-image-3
name: Qwen Image 3
owned_by: qwen
type: image
description: "Qwen-Image-3.0 is the faster, lower-priced standard tier of Alibaba's hosted Qwen-Image-3.0 generation and editing model, with prompts up to 4.5K tokens, text rendering down to 10 px in 12 languages and up to 2048x2048 output."
aliases: [qwen-image-3.0, qwen/qwen-image-3-20260805, dashscope/qwen-image-3.0]
context_length: 65536
max_output_tokens: 58982
capabilities: [vision]
supported_parameters: [max_tokens, presence_penalty, response_format, seed, temperature, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
  tokenizer: Qwen
open_weights: false
license: proprietary
release_date: "2026-08-04"
sources:
  - https://openrouter.ai/qwen/qwen-image-3
  - https://openrouter.ai/api/v1/models/qwen/qwen-image-3/endpoints
  - https://openrouter.ai/api/v1/models
  - https://www.alibabacloud.com/help/en/model-studio/image-model
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://artificialanalysis.ai/image/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Qwen Image 3

## Overview
Qwen-Image-3.0 (Model Studio id `qwen-image-3.0`) is the standard tier of Qwen-Image-3.0, which Model Studio describes as a faster version of qwen-image-3.0-pro; no weights are published. OpenRouter lists it as `qwen/qwen-image-3` (added 2026-08-05), served by Alibaba. The same id handles text-to-image and editing, with up to three reference images, negative prompts, up to six outputs per call and resolutions up to 2048x2048. Model Studio says it follows prompts of up to 4.5K tokens in one pass, renders 10 px text clearly in 12 languages and 20+ fonts for infographics and interfaces, and suits batch output of posters, web pages and similar daily tasks at lower cost. Model Studio released it on 2026-08-04. OpenRouter charges $0.03 per output image at 1K and $0.003 per input image; Model Studio's Singapore price is $0.03 per output image at both 1K and 2K. OpenRouter's per-token price fields read zero, so the card carries no `pricing`.

## Strengths
- Artificial Analysis image arena: Elo 1070 for text-to-image and 1068 for image editing.
- Same flat output price at 2K as at 1K on Model Studio.

## Limitations
- Below Qwen-Image-3.0-Pro on both AA arenas (1095 and 1091).
- Closed weights; at most three reference images.

## Good for
- Bulk posters, banners and interface images with readable text.
- Everyday edits where Pro's 2K price is not needed.
