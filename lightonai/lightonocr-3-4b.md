---
id: lightonai/lightonocr-3-4b
name: LightOnOCR-3-4B
owned_by: lightonai
type: llm
description: LightOnOCR-3-4B is the largest model of LightOn's Apache-2.0 LightOnOCR-3 family, a Qwen3.5-architecture OCR VLM that transcribes pages or, with the grounding prompt, returns labelled blocks with boxes, image descriptions and chart data.
aliases: [lightonai/LightOnOCR-3-4B]
context_length: 262144
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-10-08"
sources:
  - https://huggingface.co/lightonai/LightOnOCR-3-4B
  - https://huggingface.co/api/models/lightonai/LightOnOCR-3-4B
  - https://huggingface.co/lightonai/LightOnOCR-3-4B/raw/main/config.json
  - https://huggingface.co/blog/lightonai/lightonocr-3
  - https://github.com/lightonai/LightOnOCR
  - https://docling-project.github.io/docling/usage/vision_models/
  - https://docling-project.github.io/docling/usage/model_catalog/
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# LightOnOCR-3-4B

## Overview
LightOn released the LightOnOCR-3 family on 2026-10-08 under Apache 2.0 for research and commercial use (repo created 2026-10-06). OpenRouter does not list it; the id follows the Hugging Face repo `lightonai/LightOnOCR-3-4B`. It uses the Qwen3.5 vision-language architecture (4.54B parameters, 262,144 positions; LightOn says it is based on Qwen3.5-4B) and loads with the Qwen3.5 classes in transformers 5.2 or later, with thinking disabled. An empty prompt returns the page as Markdown, as with LightOnOCR-2. The `grounding` prompt prefixes each block with one of 16 labels (text, title, table, formula, chart, image, header, footer and others) and a box in 0 to 1,000 page coordinates, adds short image descriptions and turns charts into HTML tables of their data, for about 25% more output tokens (1,433 against 1,158 per page). Other instructions are out of distribution. LightOn recommends rendering at 400 DPI with a 2,048-pixel long side.

## Strengths
- In LightOn's runs: olmOCR-bench 86.3 (Chandra 2 85.8), ParseBench five-category overall 75.1 (first, with 66.1 on charts) and fr-bench-pdf2md 74.1.
- 3.36 pages per second on one H100 at 1,540 pixels; 21% more pages per second than Chandra OCR 2 on the same base at each model's benchmark setting.
- vLLM (0.30.0 or later), transformers and Docling's `lightonocr3_4b` preset.

## Limitations
- Infinity Parser Pro (35.1B) scores higher on olmOCR-bench (87.6), old scans and headers and footers.
- Scores use LightOn's published output normalisation; no OmniDocBench result.
- Slower than the 0.8B and 1B siblings.

## Good for
- Highest-accuracy LightOn OCR with layout, image and chart data in one pass.
- RAG ingestion that needs block boxes for citations.
