---
id: openai/gpt-5.6-sol-pro
name: GPT-5.6 Sol Pro
owned_by: openai
type: llm
description: GPT-5.6 Sol Pro is OpenRouter's id for OpenAI's GPT-5.6 Sol run with reasoning.mode set to pro, OpenAI's named replacement for GPT-5 Pro and o3-pro, billed at Sol's per-token rates.
aliases: [openai/gpt-5.6-sol-pro-20260709, "openai/gpt-5.6-sol-pro:batch"]
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
  input: 4
  output: 20
  cache_read: 0.4
  cache_write: 5
sources:
  - https://openrouter.ai/openai/gpt-5.6-sol-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-6-sol
  - https://developers.openai.com/api/docs/models/gpt-5.6-sol
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/guides/latest-model/gpt-5.6
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
retrieved: "2026-11-01"
---

# GPT-5.6 Sol Pro

## Overview
GPT-5.6 Sol Pro is OpenRouter's id for GPT-5.6 Sol with `reasoning.mode` set to `pro`. OpenAI has no separate model id for it: GPT-5.6 and GPT-6 models accept `standard` (default) or `pro` mode in the Responses API, and OpenAI's GPT-5.6 guide says to keep the base model and set the mode rather than switch to a Pro slug. Pro mode does more model work per request and bills those tokens at the model's standard rates; effort is chosen separately. OpenAI's deprecations page names `gpt-5.6-sol` with `reasoning.mode: pro` as the replacement for GPT-5 Pro and o3-pro (both shutting down December 11, 2026) and o1-pro. Everything else follows GPT-5.6 Sol, the flagship above GPT-5.6 Terra and GPT-5.6 Luna: text and image input, text output, a 1,050,000-token context window, 128,000 max output tokens and a February 16, 2026 knowledge cutoff. OpenRouter listed it on July 9, 2026. OpenAI gives GPT-5.6 Sol no retirement date; Artificial Analysis marks it superseded by GPT-6 Sol.

## Strengths
- Higher-quality responses on complex tasks than standard mode, per OpenRouter.
- No Pro price premium: GPT-5.6 Sol's per-token rates, against 30 USD input and 180 USD output for GPT-5.5 Pro.
- OpenRouter lists none, low, medium (default), high, xhigh and max effort.

## Limitations
- OpenRouter says a typical request costs several times more than on GPT-5.6 Sol and takes much longer to complete.
- Artificial Analysis does not test pro mode; its GPT-5.6 Sol (Max) results are for standard mode.
- On OpenAI's API, pro mode is available only in the Responses API.
- Sol's 4 USD input and 20 USD output price is promotional, held at least through November 21, 2026. Closed weights.

## Good for
- Replacing GPT-5 Pro or o3-pro.
- The hardest coding and analysis problems in a GPT-5.6 deployment.
- Background or batch jobs that can wait.
