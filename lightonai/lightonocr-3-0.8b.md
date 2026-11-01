---
id: lightonai/lightonocr-3-0.8b
name: LightOnOCR-3-0.8B
owned_by: lightonai
type: llm
description: LightOnOCR-3-0.8B is the smallest model of LightOn's Apache-2.0 LightOnOCR-3 family, a Qwen3.5-architecture OCR VLM that nearly matches the 4B model on olmOCR-bench and ParseBench.
aliases: [lightonai/LightOnOCR-3-0.8B]
context_length: 262144
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-10-08"
sources:
  - https://huggingface.co/lightonai/LightOnOCR-3-0.8B
  - https://huggingface.co/api/models/lightonai/LightOnOCR-3-0.8B
  - https://huggingface.co/lightonai/LightOnOCR-3-0.8B/raw/main/config.json
  - https://huggingface.co/blog/lightonai/lightonocr-3
  - https://github.com/lightonai/LightOnOCR
  - https://docling-project.github.io/docling/usage/vision_models/
  - https://docling-project.github.io/docling/usage/model_catalog/
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# LightOnOCR-3-0.8B

## Overview
LightOnOCR-3-0.8B belongs to the LightOnOCR-3 family that LightOn released on 2026-10-08 under Apache 2.0 for research and commercial use (repo created 2026-10-07). OpenRouter does not list it; the id follows the Hugging Face repo `lightonai/LightOnOCR-3-0.8B`. It uses the Qwen3.5 vision-language architecture (853M parameters, 262,144 positions) and loads with the Qwen3.5 classes in transformers 5.2 or later, with thinking disabled. An empty prompt returns the page as Markdown; the `grounding` prompt prefixes each block with a label and a box in 0 to 1,000 page coordinates, adds short image descriptions and turns charts into HTML tables of their data. LightOn recommends rendering at 400 DPI with a 2,048-pixel long side.

## Strengths
- In LightOn's runs: olmOCR-bench 85.5 with the family's best long-tiny-text score (94.1), ParseBench five-category 74.6 (second only to the 4B) and fr-bench-pdf2md 70.5.
- 4.78 pages per second on one H100 at 1,540 pixels, the fastest of the family.
- vLLM (0.30.0 or later), transformers and Docling's `lightonocr3_08b` preset.

## Limitations
- Weaker than the 4B on handwriting (33.3 against 46.1 on fr-bench-pdf2md) and forms.
- Benchmarks are LightOn's own with its output normalisation; no OmniDocBench result.
- Instructions other than the empty and `grounding` prompts are out of distribution.

## Good for
- High-throughput OCR with layout boxes, image descriptions and chart data.
- Smaller GPUs and cost-sensitive batch jobs.
