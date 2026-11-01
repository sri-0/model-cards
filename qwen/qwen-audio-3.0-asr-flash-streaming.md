---
id: qwen/qwen-audio-3.0-asr-flash-streaming
name: Qwen-Audio-3.0-ASR-Flash-Streaming
owned_by: qwen
type: llm
description: "Qwen-Audio-3.0-ASR-Flash-Streaming is the real-time member of Model Studio Qwen-Audio-3.0 speech recognition family, covering the seven major Chinese dialect groups and 30 languages."
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2026-07-30"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/qwen-real-time-speech-recognition
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.0-ASR-Flash-Streaming

## Overview
Qwen-Audio-3.0-ASR-Flash-Streaming (Model Studio id `qwen-audio-3.0-asr-flash-streaming`) is the real-time model added on 2026-07-30 with the non-real-time Qwen-Audio-3.0-ASR-Flash and its Filetrans version; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio has no separate model page for it; its release note for the three models lists support for the seven major Chinese dialect groups (Mandarin, Wu, Xiang, Gan, Hakka, Min and Yue) and more than 20 regional accents, better recognition of classical Chinese poetry for education, culture and audiobooks, improved punctuation and normalisation of numbers, dates and money amounts, and 30 languages. It streams over Model Studio's real-time recognition interface. The price is $0.00009 per second of audio in Singapore and $0.000047 in China (Beijing), with output free.

## Strengths
- Real-time dialect recognition.

## Limitations
- No dedicated model page; details come from the family release note.
- Superseded by Qwen-Audio-3.1-ASR-Flash-Streaming.

## Good for
- Live captions for dialect-rich Chinese speech.
