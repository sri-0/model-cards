---
id: baidu/qianfan-ocr
name: Qianfan-OCR
owned_by: baidu
type: llm
description: Qianfan-OCR is Baidu Qianfan's 4B open-weight end-to-end document-intelligence VLM (Qianfan-ViT plus Qwen3-4B) that converts pages straight to Markdown, with an optional Layout-as-Thought thinking phase in place of a separate layout model.
aliases: [baidu/Qianfan-OCR]
context_length: 32768
capabilities: [vision, reasoning]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-03-12"
sources:
  - https://huggingface.co/baidu/Qianfan-OCR
  - https://huggingface.co/api/models/baidu/Qianfan-OCR
  - https://huggingface.co/baidu/Qianfan-OCR/raw/main/config.json
  - https://arxiv.org/abs/2603.13398
  - https://github.com/baidubce/Qianfan-VL
  - https://github.com/baidubce/qianfan-models-cookbook
  - https://openrouter.ai/api/v1/models
retrieved: "2026-10-16"
---

# Qianfan-OCR

## Overview
Qianfan-OCR was announced on 2026-03-12 in Baidu's qianfan-models-cookbook (on Baidu AI Cloud, weights to follow); the Hugging Face repo and the Qianfan-VL README date the open weights to 2026-03-18, under Apache 2.0. OpenRouter does not list it; the id follows the Hugging Face repo `baidu/Qianfan-OCR`. It is a 4B end-to-end vision-language model (4.74B parameters in the safetensors): a 24-layer Qianfan-ViT AnyResolution encoder (up to 4K), a two-layer MLP adapter and a Qwen3-4B decoder. Unlike the PaddleOCR-VL pipeline it has no layout model: it writes Markdown directly, and the optional Layout-as-Thought mode (`enable_thinking=True`) first emits bounding boxes, 25 element types and reading order inside think tokens. The text config gives 32,768 positions (extendable to 131K per the card).

## Strengths
- Baidu reports OmniDocBench v1.5 overall 93.12 (first among end-to-end models; its own table places the PaddleOCR-VL-1.5 pipeline at 94.50), olmOCR-bench 79.8, OCRBench 880, a mean of 87.9 across five key-information-extraction benchmarks, ChartQA 88.1 and DocVQA 92.8.
- 192 languages across Latin, Cyrillic, Arabic, South and Southeast Asian and CJK scripts.
- Prompt-driven output: Markdown, JSON or HTML, HTML tables, LaTeX formulas, chart QA, key information extraction, document QA, handwriting and scene text.
- 1.024 pages per second with W8A8 on one A100 under vLLM 0.10.2 (0.503 in BF16); runs with transformers, vLLM (InternVLChatModel override) and on Baidu's Qianfan platform.

## Limitations
- Thinking mode is advised only for heterogeneous pages; it is slower (examples allow 16,384 new tokens).
- DocVQA and TextVQA trail Qwen3-VL-4B in Baidu's table.
- No GGUF, MLX or SGLang instructions; no OmniDocBench v1.6 or Real5-OmniDocBench results.

## Good for
- One-model parsing plus field extraction from invoices, receipts, certificates and ID cards.
- Chart reading and document QA, where OCR-then-LLM pipelines lose structure.
- Teams already on Baidu's Qianfan platform.
