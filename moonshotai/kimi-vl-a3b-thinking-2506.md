---
id: moonshotai/kimi-vl-a3b-thinking-2506
name: Kimi-VL-A3B-Thinking-2506
owned_by: moonshotai
type: llm
description: Kimi-VL-A3B-Thinking-2506 is Moonshot AI's small open-weight (MIT) vision-language reasoning model, a 16B-total, 3B-active mixture-of-experts model that reads images, video and long documents with a 128K context.
aliases: [moonshotai/Kimi-VL-A3B-Thinking-2506]
context_length: 131072
capabilities: [reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-06-21"
sources:
  - https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking-2506
  - https://huggingface.co/api/models/moonshotai/Kimi-VL-A3B-Thinking-2506
  - https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking-2506/raw/main/config.json
  - https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Kimi-VL-A3B-Thinking-2506

## Overview
Kimi-VL-A3B-Thinking-2506 is the June 2025 update of Moonshot AI's Kimi-VL thinking model; the Hugging Face repo was created on 2025-06-21 and Moonshot asks users to prefer it over the original Kimi-VL-A3B-Thinking. Kimi-VL pairs the native-resolution MoonViT encoder with a mixture-of-experts language model of 16B total and about 3B activated parameters (2.8B in the decoder), fine-tuned from Kimi-VL-A3B-Instruct. It takes images, video and text and returns a `◁think▷` reasoning block followed by an answer. Context is 131,072 tokens and a single image can carry up to 3.2 million pixels, four times the earlier version. OpenRouter does not list it; the id follows the Hugging Face repo. Weights are MIT-licensed.

## Strengths
- Moonshot reports 56.9 on MathVision, 80.1 on MathVista, 64.0 on MMMU and 46.3 on MMMU-Pro, while using about 20% fewer thinking tokens than the first release.
- Unlike the first thinking release, it matches or beats Kimi-VL-A3B-Instruct on general perception: 84.4 on MMBench-EN-v1.1 and 869 on OCRBench.
- Video and GUI grounding: 65.2 on VideoMMMU, 52.8 on ScreenSpot-Pro and 52.5 on OSWorld-G, per Moonshot.

## Limitations
- Text-only skills are modest: Moonshot reports 42.3 on GPQA Diamond.
- Long outputs (up to 32K tokens); Moonshot recommends vLLM with flash-attn and temperature 0.8.
- No tool-calling format is documented.

## Good for
- Local multimodal reasoning on a single GPU: maths diagrams, charts and long PDFs.
- Screen understanding and GUI-agent grounding experiments.
