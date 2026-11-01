---
id: openai/gpt-5.1
name: GPT-5.1
owned_by: openai
type: llm
description: GPT-5.1 is OpenAI's November 2025 flagship for coding and agentic tasks with adaptive reasoning that can be switched off, now deprecated with shutdown set for 1 April 2027.
aliases: [gpt-5.1, gpt-5.1-2025-11-13, openai/gpt-5.1-20251113, openai/gpt-5.1:batch, azure/gpt-5.1, azure/gpt-5.1-2025-11-13]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [image, text, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-11-13"
knowledge_cutoff: "2024-09"
pricing:
  input: 1.25
  output: 10
  cache_read: 0.125
benchmarks:
  coding_index: 49.4
  gpqa_diamond: 87.3
  humanitys_last_exam: 28.5
  ifbench: 72.9
  long_context_reasoning: 80.0
  mmmu_pro: 75.5
  output_tokens_per_second: 92.5
  tau2_bench: 81.9
  terminal_bench_hard: 45.5
  time_to_first_token_seconds: 37.82
benchmark_variant: GPT-5.1 (High)
sources:
  - https://openrouter.ai/openai/gpt-5.1
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-1
  - https://developers.openai.com/api/docs/models/gpt-5.1
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.1

## Overview
GPT-5.1 is a proprietary OpenAI model released on 13 November 2025 as the flagship of the GPT-5 family. OpenRouter says it improves on GPT-5 in general-purpose reasoning, instruction adherence and conversational style, and uses adaptive reasoning to allocate computation per request. It takes text and image input and returns text, with a 400,000-token context window, 128,000 max output tokens and a 30 September 2024 knowledge cutoff. `reasoning.effort` supports none (the default), low, medium and high, so reasoning must be requested explicitly. The pinned snapshot is `gpt-5.1-2025-11-13`. OpenAI deprecated it on 1 October 2026 and shuts it down on 1 April 2027, naming `gpt-6-sol` as the replacement. Azure runs it as `gpt-5.1` version 2025-11-13, GA until 13 July 2027, and uses it as the automatic upgrade target for retiring gpt-4o deployments.

## Strengths
- Artificial Analysis measured the High variant at 87.3% on GPQA Diamond, 80.0% on AA-LCR and 45.5% on Terminal-Bench Hard, up from 32.6% for GPT-5 (High).
- OpenRouter reports an Artificial Analysis Coding Index of 49.4.
- Time to first token at High of about 38 seconds, less than half of GPT-5 (High).
- Same price as GPT-5: 1.25 USD input and 10 USD output per million tokens, cache reads at 0.125.
- Chat Completions, Responses and Batch endpoints; `openai/gpt-5.1:batch` on OpenRouter shares this card.

## Limitations
- Deprecated, with shutdown on 1 April 2027.
- Knowledge stops at September 2024, the same cutoff as GPT-5.
- Reasoning is off by default, so the benchmark figures above need `reasoning.effort` set.
- Closed weights. API access only.

## Good for
- General assistant and agent work on a pinned GPT-5-family snapshot until April 2027.
- Low-latency chat with reasoning off, and harder coding or analysis with it on.
- Azure deployments inheriting the gpt-4o upgrade path.
