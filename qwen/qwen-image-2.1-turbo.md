---
id: qwen/qwen-image-2.1-turbo
name: Qwen Image 2.1 Turbo
owned_by: qwen
type: image
description: "Qwen-Image-2.1-Turbo is the fast, low-cost tier of the Qwen-Image-2.1 series, an 8-step distilled checkpoint of the 7B-parameter unified generation and editing model, open-weight under the Qwen Research License and hosted on Model Studio and OpenRouter."
aliases: [qwen-image-2.1-turbo, Qwen/Qwen-Image-2.1-Turbo, qwen/qwen-image-2.1-turbo-20261016]
context_length: 65536
max_output_tokens: 58982
capabilities: [vision]
supported_parameters: [max_tokens, presence_penalty, response_format, seed, temperature, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
  tokenizer: Qwen
open_weights: true
license: Qwen Research License Agreement
release_date: "2026-10-09"
sources:
  - https://openrouter.ai/qwen/qwen-image-2.1-turbo
  - https://openrouter.ai/api/v1/models/qwen/qwen-image-2.1-turbo/endpoints
  - https://openrouter.ai/api/v1/models
  - https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo
  - https://huggingface.co/api/models/Qwen/Qwen-Image-2.1-Turbo
  - https://github.com/QwenLM/Qwen-Image-2.1
  - https://huggingface.co/Qwen/Qwen-Image-2.1/raw/main/LICENSE
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://artificialanalysis.ai/image/models
retrieved: "2026-11-01"
---

# Qwen Image 2.1 Turbo

## Overview
Qwen-Image-2.1-Turbo was released on 2026-10-09 as both open weights (Hugging Face repo Qwen/Qwen-Image-2.1-Turbo) and a hosted API (Model Studio id `qwen-image-2.1-turbo`, which Model Studio calls open-source). OpenRouter lists it as `qwen/qwen-image-2.1-turbo` (added 2026-10-16), served by Alibaba. It is an accelerated checkpoint of Qwen-Image-2.1 with the same 7B visual generation architecture, generating and editing images in 8 denoising steps with CFG 1; the saved schedule loads automatically in Diffusers' `QwenImage21Pipeline` (transformers 5.17 or later), and prefix KV caching reuses text and reference-image context across steps. Like the base model it handles transparent RGBA images and multi-reference editing; OpenRouter documents 1K and 2K output, up to six images and up to four reference images per request. OpenRouter charges $0.0184 per image at 1K and Model Studio $0.016 in Singapore; OpenRouter's per-token price fields read zero, so the card carries no `pricing`. Self-hosted weights fall under the Qwen Research License Agreement: research and evaluation only, with a separate licence needed for commercial use.

## Strengths
- Artificial Analysis image arena: Elo 1029 for text-to-image and 1064 for editing.
- Lowest price in the Qwen-Image-2.1 series and 8-step generation.

## Limitations
- Below Qwen-Image-2.1 and 2.1-Pro on both AA arenas.
- Setting `num_inference_steps` does not override the saved 8-step schedule.
- Non-commercial licence for the downloadable weights.

## Good for
- High-volume, low-cost generation and edits through the API.
- Fast local experiments on the Qwen-Image-2.1 architecture.
