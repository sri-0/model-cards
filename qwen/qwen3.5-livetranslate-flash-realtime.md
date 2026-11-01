---
id: qwen/qwen3.5-livetranslate-flash-realtime
name: Qwen3.5-LiveTranslate-Flash-Realtime
owned_by: qwen
type: llm
description: "Qwen3.5-LiveTranslate-Flash-Realtime is Alibaba hosted real-time speech and audio-visual translation model on Model Studio, translating among 60 languages with 2.3-second latency, speaker diarisation, hotwords and voice cloning."
aliases: [qwen3.5-livetranslate-flash-realtime-2026-05-19]
capabilities: [vision]
architecture:
  input_modalities: [audio, image]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-05-19"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-5-livetranslate-flash-realtime
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.5-LiveTranslate-Flash-Realtime

## Overview
Qwen3.5-LiveTranslate-Flash-Realtime (Model Studio id `qwen3.5-livetranslate-flash-realtime`, with snapshot `qwen3.5-livetranslate-flash-realtime-2026-05-19`) was released on 2026-05-19; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio's real-time translation guide says the LiveTranslate realtime models take audio and images and output text or speech in the target language, translating between 60 languages (29 with audio and text output, 31 with text only). They read visual cues such as lip movements, gestures and on-screen text to resolve ambiguity, reach latency as low as 2.3 seconds, separate speakers in turn-taking, predict semantic units to handle word-order differences, match the source intonation and emotion, accept hotwords, and can clone the speaker's voice in real time or from a saved profile. Access is over AOQ, WebRTC or WebSocket. Singapore prices per million tokens: $7.50 audio input, $0.55 image input, $20 text output and $30 audio output.

## Strengths
- Simultaneous interpretation with cloned voices.
- Visual cues improve accuracy in noise.

## Limitations
- Parameters and events differ from Qwen3.8-LiveTranslate-Flash-Realtime.

## Good for
- Live meetings and video streams across languages.
