---
id: openai/gpt-5-chat-latest
name: GPT-5 Chat
owned_by: openai
type: llm
description: gpt-5-chat-latest was OpenAI's API alias for the GPT-5 snapshot used in ChatGPT, released with GPT-5 in August 2025 and shut down on 23 July 2026.
aliases: [gpt-5-chat-latest, gpt-5-chat, azure/gpt-5-chat]
context_length: 128000
max_output_tokens: 16384
capabilities: [tool_calling, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-08-07"
knowledge_cutoff: "2024-09"
benchmarks:
  gpqa_diamond: 68.6
  humanitys_last_exam: 6.6
  ifbench: 45.0
  long_context_reasoning: 65.0
  tau2_bench: 0
  terminal_bench_hard: 12.9
benchmark_variant: GPT-5 (ChatGPT)
sources:
  - https://developers.openai.com/api/docs/models/gpt-5-chat-latest
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/deprecations
  - https://artificialanalysis.ai/models/gpt-5-chatgpt
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5 Chat

## Overview
Shut down: OpenAI announced the deprecation on 22 April 2026 and shut `gpt-5-chat-latest` down on 23 July 2026, naming `gpt-5.6-sol` as the replacement. OpenRouter does not list it; the id is OpenAI's API id, and LiteLLM also uses `gpt-5-chat`. OpenAI's page says it points to the GPT-5 snapshot previously used in ChatGPT; Artificial Analysis dates GPT-5 (ChatGPT) to 7 August 2025, the day the GPT-5 family reached the API. It took text and images and returned text, with a 128,000-token context window, 16,384 max output tokens and a 30 September 2024 knowledge cutoff; the page also states 272,000 maximum input tokens. It ran on Chat Completions and Responses with function calling, structured outputs and streaming, and the Responses tools web search, file search, image generation, code interpreter and MCP. OpenAI priced it like GPT-5: 1.25 USD input, 0.125 cached input and 10 USD output per million tokens. Microsoft Foundry retired its `gpt-5-chat` versions 2025-10-03 and 2025-08-07 on 13 May and 29 June 2026, pointing to `gpt-chat-latest`.

## Strengths
- Artificial Analysis measured GPT-5 (ChatGPT) at 68.6% on GPQA Diamond, 65.0% on AA-LCR and 45.0% on IFBench.
- ChatGPT's conversational tuning at GPT-5's price, with function calling and structured outputs.

## Limitations
- Shut down; requests to the id fail.
- Artificial Analysis scored 0 on tau2-bench and 12.9% on Terminal-Bench Hard, weak for agent work.
- A moving alias with no pinned snapshot.
- Output capped at 16,384 tokens; the page lists no reasoning-token support.

## Good for
- Recognising the id in 2025 chat integrations and evaluation logs.
- Planning a migration to `gpt-5.6-sol` or the current `chat-latest`.
