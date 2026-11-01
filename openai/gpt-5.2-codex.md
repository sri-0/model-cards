---
id: openai/gpt-5.2-codex
name: GPT-5.2-Codex
owned_by: openai
type: llm
description: GPT-5.2-Codex is OpenAI's January 2026 upgrade of GPT-5.1-Codex for long-horizon agentic coding, served through the Responses API only and shut down by OpenAI on 23 July 2026.
aliases: [gpt-5.2-codex, openai/gpt-5.2-codex-20260114, azure/gpt-5.2-codex]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-01-14"
knowledge_cutoff: "2025-08"
pricing:
  input: 1.75
  output: 14
  cache_read: 0.175
benchmarks:
  gpqa_diamond: 89.9
  humanitys_last_exam: 35.7
  ifbench: 77.6
  long_context_reasoning: 82.3
  mmmu_pro: 76.3
  output_tokens_per_second: 90.4
  tau2_bench: 92.1
  terminal_bench_hard: 37.1
  time_to_first_token_seconds: 117.85
benchmark_variant: GPT-5.2 Codex (Xhigh)
sources:
  - https://openrouter.ai/openai/gpt-5.2-codex
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-2-codex
  - https://developers.openai.com/api/docs/models/gpt-5.2-codex
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.2-Codex

## Overview
GPT-5.2-Codex is a proprietary OpenAI model released to the Responses API on 14 January 2026; Artificial Analysis dates it 11 December 2025, when it reached Codex with GPT-5.2. OpenAI's docs call it its most intelligent coding model at the time, optimised for long-horizon agentic coding; OpenRouter describes it as an upgraded GPT-5.1-Codex for interactive sessions and long independent engineering runs. It takes text and image input and returns text, with a 400,000-token context window, 272,000 max input tokens, 128,000 max output tokens and a 31 August 2025 knowledge cutoff. `reasoning.effort` supports low, medium, high and xhigh; OpenRouter marks reasoning as mandatory with medium as the default. Responses tools include function calling, web search, hosted shell and skills. OpenAI announced its shutdown on 22 April 2026 and shut it down on 23 July 2026, naming `gpt-5.6-sol` as the replacement; Artificial Analysis points to GPT-5.3 Codex. OpenRouter still listed the id on 1 November 2026. Azure runs `gpt-5.2-codex` version 2026-01-14 as GA until 13 July 2027.

## Strengths
- Artificial Analysis measured the Xhigh variant at 92.1% on tau2-bench, 89.9% on GPQA Diamond, 82.3% on AA-LCR and 77.6% on IFBench.
- Hosted shell and skills tools for agentic coding on the Responses API.
- About 90 output tokens per second at Xhigh, faster than GPT-5.2 (Xhigh).
- Knowledge to August 2025.

## Limitations
- Shut down on OpenAI's API since 23 July 2026.
- Responses API only; no Chat Completions or Batch.
- Terminal-Bench Hard of 37.1% at Xhigh is below GPT-5.2 (Xhigh) at 47.0%.
- Time to first token at Xhigh was about 118 seconds, including reasoning. Closed weights.

## Good for
- Long agentic coding sessions on an Azure deployment or an OpenRouter route that still serves it.
- A reference point when migrating Codex workloads to GPT-5.3-Codex or GPT-5.6 Sol.
