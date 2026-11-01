---
id: qwen/qwen-plus-character
name: Qwen-Plus-Character
owned_by: qwen
type: llm
description: "Qwen-Plus-Character is Alibaba hosted Qwen role-playing model on Model Studio, tuned to follow character instructions, advance conversations and show empathy, with deep restoration of personalised characters."
context_length: 131072
max_output_tokens: 32768
capabilities: [structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-03-20"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-plus-character
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/role-play
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Plus-Character

## Overview
Qwen-Plus-Character (Model Studio id `qwen-plus-character`) is the Qwen role-playing model, first released on 2025-03-20 in China (Beijing), with later releases in other regions; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio calls it a dynamically updated version, with notice given before model updates, suited to anthropomorphic role-play, with better adherence to predefined character instructions, conversation advancement, active listening and empathy, and deep restoration of personalised characters. Limits are 131,072 tokens of context and input with 32,768 output tokens in Singapore, and 32,768 tokens in China (Beijing). It supports structured output and context caching, and web search in Beijing and Frankfurt, but not function calling. Prices per million tokens are $0.50 input, $1.40 output and $0.10 for cached input in Singapore, and $0.115, $0.287 and $0.023 in the Global regions.

## Strengths
- Consistent personas over long chats.
- Session cache discount for long role-play.

## Limitations
- No function calling.
- Context differs by region.

## Good for
- Companion apps, game characters and interactive fiction.
