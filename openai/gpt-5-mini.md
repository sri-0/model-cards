---
id: openai/gpt-5-mini
name: GPT-5 Mini
owned_by: openai
type: llm
description: GPT-5 mini is the mid-sized member of OpenAI's August 2025 GPT-5 family for cost-sensitive, low-latency, high-volume reasoning work, now deprecated with shutdown set for 11 December 2026.
aliases: [gpt-5-mini, gpt-5-mini-2025-08-07, openai/gpt-5-mini-2025-08-07, openai/gpt-5-mini:batch, azure/gpt-5-mini, azure/gpt-5-mini-2025-08-07]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-08-07"
knowledge_cutoff: "2024-05"
pricing:
  input: 0.25
  output: 2
  cache_read: 0.025
benchmarks:
  coding_index: 15.6
  agentic_index: 6.8
  gpqa_diamond: 82.8
  humanitys_last_exam: 21.5
  ifbench: 75.4
  long_context_reasoning: 72.3
  mmmu_pro: 70.1
  output_tokens_per_second: 107.9
  scicode: 39.0
  tau2_bench: 68.4
  terminal_bench_4: 0
  terminal_bench_hard: 33.3
  time_to_first_token_seconds: 61.34
benchmark_variant: GPT-5 mini (High)
sources:
  - https://openrouter.ai/openai/gpt-5-mini
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-mini
  - https://developers.openai.com/api/docs/models/gpt-5-mini
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5 Mini

## Overview
GPT-5 mini is the mid-sized model of OpenAI's GPT-5 family, released to the API on 7 August 2025. OpenAI's docs position it for cost-sensitive, low-latency, high-volume workloads with well-defined tasks and precise prompts. It takes text and image input and returns text, with a 400,000-token context window, 272,000 max input tokens, 128,000 max output tokens and a 31 May 2024 knowledge cutoff. OpenRouter marks reasoning as mandatory with minimal, low, medium and high effort and medium as the default. The pinned snapshot is `gpt-5-mini-2025-08-07`. OpenAI deprecated it on 11 June 2026 with shutdown on 11 December 2026 and names `gpt-5.6-terra` as the replacement; its docs recommend GPT-5.6 Terra for new low-latency work. Azure runs it as `gpt-5-mini` version 2025-08-07, GA until 13 July 2027.

## Strengths
- Low price: 0.25 USD input and 2 USD output per million tokens, with cache reads at 0.025.
- Artificial Analysis measured the High variant at 82.8% on GPQA Diamond, 75.4% on IFBench and 72.3% on AA-LCR.
- About 108 output tokens per second at High.
- Tool calling, structured outputs and image input on the Chat Completions, Responses and Batch endpoints; `openai/gpt-5-mini:batch` on OpenRouter shares this card.

## Limitations
- Deprecated, with shutdown on 11 December 2026.
- Knowledge stops at May 2024, four months earlier than GPT-5.
- Scored 0 on Terminal-Bench 4.0 and 33.3% on Terminal-Bench Hard at High; OpenRouter reports a Coding Index of 15.6 and an Agentic Index of 6.8.
- Time to first token at High was about 61 seconds, including reasoning.
- Closed weights. API access only.

## Good for
- High-volume classification, extraction and summarisation where GPT-5 costs too much.
- Well-specified tasks with precise prompts, per OpenAI.
- Deployments pinned to the 2025-08-07 snapshot until shutdown.
