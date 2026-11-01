---
id: paddlepaddle/paddleocr-vl
name: PaddleOCR-VL
owned_by: baidu
type: llm
description: PaddleOCR-VL is Baidu's 0.9B open-weight document-parsing vision-language model (NaViT-style encoder plus ERNIE-4.5-0.3B) that runs behind the PP-DocLayoutV2 layout model in the PaddleOCR pipeline.
aliases: [PaddlePaddle/PaddleOCR-VL, PaddleOCR-VL-0.9B]
context_length: 131072
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-16"
sources:
  - https://huggingface.co/PaddlePaddle/PaddleOCR-VL
  - https://huggingface.co/api/models/PaddlePaddle/PaddleOCR-VL
  - https://huggingface.co/PaddlePaddle/PaddleOCR-VL/raw/main/config.json
  - https://arxiv.org/abs/2510.14528
  - https://github.com/PaddlePaddle/PaddleOCR
  - https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL.html
  - https://www.paddleocr.ai/latest/en/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL.html
  - https://docs.vllm.ai/projects/recipes/en/latest/PaddlePaddle/PaddleOCR-VL.html
  - https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6-GGUF
  - https://openrouter.ai/api/v1/models
retrieved: "2026-10-16"
---

# PaddleOCR-VL

## Overview
PaddleOCR-VL was released on 2025-10-16 with PaddleOCR 3.3.0 under Apache 2.0. OpenRouter does not list it; the id follows the Hugging Face repo `PaddlePaddle/PaddleOCR-VL` under the PaddlePaddle organisation, filed here under Baidu. The VLM component, PaddleOCR-VL-0.9B, pairs a NaViT-style dynamic-resolution vision encoder with the ERNIE-4.5-0.3B decoder; config.json gives 131,072 positions. It is not a standalone page parser: the PaddleOCR pipeline (`pipeline_version="v1"`) first runs the PP-DocLayoutV2 layout model, then sends each crop to the VLM with a task prompt (`OCR:`, `Table Recognition:`, `Formula Recognition:`, `Chart Recognition:`) and assembles Markdown and JSON. It is superseded by 1.5 (January 2026) and 1.6 (May 2026).

## Strengths
- 109 languages spanning Latin, Cyrillic, Arabic, Devanagari, Thai and CJK scripts.
- Baidu reports state-of-the-art overall, text, formula, table and reading-order results on OmniDocBench v1.5 and v1.0, plus its in-house OCR, table, formula and chart sets, all published only as images.
- Served by the PaddleOCR pipeline, a vLLM server (`vllm serve PaddlePaddle/PaddleOCR-VL --trust-remote-code`, OpenAI-compatible), SGLang, FastDeploy, transformers with custom code, and llama.cpp through a community port.
- vLLM needs compute capability 8.0 and CUDA 12.6; PaddlePaddle or transformers inference needs 7.0 and CUDA 11.8.

## Limitations
- Running the VLM alone skips layout analysis; Baidu's docs say this lowers accuracy and can hallucinate text.
- Chart recognition is off by default (`use_chart_recognition=True`); the FAQ says fine-tuning is not yet supported.
- No seal recognition or text spotting; both arrived in 1.5.
- T4/V100 GPUs are not recommended for vLLM; official GGUF files exist only for 1.5 and 1.6.

## Good for
- Converting PDFs and scans to Markdown or JSON on modest hardware.
- Multilingual text, table, formula and chart extraction in batch.
- Deployments pinned to the v1 pipeline; new projects should start from 1.6.
