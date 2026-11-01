---
id: docling-project/smoldocling-256m-preview
name: SmolDocling-256M-preview
owned_by: ibm
type: llm
description: SmolDocling-256M-preview is IBM Research and Hugging Face's experimental 256M-parameter document-conversion VLM (a SmolVLM-256M fine-tune) that outputs DocTags; Granite-Docling-258M has replaced it.
aliases: [docling-project/SmolDocling-256M-preview, ds4sd/SmolDocling-256M-preview, docling-project/SmolDocling-256M-preview-mlx-bf16, ds4sd/SmolDocling-256M-preview-mlx-bf16]
context_length: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: CDLA-Permissive-2.0
release_date: "2025-03-14"
sources:
  - https://huggingface.co/docling-project/SmolDocling-256M-preview
  - https://huggingface.co/api/models/docling-project/SmolDocling-256M-preview
  - https://huggingface.co/docling-project/SmolDocling-256M-preview/raw/main/config.json
  - https://huggingface.co/docling-project/SmolDocling-256M-preview-mlx-bf16
  - https://arxiv.org/abs/2503.11576
  - https://www.ibm.com/new/announcements/granite-docling-end-to-end-document-conversion
  - https://docling-project.github.io/docling/usage/vision_models/
  - https://github.com/opendatalab/OmniDocBench
  - https://www.paddleocr.ai/latest/en/version3.x/algorithm/PP-StructureV3/PP-StructureV3.html
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# SmolDocling-256M-preview

## Overview
SmolDocling-256M-preview, from IBM Research's Docling team with Hugging Face, was described in arXiv 2503.11576 on 2025-03-14 (repo created 2025-02-12). The repo moved from `ds4sd` to `docling-project`; OpenRouter does not list it. It fine-tunes SmolVLM-256M-Instruct on the Idefics3 architecture (256.5M parameters, 8,192 positions) and writes DocTags that Docling exports to Markdown, HTML or JSON. Repository metadata gives CDLA-Permissive-2.0 while the card text says Apache 2.0. IBM now directs users to Granite-Docling-258M, which receives the updates.

## Strengths
- One model covers OCR, layout with bounding boxes, code with indentation, formulas, charts, OTSL tables, figure classification, caption linking and list grouping.
- About 0.35 s per page on an A100 with vLLM, per the card.
- Runs in Docling (`smoldocling` preset), transformers, vLLM, ONNX and MLX; Docling's docs time 6.2 s per page with MLX on an M3 Max against 102 s with transformers.

## Limitations
- OmniDocBench (v1.0) overall edit distance 0.493 English and 0.816 Chinese, with English table TEDS 44.9, in the leaderboard figures reproduced by PaddleOCR and dots.ocr.
- Prone to repeating one token in a loop; IBM fixed this in Granite-Docling.
- Trained on English; usable on Latin-script text only.
- A preview with no further updates.

## Good for
- Existing SmolDocling deployments and DocTags experiments.
- Baseline comparisons against Granite-Docling.
