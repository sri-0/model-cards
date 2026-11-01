---
id: openai/gpt-5-codex
name: GPT-5 Codex
owned_by: openai
type: llm
description: GPT-5-Codex is OpenAI's September 2025 version of GPT-5 tuned for agentic coding in Codex, served through the Responses API only and shut down by OpenAI on 23 July 2026.
aliases: [gpt-5-codex, azure/gpt-5-codex]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-09-23"
knowledge_cutoff: "2024-09"
benchmarks:
  gpqa_diamond: 83.7
  humanitys_last_exam: 27.8
  ifbench: 74.1
  long_context_reasoning: 71.7
  mmmu_pro: 73.8
  output_tokens_per_second: 173.4
  tau2_bench: 86.8
  terminal_bench_hard: 37.9
  time_to_first_token_seconds: 10.22
benchmark_variant: GPT-5 Codex (High)
sources:
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-codex
  - https://developers.openai.com/api/docs/models/gpt-5-codex
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5 Codex

## Overview
GPT-5-Codex is a proprietary OpenAI model that OpenAI's changelog describes as a special-purpose model built and optimised for the Codex CLI, launched in the API on 23 September 2025 (Artificial Analysis gives the same date). OpenRouter does not list it; the id follows OpenAI's API id `gpt-5-codex`. OpenAI's docs give a 400,000-token context window, 272,000 max input tokens, 128,000 max output tokens and a 30 September 2024 knowledge cutoff, with text and image input, reasoning tokens, function calling, structured outputs, web search and prompt caching on the Responses API only. OpenAI priced it at 1.25 USD input, 0.125 cached input and 10 USD output per million tokens. OpenAI announced the shutdown on 22 April 2026 and shut the model down on 23 July 2026, naming `gpt-5.6-sol` as the replacement; Artificial Analysis points to GPT-5.1 Codex as its successor. Azure lists `gpt-5-codex` version 2025-09-15 as GA with a retirement date of 17 March 2027.

## Strengths
- Artificial Analysis measured the High variant at 86.8% on tau2-bench, 83.7% on GPQA Diamond and 37.9% on Terminal-Bench Hard, ahead of GPT-5 (High) on the terminal benchmark.
- About 173 output tokens per second and a 10-second time to first token at High, far quicker than GPT-5 (High).
- Image input, so screenshots and diagrams can accompany code.

## Limitations
- Shut down on OpenAI's API since 23 July 2026; only Azure still lists a deployment.
- Responses API only; no Chat Completions or Batch.
- OpenAI's docs do not list reasoning effort levels for it.
- Knowledge stops at September 2024. Closed weights.

## Good for
- Historical reference for Codex CLI pipelines built on it, now migrated to GPT-5.6 Sol or a later Codex model.
- Azure deployments that still run the 2025-09-15 version.
