---
id: openai/gpt-5-search-api
name: GPT-5 Search API
owned_by: openai
type: llm
description: gpt-5-search-api is OpenAI's current specialised search model for web search inside the Chat Completions API, recommended only for keeping an existing Chat Completions search integration.
aliases: [gpt-5-search-api, gpt-5-search-api-2025-10-14]
context_length: 200000
open_weights: false
license: proprietary
sources:
  - https://developers.openai.com/api/docs/guides/tools-web-search
  - https://developers.openai.com/api/docs/pricing
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5 Search API

## Overview
`gpt-5-search-api` is the model OpenAI's web search guide names for web search through Chat Completions. OpenRouter does not list it and OpenAI has no model page for it; the id comes from the guide and the pricing page, and LiteLLM also lists the snapshot `gpt-5-search-api-2025-10-14`. The guide recommends it only to preserve an existing Chat Completions integration, and as the Chat Completions replacement for `gpt-4o-search-preview` and `gpt-4o-mini-search-preview`, which shut down on 23 July 2026. New integrations should use the Responses API `web_search` tool with GPT-5.5. Like the earlier search models, it always searches before responding, and the guide gives it a 200,000-token context window. The pricing page lists it under Specialized models at 1.25 USD input, 0.125 cached input and 10 USD output per million tokens; LiteLLM adds 0.01 USD per search query and lists 272,000 input and 128,000 output tokens, function calling, vision and structured output.

## Strengths
- Web-grounded answers from a plain Chat Completions request.
- Larger context than the 128,000-token GPT-4o search previews.
- GPT-5's token price.

## Limitations
- No domain filters, complete source lists, live-access control or returned-token budget control, which Responses `web_search` supports.
- Searches on every request, so latency and search fees apply to all prompts.
- OpenAI publishes no model page, release date, output limit or knowledge cutoff.
- No Artificial Analysis results.

## Good for
- Keeping an existing Chat Completions search integration running.
- Migrating off the GPT-4o search previews without moving to Responses.
