---
id: openai/gpt-4o-search-preview
name: GPT-4o Search Preview
owned_by: openai
type: llm
description: GPT-4o Search Preview was OpenAI's specialised model for web search in the Chat Completions API, announced in March 2025 and shut down on 23 July 2026.
aliases: [gpt-4o-search-preview, gpt-4o-search-preview-2025-03-11]
context_length: 128000
max_output_tokens: 16384
capabilities: [structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-03-11"
knowledge_cutoff: "2023-10"
sources:
  - https://developers.openai.com/api/docs/models/gpt-4o-search-preview
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/guides/tools-web-search
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o Search Preview

## Overview
Shut down: OpenAI announced the deprecation on 22 April 2026 and shut the `gpt-4o-search-preview-2025-03-11` snapshot down on 23 July 2026, naming `gpt-5.6-terra` as the substitute. The web search guide now points Chat Completions users to `gpt-5-search-api` and everyone else to the Responses `web_search` tool. OpenRouter does not list it; the id is OpenAI's API id. OpenAI announced it on 11 March 2025 with the Responses API and its built-in tools. It is a specialised model trained to understand and run web search queries inside Chat Completions; the guide says these search models always search before responding. The model page gives a 128,000-token context window, 16,384 max output tokens and an October 2023 knowledge cutoff, with streaming and structured outputs. It lists text as the only input modality but also image input as a feature. OpenAI priced it at 2.50 USD input and 10 USD output per million tokens, plus a fee per search call.

## Strengths
- Web-grounded answers from a plain Chat Completions request, with no tool loop to build.
- Same token price as GPT-4o.

## Limitations
- Shut down; requests to the id fail.
- No domain filters, complete source lists, live-access control or returned-token budget, which the Responses `web_search` tool offers.
- Searches on every request, adding latency and per-call fees even when not needed.
- No function calling listed, and no Artificial Analysis results.

## Good for
- Recognising the id in older Chat Completions search integrations.
- Planning a migration to `gpt-5-search-api` or Responses `web_search`.
