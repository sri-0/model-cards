---
id: qwen/qwen3-asr-flash-realtime
name: Qwen3-ASR-Flash-Realtime
owned_by: qwen
type: llm
description: "Qwen3-ASR-Flash-Realtime is the real-time streaming version of Alibaba hosted Qwen3-ASR-Flash speech recognition on Model Studio, with automatic language detection across 11 languages."
aliases: [qwen3-asr-flash-realtime-2025-10-27, qwen3-asr-flash-realtime-2026-02-10]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2025-10-27"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-asr-flash-realtime
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/qwen-real-time-speech-recognition
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-ASR-Flash-Realtime

## Overview
Qwen3-ASR-Flash-Realtime (Model Studio id `qwen3-asr-flash-realtime`, with snapshots `qwen3-asr-flash-realtime-2025-10-27` and `qwen3-asr-flash-realtime-2026-02-10`) is the real-time version of Qwen3-ASR-Flash (qwen/qwen3-asr-flash), released on 2025-10-27 in China (Beijing) and 2025-10-29 in Singapore; no weights are published under this id and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes an LLM-based recognition model trained on massive text, multimodal and audio data that detects the language and transcribes 11 languages accurately in complex audio. It streams results over Model Studio's real-time speech recognition WebSocket interface at up to 1,200 requests per minute. The price is $0.00009 per second of audio in Singapore and $0.000047 in China (Beijing), about two and a half times the non-real-time rate in Singapore.

## Strengths
- Live captions and voice input with low latency.
- Automatic language detection.

## Limitations
- 11 languages, fewer than the file-based models list.
- Model Studio now recommends Qwen-Audio-3.1-ASR-Flash-Streaming.

## Good for
- Live subtitles and voice interfaces.
