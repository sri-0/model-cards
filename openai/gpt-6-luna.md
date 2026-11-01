---
id: openai/gpt-6-luna
name: GPT-6 Luna
owned_by: openai
type: llm
description: GPT-6 Luna is the fastest and cheapest tier of OpenAI's GPT-6 family, below Astra, Sol and Terra, released in September 2026 for focused, high-volume tasks.
aliases: [gpt-6-luna, openai/gpt-6-luna-20260922, "openai/gpt-6-luna:batch", openai.gpt-6-luna, us.openai.gpt-6-luna, global.openai.gpt-6-luna, azure/gpt-6-luna, azure/gpt-6-luna-2026-09-22]
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
benchmarks:
  humanitys_last_exam: 38.5
  intelligence_index: 27.8
  long_context_reasoning: 83.3
  mmmu_pro: 79.7
  omniscience_index: -8.3
  output_tokens_per_second: 118.3
  scicode: 54.6
  terminal_bench_4: 12.6
  time_to_first_token_seconds: 97.69
benchmark_variant: GPT-6 Luna (Max)
sources:
  - https://openrouter.ai/openai/gpt-6-luna
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-6-luna
  - https://artificialanalysis.ai/models/gpt-6-sol
  - https://developers.openai.com/api/docs/models/gpt-6-luna
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-luna.html
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-6 Luna

## Overview
GPT-6 Luna is the cheapest tier of OpenAI's GPT-6 family, released on September 22, 2026 with GPT-6 Sol; OpenAI's GPT-6 guide ranks it below GPT-6.1 Terra, GPT-6.1 Sol and the flagship GPT-6 Astra and calls it the fastest and most cost-effective. OpenRouter says that at higher effort it can take on complex software engineering and computer-use tasks that previously needed a Sol-tier model. It takes text and image input and returns text, with a 1,050,000-token context window (922,000 input), 128,000 max output tokens and a May 18, 2026 knowledge cutoff. `reasoning.effort` supports none, low, medium (default), high, xhigh and max; pro mode is a Responses API setting (see GPT-6 Luna Pro). OpenAI lists only the snapshot `gpt-6-luna`; Microsoft Foundry's version is 2026-09-22 and Bedrock's id is `openai.gpt-6-luna`. It also serves OpenAI's Decisions API. OpenAI gives no retirement date and names it the replacement for GPT-4o, GPT-4.1 and their mini models (shutting down January 14, 2027) and GPT-5.4 nano (April 1, 2027).

## Strengths
- 0.10 USD input and 0.50 USD output per million tokens, half GPT-5.6 Luna's input price.
- Artificial Analysis Intelligence Index (v5.0) of 27.8 for GPT-6 Luna (Max), with 83.3% on AA-LCR and 79.7% on MMMU-Pro.
- About 118 output tokens per second at Max.

## Limitations
- Terminal-Bench 4.0 was 12.6% at Max, against 43.9% for GPT-6 Sol (Max).
- AA-Omniscience was -8.3 at Max: wrong answers outweighed correct ones.
- Time to first token at Max was about 98 seconds.
- Chat Completions allows function calling only with effort none; use the Responses API for tools.
- Prompts over 272,000 input tokens cost double on input and 1.5 times on output. Closed weights.

## Good for
- Classification, routing, extraction and summarisation at scale.
- Latency-sensitive chat.
- Replacing GPT-4o, GPT-4.1 or GPT-5.4 nano before their 2027 shutdowns.
