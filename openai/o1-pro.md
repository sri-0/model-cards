---
id: openai/o1-pro
name: o1-pro
owned_by: openai
type: llm
description: o1-pro is the extra-compute version of o1 served through the Responses API, shut down on OpenAI's API on 2026-10-23.
aliases: [o1-pro, o1-pro-2025-03-19]
context_length: 200000
max_output_tokens: 100000
capabilities: [tool_calling, reasoning, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-03-19"
knowledge_cutoff: "2023-10"
sources:
  - https://artificialanalysis.ai/models/o1-pro
  - https://developers.openai.com/api/docs/models/o1-pro
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# o1-pro

## Overview
o1-pro is the version of o1 that OpenAI ran with more compute so that it thinks harder and gives consistently better answers, released on 2025-03-19 (Artificial Analysis date; pinned snapshot `o1-pro-2025-03-19`). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix and the frontmatter carries no OpenRouter price or parameters; the limits come from OpenAI's page. It takes text and images and returns text, with a 200,000-token context window, 100,000 max output tokens, reasoning tokens and an October 2023 knowledge cutoff. It was available in the Responses API only (plus Batch), which OpenAI chose so the model could run multi-turn interactions before responding, with function calling, structured outputs and image input. OpenAI's price was $150 input and $600 output per million tokens ($75 and $300 in batch), with no cached-input rate. OpenAI lists it as Shut down: announced 2026-04-22, it left the API on 2026-10-23 with `gpt-5.6-sol` using `reasoning.mode: pro` as the recommended replacement; Artificial Analysis names o3-pro as its successor.

## Strengths
- Function calling, structured outputs and image input through the Responses API.
- 200K context with up to 100K output tokens.

## Limitations
- Shut down on OpenAI's API and not listed on OpenRouter.
- Ten times the price of o1, with no prompt caching.
- Artificial Analysis has a page for it but publishes no benchmark scores, so this card carries none.
- Responses API only; no Chat Completions, and streaming is not listed.
- Knowledge stops at October 2023.

## Good for
- Reproducing results from systems that used the Pro tier of the first o-series.
- Comparisons when evaluating OpenAI's later `reasoning.mode: pro` option.
