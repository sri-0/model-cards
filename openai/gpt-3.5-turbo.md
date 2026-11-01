---
id: openai/gpt-3.5-turbo
name: GPT-3.5 Turbo
owned_by: openai
type: llm
description: GPT-3.5 Turbo is OpenAI's legacy text-only chat model, in 4K and 16K-context snapshots, shut down on OpenAI's API on 2026-10-23.
aliases: [gpt-3.5-turbo, gpt-3.5-turbo-0125, gpt-3.5-turbo-1106, gpt-3.5-turbo-0613, gpt-3.5-turbo-16k, gpt-3.5-turbo-16k-0613, gpt-3.5-turbo-0301, gpt-3.5-turbo-completions, openai/gpt-3.5-turbo-0613, openai/gpt-3.5-turbo-16k, gpt-35-turbo, gpt-35-turbo-16k, azure/gpt-35-turbo, azure/gpt-35-turbo-16k, azure/gpt-35-turbo-16k-0613, azure/gpt-3.5-turbo]
context_length: 16385
max_output_tokens: 4096
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_completion_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2022-11-30"
knowledge_cutoff: "2021-09"
pricing:
  input: 3
  output: 4
benchmarks:
  gpqa_diamond: 29.7
benchmark_variant: GPT-3.5 Turbo
sources:
  - https://openrouter.ai/openai/gpt-3.5-turbo-16k
  - https://openrouter.ai/openai/gpt-3.5-turbo-0613
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-3-5-turbo
  - https://artificialanalysis.ai/models/gpt-3-5-turbo-0613
  - https://developers.openai.com/api/docs/models/gpt-3.5-turbo
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-3.5 Turbo

## Overview
GPT-3.5 Turbo is the text-only model OpenAI's page calls its legacy GPT model for cheaper chat and non-chat tasks; Artificial Analysis dates it to 2022-11-30. OpenRouter does not list the bare id. It lists two older endpoints: `openai/gpt-3.5-turbo-0613` (4,095-token context, $1 input and $2 output per million tokens) and `openai/gpt-3.5-turbo-16k` (16,385 tokens, $3 and $4). They share this card because OpenAI's deprecations page treats `gpt-3.5-turbo-0613` and `gpt-3.5-turbo-16k-0613` as earlier snapshots replaced by `gpt-3.5-turbo`, which since November 2023 has 16K context by default. The frontmatter uses the 16k listing, whose limits match OpenAI's page: 16,385-token context, 4,096 max output and a September 2021 knowledge cutoff. Later snapshots were `gpt-3.5-turbo-1106` and `gpt-3.5-turbo-0125` (the default, at $0.50 and $1.50 on OpenAI); `gpt-3.5-turbo-instruct` is a separate Completions model with its own card. All are shut down: 0301, 0613 and 16k-0613 on 2024-09-13, 1106 on 2026-09-28, and `gpt-3.5-turbo` itself on 2026-10-23, with `gpt-5.6-terra` as the recommended replacement. OpenAI had recommended GPT-4o mini in its place since July 2024. Azure's name for it is `gpt-35-turbo`.

## Strengths
- OpenRouter describes it as OpenAI's fastest model of its time, for chat and traditional completion tasks.
- Artificial Analysis measured 29.7% on GPQA Diamond.
- OpenRouter lists tool calling and structured outputs on both endpoints, and OpenAI offered fine-tuning.

## Limitations
- Shut down on OpenAI's API; the OpenRouter endpoints are snapshots OpenAI retired in 2024.
- 4K or 16K context, text only, and a September 2021 knowledge cutoff.
- Artificial Analysis publishes no speed, agentic or long-context results, and none at all for the 0613 snapshot.

## Good for
- Reproducing results from 2023-era applications.
- A baseline when comparing against 2023 systems.
