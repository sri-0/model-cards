---
id: qwen/qwen-flash
name: Qwen-Flash
owned_by: qwen
type: llm
description: "Qwen-Flash is Alibaba Cloud Model Studio fast, low-cost hosted Qwen3 text model with switchable thinking and non-thinking modes and a 1M-token context, now listed as legacy."
aliases: [qwen-flash-2025-07-28, qwen-flash-us, qwen-flash-2025-07-28-us]
context_length: 1000000
max_output_tokens: 32768
capabilities: [tool_calling, reasoning, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-08-01"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-flash
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Flash

## Overview
Status: Model Studio's text generation page lists qwen-flash and its snapshots among legacy models that are no longer recommended; it is still priced. Qwen-Flash (Model Studio id `qwen-flash`, functionally equivalent to `qwen-flash-2025-07-28`, with `-us` ids for US deployment) was released on 2025-08-01 internationally and 2025-08-05 in China (Beijing) as the successor Model Studio recommended for Qwen-Turbo; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio calls it a Qwen3 model that switches between thinking and non-thinking modes within a conversation, with strong complex reasoning, instruction following and text comprehension. It has a 1,000,000-token context with 997,952 input and 32,768 output tokens, structured output, prefix completion and caching; function calling and web search are listed for China (Beijing). Singapore prices per million tokens are $0.05 input and $0.40 output up to 256K input, and $0.25 and $2 from 256K to 1M, with cached input at a fifth of the input price.

## Strengths
- Very low price with a 1M context.
- Thinking can be switched per request.

## Limitations
- Legacy; Model Studio recommends qwen3.8-flash.
- Function calling only listed for China (Beijing).

## Good for
- Existing integrations pinned to qwen-flash.
- Cheap long-document summarisation.
