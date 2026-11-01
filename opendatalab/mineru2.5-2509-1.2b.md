---
id: opendatalab/mineru2.5-2509-1.2b
name: MinerU2.5-2509-1.2B
owned_by: opendatalab
type: llm
description: MinerU2.5-2509-1.2B is OpenDataLab's AGPL-3.0 1.2B document-parsing VLM that analyses layout on a downsampled page, then recognises text, formulas and tables on native-resolution crops.
aliases: [opendatalab/MinerU2.5-2509-1.2B, mlx-community/MinerU2.5-2509-1.2B-bf16]
context_length: 16384
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: AGPL-3.0
release_date: "2025-09-19"
sources:
  - https://huggingface.co/opendatalab/MinerU2.5-2509-1.2B
  - https://huggingface.co/api/models/opendatalab/MinerU2.5-2509-1.2B
  - https://huggingface.co/opendatalab/MinerU2.5-2509-1.2B/raw/main/config.json
  - https://arxiv.org/abs/2509.22186
  - https://github.com/opendatalab/MinerU
  - https://github.com/opendatalab/MinerU/releases/tag/mineru-2.5.0-released
  - https://github.com/opendatalab/mineru-vl-utils
  - https://github.com/opendatalab/OmniDocBench
  - https://arxiv.org/abs/2601.20552
  - https://github.com/allenai/olmocr
  - https://huggingface.co/mlx-community/MinerU2.5-2509-1.2B-bf16
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# MinerU2.5-2509-1.2B

## Overview
OpenDataLab released MinerU2.5 with MinerU 2.5.0 on 2025-09-19 under AGPL-3.0 (Hugging Face repo created 2025-09-17; report arXiv 2509.22186). OpenRouter does not list it; the id follows the Hugging Face repo `opendatalab/MinerU2.5-2509-1.2B`. It uses the Qwen2-VL architecture (a 32-layer vision encoder and a 24-layer decoder; 1.16B parameters, 16,384 positions). Parsing runs in two passes of the same model: layout analysis on a downsampled page, then recognition of each detected text, formula or table region from a native-resolution crop, keeping headers, footers and page numbers with a refined label set. `mineru-vl-utils` wraps the prompts for transformers and vLLM, and the hosted MinerU Open API uses the model in production. OpenDataLab also maintains OmniDocBench.

## Strengths
- OmniDocBench v1.5 overall 90.67 (as cited in arXiv 2601.20552) and v1.6 overall 93.04 on the official leaderboard.
- Long or mixed Chinese-English formulas, and rotated, borderless or partly ruled tables.
- 2.12 pages per second on one A100 with the vLLM async engine; community MLX weights.

## Limitations
- AGPL-3.0 weights, unlike the Apache-2.0 MinerU2.5-Pro.
- Superseded: MinerU2.5-Pro scores 95.69 to 95.75 on OmniDocBench v1.6 with the same architecture.
- olmOCR-bench 75.2 for MinerU 2.5.4 in Ai2's table, below Chandra and olmOCR 2.
- Two passes per page; image and chart parsing came only with the Pro models.

## Good for
- Chinese and English papers, reports and textbooks with formulas and tables.
- Existing MinerU 2.5 pipelines.
