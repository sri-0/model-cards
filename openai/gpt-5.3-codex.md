---
id: openai/gpt-5.3-codex
name: GPT-5.3-Codex
owned_by: openai
type: llm
description: GPT-5.3-Codex is OpenAI's February 2026 agentic coding model that combines GPT-5.2-Codex's software engineering with GPT-5.2's broader reasoning, served through the Responses API only and deprecated with shutdown set for 1 April 2027.
aliases: [gpt-5.3-codex, openai/gpt-5.3-codex-20260224, azure/gpt-5.3-codex]
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
release_date: "2026-02-24"
knowledge_cutoff: "2025-08"
pricing:
  input: 1.75
  output: 14
  cache_read: 0.175
benchmarks:
  gpqa_diamond: 91.5
  humanitys_last_exam: 42.5
  ifbench: 75.4
  long_context_reasoning: 83.3
  mmmu_pro: 78.5
  output_tokens_per_second: 79.1
  tau2_bench: 86.0
  terminal_bench_hard: 53.0
  time_to_first_token_seconds: 66.26
benchmark_variant: GPT-5.3 Codex (Xhigh)
sources:
  - https://openrouter.ai/openai/gpt-5.3-codex
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-3-codex
  - https://developers.openai.com/api/docs/models/gpt-5.3-codex
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.3-Codex

## Overview
GPT-5.3-Codex is a proprietary OpenAI model released to the Responses API on 24 February 2026; Artificial Analysis dates it 5 February 2026, when it reached Codex. OpenAI's docs call it the most capable agentic coding model to date, optimised for Codex; OpenRouter says it combines the software engineering performance of GPT-5.2-Codex with the broader reasoning and professional knowledge of GPT-5.2. It takes text and image input and returns text, with a 400,000-token context window, 272,000 max input tokens, 128,000 max output tokens and a 31 August 2025 knowledge cutoff. `reasoning.effort` supports low, medium, high and xhigh on OpenAI; OpenRouter also exposes none and lists medium as the default. Responses tools include function calling, web search, hosted shell and skills. OpenAI deprecated it on 1 October 2026 and shuts it down on 1 April 2027, naming `gpt-6-sol` as the replacement. Azure runs `gpt-5.3-codex` version 2026-02-24 as GA until 24 August 2027.

## Strengths
- Artificial Analysis measured the Xhigh variant at 53.0% on Terminal-Bench Hard, the best of the GPT-5.x Codex line, with 91.5% on GPQA Diamond, 83.3% on AA-LCR and 42.5% on Humanity's Last Exam.
- About 79 output tokens per second and a 66-second time to first token at Xhigh.
- Hosted shell and skills tools for agentic coding on the Responses API.
- Same price as GPT-5.2: 1.75 USD input and 14 USD output per million tokens, cache reads at 0.175.

## Limitations
- Deprecated, with shutdown on 1 April 2027.
- Responses API only; no Chat Completions or Batch.
- tau2-bench of 86.0% at Xhigh is below GPT-5.2-Codex (Xhigh) at 92.1%.
- Knowledge stops at August 2025. Closed weights.

## Good for
- Agentic coding in Codex, IDE agents and CI pipelines on a snapshot supported until April 2027.
- Terminal-heavy tasks and long repository work where GPT-5.2-Codex fell short.
