---
id: openai/gpt-5.4-nano
name: GPT-5.4 Nano
owned_by: openai
type: llm
description: GPT-5.4 nano is the smallest and cheapest GPT-5.4-class OpenAI model, aimed at simple high-volume tasks such as classification, extraction and ranking.
aliases: [gpt-5.4-nano, gpt-5.4-nano-2026-03-17]
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
release_date: "2026-03-17"
knowledge_cutoff: "2025-08"
pricing:
  input: 0.2
  output: 1.25
  cache_read: 0.02
benchmarks:
  intelligence_index: 20.7
  coding_index: 56.1
  agentic_index: 16
  omniscience_index: -29.5
  humanitys_last_exam: 28.3
  gpqa_diamond: 81.7
  scicode: 47.2
  terminal_bench_hard: 42.4
  terminal_bench_4: 0.5
  long_context_reasoning: 76.7
  ifbench: 75.9
  tau2_bench: 76
  mmmu_pro: 65.4
  output_tokens_per_second: 172.3
  time_to_first_token_seconds: 103.11
benchmark_variant: GPT-5.4 nano (Xhigh)
sources:
  - https://openrouter.ai/openai/gpt-5.4-nano
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-4-nano
  - https://developers.openai.com/api/docs/models/gpt-5.4-nano
retrieved: "2026-10-14"
---

# GPT-5.4 Nano

## Overview
GPT-5.4 nano is a proprietary OpenAI model released in March 2026. OpenAI's model page marks it as Deprecated, including the `gpt-5.4-nano-2026-03-17` snapshot. It accepts text and image input and returns text, with a 400,000-token context window, 128,000 max output tokens and an August 31, 2025 knowledge cutoff. `reasoning.effort` supports none (default), low, medium, high and xhigh.

## Strengths
- Lowest price in the GPT-5.4 family on OpenRouter: 0.2 USD input and 1.25 USD output per million tokens.
- Fast: Artificial Analysis measured about 172 tokens per second on GPT-5.4 nano (Xhigh).
- Artificial Analysis places the Xhigh variant above average for its price tier (Intelligence Index 21 against a tier median of 13).
- Tool calling, structured outputs and image input.

## Limitations
- Deprecated by OpenAI. Plan a replacement.
- OpenRouter notes it favours responsiveness over deep reasoning.
- Very verbose at Xhigh per Artificial Analysis. Time to first token at Xhigh is about 103 seconds, which includes reasoning time.
- Closed weights. Knowledge stops at August 2025.

## Good for
- Classification, data extraction and ranking at volume.
- Sub-agent execution and background pipeline steps.
- Low-latency tasks with low reasoning settings.
