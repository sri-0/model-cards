---
id: qwen/qwen-doc-turbo
name: Qwen-Doc-Turbo
owned_by: qwen
type: llm
description: "Qwen-Doc-Turbo is a hosted Model Studio Qwen model for fast information extraction from documents, including tagging, classification, content moderation and summarisation, with a 262K-token context."
context_length: 262144
max_output_tokens: 8192
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-07-23"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-doc-turbo
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Doc-Turbo

## Overview
Qwen-Doc-Turbo (Model Studio id `qwen-doc-turbo`) is a document-processing model released on 2025-07-23 and available in China (Beijing); no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio says it rapidly extracts precise information from documents and supports tagging, classification, content moderation and summarisation. It takes text and returns text, with a 262,144-token context, up to 253,952 input and 8,192 output tokens, and context caching, but no function calling, structured output or web search. It allows 600 requests and 3,000,000 tokens per minute. The price is $0.087 input and $0.144 output per million tokens, with explicit cache creation at $0.109 and cache reads at $0.009.

## Strengths
- Very low price for long-document extraction.
- Explicit context caching.

## Limitations
- China (Beijing) only.
- No structured output despite its extraction focus.

## Good for
- Bulk document tagging, classification and summarisation.
