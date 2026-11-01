---
id: openai/babbage-002
name: babbage-002
owned_by: openai
type: llm
description: babbage-002 was OpenAI's smaller GPT base model for the legacy Completions API, released in August 2023 to replace the GPT-3 ada and babbage base models and shut down on 28 September 2026.
aliases: [babbage-002, "ft:babbage-002"]
max_output_tokens: 16384
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2023-08-22"
knowledge_cutoff: "2021-09"
sources:
  - https://developers.openai.com/api/docs/models/babbage-002
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/deprecations
  - https://web.archive.org/web/20261019212943/https://openai.com/index/gpt-3-5-turbo-fine-tuning-and-api-updates/
  - https://web.archive.org/web/20261005155548/https://openai.com/index/gpt-4-api-general-availability/
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# babbage-002

## Overview
Shut down: OpenAI deprecated babbage-002 on 26 September 2025 and turned it off on 28 September 2026, naming `gpt-5.6-terra` as the replacement. OpenRouter does not list it; the id is OpenAI's API id. OpenAI announced it in July 2023 and released it on 22 August 2023, with davinci-002, as a replacement for the original GPT-3 base models, which were switched off on 4 January 2024; babbage-002 took over from ada and babbage. It is a base model: OpenAI says it understands and generates natural language or code but is not trained to follow instructions. It took text and returned text through the legacy Completions endpoint (`v1/completions`) only, supported fine-tuning, and had a September 2021 knowledge cutoff. OpenAI's page gives 16,384 max output tokens and no context window. OpenAI priced it at 0.40 USD per million tokens for both input and output. New fine-tuning training on it ended on 28 October 2024.

## Strengths
- 0.40 USD per million tokens for input and output alike; OpenAI's comparison table puts GPT-4o mini at 0.15 input and 0.60 output.
- Plain text continuation with no chat format, which suited completion-style prompts.
- Could serve as a base for fine-tuning until October 2024.

## Limitations
- Shut down on OpenAI's API; requests to the id fail.
- Not instruction-tuned: OpenAI told most customers to use GPT-3.5 or GPT-4 instead.
- Completions API only; no chat messages, tools, structured outputs or images.
- LiteLLM lists 16,384 input and 4,096 output tokens, which differs from OpenAI's output figure.
- No Artificial Analysis results.

## Good for
- Recognising the id in old completion pipelines and fine-tuned model names.
- Planning a migration to `gpt-5.6-terra`.
