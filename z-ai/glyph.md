---
id: z-ai/glyph
name: Glyph
owned_by: z-ai
type: llm
description: Glyph is an open-weight (MIT) research vision-language model in Z.ai's Hugging Face organisation that reads long text rendered as images, compressing input tokens 3-4x to stretch its effective context.
aliases: [zai-org/Glyph]
context_length: 131072
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-10-25"
sources:
  - https://huggingface.co/zai-org/Glyph
  - https://huggingface.co/api/models/zai-org/Glyph
  - https://huggingface.co/zai-org/Glyph/raw/main/config.json
  - https://github.com/thu-coai/Glyph
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Glyph

## Overview
Glyph is a framework and model for scaling context length through visual-text compression, published under Z.ai's Hugging Face organisation, with code at Tsinghua's thu-coai GitHub and the paper arXiv 2510.17800. The repository was created on 2025-10-25. Instead of feeding long text as tokens, Glyph renders it into page images and reads them with a vision-language model fine-tuned from GLM-4.1V-9B-Base, so each image token carries several words. The model itself has 131,072 positions in config.json. Rendering settings change the trade-off: at 72 DPI the authors report an average 3-4x compression, the best balance, and at 96 DPI 2-3x with usually better accuracy. English and Chinese rendering configurations and fonts ship with the code. OpenRouter does not list it; the id follows the Hugging Face repo. Weights are MIT-licensed.

## Strengths
- The authors report results matching text LLMs that use 3-4x longer contexts, and competitive LongBench and MRCR scores against its text backbone at 128K-token inputs.
- Faster prefill, decoding and training than the text backbone, with gains growing at longer sequence lengths.
- vLLM-accelerated serving, plus evaluation scripts for LongBench, MRCR and RULER.

## Limitations
- Sensitive to rendering resolution, font and spacing; post-training used one fixed configuration.
- Rare alphanumeric strings such as UUIDs are hard to read back from images, especially in very long inputs.
- Trained mainly for long-context understanding; broader abilities are untested.
- Rendering uses `reportlab`, which the authors say is still slow.

## Good for
- Research on long-context compression and vision-based reading.
- Question answering over very long documents on a single model of about 10B parameters.
