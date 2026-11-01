---
id: openai/o3-pro
name: o3 Pro
owned_by: openai
type: llm
description: o3-pro is the extra-compute version of o3 served through the Responses API, deprecated for removal from OpenAI's API on 2026-12-11.
aliases: [o3-pro, o3-pro-2025-06-10, azure/o3-pro, azure/o3-pro-2025-06-10]
context_length: 200000
max_output_tokens: 100000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools]
architecture:
  input_modalities: [text, file, image]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-06-10"
knowledge_cutoff: "2024-06"
pricing:
  input: 20
  output: 80
benchmarks:
  gpqa_diamond: 84.5
benchmark_variant: o3-pro
sources:
  - https://openrouter.ai/openai/o3-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/o3-pro
  - https://developers.openai.com/api/docs/models/o3-pro
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# o3 Pro

## Overview
o3-pro is the version of o3 that OpenAI runs with more compute per request, released on 2025-06-10 (Artificial Analysis date; pinned snapshot `o3-pro-2025-06-10`). OpenAI and OpenRouter say it thinks harder to give consistently better answers; OpenRouter marks reasoning as mandatory. It takes text and images and returns text, with a 200,000-token context window, 100,000 max output tokens and a June 2024 knowledge cutoff. It is available in the Responses API only (plus Batch), with function calling, structured outputs and image input; OpenAI recommends background mode because some requests take several minutes. The price is $20 input and $80 output per million tokens on OpenRouter and OpenAI ($10 and $40 in OpenAI's batch), with no cached-input rate. OpenAI marks it Deprecated: announced 2026-06-11, it leaves the API on 2026-12-11 with `gpt-5.6-sol` using `reasoning.mode: pro` as the recommended replacement; Artificial Analysis names GPT-5 as its successor.

## Strengths
- Artificial Analysis measured 84.5% on GPQA Diamond, above o3's 82.7%.
- Function calling, structured outputs, web search, file search, image generation and MCP tools through the Responses API.
- 200K context with up to 100K output tokens.

## Limitations
- Deprecated, with removal from OpenAI's API on 2026-12-11.
- Ten times the price of o3, with no prompt caching.
- Responses API only; no Chat Completions, and streaming is not listed.
- Artificial Analysis publishes no speed, agentic or long-context results for it.
- Knowledge stops at June 2024.

## Good for
- Hard science and maths questions where answer quality matters more than cost or latency.
- Background jobs that can wait minutes for a response.
