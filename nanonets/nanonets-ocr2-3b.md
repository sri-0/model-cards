---
id: nanonets/nanonets-ocr2-3b
name: Nanonets-OCR2-3B
owned_by: nanonets
type: llm
description: Nanonets-OCR2-3B is Nanonets' open-weight image-to-Markdown OCR model, a Qwen2.5-VL-3B-Instruct fine-tune that tags images, signatures, watermarks and checkboxes and writes tables, equations and flowcharts in structured form.
aliases: [nanonets/Nanonets-OCR2-3B, mlx-community/Nanonets-OCR2-3B-bf16]
context_length: 128000
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
release_date: "2025-10-13"
sources:
  - https://huggingface.co/nanonets/Nanonets-OCR2-3B
  - https://huggingface.co/api/models/nanonets/Nanonets-OCR2-3B
  - https://huggingface.co/nanonets/Nanonets-OCR2-3B/raw/main/config.json
  - https://github.com/NanoNets/Nanonets-OCR2
  - https://nanonets.com/research/nanonets-ocr-2/
  - https://github.com/allenai/olmocr
  - https://github.com/opendatalab/OmniDocBench
  - https://docling-project.github.io/docling/usage/vision_models/
  - https://docling-project.github.io/docling/usage/model_catalog/
  - https://huggingface.co/mlx-community/Nanonets-OCR2-3B-bf16
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Nanonets-OCR2-3B

## Overview
Nanonets published Nanonets-OCR2-3B on Hugging Face on 2025-10-13 (the date used here; the vendor gives none) alongside Nanonets-OCR2-1.5B-exp; a larger Nanonets-OCR2-Plus is available only through Nanonets' Docstrange service. OpenRouter does not list it; the id follows the Hugging Face repo `nanonets/Nanonets-OCR2-3B`. It fine-tunes Qwen2.5-VL-3B-Instruct (3.75B parameters, 128,000 positions). Given a page image it writes Markdown with LaTeX equations (inline and display), tables in Markdown and HTML, flowcharts and organisation charts as Mermaid code, tagged image descriptions, signatures, watermarks and page numbers, and checkboxes as Unicode symbols. It also answers questions about a document, replying "Not mentioned" when the answer is absent. Neither the Hugging Face repo nor the GitHub repo states a licence.

## Strengths
- In Nanonets' pairwise Markdown tests it wins 52.4% against Gemini 2.5 Flash (no thinking) and 72.9% against GPT-5; DocVQA 89.43 and ChartQA 78.56 on the IDP leaderboard.
- Trained on handwriting and many languages, including English, Chinese, French, Spanish, German, Russian, Japanese, Korean and Arabic.
- Runs with transformers, `vllm serve nanonets/Nanonets-OCR2-3B`, and Docling's `nanonets_ocr2` preset (transformers, MLX, vLLM or an OpenAI-compatible API).

## Limitations
- olmOCR-bench 69.5 ± 1.1 in Ai2's table, with 32.1 on headers and footers.
- No licence on the weights, so commercial use is unclear.
- Accuracy depends on resolution; financial tables need `repetition_penalty=1` and a special prompt.

## Good for
- Converting forms, contracts and business documents for LLM pipelines.
- Document question answering over scanned pages.
