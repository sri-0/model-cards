---
id: qwen/qwen3.5-omni-flash-realtime
name: Qwen3.5-Omni-Flash-Realtime
owned_by: qwen
type: llm
description: "Qwen3.5-Omni-Flash-Realtime is the lower-priced real-time version of Alibaba hosted Qwen3.5-Omni on Model Studio, for live audio-visual conversation with speech output, function calling, web search and semantic interruption."
aliases: [qwen3.5-omni-flash-realtime-2026-03-15]
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
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-5-omni-flash-realtime
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/realtime
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.5-Omni-Flash-Realtime

## Overview
Qwen3.5-Omni-Flash-Realtime (Model Studio id `qwen3.5-omni-flash-realtime`, documented as equivalent to the `qwen3.5-omni-flash-realtime-2026-03-15` snapshot) is the real-time counterpart of qwen/qwen3.5-omni-flash; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio released it on 2026-03-26 in Singapore and 2026-03-30 in China (Beijing). It accepts text, images, video and audio and returns text and audio, with audio input in 60+ languages, voice output in 30+ languages, controllable voice dialogue, web search, complex function calling and intelligent semantic interruption. The model page gives a 262,144-token context with 196,608 input and 65,536 output tokens and no structured output, caching or batch calls. Singapore prices per million tokens: $0.55 text, image or video input, $4.50 audio input, $3.30 text output and $17.70 audio output, with the text of spoken replies not charged.

## Strengths
- Roughly a quarter of the Plus real-time prices.
- Function calling and web search in a live voice session.

## Limitations
- No structured output.
- Model Studio publishes no quality comparison with the Plus edition.

## Good for
- Cost-sensitive live voice agents.
