---
id: qwen/qwen3.5-omni-plus-realtime
name: Qwen3.5-Omni-Plus-Realtime
owned_by: qwen
type: llm
description: "Qwen3.5-Omni-Plus-Realtime is the real-time version of Alibaba hosted Qwen3.5-Omni-Plus on Model Studio, for live audio-visual conversation with speech output, function calling, web search and semantic interruption."
aliases: [qwen3.5-omni-plus-realtime-2026-03-15]
context_length: 262144
max_output_tokens: 65536
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-03-26"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-5-omni-plus-realtime
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/realtime
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.5-Omni-Plus-Realtime

## Overview
Qwen3.5-Omni-Plus-Realtime (Model Studio id `qwen3.5-omni-plus-realtime`, functionally equivalent to the `qwen3.5-omni-plus-realtime-2026-03-15` snapshot) is the real-time counterpart of qwen/qwen3.5-omni-plus; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio released it on 2026-03-26 in Singapore and 2026-03-30 in China (Beijing). It accepts text, images, video and audio and returns text and audio, with audio input in 60+ languages, voice output in 30+ languages, controllable voice dialogue, web search, complex function calling and intelligent semantic interruption. The model page gives a 262,144-token context with 196,608 input and 65,536 output tokens, 60 requests and 100,000 tokens per minute, and no structured output, caching or batch calls. Singapore prices per million tokens: $2.10 text, image or video input, $16.50 audio input, $12.40 text output and $62 audio output, with the text of spoken replies not charged.

## Strengths
- Function calling and web search in a live voice session.
- Long 262K-token context for a real-time model.

## Limitations
- Highest per-token prices of Model Studio real-time Omni models.
- No structured output.

## Good for
- Voice assistants that call tools mid-conversation.
