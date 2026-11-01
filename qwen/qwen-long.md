---
id: qwen/qwen-long
name: Qwen-Long
owned_by: qwen
type: llm
description: "Qwen-Long is Alibaba hosted ultra-long-context Qwen model on Model Studio, handling up to 10 million tokens with built-in parsing of text, office and image documents; Model Studio lists it as legacy."
aliases: [qwen-long-latest, qwen-long-2025-01-25, qwen-long-0125]
context_length: 10000000
max_output_tokens: 8192
capabilities: [structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-long
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Long

## Overview
Status: Model Studio's text generation page lists Qwen-Long among legacy models that are no longer recommended, and the current pricing page no longer prices it. Qwen-Long (Model Studio id `qwen-long`, with `qwen-long-latest` and the `qwen-long-2025-01-25` snapshot, also `qwen-long-0125`) is a hosted model with no published weights; OpenRouter does not list it, so the id is the DashScope model id, and Model Studio's release table gives no date. It handles dialogue over up to 10,000,000 tokens (about 15 million characters or 15,000 document pages) in Chinese, English and other languages, and integrates document services that parse TXT, DOCX, PDF, XLSX, EPUB, MOBI, MD and CSV files and BMP, PNG, JPG, GIF and scanned PDF images. HTTP requests carry up to 1M tokens; longer content should be submitted as files. Output is limited to 8,192 tokens, and structured output supports JSON Object mode only. The archived pricing page listed qwen-long-latest at $0.072 input and $0.287 output per million tokens in China (Beijing).

## Strengths
- 10M-token context for whole document collections.
- Built-in parsing of office files and scans.

## Limitations
- No function calling or thinking mode.
- Legacy; Model Studio no longer recommends it.

## Good for
- Question answering over very large document sets.
