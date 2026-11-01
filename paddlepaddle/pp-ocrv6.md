---
id: paddlepaddle/pp-ocrv6
name: PP-OCRv6
owned_by: baidu
type: llm
description: PP-OCRv6 is Baidu PaddleOCR's 2026 Apache-2.0 text detection and recognition family (tiny, small and medium, 1.5M to 34.5M parameters) on the PPLCNetV4 backbone, reading 50 languages with one model.
aliases: [PP-OCRv6_medium_det, PP-OCRv6_medium_rec, PP-OCRv6_small_det, PP-OCRv6_small_rec, PP-OCRv6_tiny_det, PP-OCRv6_tiny_rec, PaddlePaddle/PP-OCRv6_medium_det, PaddlePaddle/PP-OCRv6_medium_rec, PaddlePaddle/PP-OCRv6_small_det, PaddlePaddle/PP-OCRv6_small_rec, PaddlePaddle/PP-OCRv6_tiny_det, PaddlePaddle/PP-OCRv6_tiny_rec]
capabilities: [vision]
architecture:
  input_modalities: [image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-06-11"
sources:
  - https://huggingface.co/PaddlePaddle/PP-OCRv6_medium_det
  - https://huggingface.co/PaddlePaddle/PP-OCRv6_medium_rec
  - https://huggingface.co/PaddlePaddle/PP-OCRv6_small_rec
  - https://huggingface.co/PaddlePaddle/PP-OCRv6_tiny_rec
  - https://huggingface.co/api/models/PaddlePaddle/PP-OCRv6_medium_det
  - https://arxiv.org/abs/2606.13108
  - https://www.paddleocr.ai/latest/en/version3.x/algorithm/PP-OCRv6/PP-OCRv6.html
  - https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/OCR.html
  - https://www.paddleocr.ai/latest/en/version3.x/module_usage/text_detection.html
  - https://www.paddleocr.ai/latest/en/version3.x/module_usage/text_recognition.html
  - https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.7.0
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# PP-OCRv6

## Overview
PP-OCRv6 was released with PaddleOCR 3.7.0 on 2026-06-11 under Apache 2.0, with the report arXiv 2606.13108. OpenRouter does not list it; the id names the generation and the six detection and recognition models are aliases. Tiny (1.5M parameters), small (7.7M) and medium (34.5M) tiers target edge, mobile and server use. Detectors pair an LCNetV4 backbone with a RepLKFPN neck; recognisers use a light SVTR neck and a CTC head. Medium and small read 50 languages in one model (Simplified and Traditional Chinese, English, Japanese and 46 Latin-script languages; the Hugging Face card says 48); tiny drops Japanese. PP-OCRv6_medium is the default of PaddleOCR's general OCR pipeline and is published in Paddle, ONNX and safetensors formats.

## Strengths
- On Baidu's in-house benchmark, medium reaches 86.2 detection Hmean and 83.2% recognition accuracy against 81.6 and 78.1 for PP-OCRv5_server.
- Baidu reports higher recognition accuracy than Qwen3-VL-235B (74.9), Gemini-3.1-Pro (71.4) and GPT-5.5 (64.2), and detection far ahead of them (38 to 47 Hmean).
- 0.29 s per image end to end on an A100 for medium and 0.13 s for tiny; up to 5.2× faster on CPU with OpenVINO.
- Better on digital displays, dot-matrix print, tyre markings and industrial text.

## Limitations
- Every score comes from Baidu's own 16- and 15-category sets.
- Korean, Arabic, Cyrillic and Indic scripts still need the PP-OCRv5 language models.
- Text lines only; layout, tables and formulas need PP-StructureV3 or PaddleOCR-VL.

## Good for
- New PaddleOCR deployments and offline OCR on CPUs.
- Edge devices (tiny tier).
- Feeding clean text to an LLM without running a VLM.
