---
id: z-ai/glm-5.3-prime
name: GLM 5.3 Prime
owned_by: z-ai
type: llm
description: GLM-5.3-Prime is an accelerated serving variant of Z.ai's GLM-5.3 that OpenRouter lists with 1.5 to 2 times the output throughput and a 1M-token context window.
context_length: 1000000
max_output_tokens: 131072
capabilities: [tool_calling, reasoning]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, reasoning_effort, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
pricing:
  input: 2.8
  output: 8.8
  cache_read: 0.56
sources:
  - https://openrouter.ai/z-ai/glm-5.3-prime
  - https://openrouter.ai/api/v1/models
retrieved: "2026-10-14"
---

# GLM 5.3 Prime

## Overview
GLM-5.3-Prime is described by OpenRouter as the high-speed variant of GLM-5.3. It inherits GLM-5.3's capabilities and uses inference acceleration for 1.5 to 2 times the output throughput. On OpenRouter it is served via Alibaba Cloud. It accepts text and returns text, with a 1M-token context window and up to 128K output tokens. Reasoning is always on and cannot be disabled; efforts `low`, `high` and `max` are supported, with `max` as the default.

## Strengths
- Same model capabilities as GLM-5.3, with faster output.
- OpenRouter positions it for coding, long-horizon multi-turn agent orchestration, real-time conversation and streaming code generation.
- Tool calling and reasoning-effort control.

## Limitations
- Open-weight status for this variant is not stated. The published weights are for GLM-5.3.
- No Artificial Analysis data exists for GLM-5.3-Prime. See the GLM-5.3 card for measured figures.
- Text only. No image input.
- Priced higher than GLM-5.3 on OpenRouter (2.8 USD input and 8.8 USD output per million tokens).

## Good for
- Agent loops and coding tools where GLM-5.3 quality is needed with lower latency.
- Streaming code generation and interactive sessions.
