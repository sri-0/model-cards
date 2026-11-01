---
id: qwen/qwen3.8-max-prime
name: Qwen3.8 Max Prime
owned_by: qwen
type: llm
description: "Qwen3.8 Max Prime is the higher-throughput, higher-priced fast-mode SKU of Alibaba's hosted Qwen3.8 Max, with the same text, image and video input, 1M-token context, reasoning-effort control and tool support."
aliases: [qwen3.8-max-prime]
context_length: 1000000
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, reasoning_effort, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
pricing:
  input: 4
  output: 12
  cache_read: 0.5
sources:
  - https://openrouter.ai/qwen/qwen3.8-max-prime
  - https://openrouter.ai/api/v1/models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
retrieved: "2026-10-16"
---

# Qwen3.8 Max Prime

## Overview
Qwen3.8 Max Prime is a higher-throughput variant of Alibaba's hosted Qwen3.8 Max, which OpenRouter says is served as a separate SKU at a higher price point; OpenRouter listed it on 2026-09-23. Alibaba Cloud Model Studio's pricing page (read 2026-10-16) lists `qwen3.8-max-prime` as "Fast mode (Prime)" in its Global deployment table at $3.301 input and $9.902 output per million tokens for non-thinking and thinking modes up to 1M tokens; Qwen Cloud has no page for it and no weights are published. It matches Qwen3.8 Max in capability: text, image and video input, a 1,000,000-token context and 131,072-token output on OpenRouter, reasoning enabled by default with configurable effort, tool calling and structured outputs. OpenRouter charges $4 input, $12 output and $0.5 cached input per million tokens, twice the $2, $6 and $0.25 it charges for Qwen3.8 Max 0902, with no long-prompt tier. Neither OpenRouter nor Alibaba publishes a throughput figure for the Prime SKU, and no release date or knowledge cutoff is stated.

## Strengths
- Same model quality and features as Qwen3.8 Max (see qwen/qwen3.8-max-0902) with faster serving.
- Full multimodal input with 1M context and reasoning-effort control.

## Limitations
- Twice the OpenRouter price of Qwen3.8 Max 0902.
- No published speed measurement, and no Artificial Analysis figures in this card.
- Not documented on Qwen Cloud; Model Studio lists it only on the pricing page.

## Good for
- Latency-sensitive agents and interactive coding sessions that already use Qwen3.8 Max.
- Workloads where faster responses justify the premium.
