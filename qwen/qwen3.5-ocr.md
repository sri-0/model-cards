---
id: qwen/qwen3.5-ocr
name: Qwen3.5-OCR
owned_by: qwen
type: llm
description: "Qwen3.5-OCR is Alibaba hosted OCR model on Model Studio with improved document parsing, text localisation and key information extraction from real-world documents such as ID cards and driving licences."
context_length: 65536
max_output_tokens: 16384
capabilities: [vision]
architecture:
  input_modalities: [image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2026-06-16"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-5-ocr
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.5-OCR

## Overview
Qwen3.5-OCR (Model Studio id `qwen3.5-ocr`) is an OCR model released on 2026-06-16 and available in China (Beijing); no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio calls it an upgraded OCR model with better document parsing, text localisation and key information extraction, and much stronger extraction from real-world documents such as ID cards and driving licences. It takes an image and returns text, with a 65,536-token context, up to 49,152 input and 16,384 output tokens, and no function calling or structured output. It allows 6,000 requests and 30,000,000 tokens per minute. The price is $0.069 input and $0.275 output per million tokens.

## Strengths
- Key information extraction from identity documents.
- Very high rate limits.

## Limitations
- China (Beijing) only.
- No structured output.

## Good for
- Bulk ID, licence and form processing in China.
