---
id: openai/gpt-5
name: GPT-5
owned_by: openai
type: llm
description: GPT-5 is OpenAI's August 2025 reasoning model for coding and agentic tasks with configurable reasoning effort, now deprecated with shutdown set for 11 December 2026.
aliases: [gpt-5, gpt-5-2025-08-07, openai/gpt-5-2025-08-07, openai/gpt-5:batch, azure/gpt-5, azure/gpt-5-2025-08-07]
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
knowledge_cutoff: "2024-09"
pricing:
  input: 1.25
  output: 10
  cache_read: 0.125
benchmarks:
  coding_index: 37.8
  gpqa_diamond: 85.4
  humanitys_last_exam: 28.5
  ifbench: 73.1
  long_context_reasoning: 78.2
  mmmu_pro: 74.2
  output_tokens_per_second: 101.6
  tau2_bench: 84.8
  terminal_bench_hard: 32.6
  time_to_first_token_seconds: 80.85
benchmark_variant: GPT-5 (High)
sources:
  - https://openrouter.ai/openai/gpt-5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5
  - https://developers.openai.com/api/docs/models/gpt-5
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5

## Overview
GPT-5 is a proprietary OpenAI reasoning model released to the API on 7 August 2025 together with GPT-5 mini and GPT-5 nano. OpenAI's docs now describe it as its previous reasoning model for coding and agentic tasks with configurable reasoning effort. It takes text and image input and returns text, with a 400,000-token context window, 272,000 max input tokens, 128,000 max output tokens and a 30 September 2024 knowledge cutoff. `reasoning.effort` supports minimal, low, medium and high; OpenRouter marks reasoning as mandatory with medium as the default. The pinned snapshot is `gpt-5-2025-08-07`. OpenAI deprecated the model on 11 June 2026 and shuts it down on 11 December 2026, naming `gpt-5.6-sol` as the replacement; its docs point new work at GPT-6 Astra. Azure runs it as `gpt-5` version 2025-08-07, listed GA with a retirement date of 9 February 2027.

## Strengths
- Artificial Analysis measured the High variant at 85.4% on GPQA Diamond, 84.8% on tau2-bench and 78.2% on AA-LCR long-context reasoning.
- About 102 output tokens per second at High.
- Tool calling, structured outputs, image input and a `verbosity` parameter.
- Chat Completions, Responses and Batch endpoints; OpenRouter's `openai/gpt-5:batch` variant shares this card.
- OpenRouter reports an Artificial Analysis Coding Index of 37.8.

## Limitations
- Deprecated, with shutdown on 11 December 2026.
- Knowledge stops at September 2024.
- Time to first token at High was about 81 seconds in Artificial Analysis's measurement because it includes reasoning.
- Terminal-Bench Hard at 32.6% and Humanity's Last Exam at 28.5% (High) trail the later GPT-5.x releases.
- Closed weights. API access only.

## Good for
- Existing integrations pinned to the 2025-08-07 snapshot until the December 2026 shutdown.
- General reasoning, coding and multi-step tool use where effort is tuned per request.
- A baseline when comparing against the GPT-5.6 and GPT-6 replacements OpenAI names.
