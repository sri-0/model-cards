---
id: lightonai/lightonocr-3-1b
name: LightOnOCR-3-1B
owned_by: lightonai
type: llm
description: LightOnOCR-3-1B is LightOn's Apache-2.0 1B OCR model that keeps the LightOnOCR-2 architecture as a drop-in upgrade while adding the LightOnOCR-3 grounding, image description and chart extraction modes.
aliases: [lightonai/LightOnOCR-3-1B]
context_length: 16384
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-10-08"
sources:
  - https://huggingface.co/lightonai/LightOnOCR-3-1B
  - https://huggingface.co/api/models/lightonai/LightOnOCR-3-1B
  - https://huggingface.co/lightonai/LightOnOCR-3-1B/raw/main/config.json
  - https://huggingface.co/blog/lightonai/lightonocr-3
  - https://github.com/lightonai/LightOnOCR
  - https://huggingface.co/lightonai/LightOnOCR-2-1B
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# LightOnOCR-3-1B

## Overview
LightOnOCR-3-1B is part of the LightOnOCR-3 family that LightOn released on 2026-10-08 under Apache 2.0 for research and commercial use (repo created 2026-10-07). OpenRouter does not list it; the id follows the Hugging Face repo `lightonai/LightOnOCR-3-1B`. Unlike its 0.8B and 4B siblings, which move to the Qwen3.5 architecture, it keeps the LightOnOCR-2 design (Pixtral-initialised encoder, Qwen3-architecture decoder; 1.01B parameters, 16,384 positions) and loads with the `LightOnOcr` classes in transformers 5 or later, so existing LightOnOCR-2 deployments can switch without changes. An empty prompt returns Markdown; the `grounding` prompt adds labelled blocks with 0 to 1,000 boxes, short image descriptions and chart data as HTML tables. Pages should be rendered at 200 DPI with a 1,540-pixel long side.

## Strengths
- In LightOn's runs: olmOCR-bench 84.5 with the best multi-column score of the family (85.9), ParseBench five-category 71.4 and fr-bench-pdf2md 69.6.
- Lowest single-page latency of the family, 2.7 s on an H100.
- Drop-in for LightOnOCR-2-1B in vLLM and transformers.

## Limitations
- Below the 0.8B model on most benchmarks, mainly charts (57.3 on ParseBench) and visual grounding (61.7), which LightOn attributes to not starting from a pre-trained VLM.
- Benchmarks are LightOn's own with its output normalisation; no OmniDocBench result.
- Instructions other than the empty and `grounding` prompts are out of distribution.

## Good for
- Upgrading LightOnOCR-2 deployments in place.
- Latency-sensitive single-page OCR.
