---
id: qwen/qwen-vl-ocr
name: Qwen-VL-OCR
owned_by: qwen
type: llm
description: "Qwen-VL-OCR is Alibaba hosted OCR model on Model Studio, trained on Qwen-VL and, from its 2025-11-20 snapshot, the Qwen3-VL architecture, for image text recognition, document parsing and text localisation."
aliases: [qwen-vl-ocr-latest, qwen-vl-ocr-2025-11-20, qwen-vl-ocr-1120, qwen-vl-ocr-2025-08-28, qwen-vl-ocr-0828, qwen-vl-ocr-2025-04-13, qwen-vl-ocr-0413, qwen-vl-ocr-2024-10-28, qwen-vl-ocr-1028]
context_length: 38192
max_output_tokens: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-vl-ocr
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-VL-OCR

## Overview
Status: Model Studio's visual understanding page lists qwen-vl-ocr and its snapshots among legacy models that are no longer recommended; it is still priced. Qwen-VL-OCR (Model Studio id `qwen-vl-ocr`, documented as equivalent to `qwen-vl-ocr-2025-11-20`, also `qwen-vl-ocr-1120`) has dated snapshots from 2024-10-28 onwards and a `-latest` alias; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes an OCR model trained on Qwen-VL that unifies image-text recognition, parsing and processing tasks; the 2025-11-20 snapshot moves to the Qwen3-VL architecture and greatly improves document parsing and text localisation. The archived models page gives a 38,192-token context with up to 30,000 input tokens per image and 8,192 output tokens. The Singapore price is $0.07 input and $0.16 output per million tokens.

## Strengths
- Very low price for OCR and document parsing.
- Text localisation in the 2025-11-20 snapshot.

## Limitations
- Legacy; Qwen3.5-OCR is newer in China (Beijing).
- Short 38,192-token context.

## Good for
- Receipts, forms and scanned documents at volume.
