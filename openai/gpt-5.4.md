---
id: openai/gpt-5.4
name: GPT-5.4
owned_by: openai
type: llm
description: GPT-5.4 is OpenAI's general-purpose reasoning model for coding and professional work, released in March 2026, with text and image input and a context window of about 1M tokens.
aliases: [gpt-5.4, gpt-5.4-2026-03-05]
context_length: 1050000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-03-05"
knowledge_cutoff: "2025-08"
pricing:
  input: 2.5
  output: 15
  cache_read: 0.25
benchmarks:
  intelligence_index: 39
  coding_index: 71.1
  omniscience_index: 5.8
  humanitys_last_exam: 43.7
  gpqa_diamond: 92
  terminal_bench_hard: 57.6
  long_context_reasoning: 82
  ifbench: 73.9
  tau2_bench: 87.1
  mmmu_pro: 78.4
  output_tokens_per_second: 91.6
  time_to_first_token_seconds: 197.28
benchmark_variant: GPT-5.4 (Xhigh)
sources:
  - https://openrouter.ai/openai/gpt-5.4
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-4
  - https://developers.openai.com/api/docs/models/gpt-5.4
retrieved: "2026-10-14"
---

# GPT-5.4

## Overview
GPT-5.4 is a proprietary OpenAI model that, per OpenRouter, merges the Codex and GPT lines into one system. It accepts text and image input and returns text. OpenAI lists a 1,050,000-token context window, 128,000 max output tokens and an August 31, 2025 knowledge cutoff. Reasoning is controlled with `reasoning.effort`: none (default), low, medium, high and xhigh. The pinned snapshot is `gpt-5.4-2026-03-05`.

## Strengths
- Artificial Analysis rates GPT-5.4 (Xhigh) above average on its Intelligence Index (score 39, marked as estimated).
- Output speed of about 92 tokens per second on the Xhigh variant, faster than the Artificial Analysis average.
- Supports tool calling, structured outputs and image input.
- OpenRouter describes gains in coding, document understanding, tool use and instruction following.

## Limitations
- Closed weights. API access only.
- Artificial Analysis calls it somewhat expensive for its price tier. OpenRouter charges more for prompts over 272,000 tokens (input 5 and output 22.5 USD per million tokens).
- Time to first token at Xhigh is high (about 197 seconds) because it includes reasoning time.
- Knowledge stops at August 2025.

## Good for
- General-purpose assistant and agent work where one default model is wanted.
- Software engineering and multi-step tool workflows.
- Reading and reasoning over long documents and mixed text and image input.
