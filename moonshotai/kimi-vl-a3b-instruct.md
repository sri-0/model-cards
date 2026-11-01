---
id: moonshotai/kimi-vl-a3b-instruct
name: Kimi-VL-A3B-Instruct
owned_by: moonshotai
type: llm
description: Kimi-VL-A3B-Instruct is Moonshot AI's small open-weight (MIT) non-thinking vision-language model, a 16B-total, 3B-active mixture-of-experts model for OCR, long video, long documents and GUI agents with a 128K context.
aliases: [moonshotai/Kimi-VL-A3B-Instruct]
context_length: 131072
capabilities: [vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-04-09"
sources:
  - https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct
  - https://huggingface.co/api/models/moonshotai/Kimi-VL-A3B-Instruct
  - https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct/raw/main/config.json
  - https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking-2506
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Kimi-VL-A3B-Instruct

## Overview
Kimi-VL-A3B-Instruct is the non-thinking model of Moonshot AI's Kimi-VL family, published on Hugging Face on 2025-04-09 with the technical report arXiv 2504.07491. It combines the native-resolution MoonViT vision encoder (about 0.4B), an MLP projector and a mixture-of-experts language model fine-tuned from Moonlight-16B-A3B, with 16B total and 2.8B activated decoder parameters. It reads single images, multiple images, video and long documents in a 128K context (131,072 positions in config.json). Moonshot recommends it for perception, OCR, long video, long documents and agent use, and recommends temperature 0.2. OpenRouter does not list it; the id follows the Hugging Face repo. Weights are MIT-licensed.

## Strengths
- Moonshot reports 867 on OCRBench, 83.2 on InfoVQA and 84.9 on AI2D.
- GUI grounding: 92.8 on ScreenSpot-V2 and 34.5 on ScreenSpot-Pro, with 8.22 on OSWorld.
- Long inputs: 64.5 on LongVideoBench, 72.6 on Video-MME with subtitles and 35.1 on MMLongBench-Doc.
- Only about 3B active parameters, so it runs on a single GPU.

## Limitations
- No reasoning mode; Moonshot points to the thinking models for maths and harder reasoning (21.4 on MathVision here).
- Kimi-VL-A3B-Thinking-2506 matches or beats it on most general perception benchmarks Moonshot reports.
- No tool-calling format is documented.

## Good for
- Low-latency OCR, chart and document question answering.
- Screen reading and GUI-agent grounding.
- Long-video summarisation on modest hardware.
