---
id: qwen/qwen-image-2512
name: Qwen-Image-2512
owned_by: qwen
type: image
description: "Qwen-Image-2512 is the December 2025 Apache-2.0 open-weight update of the Qwen team's 20B MMDiT text-to-image model, with more realistic people, finer natural detail and better text rendering than the August Qwen-Image release."
aliases: [Qwen/Qwen-Image-2512]
architecture:
  input_modalities: [text]
  output_modalities: [image]
open_weights: true
license: Apache-2.0
release_date: "2025-12-31"
sources:
  - https://huggingface.co/Qwen/Qwen-Image-2512
  - https://huggingface.co/api/models/Qwen/Qwen-Image-2512
  - https://github.com/QwenLM/Qwen-Image
  - https://arxiv.org/abs/2508.02324
  - https://artificialanalysis.ai/image/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Image-2512

## Overview
Qwen-Image-2512 was released on 2025-12-31 (Hugging Face repo created 2025-12-30) under Apache 2.0. OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen-Image-2512. It is the December update of Qwen-Image, which Qwen describes as a 20B MMDiT image foundation model, and covers text-to-image only; editing sits in Qwen-Image-Edit-2511 (qwen/qwen-image-edit-2511). Against the August release, Qwen lists three improvements: a much less "AI-generated" look and more realistic people, finer rendering of landscapes, animal fur and other natural detail, and more accurate text with better layout and text-image composition. It loads with Diffusers (`QwenImagePipeline`); the example uses 50 steps, a true CFG scale of 4.0, a negative prompt and presets from 1328x1328 (1:1) to 1664x928 (16:9) and 928x1664 (9:16). Qwen recommends its prompt-enhancing tool for this version. LightX2V's Qwen-Image-Lightning and vLLM-Omni supported it from release.

## Strengths
- Qwen says over 10,000 blind rounds on its AI Arena rank it the strongest open-source image model, competitive with closed systems.
- Permissive licence that allows commercial use.
- Strong Chinese and English text rendering, the Qwen-Image line's focus.

## Limitations
- Artificial Analysis lists no entry for this checkpoint.
- Text-to-image only; no editing.
- At 20B it is far larger than Qwen-Image-2.1's 7B generator; LightX2V's Lightning distillation is the faster option.

## Good for
- Commercial self-hosted generation of realistic portraits and scenes.
- Posters and signage with legible text.
