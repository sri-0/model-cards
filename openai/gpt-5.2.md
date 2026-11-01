---
id: openai/gpt-5.2
name: GPT-5.2
owned_by: openai
type: llm
description: GPT-5.2 is OpenAI's December 2025 flagship for complex professional work, with adaptive reasoning from none up to xhigh effort and an August 2025 knowledge cutoff, since superseded by GPT-5.4 and later.
aliases: [gpt-5.2, gpt-5.2-2025-12-11, openai/gpt-5.2-20251211, openai/gpt-5.2:batch, azure/gpt-5.2, azure/gpt-5.2-2025-12-11]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [file, image, text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-12-11"
knowledge_cutoff: "2025-08"
pricing:
  input: 1.75
  output: 14
  cache_read: 0.175
benchmarks:
  gpqa_diamond: 90.3
  humanitys_last_exam: 37.7
  ifbench: 75.4
  long_context_reasoning: 82.7
  output_tokens_per_second: 70.3
  tau2_bench: 84.8
  terminal_bench_hard: 47.0
  time_to_first_token_seconds: 102.33
benchmark_variant: GPT-5.2 (Xhigh)
sources:
  - https://openrouter.ai/openai/gpt-5.2
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-2
  - https://developers.openai.com/api/docs/models/gpt-5.2
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.2

## Overview
GPT-5.2 is a proprietary OpenAI model released on 11 December 2025 as the then-flagship of the GPT-5 family. OpenAI's docs now call it the previous flagship for complex professional work and recommend GPT-6 Astra; OpenRouter says it improved agentic and long-context performance over GPT-5.1 with adaptive reasoning. It takes text and image input and returns text, with a 400,000-token context window, 128,000 max output tokens and a 31 August 2025 knowledge cutoff. `reasoning.effort` supports none (the default), low, medium, high and xhigh. The pinned snapshot is `gpt-5.2-2025-12-11`. OpenAI's changelog notes a roughly 40% speed-up on 3 February 2026. OpenAI's deprecations page lists no shutdown for it as of 1 November 2026; Artificial Analysis marks it superseded by GPT-5.4. Azure runs `gpt-5.2` version 2025-12-11 as GA until 8 June 2027.

## Strengths
- Artificial Analysis measured the Xhigh variant at 90.3% on GPQA Diamond, 82.7% on AA-LCR, 47.0% on Terminal-Bench Hard and 37.7% on Humanity's Last Exam, each above GPT-5.1 (High).
- Knowledge to August 2025.
- Tool calling, structured outputs, image input and `verbosity` on Chat Completions, Responses and Batch; `openai/gpt-5.2:batch` on OpenRouter shares this card.
- Cache reads at 0.175 USD per million tokens.

## Limitations
- Dearer than GPT-5.1: 1.75 USD input and 14 USD output per million tokens.
- About 70 output tokens per second and a time to first token of about 102 seconds at Xhigh, including reasoning.
- Reasoning is off by default; the benchmark figures need `reasoning.effort` set to xhigh.
- Not deprecated as of 1 November 2026, but OpenAI no longer recommends it for new work. Closed weights.

## Good for
- Professional analysis, long-document work and agentic coding on a GPT-5.x snapshot that is still supported.
- Workloads that need an August 2025 knowledge cutoff without moving to the GPT-5.4 or GPT-6 pricing tiers.
