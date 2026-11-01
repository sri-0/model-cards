---
id: openai/gpt-6-astra-pro
name: GPT-6 Astra Pro
owned_by: openai
type: llm
description: GPT-6 Astra Pro is OpenRouter's id for OpenAI's GPT-6 Astra run with reasoning.mode set to pro, which spends more model work per request on the hardest tasks, billed at Astra's per-token rates.
aliases: [openai/gpt-6-astra-pro-20260903, "openai/gpt-6-astra-pro:batch"]
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
release_date: "2026-09-03"
knowledge_cutoff: "2026-04"
pricing:
  input: 10
  output: 50
  cache_read: 1
  cache_write: 12.5
sources:
  - https://openrouter.ai/openai/gpt-6-astra-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-6-astra
  - https://developers.openai.com/api/docs/models/gpt-6-astra
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
retrieved: "2026-11-01"
---

# GPT-6 Astra Pro

## Overview
GPT-6 Astra Pro is OpenRouter's id for GPT-6 Astra with `reasoning.mode` set to `pro`. OpenAI has no separate Pro id for its GPT-6 models; its model page lists only `gpt-6-astra`. GPT-5.6 and GPT-6 models accept `standard` (default) or `pro` mode in the Responses API, independent of `reasoning.effort`. Pro mode does more model work per request and bills those tokens at the model's standard rates. Everything else follows GPT-6 Astra, the flagship above GPT-6.1 Sol, GPT-6.1 Terra and GPT-6 Luna: text and image input, text output, a 1,050,000-token context window, 128,000 max output tokens and an April 30, 2026 knowledge cutoff. OpenAI released GPT-6 Astra on September 3, 2026; OpenRouter listed the Pro id on September 4. OpenAI's deprecations page gives GPT-6 Astra no retirement date.

## Strengths
- Higher-quality responses on complex tasks than standard mode, per OpenRouter, which reserves it for hard, high-stakes problems.
- Astra's per-token rates: 10 USD input and 50 USD output per million tokens.
- OpenRouter lists low, medium (default), high, xhigh and max effort; reasoning cannot be turned off.

## Limitations
- OpenRouter says a typical request costs several times more than on GPT-6 Astra and takes much longer to complete.
- Artificial Analysis does not test pro mode; GPT-6 Astra (Max) in standard mode already took about 270 seconds to first token.
- Tool calling requires the Responses API; temperature, top_p and logprobs are not accepted.
- Prompts over 272,000 input tokens cost 20 and 75 USD per million. Closed weights.

## Good for
- The hardest problems, where answer quality outweighs any cost or latency.
- Background or batch jobs that can wait many minutes per response.
- Final review of work produced by cheaper models.
