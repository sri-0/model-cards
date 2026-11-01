---
id: qwen/qwen-image-layered
name: Qwen-Image-Layered
owned_by: qwen
type: image
description: "Qwen-Image-Layered is the Qwen team's Apache-2.0 open-weight model that decomposes an image into a variable number of RGBA layers, so each layer can be recoloured, replaced, moved, resized or deleted without affecting the rest."
aliases: [Qwen/Qwen-Image-Layered]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
open_weights: true
license: Apache-2.0
release_date: "2025-12-19"
sources:
  - https://huggingface.co/Qwen/Qwen-Image-Layered
  - https://huggingface.co/api/models/Qwen/Qwen-Image-Layered
  - https://github.com/QwenLM/Qwen-Image
  - https://arxiv.org/abs/2512.15603
  - https://artificialanalysis.ai/image/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Image-Layered

## Overview
Qwen-Image-Layered was released on 2025-12-19 (Hugging Face repo created 2025-12-17) under Apache 2.0, with the research paper arXiv 2512.15603 on 2025-12-18. OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen-Image-Layered. It takes an RGBA image, with an optional caption (it captions automatically otherwise), and returns several RGBA layers that separate semantic or structural parts of the picture. Each layer can then be edited on its own: recoloured, swapped (Qwen uses Qwen-Image-Edit for the target layer), retexted, deleted, resized without distortion or moved around the canvas, leaving the other layers untouched. The number of layers is variable (for example 3 or 8), and any layer can be decomposed again. It runs through Diffusers' `QwenImageLayeredPipeline` with transformers 4.51.3 or later; the example asks for 4 layers, 50 steps, a true CFG scale of 4.0 and the recommended 640 resolution bucket (1024 is the other option), and the quick start also installs python-pptx. vLLM-Omni supported it from release.

## Strengths
- Edits stay consistent because untouched content sits on separate layers.
- Recursive, variable-count decomposition.
- Apache 2.0 licence.

## Limitations
- Decomposition only; generating new content needs another model such as Qwen-Image-Edit.
- Qwen recommends the lower 640 resolution bucket for this version.
- Artificial Analysis lists no entry for it, and the model card publishes no benchmark tables.

## Good for
- Turning flat images into editable layers for design and slide work.
- Object removal, recolouring and repositioning with clean edges.
