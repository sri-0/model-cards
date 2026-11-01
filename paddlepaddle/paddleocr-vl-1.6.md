---
id: paddlepaddle/paddleocr-vl-1.6
name: PaddleOCR-VL-1.6
owned_by: baidu
type: llm
description: PaddleOCR-VL-1.6 is Baidu's current 0.9B open-weight document-parsing VLM, architecture-identical to 1.5 but post-trained with targeted data and reinforcement learning to reach a reported 96.33% on OmniDocBench v1.6.
aliases: [PaddlePaddle/PaddleOCR-VL-1.6, PaddleOCR-VL-1.6-0.9B, PaddlePaddle/PaddleOCR-VL-1.6-GGUF]
context_length: 131072
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-05-28"
sources:
  - https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6
  - https://huggingface.co/api/models/PaddlePaddle/PaddleOCR-VL-1.6
  - https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6/raw/main/config.json
  - https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6-GGUF
  - https://arxiv.org/abs/2606.03264
  - https://github.com/PaddlePaddle/PaddleOCR
  - https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL.html
  - https://www.paddleocr.ai/latest/en/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL-1.6.html
  - https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL-Apple-Silicon.html
  - https://openrouter.ai/api/v1/models
retrieved: "2026-10-16"
---

# PaddleOCR-VL-1.6

## Overview
PaddleOCR-VL-1.6 was released on 2026-05-28 with PaddleOCR 3.6.0 (Hugging Face repo created 2026-05-27) under Apache 2.0; the technical report (arXiv 2606.03264) followed on 2026-06-02, announced on the card 2026-06-03. OpenRouter does not list it; the id follows the Hugging Face repo `PaddlePaddle/PaddleOCR-VL-1.6` under the PaddlePaddle organisation, filed here under Baidu. The VLM is the same 0.9B design as 1.5 (NaViT-style encoder plus ERNIE-4.5-0.3B, 131,072 positions in config.json), a drop-in swap; gains come from a data engine that targets under-optimised regions of 1.5 and three-stage post-training (continued pre-training, supervised fine-tuning, reinforcement learning). It remains a two-stage pipeline: layout analysis, then per-element recognition (OCR, table, formula, chart, seal, spotting prompts) assembled into Markdown and JSON. `pipeline_version="v1.6"` is the PaddleOCR default.

## Strengths
- Baidu reports 96.33% on OmniDocBench v1.6 and new best results on OmniDocBench v1.5 and Real5-OmniDocBench, leading text, formula and table recognition.
- Better complex tables, ancient Chinese books, rare characters, seals, spotting and charts than 1.5, at the same speed.
- Serving: PaddleOCR pipeline (`paddleocr[doc-parser]>=3.6.0`, PaddlePaddle 3.2.1 or later), Baidu Docker images for vLLM and FastDeploy (`--model_name PaddleOCR-VL-1.6-0.9B`), SGLang, MLX-VLM (`mlx-vlm>=0.3.11`, verified on an M4), llama.cpp with the official GGUF files (`llama-server`, `--temp 0`), transformers 5.0+, and DOCX export.

## Limitations
- Calling the VLM alone is not the pipeline and, per Baidu, hurts accuracy and can hallucinate.
- Spotting with GGUF needs `clip.vision.image_max_pixels` raised from 1,003,520 to 1,605,632.
- vLLM, SGLang and FastDeploy do not run natively on Windows; the FastDeploy image is about 43 GB.
- Per-category benchmark tables are images; no olmOCR-bench score is published.

## Good for
- The default choice for new PaddleOCR-VL deployments.
- Local use on Macs or CPUs through MLX-VLM or llama.cpp.
- Chinese historical and rare-character documents, seals and charts.
