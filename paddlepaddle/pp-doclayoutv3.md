---
id: paddlepaddle/pp-doclayoutv3
name: PP-DocLayoutV3
owned_by: baidu
type: llm
description: PP-DocLayoutV3 is Baidu's 33M-parameter Apache-2.0 layout model that detects document elements with multi-point boxes and predicts reading order in one pass; it is the layout front end of PaddleOCR-VL-1.5 and 1.6.
aliases: [PaddlePaddle/PP-DocLayoutV3, PaddlePaddle/PP-DocLayoutV3_safetensors, PaddlePaddle/PP-DocLayoutV3_onnx]
capabilities: [vision]
architecture:
  input_modalities: [image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-01-20"
sources:
  - https://huggingface.co/PaddlePaddle/PP-DocLayoutV3
  - https://huggingface.co/PaddlePaddle/PP-DocLayoutV3_safetensors
  - https://huggingface.co/api/models/PaddlePaddle/PP-DocLayoutV3
  - https://huggingface.co/PaddlePaddle/PP-DocLayoutV3_safetensors/raw/main/config.json
  - https://arxiv.org/abs/2606.23344
  - https://huggingface.co/PaddlePaddle/PP-DocLayoutV2
  - https://www.paddleocr.ai/latest/en/version3.x/module_usage/layout_analysis.html
  - https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.4.0
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# PP-DocLayoutV3

## Overview
PP-DocLayoutV3's Hugging Face repo was created on 2026-01-20 under Apache 2.0, and it ships as the layout module of PaddleOCR-VL-1.5 (PaddleOCR 3.4.0, 2026-01-29) and 1.6. The technical report, arXiv 2606.23344 (2026-06-22, accepted at ECCV 2026), calls it RT-DocLayout. OpenRouter does not list it; the id follows `PaddlePaddle/PP-DocLayoutV3`. Built on RT-DETR, one query-based decoder classifies elements, regresses boxes, predicts pixel masks and orders the elements, so skewed, warped and photographed pages get multi-point boxes and a reading order without a separate sorting step. The safetensors config lists 25 labels, from paragraph titles, text, tables, formulas and charts to seals, headers and footnotes. Its predecessor PP-DocLayoutV2 (October 2025, PaddleOCR-VL 1.0) chains PP-DocLayout_plus-L with a six-layer pointer network for reading order (81.4 mAP@0.5 on Baidu's 1,000-image set). The Hugging Face card also names it the layout module of GLM-OCR and Xiaomi-OCR-0.

## Strengths
- With PaddleOCR-VL-1.5-0.9B as recogniser, OmniDocBench v1.5 overall is 94.50, the best of the layout modules Baidu tested, and 92.46% averaged over OmniDocBench and five Real5-OmniDocBench distortion sets.
- 33M parameters and 132.1 FPS on an A100 (batch 32).
- Reading-order edit distance 0.041 against 0.074 with XYCut.
- Paddle, transformers (`AutoModelForObjectDetection`) and ONNX weights.

## Limitations
- Scores are measured inside full parsers, not for layout alone.
- Boxes, labels and order only; text needs a recogniser.

## Good for
- Front end for PaddleOCR-VL or other recognisers.
- Photographed, curved or skewed pages.
