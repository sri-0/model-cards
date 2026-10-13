---
id: z-ai/glm-5-turbo
name: GLM 5 Turbo
owned_by: z-ai
type: llm
description: GLM-5-Turbo is a proprietary Z.ai text model tuned for fast, long-chain agent execution, especially in OpenClaw workflows, with a 200K-token context window.
aliases: [glm-5-turbo]
context_length: 202752
max_output_tokens: 131072
capabilities: [tool_calling, reasoning]
supported_parameters: [include_reasoning, max_tokens, reasoning, response_format, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-03-15"
pricing:
  input: 1.2
  output: 4
  cache_read: 0.24
benchmarks:
  intelligence_index: 26.6
  omniscience_index: -16.4
  humanitys_last_exam: 27.8
  gpqa_diamond: 84.7
  terminal_bench_hard: 33.3
  long_context_reasoning: 71.7
  ifbench: 73.2
  tau2_bench: 98.5
benchmark_variant: GLM-5-Turbo
sources:
  - https://openrouter.ai/z-ai/glm-5-turbo
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-5-turbo
  - https://docs.z.ai/guides/llm/glm-5-turbo
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 5 Turbo

## Overview
GLM-5-Turbo was released in March 2026 and is available through Z.ai's API, not as open weights. Z.ai says it was optimised from the training stage for OpenClaw agent tasks: tool calling, following complex instructions, scheduled and persistent tasks, and long execution chains. It takes text input and returns text, with a 200K-token context window and 128K max output. Z.ai lists multiple thinking modes, streaming, function calling, context caching, structured output and MCP integration.

## Strengths
- Artificial Analysis places GLM-5-Turbo among the leading models on its Intelligence Index (score 27, marked as estimated, against a median of 12 for comparable models).
- Z.ai reports gains over GLM-5 on its ZClawBench benchmark for OpenClaw tasks, and has published that dataset.
- Designed for stable multi-step tool use and time-based, long-running tasks.

## Limitations
- Closed weights. Cannot be self-hosted.
- Text only.
- Artificial Analysis publishes no speed or latency figures for it.
- Tuning targets one agent ecosystem (OpenClaw); results elsewhere may differ.

## Good for
- OpenClaw and similar agent frameworks that chain many tool calls.
- Scheduled, persistent or long-running automation tasks.
- Multi-agent setups that need reliable instruction decomposition.
