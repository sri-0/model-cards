---
id: openai/gpt-5.1-chat-latest
name: GPT-5.1 Chat
owned_by: openai
type: llm
description: gpt-5.1-chat-latest was OpenAI's API alias for the GPT-5.1 snapshot used in ChatGPT, released with GPT-5.1 in November 2025 and shut down on 23 July 2026.
aliases: [gpt-5.1-chat-latest, azure/gpt-5.1-chat]
context_length: 128000
max_output_tokens: 16384
capabilities: [tool_calling, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-11-13"
knowledge_cutoff: "2024-09"
sources:
  - https://developers.openai.com/api/docs/models/gpt-5.1-chat-latest
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.1 Chat

## Overview
Shut down: OpenAI announced the deprecation on 22 April 2026 and shut `gpt-5.1-chat-latest` down on 23 July 2026, naming `gpt-5.6-sol` as the replacement. It had itself been the recommended replacement for `chatgpt-4o-latest`. OpenRouter does not list it; the id is OpenAI's API id. OpenAI released it on 13 November 2025 with GPT-5.1, GPT-5.1-Codex and GPT-5.1-Codex-Mini; the page says it points to the GPT-5.1 snapshot used in ChatGPT and was offered for testing chat improvements, not as the main API model. It took text and images and returned text, with a 128,000-token context window, 16,384 max output tokens and a 30 September 2024 knowledge cutoff; the page also states 272,000 maximum input tokens. It ran on Chat Completions and Responses with function calling, structured outputs, streaming and the Responses tools web search, file search, image generation, code interpreter and MCP. OpenAI priced it at 1.25 USD input, 0.125 cached input and 10 USD output per million tokens. Microsoft Foundry retired `gpt-5.1-chat` version 2025-11-13 on 29 June 2026; LiteLLM lists 111,616 input tokens for Azure.

## Strengths
- ChatGPT's GPT-5.1 conversational tuning through the API.
- Function calling, structured outputs and image input at GPT-5's token price.

## Limitations
- Shut down; requests to the id fail.
- A moving alias with no pinned snapshot, so behaviour could change without notice.
- Output capped at 16,384 tokens.
- No Artificial Analysis results.

## Good for
- Recognising the id in chat integrations from late 2025.
- Planning a migration to `gpt-5.6-sol` or the current `chat-latest`.
