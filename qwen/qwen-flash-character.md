---
id: qwen/qwen-flash-character
name: Qwen-Flash-Character
owned_by: qwen
type: llm
description: "Qwen-Flash-Character is the low-cost Qwen role-playing model on Model Studio, tuned for multilingual anthropomorphic interaction with character consistency and Japanese localisation."
context_length: 32768
max_output_tokens: 32768
capabilities: [structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2026-01-13"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-flash-character
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Flash-Character

## Overview
Qwen-Flash-Character (Model Studio id `qwen-flash-character`) is a role-playing model released on 2026-01-13 in China (Beijing) and Singapore and on 2026-08-30 in US (Virginia); no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes the role-playing series as optimised here for multilingual anthropomorphic interaction, with character consistency, context-aware dialogue progression, empathetic engagement and improved Japanese localisation, including dialects and honorifics. Limits are 32,768 tokens of context, input and output in Singapore, and an 8,192-token context with 4,096 output tokens in China (Beijing). It supports structured output and context caching, and web search in Beijing, but not function calling. Prices per million tokens are $0.05 input, $0.40 output and $0.01 for cached input in Singapore, and $0.034, $0.203 and $0.007 in US (Virginia).

## Strengths
- A tenth of Qwen-Plus-Character input price.
- Session cache discount.

## Limitations
- Shorter context than Qwen-Plus-Character in Singapore.
- No function calling.

## Good for
- High-volume character chat.
