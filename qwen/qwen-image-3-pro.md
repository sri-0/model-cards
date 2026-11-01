---
id: qwen/qwen-image-3-pro
name: Qwen Image 3 Pro
owned_by: qwen
type: image
description: "Qwen-Image-3.0-Pro is Alibaba's hosted flagship Qwen image generation and editing model, taking prompts of up to 4.5K tokens and rendering dense layouts and text down to 10 px in 12 languages at up to 2048x2048."
aliases: [qwen-image-3.0-pro, qwen/qwen-image-3-pro-20260805, dashscope/qwen-image-3.0-pro]
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
release_date: "2026-07-20"
sources:
  - https://openrouter.ai/qwen/qwen-image-3-pro
  - https://openrouter.ai/api/v1/models/qwen/qwen-image-3-pro/endpoints
  - https://openrouter.ai/api/v1/models
  - https://www.alibabacloud.com/help/en/model-studio/image-model
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://artificialanalysis.ai/image/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Qwen Image 3 Pro

## Overview
Qwen-Image-3.0-Pro (Model Studio id `qwen-image-3.0-pro`) is the top hosted model in Alibaba's Qwen Image line; no weights are published. OpenRouter lists it as `qwen/qwen-image-3-pro` (added 2026-08-05), served by Alibaba. One model id covers text-to-image and editing: prompts of up to 4.5K tokens, one to three input images, negative prompts, up to six images per call and 1K or 2K output up to 2048x2048. Model Studio says it lays out dense pages such as newspapers, storyboards, menus and exam papers in one pass, renders text as small as 10 px in 12 languages and 20+ fonts, reproduces fine detail such as pores and strands of hair, and simulates web, game and live-stream interfaces. Model Studio released it on 2026-07-20 and recommends it first for both generation and editing. OpenRouter charges $0.04 per output image at 1K, $0.075 at 2K and $0.003 per input image, the same as Model Studio's Singapore prices; its per-token price fields read zero, so the card carries no `pricing`.

## Strengths
- Artificial Analysis image arena: Elo 1095 for text-to-image and 1091 for image editing, the highest of the Qwen image models AA lists.
- Long, structured prompts and small multilingual text.

## Limitations
- Closed weights.
- At most three reference images; Model Studio suggests wan2.7-image-pro for up to nine references or output above 2K.

## Good for
- Posters, infographics, menus and interface mock-ups with exact text.
- Product and portrait edits from a few references.
