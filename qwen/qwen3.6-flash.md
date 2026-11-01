---
id: qwen/qwen3.6-flash
name: Qwen3.6 Flash
owned_by: qwen
type: llm
description: "Qwen3.6 Flash is Alibaba's hosted Qwen3.6 vision-language model with a 1M-token context, served on Model Studio as qwen3.6-flash (snapshot 2026-04-16), with stronger agentic coding and spatial understanding than Qwen3.5 Flash."
aliases: [qwen3.6-flash, qwen3.6-flash-2026-04-16]
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
  input: 0.1875
  output: 1.125
  cache_write: 0.234375
sources:
  - https://openrouter.ai/qwen/qwen3.6-flash
  - https://openrouter.ai/api/v1/models
  - https://www.qwencloud.com/models/qwen3.6-flash
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
retrieved: "2026-10-16"
---

# Qwen3.6 Flash

## Overview
Qwen3.6 Flash is Alibaba's hosted Flash tier of the Qwen3.6 series, served through Alibaba Cloud Model Studio and Qwen Cloud with no published weights. Model Studio's pricing page (read 2026-10-16) says the stable `qwen3.6-flash` is currently equivalent to `qwen3.6-flash-2026-04-16`, and OpenRouter listed the model on 2026-04-27. Qwen Cloud describes a significant performance boost over Qwen3.5 Flash: agentic coding well ahead of its predecessor on several code-agent benchmarks, better mathematical and code reasoning, and markedly improved spatial intelligence with better object localisation and detection. It is a native vision-language model taking text, image and video input, with thinking togglable per request. OpenRouter lists a 1,000,000-token context and 65,536-token output; Qwen Cloud gives 991K max input and 65K max output. OpenRouter's description states that tiered pricing kicks in above 256K tokens and that prompt caching is supported with explicit cache read and cache creation pricing. The card's pricing is the base tier: $0.1875 input, $1.125 output and $0.234375 cache write per million tokens; from 256,000 prompt tokens OpenRouter charges $0.75, $3 and $0.9375. Model Studio's International list price is $0.25 input and $1.5 output for the first 256K tokens. Model Studio now files the Qwen3.6 models as legacy.

## Strengths
- Stronger agentic coding and visual grounding than Qwen3.5 Flash, according to Qwen Cloud.
- 1M context, image and video input, function calling, built-in tools and structured output at Flash-tier prices.

## Limitations
- Legacy on Model Studio; Qwen3.7 Flash and Qwen3.8 Flash have followed it.
- Artificial Analysis figures are not recorded in this card.
- Long prompts cost four times the base input price on OpenRouter.

## Good for
- Low-cost coding and tool-use agents.
- Object detection, localisation and document understanding over images and video.
