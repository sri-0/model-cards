---
id: qwen/qwen-audio-3.0-asr-flash-filetrans
name: Qwen-Audio-3.0-ASR-Flash-Filetrans
owned_by: qwen
type: llm
description: "Qwen-Audio-3.0-ASR-Flash-Filetrans is a hosted Model Studio non-real-time transcription model for full-length audio and video files, with context enhancement and domain hotwords."
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2026-07-30"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-0-asr-flash-filetrans
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/qwen-speech-recognition
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.0-ASR-Flash-Filetrans

## Overview
Qwen-Audio-3.0-ASR-Flash-Filetrans (Model Studio id `qwen-audio-3.0-asr-flash-filetrans`) is a high-performance transcription model for non-real-time processing of full-length audio and video files, released on 2026-07-30 alongside Qwen-Audio-3.0-ASR-Flash; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio says it integrates context enhancement and improves recognition of domain-specific hotwords, for short-video subtitling, customer-service quality inspection and financial dual-recording. The release note for the 3.0 ASR family adds the seven major Chinese dialect groups with 20+ accents, classical poetry tuning, better punctuation and number normalisation, and 30 languages. Jobs run asynchronously on files of up to 2 GB and 12 hours. The price is $0.000035 per second of audio in Singapore and $0.000032 in China (Beijing), with output free.

## Strengths
- Hotwords for domain vocabulary.
- Long files in one job.

## Limitations
- No streaming results.
- Superseded by Qwen-Audio-3.1-ASR-Flash-Filetrans.

## Good for
- Subtitling and customer-service call review.
