---
id: qwen/qwen-audio-3.1-realtime-plus
name: Qwen-Audio-3.1-Realtime-Plus
owned_by: qwen
type: llm
description: "Qwen-Audio-3.1-Realtime-Plus is Alibaba current higher-quality hosted real-time duplex speech model on Model Studio, with text and audio in and out, function calling, web search and voice cloning."
context_length: 262144
max_output_tokens: 16384
capabilities: [tool_calling]
architecture:
  input_modalities: [text, audio]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-09-20"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-1-realtime-plus
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.1-Realtime-Plus

## Overview
Qwen-Audio-3.1-Realtime-Plus (Model Studio id `qwen-audio-3.1-realtime-plus`) is a real-time duplex speech model released on 2026-09-20 and listed first among speech-to-speech models on Model Studio's models page; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. It takes text and audio and returns text and audio, with function calling, web search through `enable_search` (not together with function calling) and voice cloning; the default voice is longanqian_v3.1. Limits are a 262,144-token context with 245,760 input and 16,384 output tokens, at 60 requests and 100,000 tokens per minute, where WebSocket requests count connections. Singapore prices per million tokens: $0.80 text input, $6.40 audio input, $6.40 text output and $24 audio output; text-only replies bill at the text rate and replies with audio bill only the audio.

## Strengths
- Long 262K-token context for a speech model.
- Voice cloning in a live session.

## Limitations
- Web search and function calling cannot run together.
- Higher price than the Flash edition.

## Good for
- Premium voice assistants and character voices.
