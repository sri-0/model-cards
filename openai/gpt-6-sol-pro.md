---
id: openai/gpt-6-sol-pro
name: GPT-6 Sol Pro
owned_by: openai
type: llm
description: GPT-6 Sol Pro is OpenRouter's id for OpenAI's GPT-6 Sol run with reasoning.mode set to pro, which spends more model work per request on complex tasks, billed at Sol's per-token rates.
aliases: [openai/gpt-6-sol-pro-20260922, "openai/gpt-6-sol-pro:batch"]
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
knowledge_cutoff: "2026-04"
pricing:
  input: 2
  output: 10
  cache_read: 0.2
  cache_write: 2.5
sources:
  - https://openrouter.ai/openai/gpt-6-sol-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-6-sol
  - https://developers.openai.com/api/docs/models/gpt-6-sol
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
retrieved: "2026-11-01"
---

# GPT-6 Sol Pro

## Overview
GPT-6 Sol Pro is OpenRouter's id for GPT-6 Sol with `reasoning.mode` set to `pro`. OpenAI has no separate Pro id for its GPT-6 models; its model page lists only `gpt-6-sol`. GPT-5.6 and GPT-6 models accept `standard` (default) or `pro` mode in the Responses API, independent of `reasoning.effort`. Pro mode does more model work per request and bills those tokens at the model's standard rates. Everything else follows GPT-6 Sol, the high-end tier below GPT-6 Astra and above GPT-6 Luna, since followed by GPT-6.1 Sol and GPT-6.1 Terra: text and image input, text output, a 1,050,000-token context window, 128,000 max output tokens and an April 20, 2026 knowledge cutoff. OpenRouter listed it on September 22, 2026, the day GPT-6 Sol was released. OpenAI's deprecations page gives GPT-6 Sol no retirement date.

## Strengths
- Higher-quality responses on complex tasks than standard mode, per OpenRouter, which reserves it for hard, high-stakes problems.
- GPT-6 Sol's per-token rates: 2 USD input and 10 USD output per million tokens.
- OpenRouter lists none, low, medium (default), high, xhigh and max effort.

## Limitations
- OpenRouter says a typical request costs several times more than on GPT-6 Sol and takes much longer to complete.
- Artificial Analysis does not test pro mode; its GPT-6 Sol (Max) results are for standard mode.
- GPT-6 Sol supports function calling in Chat Completions only with effort none; use the Responses API for tools.
- Prompts over 272,000 input tokens cost 4 and 15 USD per million. Closed weights.

## Good for
- The hardest coding and agent problems in a deployment pinned to GPT-6 Sol.
- Background or batch jobs that can wait for long responses.
- Checking the work of standard-mode runs.
