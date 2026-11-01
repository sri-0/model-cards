---
id: qwen/qwen3.8-omni-flash-realtime
name: Qwen3.8-Omni-Flash-Realtime
owned_by: qwen
type: llm
description: "Qwen3.8-Omni-Flash-Realtime is Alibaba hosted real-time audio and video interaction model on Model Studio, with text and speech output, custom and remote MCP tool calling, and multichannel audio input."
max_output_tokens: 65536
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, audio, video]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-09-21"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-8-omni-flash-realtime
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/realtime
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.8-Omni-Flash-Realtime

## Overview
Qwen3.8-Omni-Flash-Realtime (Model Studio id `qwen3.8-omni-flash-realtime`) is the real-time member of the Qwen3.8 Omni line, released on 2026-09-21 in China (Beijing) and Singapore and recommended on Model Studio's models page for real-time audio-video conversation; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. It takes text, streaming audio and video as consecutive frames and returns text and audio, with custom tool calling, remote MCP tools, 1-, 2- or 4-channel 16 kHz PCM audio over WebSocket, optional video aggregation and the default voice Tina. Access is through WebSocket, WebRTC or AOQ. Limits are 196,608 total input tokens and 65,536 output tokens, with audio history of up to 100 turns and 600 seconds and video history of up to 50 turns and 240 seconds. Singapore prices per million tokens: $0.23 text, image or video input, $0.93 audio input, $0.70 text output and $1.87 audio output; unlike Qwen3.5-Omni-Realtime, the text of spoken replies is also billed.

## Strengths
- MCP and custom tools in a live session.
- Lowest per-token prices of Model Studio real-time Omni models.

## Limitations
- Older history is dropped past the turn and duration limits.
- Text of spoken replies is billed as well as audio.

## Good for
- Real-time voice and video agents that use tools.
