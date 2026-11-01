---
id: qwen/qwen-image-edit-plus
name: Qwen-Image-Edit-Plus
owned_by: qwen
type: image
description: "Qwen-Image-Edit-Plus is a hosted Model Studio image-editing model that speeds up and stabilises the original Qwen-Image-Edit and returns several images per request; its December 2025 snapshot adds better consistency, industrial design, geometric reasoning and built-in LoRA effects."
aliases: [qwen-image-edit-plus-2025-10-30, qwen-image-edit-plus-2025-12-15]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
open_weights: false
license: proprietary
release_date: "2025-10-30"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Image-Edit-Plus

## Overview
Status: Model Studio's current pricing and image-generation pages no longer list qwen-image-edit-plus or its snapshots; archived pricing pages show them on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for them. Qwen-Image-Edit-Plus (Model Studio id `qwen-image-edit-plus`) is a hosted editing model; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio documented the stable id as currently equivalent to `qwen-image-edit-plus-2025-10-30`, released on 2025-10-30 in China (Beijing) and 2025-10-31 in Singapore, which builds on the initial Qwen-Image-Edit with faster responses, better stability and several output images per request. The `qwen-image-edit-plus-2025-12-15` snapshot adds stronger character consistency, industrial design and geometric reasoning, built-in LoRA effects such as lighting, and less image drift; those are the same changes Qwen lists for the open Qwen-Image-Edit-2511, though Model Studio does not say they share weights. All three ids cost $0.03 per output image in Singapore and $0.028671 in China (Beijing).

## Strengths
- Lower latency than the original qwen-image-edit ($0.045 per image).
- Multiple outputs per call.

## Limitations
- No longer listed for sale on Model Studio.
- Artificial Analysis publishes no score under this id.
- Closed weights.

## Good for
- Interpreting older integrations that used qwen-image-edit-plus.
- Batch product and portrait edits through the API.
