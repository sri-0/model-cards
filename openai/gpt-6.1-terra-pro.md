---
id: openai/gpt-6.1-terra-pro
name: GPT-6.1 Terra Pro
owned_by: openai
type: llm
description: GPT-6.1 Terra Pro is OpenRouter's id for OpenAI's GPT-6.1 Terra run with reasoning.mode set to pro, which spends more model work per request on complex tasks, billed at Terra's per-token rates.
aliases: [openai/gpt-6.1-terra-pro-20261026, "openai/gpt-6.1-terra-pro:batch"]
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
release_date: "2026-10-26"
knowledge_cutoff: "2026-06"
pricing:
  input: 1
  output: 5
  cache_read: 0.05
  cache_write: 1.25
sources:
  - https://openrouter.ai/openai/gpt-6.1-terra-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-6-1-terra
  - https://developers.openai.com/api/docs/models/gpt-6.1-terra
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
retrieved: "2026-11-01"
---

# GPT-6.1 Terra Pro

## Overview
GPT-6.1 Terra Pro is OpenRouter's id for GPT-6.1 Terra with `reasoning.mode` set to `pro`. OpenAI has no separate Pro id for its GPT-6 models; its model page lists only `gpt-6.1-terra`. GPT-5.6 and GPT-6 models accept `standard` (default) or `pro` mode in the Responses API, independent of `reasoning.effort`. Pro mode does more model work per request and bills those tokens at the model's standard rates. Everything else follows GPT-6.1 Terra, the mid tier below GPT-6 Astra and GPT-6.1 Sol and above GPT-6 Luna: text and image input, text output, a 1,050,000-token context window, 128,000 max output tokens and a June 1, 2026 knowledge cutoff. OpenRouter listed it on October 26, 2026, the day GPT-6.1 Terra was released. OpenAI's deprecations page gives GPT-6.1 Terra no retirement date.

## Strengths
- Higher-quality responses on complex tasks than standard mode, per OpenRouter, which reserves it for hard, high-stakes problems.
- Terra's per-token rates: 1 USD input and 5 USD output per million tokens.
- OpenRouter lists low, medium (default), high, xhigh and max effort for the Pro id, with reasoning always on, although the base id also accepts none.

## Limitations
- OpenRouter says a typical request costs several times more than on GPT-6.1 Terra and takes much longer to complete.
- Artificial Analysis does not test pro mode; GPT-6.1 Terra (Max) in standard mode already took about 275 seconds to first token.
- Tool calling requires the Responses API.
- Prompts over 272,000 input tokens cost double on input and 1.5 times on output. Closed weights.

## Good for
- Harder screenshot, computer-use or writing tasks in a Terra-based pipeline.
- Getting more from Terra before paying Sol prices.
- Batch work where latency does not matter.
