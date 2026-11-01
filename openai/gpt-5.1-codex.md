---
id: openai/gpt-5.1-codex
name: GPT-5.1-Codex
owned_by: openai
type: llm
description: GPT-5.1-Codex is OpenAI's November 2025 version of GPT-5.1 tuned for agentic coding in Codex, served through the Responses API only and shut down by OpenAI on 23 July 2026.
aliases: [gpt-5.1-codex, openai/gpt-5.1-codex-20251113, azure/gpt-5.1-codex, azure/gpt-5.1-codex-2025-11-13]
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
release_date: "2025-11-13"
knowledge_cutoff: "2024-09"
pricing:
  input: 1.25
  output: 10
  cache_read: 0.13
benchmarks:
  gpqa_diamond: 86.0
  humanitys_last_exam: 25.7
  ifbench: 70.0
  long_context_reasoning: 69.3
  mmmu_pro: 72.5
  output_tokens_per_second: 126.8
  tau2_bench: 83.0
  terminal_bench_hard: 34.8
  time_to_first_token_seconds: 7.47
benchmark_variant: GPT-5.1 Codex (High)
sources:
  - https://openrouter.ai/openai/gpt-5.1-codex
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-1-codex
  - https://developers.openai.com/api/docs/models/gpt-5.1-codex
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.1-Codex

## Overview
GPT-5.1-Codex is a proprietary OpenAI model released to the Responses API on 13 November 2025 with GPT-5.1 and GPT-5.1-Codex-Mini. OpenAI's docs call it a version of GPT-5.1 optimised for agentic coding in Codex; OpenRouter adds that it is built for both interactive sessions and long independent runs of engineering tasks. It takes text and image input and returns text, with a 400,000-token context window, 128,000 max output tokens and a 30 September 2024 knowledge cutoff. OpenRouter lists reasoning as mandatory with low, medium and high effort and medium as the default. OpenAI announced its shutdown on 22 April 2026 and shut it down on 23 July 2026, naming `gpt-5.6-sol` as the replacement; Artificial Analysis points to GPT-5.2 Codex as the successor. OpenRouter still listed the id on 1 November 2026. Azure runs `gpt-5.1-codex` version 2025-11-13 as GA until 15 May 2027.

## Strengths
- Artificial Analysis measured the High variant at 86.0% on GPQA Diamond, 83.0% on tau2-bench and 72.5% on MMMU-Pro.
- About 127 output tokens per second and a 7.5-second time to first token at High, the quickest start of the GPT-5.1 line.
- Function calling, structured outputs, web search and prompt caching on the Responses API.
- Priced like GPT-5.1 at 1.25 USD input and 10 USD output per million tokens.

## Limitations
- Shut down on OpenAI's API since 23 July 2026.
- Responses API only; no Chat Completions or Batch.
- Terminal-Bench Hard at 34.8% (High) is below GPT-5.1 (High) at 45.5%, and AA-LCR of 69.3% is lower too.
- Knowledge stops at September 2024. Closed weights.

## Good for
- Codex-style coding agents that still route through OpenRouter or an Azure deployment.
- Historical reference when migrating to GPT-5.2 Codex, GPT-5.3 Codex or GPT-5.6 Sol.
