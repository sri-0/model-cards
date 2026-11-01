---
id: qwen/qvq-72b-preview
name: QVQ 72B Preview
owned_by: qwen
type: llm
description: QVQ 72B Preview is Qwen's December 2024 experimental open-weight visual reasoning model, built on Qwen2-VL-72B, that reasons step by step over a single image before answering.
aliases: [Qwen/QVQ-72B-Preview, qvq-72b-preview]
context_length: 128000
capabilities: [reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Qwen License Agreement
release_date: "2024-12-25"
sources:
  - https://huggingface.co/Qwen/QVQ-72B-Preview
  - https://huggingface.co/api/models/Qwen/QVQ-72B-Preview
  - https://huggingface.co/Qwen/QVQ-72B-Preview/raw/main/config.json
  - https://huggingface.co/Qwen/QVQ-72B-Preview/blob/main/LICENSE
  - https://qwenlm.github.io/blog/qvq-72b-preview/
  - https://github.com/QwenLM/Qwen3-VL
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# QVQ 72B Preview

## Overview
QVQ-72B-Preview is an experimental research model for visual reasoning, announced in the Qwen blog on 2024-12-25 (the Hugging Face repo was created 2024-12-24). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. Its base model is Qwen2-VL-72B; Hugging Face counts 73.4B parameters, and config.json sets 128,000 positions, which this card uses. The model card says it supports only single-round dialogue with images and no video input. Qwen's example system prompt asks it to think step by step. The weights use the Qwen License, which requires a separate licence for products with more than 100 million monthly active users. Alibaba Cloud Model Studio (archived 2026-06-06) lists qvq-72b-preview in the Beijing region only, at $1.721 per million input and $5.161 per million output tokens, with a 32,768-token window.

## Strengths
- Qwen reports MMMU 70.3, MathVista 71.4, MathVision 35.9 and OlympiadBench 20.4, against 64.5, 70.5, 25.9 and 11.2 for Qwen2-VL-72B.
- On MathVista it edges o1 (71.0) and leads GPT-4o (63.8) and Claude 3.5 Sonnet (65.3) in Qwen's table.

## Limitations
- o1 leads it on MMMU (77.3) and GPT-4o on OlympiadBench (25.9).
- Qwen lists language mixing, recursive reasoning loops, safety concerns, loss of focus on the image during long reasoning (causing hallucinations), and no gain over Qwen2-VL-72B on basic recognition of people, animals or plants.
- Single turn, single image, no video; no published knowledge cutoff.

## Good for
- Research on multimodal reasoning.
- Visual maths and science problems.
- Comparisons with later Qwen VL reasoning models.
