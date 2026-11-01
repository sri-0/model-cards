---
id: qwen/qwen-audio-3.0-realtime-flash
name: Qwen-Audio-3.0-Realtime-Flash
owned_by: qwen
type: llm
description: "Qwen-Audio-3.0-Realtime-Flash is the low-latency edition of Alibaba hosted Qwen 3.0 duplex speech dialogue model on Model Studio, with audio and text in and out, function calling and web search."
context_length: 40960
max_output_tokens: 8192
capabilities: [tool_calling, reasoning]
architecture:
  input_modalities: [text, audio]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-07-14"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-0-realtime-flash
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.0-Realtime-Flash

## Overview
Qwen-Audio-3.0-Realtime-Flash (Model Studio id `qwen-audio-3.0-realtime-flash`) is the Flash edition of Model Studio's Qwen 3.0 real-time speech dialogue model, released on 2026-07-14 in China (Beijing) and 2026-08-10 in Singapore; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes a duplex speech model, ranked first on Artificial Analysis's speech-to-speech benchmark per Model Studio, that uses parallel inference and full-streaming optimisation for a low-latency, fast and smart dialogue experience. It takes audio and text and returns audio and text, with function calling and web search but no structured output, caching or batch calls. Limits are a 40,960-token context with 16,384 input and 8,192 output tokens, and a 1,024-token chain of thought in thinking mode. Singapore prices per million tokens: $0.23 text input, $0.93 audio input, $0.70 text output and $1.87 audio output.

## Strengths
- Low latency for duplex voice.
- Audio at $0.93 input and $1.87 output, against $6.40 and $24 for the Plus edition.

## Limitations
- Short 40,960-token context.
- Superseded by Qwen-Audio-3.1-Realtime-Flash.

## Good for
- High-volume voice agents and customer service.
