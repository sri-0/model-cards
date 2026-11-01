---
id: qwen/qwen-image-2.1
name: Qwen-Image-2.1
owned_by: qwen
type: image
description: "Qwen-Image-2.1 is the Qwen team's open-weight unified text-to-image and image-editing model with a 7B-parameter visual generator, native 2K output, transparent RGBA images and up to 10 reference images, released under the non-commercial Qwen Research License."
aliases: [Qwen/Qwen-Image-2.1]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
open_weights: true
license: Qwen Research License Agreement
release_date: "2026-09-20"
sources:
  - https://huggingface.co/Qwen/Qwen-Image-2.1
  - https://huggingface.co/api/models/Qwen/Qwen-Image-2.1
  - https://huggingface.co/Qwen/Qwen-Image-2.1/raw/main/LICENSE
  - https://github.com/QwenLM/Qwen-Image-2.1
  - https://artificialanalysis.ai/image/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Image-2.1

## Overview
Qwen-Image-2.1 was released on 2026-09-20 (Hugging Face repo created 2026-09-14). OpenRouter does not list this checkpoint; the id follows the Hugging Face repo Qwen/Qwen-Image-2.1. It combines text-to-image generation and image editing in one model with a 7B-parameter visual generation component (32 single-stream DiT layers), mixed-granularity attention and prefix KV-cache reuse. It generates regular or transparent RGBA images, edits transparent layers, extracts subjects from photos, accepts up to 10 reference images and takes local edit marks such as circles, painted annotations or masks. Native resolution is 2048x2048 with presets from 16:9 to 9:16, and the default is 40 denoising steps. Diffusers (`QwenImage21Pipeline`, transformers 5.17 or later), ComfyUI, vLLM-Omni, SGLang, LightX2V and OpenVINO supported it from day one. Qwen also ships two Qwen3.5-VL 9B prompt-rewriting models for short prompts. Separate cards cover the 8-step Turbo checkpoint (qwen/qwen-image-2.1-turbo) and the hosted Pro API (qwen/qwen-image-2.1-pro).

## Strengths
- Artificial Analysis image arena: Elo 1042 for text-to-image and 1081 for image editing, second among Qwen models for editing after Qwen-Image-3.0-Pro.
- Improved typography, portrait lighting and fine detail, per Qwen.
- Multi-reference edits that keep people and products consistent.

## Limitations
- Non-commercial: the Qwen Research License allows research and evaluation only; commercial use needs a separate licence from Qwen.
- On AA's text-to-image arena it trails Qwen-Image-2.1-Pro (1056) and Qwen-Image-3.0 (1070).
- The model card publishes no benchmark tables.

## Good for
- Research on unified generation and editing, including transparent assets.
- Local prototyping with a 7B visual generator.
