---
id: lightonai/lightonocr-1b-1025
name: LightOnOCR-1B-1025
owned_by: lightonai
type: llm
description: LightOnOCR-1B-1025 is LightOn's first Apache-2.0 end-to-end OCR model, a 1B VLM pairing a Pixtral vision encoder with a Qwen3 decoder that turns European-language PDF pages into Markdown at 5.71 pages per second on an H100.
aliases: [lightonai/LightOnOCR-1B-1025]
context_length: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-23"
sources:
  - https://huggingface.co/lightonai/LightOnOCR-1B-1025
  - https://huggingface.co/api/models/lightonai/LightOnOCR-1B-1025
  - https://huggingface.co/lightonai/LightOnOCR-1B-1025/raw/main/config.json
  - https://huggingface.co/blog/lightonai/lightonocr
  - https://huggingface.co/lightonai/LightOnOCR-0.9B-32k-1025
  - https://huggingface.co/lightonai/LightOnOCR-0.9B-16k-1025
  - https://arxiv.org/abs/2601.14251
  - https://huggingface.co/lightonai/LightOnOCR-2-1B
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# LightOnOCR-1B-1025

## Overview
LightOn announced LightOnOCR-1B on 2025-10-23 (Hugging Face repo created 2025-10-20) under Apache 2.0. OpenRouter does not list it; the id follows the Hugging Face repo `lightonai/LightOnOCR-1B-1025` under a new `lightonai` directory. It joins a native-resolution vision transformer initialised from Pixtral (the Mistral 3.1 ViT) to a Qwen3-architecture language model through a new projection layer that downsamples vision tokens by four (1.16B parameters, 8,192 positions). It was distilled from larger open VLMs on a large PDF corpus of papers, books, receipts, invoices, tables, forms and handwriting, mostly in Latin-script European languages. It is end to end: one page image in, full-page Markdown out, with no layout stage. Two pruned-vocabulary variants (32k and 16k tokens, LightOnOCR-0.9B-32k-1025 and -16k-1025) trade language coverage for speed.

## Strengths
- 5.71 pages per second on one H100 (about 493,000 pages a day), under $0.01 per 1,000 pages by LightOn's estimate.
- LightOn reports it 5× faster than dots.ocr, 2× faster than PaddleOCR-VL-0.9B and 1.73× faster than DeepSeek-OCR, with olmOCR-bench quality on par with dots.ocr and 16 points above Qwen3-VL-2B.
- Upstream vLLM support since v0.11.1; fully differentiable for LoRA fine-tuning.

## Limitations
- Not optimised for Chinese; LightOn publishes no OmniDocBench score.
- Superseded by LightOnOCR-2-1B and the LightOnOCR-3 family.
- Pages should be rendered at about 1,540 pixels on the long side.

## Good for
- High-volume English and European-language PDF conversion on a single GPU.
- A small base for domain fine-tuning.
