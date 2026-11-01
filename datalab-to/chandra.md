---
id: datalab-to/chandra
name: Chandra
owned_by: datalab
type: llm
description: Chandra is Datalab's first open-weight OCR model, a 9B Qwen3-VL-based VLM that converts images and PDFs to Markdown, HTML or JSON with layout, under a modified OpenRAIL-M licence.
aliases: [mlx-community/chandra-8bit]
context_length: 262144
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Modified OpenRAIL-M
release_date: "2025-10-21"
sources:
  - https://huggingface.co/datalab-to/chandra
  - https://huggingface.co/api/models/datalab-to/chandra
  - https://huggingface.co/datalab-to/chandra/raw/main/config.json
  - https://huggingface.co/datalab-to/chandra/raw/main/LICENSE
  - https://github.com/datalab-to/chandra
  - https://github.com/datalab-to/chandra/releases/tag/v0.1.0
  - https://github.com/allenai/olmocr
  - https://huggingface.co/datalab-to/chandra-ocr-2
  - https://huggingface.co/blog/lightonai/lightonocr-2
  - https://huggingface.co/mlx-community/chandra-8bit
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Chandra

## Overview
Datalab, the maker of Marker and Surya, released Chandra on 2025-10-21 (chandra-ocr v0.1.0). OpenRouter does not list it; the id follows the Hugging Face repo `datalab-to/chandra` under a new `datalab-to` directory. The weights use the AI Pubs OpenRAIL-M licence as modified by Datalab, while the code is Apache 2.0. It is a Qwen3-VL model (8.77B parameters, 262,144 positions in config.json) that converts pages to Markdown, HTML or JSON with detailed layout, reconstructs forms with checkboxes, handles handwriting, tables and maths, and extracts images and diagrams with captions. Datalab lists 40+ languages. The `chandra-ocr` package runs it through a vLLM server or transformers. Chandra OCR 2 (March 2026) replaces it.

## Strengths
- olmOCR-bench 83.1 ± 0.9 in Datalab's run, the highest entry in Ai2's olmOCR README table (olmOCR 2 82.4); 92.3 on long tiny text and 88.0 on tables.
- Strong handwriting and form reconstruction.
- Hosted API and free playground at Datalab.

## Limitations
- At about 9B parameters it is heavier than 1B-class parsers; LightOn reports LightOnOCR-2-1B 3.3× faster.
- The licence is free only for research, personal use and startups under $2M funding or revenue, and bars use that competes with Datalab's API.
- No OmniDocBench result published.
- Superseded by Chandra OCR 2 (85.8 on olmOCR-bench).

## Good for
- Handwritten forms, scanned records and tables.
- Teams already using Marker or Datalab's API.
