---
id: qwen/qwen3.5-plus-20260420
name: Qwen3.5 Plus 2026-04-20
owned_by: qwen
type: llm
description: "Qwen3.5 Plus (snapshot 2026-04-20) is the newer of Alibaba's two hosted Qwen3.5 Plus snapshots, a 1M-context vision-language mixture-of-experts model with better agentic coding and faster inference than the 2026-02-15 snapshot."
aliases: [qwen3.5-plus-2026-04-20]
context_length: 1000000
max_output_tokens: 65536
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: false
license: proprietary
pricing:
  input: 0.3
  output: 1.8
  cache_write: 0.375
sources:
  - https://openrouter.ai/qwen/qwen3.5-plus-20260420
  - https://openrouter.ai/api/v1/models
  - https://www.qwencloud.com/models/qwen3.5-plus-2026-04-20
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
retrieved: "2026-10-16"
---

# Qwen3.5 Plus 2026-04-20

## Overview
Qwen3.5 Plus 2026-04-20 is the newer of the two Qwen3.5 Plus snapshots that OpenRouter serves (the older is qwen/qwen3.5-plus-02-15); both ids remain available. Qwen Cloud describes a substantial improvement in agentic coding over the February 15th snapshot, with significantly faster inference while knowledge, reasoning and long-context handling stay at the same level, and says the version is based on a snapshot taken on 2026-04-20. OpenRouter listed it on 2026-04-27. On Alibaba Cloud Model Studio it is the id `qwen3.5-plus-2026-04-20`; the stable `qwen3.5-plus` still resolves to the February snapshot according to the pricing page read on 2026-10-16, and the Qwen3.5 models are filed as legacy. Like the earlier snapshot it is a hosted-only vision-language mixture-of-experts model with text, image and video input, thinking togglable per request, a 1,000,000-token context and a 65,536-token output limit (Qwen Cloud: 991K max input, 65K max output). OpenRouter charges $0.3 input, $1.8 output and $0.375 cache write per million tokens up to 256,000 prompt tokens, and $0.375, $2.25 and $0.46875 from there; Model Studio's International list price is $0.4 and $2.4 for the first 256K tokens.

## Strengths
- Better agentic coding and faster responses than the February snapshot, according to Qwen Cloud.
- 1M context, image and video input, function calling, built-in tools and structured output.
- Qwen suggests it for coding agents, production workflows and high-throughput use.

## Limitations
- Legacy on Model Studio; Qwen3.6 Plus and later models replaced it in the recommended list.
- Artificial Analysis figures are not recorded in this card.
- Prompts of 256,000 tokens or more are billed at the higher tier on OpenRouter.

## Good for
- Coding agents and automated workflows that want Qwen3.5 Plus quality at lower latency.
- Long-context extraction and summarisation.
