---
id: openai/gpt-4.5-preview
name: GPT-4.5 Preview
owned_by: openai
type: llm
description: GPT-4.5 Preview was a research preview of OpenAI's GPT-4.5, which OpenAI called its largest and most capable chat model when it was released in February 2025, shut down on 14 July 2025.
aliases: [gpt-4.5-preview, gpt-4.5-preview-2025-02-27, azure/gpt-4.5-preview]
context_length: 128000
max_output_tokens: 16384
capabilities: [tool_calling, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-02-27"
knowledge_cutoff: "2023-10"
sources:
  - https://developers.openai.com/api/docs/models/gpt-4.5-preview
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://artificialanalysis.ai/models/gpt-4-5-preview
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4.5 Preview

## Overview
Shut down: OpenAI announced the deprecation on 14 April 2025, the day GPT-4.1 launched, and removed `gpt-4.5-preview` from the API on 14 July 2025, naming `gpt-4.1` as the replacement; the model page also suggests o3. OpenRouter does not list it; the id is OpenAI's API id. OpenAI released the research preview on 27 February 2025, calling it its largest and most capable chat model yet, with a high "EQ" and understanding of user intent that made it better at creative tasks and agentic planning. Its only snapshot was `gpt-4.5-preview-2025-02-27`. It took text and images, returned text, and had a 128,000-token context window, 16,384 max output tokens and an October 2023 knowledge cutoff. It ran on Chat Completions, Responses, Assistants and Batch with function calling, structured outputs, system messages, streaming and prompt caching. OpenAI priced it at 75 USD input, 37.50 cached input and 150 USD output per million tokens.

## Strengths
- OpenAI positioned it for writing, creative work and planning where tone and intent matter.
- Full tool support: function calling, structured outputs, image input and caching.

## Limitations
- Shut down after less than five months; requests to the id fail.
- 75 and 150 USD per million tokens, against 2 and 8 USD for GPT-4.1 or o3 in OpenAI's comparison.
- No reasoning tokens.
- Artificial Analysis lists it (released 27 February 2025, deprecated in favour of GPT-4.1) but publishes no evaluation results for it.

## Good for
- Recognising the id in early-2025 integrations and evaluation logs.
- Historical comparison of OpenAI's large non-reasoning chat models.
