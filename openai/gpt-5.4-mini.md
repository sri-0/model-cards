---
id: openai/gpt-5.4-mini
name: GPT-5.4 Mini
owned_by: openai
type: llm
description: GPT-5.4 mini is a smaller, faster and cheaper GPT-5.4-class OpenAI model for high-volume reasoning, coding and agent work, with a 400K-token context window.
aliases: [gpt-5.4-mini, gpt-5.4-mini-2026-03-17]
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
  input: 0.75
  output: 4.5
  cache_read: 0.075
benchmarks:
  intelligence_index: 24.1
  coding_index: 56.1
  agentic_index: 17.9
  omniscience_index: -18.9
  humanitys_last_exam: 28.1
  gpqa_diamond: 87.5
  scicode: 52.1
  terminal_bench_hard: 52.3
  terminal_bench_4: 2
  long_context_reasoning: 77
  ifbench: 73.3
  tau2_bench: 83.3
  mmmu_pro: 73.3
  output_tokens_per_second: 233.1
  time_to_first_token_seconds: 127.99
benchmark_variant: GPT-5.4 mini (Xhigh)
sources:
  - https://openrouter.ai/openai/gpt-5.4-mini
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-4-mini
  - https://developers.openai.com/api/docs/models/gpt-5.4-mini
retrieved: "2026-10-14"
---

# GPT-5.4 Mini

## Overview
GPT-5.4 mini is a proprietary OpenAI model released in March 2026. OpenAI describes it as its strongest mini model for coding, computer use and subagents. It accepts text and image input and returns text, with a 400,000-token context window, 128,000 max output tokens and an August 31, 2025 knowledge cutoff. `reasoning.effort` supports none (default), low, medium, high and xhigh. The pinned snapshot is `gpt-5.4-mini-2026-03-17`.

## Strengths
- Fast: Artificial Analysis measured about 233 tokens per second on GPT-5.4 mini (Xhigh).
- Low price per token (0.75 USD input and 4.5 USD output per million tokens on OpenRouter), which Artificial Analysis calls well priced.
- Tool calling, structured outputs and image input.
- Same reasoning-effort controls as GPT-5.4.

## Limitations
- Artificial Analysis rates the Xhigh variant below average on its Intelligence Index (score 24) and very verbose: it generated 230M tokens during the index run against a median of 85M.
- Time to first token at Xhigh is about 128 seconds, which includes reasoning time.
- Smaller context window than GPT-5.4.
- Closed weights. Knowledge stops at August 2025.

## Good for
- High-throughput chat and coding assistants.
- Subagents and worker steps in multi-agent systems.
- Workloads where cost and latency matter more than peak reasoning quality.
