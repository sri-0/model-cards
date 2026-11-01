---
id: openai/gpt-4-32k
name: GPT-4 32K
owned_by: openai
type: llm
description: GPT-4 32K was OpenAI's 32,768-token-context version of the original GPT-4, released with GPT-4 in March 2023 at twice GPT-4's price and shut down on 6 June 2025.
aliases: [gpt-4-32k, gpt-4-32k-0613, gpt-4-32k-0314, azure/gpt-4-32k, azure/gpt-4-32k-0613]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2023-03-14"
knowledge_cutoff: "2021-09"
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://web.archive.org/web/20230603183535/https://platform.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20240316055621/https://openai.com/api/pricing/
  - https://web.archive.org/web/20240315/https://openaiapi-site.azureedge.net/public-assets/d/d419c3241b/static/js/main.7e794804.js
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4 32K

## Overview
Shut down: OpenAI announced on 6 June 2024 that `gpt-4-32k`, `gpt-4-32k-0613` and `gpt-4-32k-0314` would be retired, limited them to existing users from 17 June 2024, and shut all three down on 6 June 2025, naming `gpt-4o` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page for it; the id is OpenAI's API id, with its own rows and price on the deprecations page. OpenAI's 2023 model docs described `gpt-4-32k` as having the same capabilities as the base `gpt-4` model with four times the context length, 32,768 tokens, and training data up to September 2021. Its first snapshot, `gpt-4-32k-0314`, dated from 14 March 2023; `gpt-4-32k-0613` followed. Like GPT-4 it was a text-only chat model, in limited beta at first. OpenAI priced it at 60 USD input and 120 USD output per million tokens, double `gpt-4`. LiteLLM lists Azure's `gpt-4-32k` deployments with 32,768 input and 4,096 output tokens.

## Strengths
- Four times GPT-4's 8,192-token context; GPT-4 Turbo's 128K followed in November 2023.
- The same GPT-4 capabilities as the 8K model.

## Limitations
- Shut down; requests to the id fail.
- 60 and 120 USD per million tokens, the highest GPT-4 price.
- Text only, with a September 2021 knowledge cutoff.
- OpenAI published no output limit for it, and Artificial Analysis has no results.

## Good for
- Recognising the id in 2023 and 2024 long-document pipelines.
- Historical comparison of OpenAI context-window sizes.
