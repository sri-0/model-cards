---
id: qwen/qwen3.5-flash-02-23
name: Qwen3.5 Flash
owned_by: qwen
type: llm
description: "Qwen3.5 Flash (snapshot 2026-02-23) is Alibaba's hosted vision-language mixture-of-experts model with a 1M-token context, the production version of the open Qwen3.5-35B-A3B, served on Model Studio as qwen3.5-flash."
aliases: [qwen3.5-flash, qwen3.5-flash-2026-02-23]
context_length: 1000000
max_output_tokens: 65536
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: false
license: proprietary
pricing:
  input: 0.065
  output: 0.26
sources:
  - https://openrouter.ai/qwen/qwen3.5-flash-02-23
  - https://openrouter.ai/api/v1/models
  - https://www.qwencloud.com/models/qwen3.5-flash
  - https://huggingface.co/Qwen/Qwen3.5-35B-A3B
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
retrieved: "2026-10-16"
---

# Qwen3.5 Flash

## Overview
Qwen3.5 Flash is Alibaba's hosted Flash tier of the Qwen3.5 series, served through Alibaba Cloud Model Studio and Qwen Cloud with no published weights; Qwen's Hugging Face card for Qwen3.5-35B-A3B names Qwen3.5 Flash as that model's hosted version with a 1M-token default context and built-in tools. OpenRouter's id carries the 2026-02-23 snapshot date and OpenRouter listed it on 2026-02-25. Model Studio's pricing page (read 2026-10-16) says the stable `qwen3.5-flash` is currently equivalent to `qwen3.5-flash-2026-02-23`, and files the Qwen3.5 models as legacy. It is a native vision-language model on a hybrid architecture of linear attention and sparse mixture-of-experts, taking text, image and video input with thinking togglable per request. OpenRouter lists a 1,000,000-token context and 65,536-token output; Qwen Cloud gives 991K max input, 65K max output and 81K max reasoning tokens. OpenRouter charges $0.065 input and $0.26 output per million tokens with no long-prompt tier; Model Studio's International list price is $0.1 and $0.4.

## Strengths
- Cheapest Qwen3.5 hosted model, with the full 1M context, image and video input, function calling, built-in tools and structured output.
- Qwen describes fast responses balancing speed and performance, and a leap over the Qwen3 series.
- For the open Qwen3.5-35B-A3B it is based on, Qwen reports SWE-bench Verified 69.2 and TAU2-Bench 81.2; the hosted snapshot is not benchmarked separately there.

## Limitations
- Legacy on Model Studio; Qwen3.6, 3.7 and 3.8 Flash have followed it.
- Artificial Analysis figures are not recorded in this card.
- 65,536-token output limit, and no published release date beyond the snapshot id.

## Good for
- Low-cost multimodal chat, extraction and summarisation over long inputs.
- Existing integrations pinned to the February 2026 snapshot.
