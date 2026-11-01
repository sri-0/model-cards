---
id: openai/gpt-5.6-luna-pro
name: GPT-5.6 Luna Pro
owned_by: openai
type: llm
description: GPT-5.6 Luna Pro is OpenRouter's id for OpenAI's GPT-5.6 Luna run with reasoning.mode set to pro, which spends more model work per request on complex tasks, billed at Luna's per-token rates.
aliases: [openai/gpt-5.6-luna-pro-20260709, "openai/gpt-5.6-luna-pro:batch"]
context_length: 1050000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [file, image, text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-07-09"
knowledge_cutoff: "2026-02"
pricing:
  input: 0.2
  output: 1.2
  cache_read: 0.02
  cache_write: 0.25
sources:
  - https://openrouter.ai/openai/gpt-5.6-luna-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-6-luna
  - https://developers.openai.com/api/docs/models/gpt-5.6-luna
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/guides/latest-model/gpt-5.6
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
retrieved: "2026-11-01"
---

# GPT-5.6 Luna Pro

## Overview
GPT-5.6 Luna Pro is OpenRouter's id for GPT-5.6 Luna with `reasoning.mode` set to `pro`. OpenAI has no separate model id for it: GPT-5.6 and GPT-6 models accept `standard` (default) or `pro` mode in the Responses API, and OpenAI's GPT-5.6 guide says to keep the base model and set the mode rather than switch to a Pro slug. Pro mode does more model work per request and bills those tokens at the model's standard rates; effort is chosen separately. Everything else follows GPT-5.6 Luna, the cheapest tier below GPT-5.6 Terra and GPT-5.6 Sol: text and image input, text output, a 1,050,000-token context window, 128,000 max output tokens and a February 16, 2026 knowledge cutoff. OpenRouter listed it on July 9, 2026, the family's launch day. OpenAI gives GPT-5.6 Luna no retirement date; Artificial Analysis marks it superseded by GPT-6 Luna, which also supports pro mode.

## Strengths
- Higher-quality responses on complex tasks than standard mode, per OpenRouter.
- Luna's per-token rates: 0.20 USD input and 1.20 USD output per million tokens, after an 80% cut on July 30, 2026.
- OpenRouter lists none, low, medium (default), high, xhigh and max effort.

## Limitations
- OpenRouter says a typical request costs several times more than on GPT-5.6 Luna and takes much longer to complete.
- Artificial Analysis does not test pro mode; its GPT-5.6 Luna (Max) results are for standard mode.
- On OpenAI's API, pro mode is available only in the Responses API.
- Prompts over 272,000 input tokens cost double on input and 1.5 times on output. Closed weights.

## Good for
- Harder reasoning steps inside otherwise cheap, high-volume pipelines.
- Trying pro mode before paying Terra or Sol prices.
- Batch work where latency does not matter.
