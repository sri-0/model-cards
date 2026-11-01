---
id: paddlepaddle/paddleocr-vl-1.5
name: PaddleOCR-VL-1.5
owned_by: baidu
type: llm
description: PaddleOCR-VL-1.5 is Baidu's multi-task 0.9B open-weight document-parsing VLM that adds seal recognition, text spotting and polygon localisation (via PP-DocLayoutV3) and reports 94.5% on OmniDocBench v1.5.
aliases: [PaddlePaddle/PaddleOCR-VL-1.5, PaddleOCR-VL-1.5-0.9B, PaddlePaddle/PaddleOCR-VL-1.5-GGUF]
context_length: 131072
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-01-29"
sources:
  - https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5
  - https://huggingface.co/api/models/PaddlePaddle/PaddleOCR-VL-1.5
  - https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5/raw/main/config.json
  - https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5-GGUF
  - https://arxiv.org/abs/2601.21957
  - https://ernie.baidu.com/blog/posts/paddleocr-vl-1.5/
  - https://github.com/PaddlePaddle/PaddleOCR
  - https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL.html
  - https://www.paddleocr.ai/latest/en/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL-1.5.html
  - https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL-Apple-Silicon.html
  - https://openrouter.ai/api/v1/models
retrieved: "2026-10-16"
---

# PaddleOCR-VL-1.5

## Overview
PaddleOCR-VL-1.5 was announced on 2026-01-29 (ERNIE blog, PaddleOCR 3.4.0; Hugging Face repo created 2026-01-28) under Apache 2.0. OpenRouter does not list it; the id follows the Hugging Face repo `PaddlePaddle/PaddleOCR-VL-1.5` under the PaddlePaddle organisation, filed here under Baidu. The VLM keeps the original 0.9B design (NaViT-style encoder plus ERNIE-4.5-0.3B, 958.6M parameters, 131,072 positions in config.json) but is retrained as a multi-task model with two new prompts, `Spotting:` and `Seal Recognition:`, beside OCR, table, formula and chart. In the PaddleOCR pipeline (`pipeline_version="v1.5"`) the layout stage is PP-DocLayoutV3, which localises irregular polygonal regions on skewed or warped pages; `restructure_pages` merges tables and heading levels across pages. Output is Markdown and JSON. Hugging Face marks 1.6, an architecture-compatible drop-in, as the newer version.

## Strengths
- Baidu reports 94.5% on OmniDocBench v1.5 and the best results in all five Real5-OmniDocBench scenarios: scanning, warping, screen photography, illumination and skew.
- 111 languages per the PaddleOCR README (109 plus Tibetan and Bengali), with better rare characters, ancient texts, multilingual tables, underlines and checkboxes.
- Serving: PaddleOCR pipeline (`paddleocr[doc-parser]>=3.4.0`, PaddlePaddle 3.2.1), Baidu's vLLM Docker image (`--model_name PaddleOCR-VL-1.5-0.9B`), SGLang, FastDeploy, MLX-VLM on Apple silicon, llama.cpp with the official GGUF repo (added 2026-03-06), and transformers 5.0 or later.

## Limitations
- The VLM alone is not the pipeline; Baidu warns that skipping layout analysis lowers accuracy and can hallucinate text.
- Spotting needs images under 1,500 px upscaled twofold and `max_pixels` raised to 1,605,632.
- Only the headline score is text; per-category OmniDocBench, Real5 and A100 timing figures are images.
- Superseded by PaddleOCR-VL-1.6.

## Good for
- Photographed or scanned documents with skew, warping or poor lighting.
- Stamp and seal reading, and text spotting that returns coordinates.
- Long reports where tables and headings continue across pages.
