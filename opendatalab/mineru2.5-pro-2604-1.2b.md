---
id: opendatalab/mineru2.5-pro-2604-1.2b
name: MinerU2.5-Pro-2604-1.2B
owned_by: opendatalab
type: llm
description: MinerU2.5-Pro-2604-1.2B is OpenDataLab's April 2026 Apache-2.0 retraining of the MinerU2.5 1.2B parser on 65.5M curated pages, scoring 95.69 on OmniDocBench v1.6.
aliases: [opendatalab/MinerU2.5-Pro-2604-1.2B, carlesonielfa/MinerU2.5-Pro-2604-1.2B-mlx-bf16]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-04-02"
sources:
  - https://huggingface.co/opendatalab/MinerU2.5-Pro-2604-1.2B
  - https://huggingface.co/api/models/opendatalab/MinerU2.5-Pro-2604-1.2B
  - https://huggingface.co/opendatalab/MinerU2.5-Pro-2604-1.2B/raw/main/config.json
  - https://arxiv.org/abs/2604.04771
  - https://huggingface.co/opendatalab/MinerU2.5-Pro-2605-1.2B
  - https://github.com/opendatalab/MinerU
  - https://github.com/opendatalab/OmniDocBench
  - https://docling-project.github.io/docling/usage/vision_models/
  - https://docling-project.github.io/docling/usage/model_catalog/
  - https://huggingface.co/carlesonielfa/MinerU2.5-Pro-2604-1.2B-mlx-bf16
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# MinerU2.5-Pro-2604-1.2B

## Overview
OpenDataLab published MinerU2.5-Pro-2604 on Hugging Face on 2026-04-02 under Apache 2.0, with the report "MinerU2.5-Pro: Pushing the Limits of Data-Centric Document Parsing at Scale" (arXiv 2604.04771, 2026-04-06). OpenRouter does not list it; the id follows the Hugging Face repo `opendatalab/MinerU2.5-Pro-2604-1.2B`. The 1.2B Qwen2-VL architecture of MinerU2.5 is unchanged (1.16B parameters); config.json gives 32,768 positions at the top level and 8,192 in its text config, so no context length is recorded here. The gains come from data: 65.5M training samples chosen for diversity and difficulty, annotations checked by cross-model consistency and a judge-and-refine loop, and three-stage training ending in GRPO alignment. It adds image and chart parsing, truncated-paragraph merging and in-table images. The May update, MinerU2.5-Pro-2605, fixes layout misclassification.

## Strengths
- OmniDocBench v1.6 overall 95.69 against 92.98 for MinerU2.5, with text edit distance 0.036 and formula CDM 97.29; table TEDS up 5.54 points.
- Docling's `mineru2_pro` preset uses this checkpoint through transformers, MLX or an OpenAI-compatible API.
- Same `mineru-vl-utils` and vLLM workflow as MinerU2.5.

## Limitations
- OpenDataLab reports category errors in layout detection and missed `image_block` regions, fixed in 2605.
- OmniDocBench v1.6 is OpenDataLab's own protocol, introduced in this paper.
- Docling's preset does not enable image analysis or cross-page table merging.

## Good for
- Docling deployments using the `mineru2_pro` preset.
- Pinning results to the April 2026 weights.
