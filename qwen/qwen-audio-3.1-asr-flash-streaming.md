---
id: qwen/qwen-audio-3.1-asr-flash-streaming
name: Qwen-Audio-3.1-ASR-Flash-Streaming
owned_by: qwen
type: llm
description: "Qwen-Audio-3.1-ASR-Flash-Streaming is Alibaba current hosted real-time speech recognition model on Model Studio for conferencing, live subtitles and voice interaction, with Chinese-English switching, dialects and hotwords."
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2026-09-21"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-1-asr-flash-streaming
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/qwen-real-time-speech-recognition
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.1-ASR-Flash-Streaming

## Overview
Qwen-Audio-3.1-ASR-Flash-Streaming (Model Studio id `qwen-audio-3.1-asr-flash-streaming`) is an end-to-end real-time speech recognition model released on 2026-09-21 and listed on Model Studio's models page for real-time recognition; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes low-latency, high-accuracy streaming transcription for real-time conferencing, live subtitles and intelligent interaction, with multilingual and regional Chinese dialect recognition, seamless switching between Chinese and English, hotword and context enhancement, punctuation prediction, text normalisation, strong noise robustness and controllable dialect output as transcription (ASR) or translation (AST). It streams over Model Studio's real-time speech recognition WebSocket interface at up to 1,200 requests per minute. It is billed by tokens: $0.93 input and $0.70 output per million tokens in Singapore.

## Strengths
- Low-latency streaming with Chinese-English code switching.
- Noise robustness, per Model Studio.

## Limitations
- Token billing is harder to compare with per-second ASR prices.

## Good for
- Live meetings, subtitles and voice assistants.
