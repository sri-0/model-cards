---
id: openai/gpt-5-pro
name: GPT-5 Pro
owned_by: openai
type: llm
description: GPT-5 Pro is the high-compute version of OpenAI's GPT-5 that thinks longer for more precise answers, served through the Responses API only, now deprecated with shutdown set for 11 December 2026.
aliases: [gpt-5-pro, gpt-5-pro-2025-10-06, openai/gpt-5-pro-2025-10-06, openai/gpt-5-pro:batch, azure/gpt-5-pro]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [image, text, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-10-06"
knowledge_cutoff: "2024-09"
pricing:
  input: 15
  output: 120
sources:
  - https://openrouter.ai/openai/gpt-5-pro
  - https://openrouter.ai/api/v1/models
  - https://developers.openai.com/api/docs/models/gpt-5-pro
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5 Pro

## Overview
GPT-5 Pro is a proprietary OpenAI model released to the API on 6 October 2025. OpenAI's docs describe it as a version of GPT-5 that uses more compute to think harder and give consistently better answers. It takes text and image input and returns text, with a 400,000-token context window, 128,000 max output tokens and a 30 September 2024 knowledge cutoff. `reasoning.effort` defaults to, and only supports, high. The pinned snapshot is `gpt-5-pro-2025-10-06`. OpenAI deprecated it on 11 June 2026 and shuts it down on 11 December 2026, naming `gpt-5.6-sol` with `reasoning.mode: pro` as the replacement. Azure runs it as `gpt-5-pro` version 2025-10-06, GA until 7 April 2027.

## Strengths
- OpenRouter positions it for complex tasks that need step-by-step reasoning, instruction following and accuracy.
- Tool calling, structured outputs, image input, file search, web search and MCP on the Responses API.
- Same 400,000-token window as GPT-5.

## Limitations
- Deprecated, with shutdown on 11 December 2026.
- Responses API only, not Chat Completions; OpenAI also lists Batch as supported. Code interpreter is not supported.
- Expensive: 15 USD input and 120 USD output per million tokens on OpenRouter, with no cache-read price.
- Only the high reasoning effort; no way to trade quality for latency.
- Artificial Analysis publishes no page for this model, so there are no independent benchmarks here.
- Knowledge stops at September 2024. Closed weights.

## Good for
- Hard, high-stakes questions where answer quality outweighs cost and speed.
- Batch or background jobs that can wait for long responses.
- Checking work produced by cheaper GPT-5 variants, until migration to GPT-5.6 Sol in pro mode.
