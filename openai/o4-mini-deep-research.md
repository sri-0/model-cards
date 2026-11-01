---
id: openai/o4-mini-deep-research
name: o4-mini-deep-research
owned_by: openai
type: llm
description: o4-mini-deep-research was OpenAI's faster, cheaper deep research variant of o4-mini for multi-step web and private-data research in the Responses API, released in June 2025 and shut down on 23 July 2026.
aliases: [o4-mini-deep-research, o4-mini-deep-research-2025-06-26]
context_length: 200000
max_output_tokens: 100000
capabilities: [reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-06-24"
knowledge_cutoff: "2024-06"
sources:
  - https://developers.openai.com/api/docs/models/o4-mini-deep-research
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/guides/deep-research
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# o4-mini-deep-research

## Overview
Shut down: OpenAI announced the deprecation on 22 April 2026 and shut `o4-mini-deep-research` and its snapshot `o4-mini-deep-research-2025-06-26` down on 23 July 2026, naming `gpt-5.6-sol` as the replacement. OpenRouter does not list it; the id is OpenAI's API id. OpenAI's changelog dates the release 24 June 2025, alongside o3-deep-research, as deep research variants of the o-series reasoning models. OpenAI calls it the faster, more affordable of the two. It searches and synthesises information from the internet and from private data brought in through MCP connectors or file search; a request needs at least one such data source and can add code interpreter. The model page gives a 200,000-token context window, 100,000 max output tokens, a June 2024 knowledge cutoff, reasoning tokens and text and image input, on Responses and Batch only. OpenAI priced it at 2 USD input, 0.50 cached input and 8 USD output per million tokens, a fifth of o3-deep-research, plus tool-call fees.

## Strengths
- Deep research at o3's token price rather than o3-deep-research's 10 and 40 USD.
- Same tool set as the larger model: web search, MCP and code interpreter.
- Batch support for offline research jobs.

## Limitations
- Shut down; requests to the id fail.
- Multi-step runs are slow; OpenAI recommends background mode, which is not compatible with Zero Data Retention.
- Expects a fully formed prompt; the API adds no clarification step.
- No function calling listed, and no Artificial Analysis results.

## Good for
- Recognising the id in research pipelines built in 2025 and 2026.
- Planning a migration to `gpt-5.6-sol` with the hosted web search tool.
