---
id: openai/gpt-6-luna-pro
name: GPT-6 Luna Pro
owned_by: openai
type: llm
description: GPT-6 Luna Pro is OpenRouter's id for OpenAI's GPT-6 Luna run with reasoning.mode set to pro, which spends more model work per request on complex tasks, billed at Luna's per-token rates.
aliases: [openai/gpt-6-luna-pro-20260922, "openai/gpt-6-luna-pro:batch"]
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
release_date: "2026-09-22"
knowledge_cutoff: "2026-05"
pricing:
  input: 0.1
  output: 0.5
  cache_read: 0.01
  cache_write: 0.125
sources:
  - https://openrouter.ai/openai/gpt-6-luna-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-6-luna
  - https://developers.openai.com/api/docs/models/gpt-6-luna
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
retrieved: "2026-11-01"
---

# GPT-6 Luna Pro

## Overview
GPT-6 Luna Pro is OpenRouter's id for GPT-6 Luna with `reasoning.mode` set to `pro`. OpenAI has no separate Pro id for its GPT-6 models; its model page lists only `gpt-6-luna`. GPT-5.6 and GPT-6 models accept `standard` (default) or `pro` mode in the Responses API, independent of `reasoning.effort`. Pro mode does more model work per request and bills those tokens at the model's standard rates. Everything else follows GPT-6 Luna, the cheapest tier below GPT-6.1 Terra, GPT-6.1 Sol and GPT-6 Astra: text and image input, text output, a 1,050,000-token context window, 128,000 max output tokens and a May 18, 2026 knowledge cutoff. OpenRouter listed it on September 22, 2026, the day GPT-6 Luna was released. OpenAI's deprecations page gives GPT-6 Luna no retirement date.

## Strengths
- Higher-quality responses on complex tasks than standard mode, per OpenRouter, which reserves it for hard, high-stakes problems.
- Luna's per-token rates: 0.10 USD input and 0.50 USD output per million tokens, the lowest in the GPT-6 family.
- OpenRouter lists none, low, medium (default), high, xhigh and max effort.

## Limitations
- OpenRouter says a typical request costs several times more than on GPT-6 Luna and takes much longer to complete.
- Artificial Analysis does not test pro mode; its GPT-6 Luna (Max) results are for standard mode.
- GPT-6 Luna supports function calling in Chat Completions only with effort none; use the Responses API for tools.
- Prompts over 272,000 input tokens cost double on input and 1.5 times on output. Closed weights.

## Good for
- Harder reasoning steps inside otherwise cheap, high-volume GPT-6 pipelines.
- Trying pro mode before paying Terra or Sol prices.
- Batch work where latency does not matter.
