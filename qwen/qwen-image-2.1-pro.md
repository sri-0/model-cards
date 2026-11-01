---
id: qwen/qwen-image-2.1-pro
name: Qwen Image 2.1 Pro
owned_by: qwen
type: image
description: "Qwen-Image-2.1-Pro is the higher-quality hosted tier of Alibaba's Qwen-Image-2.1 series, a unified image generation and editing model with a 7B-parameter visual generator, transparent-image support and multi-reference editing."
aliases: [qwen-image-2.1-pro, qwen/qwen-image-2.1-pro-20261016]
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
release_date: "2026-10-02"
sources:
  - https://openrouter.ai/qwen/qwen-image-2.1-pro
  - https://openrouter.ai/api/v1/models/qwen/qwen-image-2.1-pro/endpoints
  - https://openrouter.ai/api/v1/models
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://github.com/QwenLM/Qwen-Image-2.1
  - https://artificialanalysis.ai/image/models
retrieved: "2026-11-01"
---

# Qwen Image 2.1 Pro

## Overview
Qwen-Image-2.1-Pro (Model Studio id `qwen-image-2.1-pro`) is the hosted higher-quality tier of the Qwen-Image-2.1 series; OpenRouter lists it as `qwen/qwen-image-2.1-pro` (added 2026-10-16), served by Alibaba, and recommends it over Turbo when fidelity matters more than cost or speed. Model Studio's release table dates it 2026-10-02, and Qwen announced the Pro and Turbo APIs on 2026-10-09. Model Studio describes it as unifying text-to-image and editing in one model with a 7B-parameter visual generation component, native generation and editing of transparent images, up to 10 reference images, local edits, and better preservation of people and products, typography and portrait lighting. OpenRouter documents 1K and 2K output, 13 aspect ratios, up to six images per request and up to four reference images. The open-weight Qwen-Image-2.1 checkpoint (qwen/qwen-image-2.1) shares the series description, but Qwen does not say the Pro API serves those weights, and AA rates the two separately. OpenRouter charges $0.046 per image at 1K; Model Studio's Singapore price is $0.04 per image. OpenRouter's per-token price fields read zero, so the card carries no `pricing`.

## Strengths
- Artificial Analysis image arena: Elo 1056 for text-to-image (above open Qwen-Image-2.1 at 1042) and 1069 for editing.
- Transparent RGBA output and multi-reference edits.

## Limitations
- Below Qwen-Image-3.0 and 3.0-Pro for text-to-image on AA, and below open Qwen-Image-2.1 (1081) for editing.
- Closed weights.

## Good for
- Transparent assets such as stickers and layered graphics.
- Identity-preserving edits of people and products.
