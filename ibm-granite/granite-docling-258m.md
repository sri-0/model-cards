---
id: ibm-granite/granite-docling-258m
name: Granite-Docling-258M
owned_by: ibm
type: llm
description: Granite-Docling-258M is IBM Research's Apache-2.0 258M-parameter document-conversion VLM (SigLIP2 encoder plus a Granite 165M decoder) that writes pages as DocTags for the Docling toolkit.
aliases: [ibm-granite/granite-docling-258M, ibm-granite/granite-docling-258M-mlx, ibm-granite/granite-docling-258M-GGUF, ggml-org/granite-docling-258M-GGUF, ibm/granite-docling, "ibm/granite-docling:258m"]
context_length: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-09-17"
sources:
  - https://huggingface.co/ibm-granite/granite-docling-258M
  - https://huggingface.co/api/models/ibm-granite/granite-docling-258M
  - https://huggingface.co/ibm-granite/granite-docling-258M/raw/main/config.json
  - https://huggingface.co/ibm-granite/granite-docling-258M-mlx
  - https://huggingface.co/ibm-granite/granite-docling-258M-GGUF
  - https://huggingface.co/ggml-org/granite-docling-258M-GGUF
  - https://www.ibm.com/new/announcements/granite-docling-end-to-end-document-conversion
  - https://www.ibm.com/granite/docs/models/docling
  - https://arxiv.org/abs/2605.19866
  - https://docling-project.github.io/docling/
  - https://docling-project.github.io/docling/usage/model_catalog/
  - https://docling-project.github.io/docling/usage/vision_models/
  - https://github.com/docling-project/docling
  - https://ollama.com/ibm/granite-docling
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Granite-Docling-258M

## Overview
IBM Research released Granite-Docling-258M on 2025-09-17 under Apache 2.0 as the product-ready successor to SmolDocling-256M-preview. OpenRouter does not list it; the id follows the Hugging Face repo `ibm-granite/granite-docling-258M`. It builds on Idefics3 with a siglip2-base-patch16-512 encoder, a pixel-shuffle projector and a Granite 165M decoder (257.5M parameters, 8,192 positions in config.json). It turns a page image into DocTags, IBM's markup that keeps layout, location and content apart; docling-core converts DocTags to Markdown, HTML or JSON. Prompts select full-page conversion or element tasks: chart to table, formula to LaTeX, code, OTSL tables and OCR of a given region. It is the default VLM of [Docling](https://docling-project.github.io/docling/), IBM's MIT-licensed conversion toolkit (an LF AI & Data project), whose standard pipeline instead chains the Heron layout model, OCR engines and TableFormer, with optional CodeFormulaV2 enrichment.

## Strengths
- IBM's card scores against SmolDocling: full-page OCR F1 0.84 (0.80), layout mAP 0.27 (0.23), code F1 0.988, equation F1 0.968, FinTabNet TEDS 0.97 structure and 0.96 with content (0.82, 0.76), OCRBench 500 (338).
- Fewer repetition loops than SmolDocling; experimental Japanese, Arabic and Chinese.
- Serving: Docling (`--pipeline vlm --vlm-model granite_docling`), transformers, vLLM, MLX, IBM's GGUF files with an mmproj projector, and Ollama (`ibm/granite-docling`).

## Limitations
- IBM's own OmniDocBench run (arXiv 2605.19866) gives English-subset edit distances of 0.78 text, 0.44 table and 0.69 reading order (lower is better) and Chinese table TEDS of 0.01; the two-stage variant does much better.
- Not meant for general image understanding; IBM recommends using it inside Docling.
- vLLM needs `--revision untied`; GPUs without bfloat16 (such as the T4) print only "!" unless run in float32.

## Good for
- Docling pipelines that want one small model for layout, tables, code and maths.
- CPU or Apple Silicon conversion of English PDFs for RAG.
