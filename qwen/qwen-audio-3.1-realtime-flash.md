---
id: qwen/qwen-audio-3.1-realtime-flash
name: Qwen-Audio-3.1-Realtime-Flash
owned_by: qwen
type: llm
description: "Qwen-Audio-3.1-Realtime-Flash is Alibaba current low-cost hosted real-time duplex speech model on Model Studio, with text and audio in and out, function calling, web search, voice cloning and turn-detection modes."
context_length: 262144
max_output_tokens: 16384
capabilities: [tool_calling]
architecture:
  input_modalities: [text, audio]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-10-27"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-1-realtime-flash
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.1-Realtime-Flash

## Overview
Qwen-Audio-3.1-Realtime-Flash (Model Studio id `qwen-audio-3.1-realtime-flash`) is a real-time duplex speech model released on 2026-10-27; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. It takes text and audio and returns text and audio over WebSocket, WebRTC or AOQ, with function calling, web search (both can be enabled together) and voice cloning; the default voice is longanqian_v3.1, and `enable_thinking` is not supported. Turn handling offers server_vad, smart_turn, smart_turn_v2 (recommended) and push-to-talk, with speaker enhancement in the smart-turn modes. Limits are a 262,144-token context with 245,760 input and 16,384 output tokens and audio history of up to 50 turns and 300 seconds. Singapore prices per million tokens: $0.23 text input, $0.93 audio input, $0.70 text output and $1.87 audio output.

## Strengths
- Tools and web search together in a live session.
- Low price per token.

## Limitations
- No thinking mode.
- Older audio history is limited to 50 turns and 300 seconds.

## Good for
- Low-cost voice agents and customer service.
