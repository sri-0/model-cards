---
id: qwen/qwen-image-edit-2509
name: Qwen-Image-Edit-2509
owned_by: qwen
type: image
description: "Qwen-Image-Edit-2509 is the September 2025 Apache-2.0 open-weight update of the Qwen team's image editor, adding multi-image editing with one to three inputs, better person, product and text consistency, and native ControlNet support."
aliases: [Qwen/Qwen-Image-Edit-2509]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
open_weights: true
license: Apache-2.0
release_date: "2025-09-22"
sources:
  - https://huggingface.co/Qwen/Qwen-Image-Edit-2509
  - https://huggingface.co/api/models/Qwen/Qwen-Image-Edit-2509
  - https://github.com/QwenLM/Qwen-Image
  - https://arxiv.org/abs/2508.02324
  - https://artificialanalysis.ai/image/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Image-Edit-2509

## Overview
Qwen-Image-Edit-2509 was released on 2025-09-22 under Apache 2.0 as the monthly iteration of Qwen-Image-Edit. OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen-Image-Edit-2509. It keeps the Qwen-Image-Edit architecture and is further trained on concatenated images, so it edits across several inputs, such as person plus person, person plus product or person plus scene, with best results from one to three images. For single images Qwen reports better preservation of facial identity across portrait styles and pose changes, better product identity for poster edits, and text edits that change font, colour and material as well as content. It natively accepts ControlNet inputs such as depth maps, edge maps and keypoint maps, for example to change a person's pose. It loads with Diffusers' `QwenImageEditPlusPipeline`; the example uses 40 steps and a true CFG scale of 4.0. Qwen-Image-Edit-2511 (qwen/qwen-image-edit-2511) succeeded it in December 2025.

## Strengths
- Artificial Analysis image-editing Elo 965 (listed as Qwen Image Edit Plus 2509), well above the original Qwen-Image-Edit at 889.
- Multi-image composition and pose control.
- Apache 2.0 licence.

## Limitations
- Below Qwen-Image-Edit-2511 (991) on AA's editing arena.
- Qwen says results are best with one to three input images.

## Good for
- Product posters and person-plus-product composites.
- Pose and structure edits guided by ControlNet maps.
