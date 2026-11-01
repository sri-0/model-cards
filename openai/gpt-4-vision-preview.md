---
id: openai/gpt-4-vision-preview
name: GPT-4 Turbo with Vision Preview
owned_by: openai
type: llm
description: gpt-4-vision-preview was OpenAI's November 2023 preview of GPT-4 Turbo with image input in the Chat Completions API, shut down on 6 December 2024.
aliases: [gpt-4-vision-preview, gpt-4-1106-vision-preview, azure/gpt-4-turbo-vision-preview]
context_length: 128000
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2023-11-06"
knowledge_cutoff: "2023-04"
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://web.archive.org/web/20231231174614/https://openai.com/blog/new-models-and-developer-products-announced-at-devday
  - https://web.archive.org/web/20240316055621/https://openai.com/api/pricing/
  - https://web.archive.org/web/20240315/https://openaiapi-site.azureedge.net/public-assets/d/d419c3241b/static/js/main.7e794804.js
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4 Turbo with Vision Preview

## Overview
Shut down: OpenAI announced on 6 June 2024 that `gpt-4-vision-preview` and `gpt-4-1106-vision-preview` would be retired, limited them to existing users from 17 June 2024, and shut both down on 6 December 2024, naming `gpt-4o` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page for it; the id is OpenAI's API id. OpenAI introduced it at DevDay on 6 November 2023 as GPT-4 Turbo with vision: GPT-4 Turbo accepting images in Chat Completions for captions, detailed image analysis and documents with figures. GPT-4 Turbo had a 128K context window and knowledge of events up to April 2023. The deprecations page lists both ids at one price, and the 2024 pricing page lists only `gpt-4-1106-vision-preview`, so this card treats that id as the dated snapshot. OpenAI priced it at 10 USD input and 30 USD output per million tokens, with image input billed by size (0.00765 USD for a 1080 by 1080 image at launch). Vision later moved into the GA GPT-4 Turbo model, which has its own card.

## Strengths
- OpenAI's first API model to take image input.
- 128K context, matching GPT-4 Turbo.

## Limitations
- Shut down; requests to the id fail.
- A preview: OpenAI's 2024 API reference said `logprobs` was not available on it, and OpenRouter's GPT-4 Turbo listing says vision requests can now use JSON mode and function calling, a change that came with the GA model.
- LiteLLM lists Azure's version with 4,096 output tokens; OpenAI published no output limit.
- No Artificial Analysis results.

## Good for
- Recognising the id in late-2023 image-understanding code.
- Planning a migration to GPT-4o or a current vision model.
