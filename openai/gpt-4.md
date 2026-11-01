---
id: openai/gpt-4
name: GPT-4
owned_by: openai
type: llm
description: GPT-4 is OpenAI's original 8K-context text-only GPT-4 model of March 2023, shut down on OpenAI's API on 2026-10-23 but still listed by OpenRouter.
aliases: [gpt-4, gpt-4-0613, gpt-4-0314, gpt-4-completions, gpt-4-0613-completions, azure/gpt-4, azure/gpt-4-0613]
context_length: 8191
max_output_tokens: 4096
capabilities: [tool_calling]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_completion_tokens, presence_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2023-03-14"
knowledge_cutoff: "2023-12"
pricing:
  input: 30
  output: 60
benchmarks:
  coding_index: 13.1
  gpqa_diamond: 34.9
  ifbench: 33.2
benchmark_variant: GPT-4
sources:
  - https://openrouter.ai/openai/gpt-4
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-4
  - https://developers.openai.com/api/docs/models/gpt-4
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4

## Overview
GPT-4 is OpenAI's original GPT-4 model, released on 2023-03-14 (Artificial Analysis date). It is text-only, with an 8,192-token context window on OpenAI's page (OpenRouter lists 8,191) and 8,192 max output tokens per OpenAI (4,096 on OpenRouter). OpenAI's page gives a knowledge cutoff of December 2023, which the frontmatter follows; OpenRouter and Artificial Analysis both give September 2021. The snapshots are `gpt-4-0613` (the default) and `gpt-4-0314`; the 32K-context `gpt-4-32k` model and its snapshots have their own card. OpenAI served it on Chat Completions, Responses, Batch and Fine-tuning with streaming, at $30 input and $60 output per million tokens; its page lists neither function calling nor structured outputs, though OpenRouter reports tool calling. OpenAI lists it as Shut down: `gpt-4-0314` on 2026-03-26 (replacement GPT-5 or GPT-4.1), and `gpt-4` and `gpt-4-0613` on 2026-10-23 (replacement `gpt-5.6-sol`). OpenRouter still listed `openai/gpt-4` on 2026-11-01 at OpenAI's old price.

## Strengths
- OpenRouter describes it as solving difficult problems with greater accuracy than earlier models thanks to broader general knowledge, and reports a Coding Index of 13.1.
- Artificial Analysis measured 34.9% on GPQA Diamond and 33.2% on IFBench.

## Limitations
- Shut down on OpenAI's API, and $60 per million output tokens on OpenRouter.
- 8K context window and text-only input.
- Artificial Analysis publishes no speed or agentic results for it.
- Sources disagree on the knowledge cutoff (see Overview).

## Good for
- Reproducing 2023 and 2024 results that were built on it.
- Comparisons against a known 2023 baseline.
