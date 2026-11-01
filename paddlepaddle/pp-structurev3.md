---
id: paddlepaddle/pp-structurev3
name: PP-StructureV3
owned_by: baidu
type: llm
description: PP-StructureV3 is PaddleOCR's Apache-2.0 document-parsing pipeline that chains layout detection, PP-OCRv5, table, formula, seal and optional chart models to turn PDFs and images into Markdown, JSON and Word.
aliases: [PP-StructureV3]
capabilities: [vision]
architecture:
  input_modalities: [image, file]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-05-20"
sources:
  - https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PP-StructureV3.html
  - https://www.paddleocr.ai/latest/en/version3.x/algorithm/PP-StructureV3/PP-StructureV3.html
  - https://www.paddleocr.ai/latest/en/version3.x/module_usage/layout_detection.html
  - https://huggingface.co/PaddlePaddle/PP-DocLayout_plus-L
  - https://huggingface.co/PaddlePaddle/PP-OCRv5_server_det
  - https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.0.0
  - https://arxiv.org/abs/2507.05595
  - https://arxiv.org/abs/2601.20552
  - https://github.com/opendatalab/OmniDocBench
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# PP-StructureV3

## Overview
PP-StructureV3 shipped with PaddleOCR 3.0.0 on 2025-05-20 under Apache 2.0. It is a pipeline (`paddleocr pp_structurev3`), not a single model, so it has no Hugging Face repo and OpenRouter does not list it; the id names the pipeline. Seven modules run in turn: layout detection (PP-DocLayout_plus-L, an RT-DETR-L model with 83.2 mAP@0.5 on Baidu's set, plus PP-DocBlockLayout for regions), general OCR (PP-OCRv5 server models by default), optional document preprocessing, table recognition (SLANeXt models), seal recognition, formula recognition (PP-FormulaNet_plus) and chart parsing with PP-Chart2Table, off by default. It restores multi-column reading order and saves JSON, Markdown and Word files from PDFs or images.

## Strengths
- PaddleOCR's OmniDocBench (v1.0) table gives overall edit distance 0.145 English and 0.206 Chinese, ahead of MinerU 0.9.3 (0.150, 0.357), Mathpix (0.191, 0.365) and Docling 2.14.0 (0.589, 0.909).
- OmniDocBench v1.5 overall 86.73, as cited from the OmniDocBench repo in arXiv 2601.20552.
- 1.12 s per page on an A100 with server OCR and PP-FormulaNet-L, 0.64 s with mobile OCR and PP-FormulaNet-M; runs on CPU, with PaddlePaddle or ONNX Runtime engines and a serving option.
- Each module can be swapped, fine-tuned or switched off.

## Limitations
- Behind VLM parsers on OmniDocBench v1.5: PaddleOCR-VL scores 92.86 and MinerU2.5 90.67 in the same table.
- Many models to download and configure.
- Chart parsing raises A100 time to 2.76 s per page; peak VRAM reaches about 22 GB in Baidu's A100 tests.

## Good for
- Document parsing on CPUs or modest GPUs without a VLM.
- Chinese documents with seals, formulas and complex tables.
- Pipelines that need per-module control.
