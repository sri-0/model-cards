---
id: openai/gpt-chat-latest
name: GPT Chat Latest
owned_by: openai
type: llm
description: GPT Chat Latest is OpenRouter's listing of OpenAI's chat-latest alias, which always resolves to the Instant model currently used in ChatGPT, so the underlying snapshot changes without notice.
aliases: [chat-latest, gpt-chat-latest, openai/gpt-chat-latest-20260505, azure/chat-latest, azure/gpt-chat-latest]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [max_tokens, response_format, seed, structured_outputs, tool_choice, tools]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-05-05"
knowledge_cutoff: "2026-04"
pricing:
  input: 5
  output: 30
  cache_read: 0.5
sources:
  - https://openrouter.ai/openai/gpt-chat-latest
  - https://openrouter.ai/api/v1/models
  - https://developers.openai.com/api/docs/models/chat-latest
  - https://developers.openai.com/api/docs/models/gpt-5-chat-latest
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Chat Latest

## Overview
`openai/gpt-chat-latest` is OpenRouter's name for OpenAI's `chat-latest` API alias, which OpenAI's docs describe as the latest Instant model used in ChatGPT, with the underlying snapshot updated regularly. OpenAI does not name the snapshot. Its changelog records the alias going live on 5 May 2026 and snapshot updates on 28 May, 24 June, 6 August and 7 October 2026, the last described as pointing to the latest model available in ChatGPT; Azure lists matching `gpt-chat-latest` versions, all in preview. As of 1 November 2026 the model page gives a 20 April 2026 knowledge cutoff, a 400,000-token context window, 272,000 max input tokens and 128,000 max output tokens, with text and image input. It replaces the dated `gpt-5-chat-latest` alias (the GPT-5 snapshot from ChatGPT, 128,000-token context), which OpenAI shut down on 23 July 2026; Azure names `gpt-chat-latest` as the replacement for its retired `gpt-5-chat`, `gpt-5.1-chat`, `gpt-5.2-chat` and `gpt-5.3-chat` deployments.

## Strengths
- Tracks ChatGPT's current default conversational model without code changes.
- Tool calling, structured outputs, streaming and image input on Chat Completions and Responses; Responses tools include web search, file search, image generation, code interpreter and MCP.
- Cache reads at 0.5 USD per million tokens.

## Limitations
- The model behind the alias changes without a version pin, so behaviour and quality can shift between calls; OpenAI recommends GPT-6 Astra for production API use.
- No reasoning-effort control is exposed on OpenRouter.
- 5 USD input and 30 USD output per million tokens, more than the pinned GPT-5.x models.
- Artificial Analysis has no page for the alias, so no independent benchmarks are recorded here.
- No Batch endpoint. Closed weights.

## Good for
- Consumer-style chat products that should match what ChatGPT users see.
- Quick prototypes where tracking the newest Instant model matters more than reproducibility.
