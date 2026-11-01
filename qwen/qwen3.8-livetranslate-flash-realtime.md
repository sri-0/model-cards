---
id: qwen/qwen3.8-livetranslate-flash-realtime
name: Qwen3.8-LiveTranslate-Flash-Realtime
owned_by: qwen
type: llm
description: "Qwen3.8-LiveTranslate-Flash-Realtime is Alibaba hosted multilingual real-time audio and video translation model on Model Studio, understanding 60 languages and speaking 29."
context_length: 53248
max_output_tokens: 4096
capabilities: [vision]
architecture:
  input_modalities: [audio, image]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-8-livetranslate-flash-realtime
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-5-livetranslate-flash-realtime
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.8-LiveTranslate-Flash-Realtime

## Overview
Qwen3.8-LiveTranslate-Flash-Realtime (Model Studio id `qwen3.8-livetranslate-flash-realtime`) is the newest real-time translation model on Model Studio and the one its real-time translation guide uses in examples; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio's release table gives no date for it. It accepts audio and images and produces text and audio, understanding 60 languages and speaking 29. It has a 53,248-token context with 49,152 input and 4,096 output tokens, and no function calling, structured output or caching. It is called through the Realtime API over AOQ, WebRTC or WebSocket; `session.output_modalities` selects the outputs, and translated text streams as `response.text.delta` or `response.audio_transcript.delta`. Its parameters and events differ from Qwen3.5-LiveTranslate-Flash-Realtime. Singapore prices per million tokens: $7.50 audio input, $0.55 image input, $20 text output and $30 audio output, at 10 requests per minute.

## Strengths
- Speech output in 29 languages.
- Visual input for context.

## Limitations
- Only 10 requests per minute by default.
- Not a drop-in replacement for the Qwen3.5 version.

## Good for
- Live interpretation of calls and video.
