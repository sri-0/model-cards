---
id: openai/gpt-5-nano
name: GPT-5 Nano
owned_by: openai
type: llm
description: GPT-5 nano is the smallest and cheapest member of OpenAI's August 2025 GPT-5 family, aimed at summarisation and classification, now deprecated with shutdown set for 11 December 2026.
aliases: [gpt-5-nano, gpt-5-nano-2025-08-07, openai/gpt-5-nano-2025-08-07, openai/gpt-5-nano:batch, azure/gpt-5-nano, azure/gpt-5-nano-2025-08-07]
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
  input: 0.05
  output: 0.4
  cache_read: 0.005
benchmarks:
  gpqa_diamond: 67.6
  humanitys_last_exam: 9.5
  ifbench: 67.6
  long_context_reasoning: 45.0
  mmmu_pro: 61.0
  output_tokens_per_second: 144.3
  tau2_bench: 36.5
  terminal_bench_hard: 12.1
  time_to_first_token_seconds: 76.77
benchmark_variant: GPT-5 nano (High)
sources:
  - https://openrouter.ai/openai/gpt-5-nano
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-nano
  - https://developers.openai.com/api/docs/models/gpt-5-nano
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5 Nano

## Overview
GPT-5 nano is the smallest model of OpenAI's GPT-5 family, released to the API on 7 August 2025. OpenAI's docs call it the fastest, most cost-efficient version of GPT-5 and suggest it for summarisation and classification; OpenRouter describes it as built for developer tools and low-latency interactions with limited reasoning depth. It takes text and image input and returns text, with a 400,000-token context window, 272,000 max input tokens, 128,000 max output tokens and a 31 May 2024 knowledge cutoff. OpenRouter marks reasoning as mandatory with minimal, low, medium and high effort and medium as the default. The pinned snapshot is `gpt-5-nano-2025-08-07`. OpenAI deprecated it on 11 June 2026 with shutdown on 11 December 2026 and names `gpt-5.6-luna` as the replacement. Azure runs it as `gpt-5-nano` version 2025-08-07, GA until 9 February 2027.

## Strengths
- Cheapest of the family: 0.05 USD input and 0.4 USD output per million tokens, cache reads at 0.005.
- About 144 output tokens per second at High, the fastest GPT-5 variant Artificial Analysis measured.
- Tool calling, structured outputs and image input; Chat Completions, Responses and Batch endpoints (`openai/gpt-5-nano:batch` on OpenRouter).
- Responses API tools include web search, file search, code interpreter and MCP.

## Limitations
- Deprecated, with shutdown on 11 December 2026.
- Artificial Analysis scores at High are well below GPT-5 mini: 67.6% on GPQA Diamond, 45.0% on AA-LCR, 36.5% on tau2-bench and 12.1% on Terminal-Bench Hard.
- Knowledge stops at May 2024.
- Time to first token at High was about 77 seconds, including reasoning.
- Closed weights.

## Good for
- Bulk summarisation, classification and extraction at the lowest price in the family.
- Latency-sensitive developer tooling with simple prompts.
- Deployments pinned to the 2025-08-07 snapshot until shutdown.
