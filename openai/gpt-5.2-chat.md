---
id: openai/gpt-5.2-chat
name: GPT-5.2 Chat
owned_by: openai
type: llm
description: GPT-5.2 Chat (Instant) is the low-latency ChatGPT snapshot of OpenAI's GPT-5.2, exposed in the API as gpt-5.2-chat-latest and shut down by OpenAI on 10 August 2026 in favour of the chat-latest alias.
aliases: [gpt-5.2-chat-latest, openai/gpt-5.2-chat-20251211, azure/gpt-5.2-chat]
context_length: 128000
max_output_tokens: 32000
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [max_completion_tokens, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [file, image, text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-12-11"
knowledge_cutoff: "2025-08"
pricing:
  input: 1.75
  output: 14
  cache_read: 0.175
sources:
  - https://openrouter.ai/openai/gpt-5.2-chat
  - https://openrouter.ai/api/v1/models
  - https://developers.openai.com/api/docs/models/gpt-5.2-chat-latest
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.2 Chat

## Overview
GPT-5.2 Chat, which OpenRouter also calls Instant, is the GPT-5.2 snapshot used in ChatGPT, exposed in OpenAI's API as `gpt-5.2-chat-latest`. OpenRouter describes it as the fast, lightweight member of the 5.2 family for low-latency chat that selectively thinks on harder prompts. OpenRouter's canonical slug and Azure's first version are dated 11 December 2025, the day GPT-5.2 was released; OpenAI's changelog records the slug being re-pointed to the newest ChatGPT model on 10 February 2026, which Azure lists as a second version. OpenAI gives a 128,000-token context window, 16,384 max output tokens and a 31 August 2025 knowledge cutoff; OpenRouter lists 32,000 max output tokens. OpenAI announced its shutdown on 8 May 2026 and shut it down on 10 August 2026, naming `gpt-5.6-sol` as the replacement and GPT-6 Astra for most API use. Azure retired both versions by 29 June 2026 in favour of `gpt-chat-latest`. OpenRouter still listed the id on 1 November 2026.

## Strengths
- Tuned for conversational chat with low latency.
- Tool calling, structured outputs, streaming and image input on Chat Completions and Responses; Responses tools include web search, file search, image generation, code interpreter and MCP.
- Priced like GPT-5.2 at 1.75 USD input and 14 USD output per million tokens, cache reads at 0.175.

## Limitations
- Shut down on OpenAI's API since 10 August 2026 and retired on Azure.
- 128,000-token context and 16,384-token output on OpenAI, well below the 400,000 and 128,000 of GPT-5.2.
- No reasoning-effort control and no Batch endpoint.
- Artificial Analysis has no page for it, so no independent benchmarks are recorded here.
- Closed weights.

## Good for
- Historical reference for chat products that pinned the ChatGPT GPT-5.2 snapshot.
- Routes that still serve it through OpenRouter, pending a move to `chat-latest` or GPT-5.6 Sol.
