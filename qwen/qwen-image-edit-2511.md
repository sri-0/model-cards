---
id: qwen/qwen-image-edit-2511
name: Qwen-Image-Edit-2511
owned_by: qwen
type: image
description: "Qwen-Image-Edit-2511 is the Qwen team's Apache-2.0 open-weight image-editing model in the Qwen-Image line, improving on Qwen-Image-Edit-2509 with less image drift, steadier single- and multi-person consistency, built-in popular LoRAs and stronger geometric reasoning."
aliases: [Qwen/Qwen-Image-Edit-2511]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
open_weights: true
license: Apache-2.0
release_date: "2025-12-23"
sources:
  - https://huggingface.co/Qwen/Qwen-Image-Edit-2511
  - https://huggingface.co/api/models/Qwen/Qwen-Image-Edit-2511
  - https://github.com/QwenLM/Qwen-Image
  - https://arxiv.org/abs/2508.02324
  - https://artificialanalysis.ai/image/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Image-Edit-2511

## Overview
Qwen-Image-Edit-2511 was released on 2025-12-23 (Hugging Face repo created 2025-12-17) under Apache 2.0. OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen-Image-Edit-2511. It is the editing model of the Qwen-Image line, which Qwen describes as a 20B MMDiT image foundation model, and succeeds Qwen-Image-Edit-2509. It runs through Diffusers' `QwenImageEditPlusPipeline`, takes one or more input images with an English or Chinese instruction, and the example uses 40 inference steps with a true CFG scale of 4.0. Qwen lists five changes over 2509: less image drift, better character consistency, selected community LoRAs (such as lighting enhancement and new viewpoints) built into the base weights, stronger industrial-design generation, and stronger geometric reasoning such as drawing auxiliary construction lines. vLLM-Omni, SGLang-Diffusion and LightX2V supported it from release; LightX2V reports a 42.55x overall speedup with distillation. It is the newest checkpoint in the Qwen-Image-Edit line; the later Qwen-Image-2.1 (qwen/qwen-image-2.1) merges generation and editing under a non-commercial licence.

## Strengths
- Fuses separate portraits into one coherent group photo while keeping identities, per Qwen.
- Permissive licence that allows commercial use.

## Limitations
- Artificial Analysis image-editing Elo 991 (listed as Qwen Image Edit Plus 2511), well below Qwen-Image-2.1 at 1081.
- Editing only; text-to-image needs Qwen-Image-2512 or a newer generator.
- The model card publishes no benchmark tables.

## Good for
- Commercial product and portrait editing on self-hosted GPUs.
- Industrial design variants and material swaps.
