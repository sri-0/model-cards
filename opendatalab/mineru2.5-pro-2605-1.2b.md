---
id: opendatalab/mineru2.5-pro-2605-1.2b
name: MinerU2.5-Pro-2605-1.2B
owned_by: opendatalab
type: llm
description: MinerU2.5-Pro-2605-1.2B is OpenDataLab's current Apache-2.0 1.2B document parser, the May 2026 update of MinerU2.5-Pro with cleaner layout detection and better chart, flowchart and seal analysis.
aliases: [opendatalab/MinerU2.5-Pro-2605-1.2B]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-05-21"
sources:
  - https://huggingface.co/opendatalab/MinerU2.5-Pro-2605-1.2B
  - https://huggingface.co/api/models/opendatalab/MinerU2.5-Pro-2605-1.2B
  - https://huggingface.co/opendatalab/MinerU2.5-Pro-2605-1.2B/raw/main/config.json
  - https://arxiv.org/abs/2604.04771
  - https://github.com/opendatalab/MinerU
  - https://github.com/opendatalab/mineru-vl-utils
  - https://github.com/opendatalab/OmniDocBench
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# MinerU2.5-Pro-2605-1.2B

## Overview
OpenDataLab announced MinerU2.5-Pro-2605 on 2026-05-21 under Apache 2.0 (Hugging Face repo created 2026-05-20). OpenRouter does not list it; the id follows the Hugging Face repo `opendatalab/MinerU2.5-Pro-2605-1.2B`. It keeps the 1.2B Qwen2-VL architecture of MinerU2.5 (1.16B parameters; config.json gives 32,768 positions at the top level and 8,192 in its text config, so no context length is recorded) and the data-centric training of MinerU2.5-Pro (arXiv 2604.04771). The update cleans layout data to cut category errors and missed `image_block` regions, and adds a large training set for image analysis, so charts, flowcharts and seals are read better. Parsing is two-pass: layout on a downsampled page, then recognition of crops, returned as JSON that `mineru-vl-utils` converts to Markdown with truncated-paragraph merging. This is the MinerU2.5-Pro checkpoint on OmniDocBench's leaderboard.

## Strengths
- OmniDocBench v1.6 overall 95.72 on its card (95.75 on the leaderboard), text edit distance 0.036, formula CDM 97.15, table TEDS 93.62.
- Image and chart parsing, in-table images and truncated-paragraph merging.
- 2.12 pages per second on one A100 with the vLLM async engine; transformers also works.

## Limitations
- Below PaddleOCR-VL-1.6 (96.34) and smaller newcomers such as OvisOCR2 (96.47) on the OmniDocBench v1.6 leaderboard.
- Cross-page table merging is still being integrated.
- Benchmark and model come from the same lab.

## Good for
- New MinerU deployments that need commercial-friendly weights.
- Chinese and English documents with charts, formulas and tables.
