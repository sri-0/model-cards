---
id: qwen/qwen3.7-flash
name: Qwen3.7 Flash
owned_by: qwen
type: llm
description: "Qwen3.7 Flash is Alibaba's low-cost hosted vision-language reasoning model with a 1M-token context, served on Model Studio as qwen3.7-flash (snapshot 2026-07-15), with upgraded object recognition, spatial understanding and multimodal agent execution over Qwen3.6 Flash."
aliases: [qwen3.7-flash, qwen3.7-flash-2026-07-15]
context_length: 1000000
max_output_tokens: 65536
capabilities: [tool_calling, reasoning, vision]
supported_parameters: [include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, temperature, tool_choice, tools, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
pricing:
  input: 0.03
  output: 0.13
  cache_read: 0.006
  cache_write: 0.038
sources:
  - https://openrouter.ai/qwen/qwen3.7-flash
  - https://openrouter.ai/api/v1/models
  - https://www.qwencloud.com/models/qwen3.7-flash
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
retrieved: "2026-10-16"
---

# Qwen3.7 Flash

## Overview
Qwen3.7 Flash is Alibaba's hosted Flash tier of the Qwen3.7 series, served through Alibaba Cloud Model Studio and Qwen Cloud with no published weights. Model Studio's pricing page (read 2026-10-16) says the stable `qwen3.7-flash` is currently equivalent to `qwen3.7-flash-2026-07-15`, and the model is in Model Studio's current recommended list; OpenRouter listed it on 2026-07-27. Qwen Cloud describes a comprehensive upgrade over Qwen3.6 Flash in multimodal understanding and agent execution: stronger object recognition, better real-world perception and spatial intelligence, more stable execution for search and code-interpreter agents, and smoother multimodal coding. It takes text, image and video input with thinking togglable per request. OpenRouter lists a 1,000,000-token context and 65,536-token output; Qwen Cloud gives 991K max input and 131K max output. Pricing is tiered by prompt length. The card holds OpenRouter's base tier for prompts under 32,000 tokens: $0.03 input, $0.13 output, $0.006 cache read and $0.038 cache write per million tokens. From 32,000 prompt tokens OpenRouter charges $0.1, $0.4, $0.02 and $0.125, and from 256,000 tokens $0.2, $0.8, $0.04 and $0.25. Model Studio's International list price follows the same three tiers.

## Strengths
- Lowest OpenRouter price among the Qwen3.7 models, with image and video input, 1M context and function calling.
- Qwen Cloud highlights object recognition, spatial understanding and GUI or computer interaction.

## Limitations
- Artificial Analysis figures are not recorded in this card.
- The cheap tier applies only to prompts under 32,000 tokens; long prompts cost up to six times more.
- OpenRouter's listing does not include structured outputs among its capabilities.

## Good for
- Multimodal agents, visual coding and search at low cost.
- Short-prompt, high-volume vision tasks such as object recognition and screen reading.
