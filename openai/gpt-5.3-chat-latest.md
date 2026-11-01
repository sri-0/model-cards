---
id: openai/gpt-5.3-chat-latest
name: GPT-5.3 Chat
owned_by: openai
type: llm
description: gpt-5.3-chat-latest was OpenAI's API alias for the GPT-5.3 Instant snapshot used in ChatGPT, released in March 2026 and shut down on 10 August 2026.
aliases: [gpt-5.3-chat-latest, "chatgpt/gpt-5.3-chat-latest", azure/gpt-5.3-chat]
context_length: 128000
max_output_tokens: 16384
capabilities: [tool_calling, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2026-03-03"
knowledge_cutoff: "2025-08"
sources:
  - https://developers.openai.com/api/docs/models/gpt-5.3-chat-latest
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.3 Chat

## Overview
Shut down: OpenAI notified users on 8 May 2026 and removed `gpt-5.3-chat-latest` from the API on 10 August 2026, naming `gpt-5.6-sol` as the replacement; the model page now recommends GPT-6 Astra. OpenRouter does not list it; the id is OpenAI's API id. OpenAI released it on 3 March 2026 on Chat Completions and Responses, pointing to the GPT-5.3 Instant snapshot used in ChatGPT, and on 16 March 2026 updated the slug to the latest model then used in ChatGPT. It took text and images and returned text, with a 128,000-token context window, 16,384 max output tokens and a 31 August 2025 knowledge cutoff; the page also states 272,000 maximum input tokens. It supported function calling, structured outputs, streaming and the Responses tools web search, file search, image generation, code interpreter and MCP. OpenAI priced it at 1.75 USD input, 0.175 cached input and 14 USD output per million tokens. Microsoft Foundry retired `gpt-5.3-chat` version 2026-03-03 on 29 June 2026, pointing to `gpt-chat-latest`. LiteLLM also lists it under its ChatGPT-subscription provider as `chatgpt/gpt-5.3-chat-latest`.

## Strengths
- ChatGPT's GPT-5.3 Instant tuning through the API, with a later knowledge cutoff than the GPT-5 and GPT-5.1 chat aliases.
- Function calling, structured outputs and image input.

## Limitations
- Shut down; requests to the id fail.
- A moving alias: its target changed within two weeks of release.
- Output capped at 16,384 tokens.
- No Artificial Analysis results.

## Good for
- Recognising the id in chat integrations from early 2026.
- Planning a migration to `gpt-5.6-sol` or the current `chat-latest`.
