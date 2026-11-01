---
id: qwen/qwen-audio-3.0-realtime-plus
name: Qwen-Audio-3.0-Realtime-Plus
owned_by: qwen
type: llm
description: "Qwen-Audio-3.0-Realtime-Plus is the standard edition of Alibaba hosted Qwen 3.0 duplex speech dialogue model on Model Studio, with audio and text in and out, function calling and web search."
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
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-0-realtime-plus
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.0-Realtime-Plus

## Overview
Qwen-Audio-3.0-Realtime-Plus (Model Studio id `qwen-audio-3.0-realtime-plus`) is the standard edition of Model Studio's Qwen 3.0 real-time speech dialogue model, released on 2026-07-14 in China (Beijing) and 2026-08-10 in Singapore; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio calls it a next-generation duplex speech model ranked first on Artificial Analysis's speech-to-speech benchmark, balancing intelligence with duplex dialogue rhythm for natural conversation. It takes audio and text and returns audio and text, with function calling and web search but no structured output, caching or batch calls. Limits are a 40,960-token context with 16,384 input and 8,192 output tokens, and a 1,024-token chain of thought in thinking mode. Singapore prices per million tokens: $0.80 text input, $6.40 audio input, $6.40 text output and $24 audio output, with the text of spoken replies not charged.

## Strengths
- Natural duplex conversation rhythm, per Model Studio.
- Tools and web search during dialogue.

## Limitations
- Short 40,960-token context.
- Superseded by Qwen-Audio-3.1-Realtime-Plus.

## Good for
- Spoken assistants where reply quality matters more than latency.
