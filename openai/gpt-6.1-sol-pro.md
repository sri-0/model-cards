---
id: openai/gpt-6.1-sol-pro
name: GPT-6.1 Sol Pro
owned_by: openai
type: llm
description: GPT-6.1 Sol Pro is OpenRouter's id for OpenAI's GPT-6.1 Sol run with reasoning.mode set to pro, which spends more model work per request on complex tasks, billed at Sol's per-token rates.
aliases: [openai/gpt-6.1-sol-pro-20260929, "openai/gpt-6.1-sol-pro:batch"]
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
release_date: "2026-09-29"
knowledge_cutoff: "2026-04"
pricing:
  input: 2
  output: 10
  cache_read: 0.1
  cache_write: 2.5
sources:
  - https://openrouter.ai/openai/gpt-6.1-sol-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-6-1-sol
  - https://developers.openai.com/api/docs/models/gpt-6.1-sol
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
retrieved: "2026-11-01"
---

# GPT-6.1 Sol Pro

## Overview
GPT-6.1 Sol Pro is OpenRouter's id for GPT-6.1 Sol with `reasoning.mode` set to `pro`. OpenAI has no separate Pro id for its GPT-6 models; its model page lists only `gpt-6.1-sol`. GPT-5.6 and GPT-6 models accept `standard` (default) or `pro` mode in the Responses API, independent of `reasoning.effort`. Pro mode does more model work per request and bills those tokens at the model's standard rates. Everything else follows GPT-6.1 Sol, the near-Astra tier below GPT-6 Astra and above GPT-6.1 Terra and GPT-6 Luna: text and image input, text output, a 1,050,000-token context window, 128,000 max output tokens and an April 30, 2026 knowledge cutoff. OpenRouter listed it on September 29, 2026, the day GPT-6.1 Sol was released. OpenAI's deprecations page gives GPT-6.1 Sol no retirement date.

## Strengths
- Higher-quality responses on complex tasks than standard mode, per OpenRouter, which reserves it for hard, high-stakes problems.
- GPT-6.1 Sol's per-token rates: 2 USD input and 10 USD output per million tokens, a fifth of Astra's.
- OpenRouter lists low, medium (default), high, xhigh and max effort; reasoning cannot be turned off.

## Limitations
- OpenRouter says a typical request costs several times more than on GPT-6.1 Sol and takes much longer to complete.
- Artificial Analysis does not test pro mode; GPT-6.1 Sol (Max) in standard mode already took about 315 seconds to first token.
- Tool calling requires the Responses API; temperature, top_p and logprobs are not accepted.
- Prompts over 272,000 input tokens cost 4 and 15 USD per million. Closed weights.

## Good for
- The hardest coding, computer-use and analysis problems without Astra prices.
- Background or batch jobs that can wait many minutes per response.
- Final review of work produced by standard-mode or cheaper models.
