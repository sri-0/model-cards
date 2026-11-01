---
id: openai/gpt-3.5-turbo-instruct
name: gpt-3.5-turbo-instruct
owned_by: openai
type: llm
description: gpt-3.5-turbo-instruct was OpenAI's 4K-context instruction-following GPT-3.5 model for the legacy Completions API, the 2023 replacement for the InstructGPT models, shut down on 28 September 2026.
aliases: [gpt-3.5-turbo-instruct, gpt-3.5-turbo-instruct-0914, azure/gpt-35-turbo-instruct, azure/gpt-35-turbo-instruct-0914, azure/gpt-3.5-turbo-instruct-0914, vercel_ai_gateway/openai/gpt-3.5-turbo-instruct]
context_length: 4096
max_output_tokens: 4096
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
knowledge_cutoff: "2021-09"
sources:
  - https://developers.openai.com/api/docs/models/gpt-3.5-turbo-instruct
  - https://developers.openai.com/api/docs/deprecations
  - https://web.archive.org/web/20261005155548/https://openai.com/index/gpt-4-api-general-availability/
  - https://web.archive.org/web/20240316055621/https://openai.com/api/pricing/
  - https://web.archive.org/web/20240315/https://openaiapi-site.azureedge.net/public-assets/d/d419c3241b/static/js/main.7e794804.js
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# gpt-3.5-turbo-instruct

## Overview
Shut down: OpenAI deprecated `gpt-3.5-turbo-instruct` on 26 September 2025 and turned it off on 28 September 2026, naming `gpt-5.6-terra` as the replacement. OpenRouter does not list it; the id is OpenAI's API id and has its own OpenAI model page, separate from GPT-3.5 Turbo. OpenAI's July 2023 GPT-4 API post named it the replacement for the InstructGPT models (text-ada-001 to text-davinci-003) and the instruct-beta models, all switched off on 4 January 2024. OpenAI describes it as having capabilities similar to GPT-3 era models and as compatible with the legacy Completions endpoint, not Chat Completions; the 2024 pricing page called it an Instruct model that only supports a 4K context window. The model page gives a 4,096-token context window, 4,096 max output tokens and a September 2021 knowledge cutoff. OpenAI priced it at 1.50 USD input and 2 USD output per million tokens, against 0.50 and 1.50 for `gpt-3.5-turbo-0125`.

## Strengths
- Follows instructions in a plain completion prompt, with no chat message format.
- A direct swap for text-davinci-003 and the other InstructGPT models in 2023-era Completions code.

## Limitations
- Shut down; requests to the id fail.
- 4K context, text only and a September 2021 knowledge cutoff.
- OpenAI's sources conflict: the page's description says Completions only, but its endpoint table now marks Chat Completions and Responses as supported and legacy Completions as not. LiteLLM lists 8,192 input tokens and OpenAI's 2024 Playground used 4,097.
- No Artificial Analysis results.

## Good for
- Recognising the id in completion-style code migrated off InstructGPT.
- Planning a migration to `gpt-5.6-terra`.
