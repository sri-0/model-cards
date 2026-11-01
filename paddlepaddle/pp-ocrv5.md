---
id: paddlepaddle/pp-ocrv5
name: PP-OCRv5
owned_by: baidu
type: llm
description: PP-OCRv5 is Baidu PaddleOCR's Apache-2.0 text detection and recognition model pair, in server and mobile tiers, for printed and handwritten Simplified Chinese, Pinyin, Traditional Chinese, English and Japanese.
aliases: [PP-OCRv5_server_det, PP-OCRv5_server_rec, PP-OCRv5_mobile_det, PP-OCRv5_mobile_rec, PaddlePaddle/PP-OCRv5_server_det, PaddlePaddle/PP-OCRv5_server_rec, PaddlePaddle/PP-OCRv5_mobile_det, PaddlePaddle/PP-OCRv5_mobile_rec]
capabilities: [vision]
architecture:
  input_modalities: [image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-05-20"
sources:
  - https://huggingface.co/PaddlePaddle/PP-OCRv5_server_det
  - https://huggingface.co/PaddlePaddle/PP-OCRv5_server_rec
  - https://huggingface.co/PaddlePaddle/PP-OCRv5_mobile_det
  - https://huggingface.co/PaddlePaddle/PP-OCRv5_mobile_rec
  - https://huggingface.co/api/models/PaddlePaddle/PP-OCRv5_server_det
  - https://huggingface.co/PaddlePaddle
  - https://www.paddleocr.ai/latest/en/version3.x/algorithm/PP-OCRv5/PP-OCRv5.html
  - https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/OCR.html
  - https://www.paddleocr.ai/latest/en/version3.x/module_usage/text_detection.html
  - https://www.paddleocr.ai/latest/en/version3.x/module_usage/text_recognition.html
  - https://www.paddleocr.ai/latest/en/version3.x/algorithm/PP-OCRv6/PP-OCRv6.html
  - https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.0.0
  - https://arxiv.org/abs/2507.05595
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# PP-OCRv5

## Overview
PP-OCRv5 shipped with PaddleOCR 3.0.0 on 2025-05-20 under Apache 2.0 (Hugging Face repos created 2025-06-04). OpenRouter does not list it, and there is no single repo: the id names the generation and the component models are aliases. Each tier pairs a text detector, which finds text lines, with a recogniser, which reads them: PP-OCRv5_server_det (84.3 MB) with PP-OCRv5_server_rec (81 MB), and PP-OCRv5_mobile_det (4.7 MB) with PP-OCRv5_mobile_rec (16 MB). Baidu also publishes language-specific mobile recognisers (Korean, Latin, East Slavic, Cyrillic, Arabic, Devanagari, Thai, Greek, Tamil, Telugu, English) plus ONNX and safetensors repos. The OCR pipeline can add document orientation, unwarping and text-line orientation models and returns text lines with boxes and scores. Since PaddleOCR 3.7 (2026-06-11) the pipeline defaults to PP-OCRv6; `ocr_version="PP-OCRv5"` selects this generation.

## Strengths
- Baidu reports a 13-point end-to-end gain over PP-OCRv4 on internal multi-scenario sets: average detection Hmean 0.827 (server) against 0.662, weighted recognition accuracy 0.840 against 0.574.
- Handles handwriting, vertical text, rare characters and Japanese in one model.
- Runs on CPU, GPU, mobile and the browser through PaddlePaddle, ONNX Runtime, transformers or C++.

## Limitations
- Superseded: PP-OCRv6_medium scores +4.6 detection and +5.1 recognition points over PP-OCRv5_server on Baidu's set.
- Slower than PP-OCRv4 because of its larger dictionary: 0.62 s against 0.29 s per image (mobile, V100).
- Text lines only, no layout, tables or formulas; all scores are internal.

## Good for
- Existing PaddleOCR 3.0 to 3.6 deployments.
- CPU or mobile OCR where a VLM is too heavy.
