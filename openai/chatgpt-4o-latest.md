---
id: openai/chatgpt-4o-latest
name: ChatGPT-4o
owned_by: openai
type: llm
description: chatgpt-4o-latest was an OpenAI API alias for the GPT-4o snapshot used in ChatGPT, added in August 2024 and shut down on 17 February 2026.
aliases: [chatgpt-4o-latest]
context_length: 128000
max_output_tokens: 16384
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2024-08-15"
knowledge_cutoff: "2023-10"
benchmarks:
  gpqa_diamond: 65.5
  humanitys_last_exam: 4.0
benchmark_variant: GPT-4o (March 2025, chatgpt-4o-latest)
sources:
  - https://developers.openai.com/api/docs/models/chatgpt-4o-latest
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://artificialanalysis.ai/models/gpt-4o-chatgpt-03-25
  - https://artificialanalysis.ai/models/gpt-4o-chatgpt
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# ChatGPT-4o

## Overview
Shut down: OpenAI notified users on 18 November 2025 and removed `chatgpt-4o-latest` from the API on 17 February 2026, recommending `gpt-5.1-chat-latest`, which has since been shut down too; the model page now points to GPT-6 Astra. OpenRouter does not list it; the id is OpenAI's API id. OpenAI's changelog added it on 15 August 2024 as a dynamic model that pointed to the latest GPT-4o model used in ChatGPT, so its behaviour changed whenever ChatGPT's GPT-4o changed. It took text and images, returned text, and had a 128,000-token context window, 16,384 max output tokens and an October 2023 knowledge cutoff. It ran on Chat Completions and Responses with streaming, predicted outputs and image input; the page lists no function calling or structured outputs. OpenAI priced it at 5 USD input and 15 USD output per million tokens, with no cached-input rate.

## Strengths
- Gave API access to the same GPT-4o tuning ChatGPT users saw.
- Artificial Analysis measured the March 2025 version at 65.5% on GPQA Diamond and 4.0% on Humanity's Last Exam, up from 51.1% and 2.7% for its February 2025 GPT-4o (ChatGPT) entry.
- Image input.

## Limitations
- Shut down; requests to the id fail.
- A moving alias with no pinned snapshot, so results were not reproducible over time.
- Double GPT-4o's price (2.50 and 10 USD) with no prompt-caching discount.
- No function calling or structured outputs listed.
- Knowledge stops at October 2023.

## Good for
- Recognising the id in older chat integrations and evaluation logs.
- Comparing past ChatGPT behaviour with later chat models.
