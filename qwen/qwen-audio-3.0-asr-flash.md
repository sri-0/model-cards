---
id: qwen/qwen-audio-3.0-asr-flash
name: Qwen-Audio-3.0-ASR-Flash
owned_by: qwen
type: llm
description: "Qwen-Audio-3.0-ASR-Flash is a hosted Model Studio short-audio speech recognition model covering the seven major Chinese dialect groups, 20+ regional accents and 30 languages, with classical poetry tuning."
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2026-07-30"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-0-asr-flash
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/qwen-speech-recognition
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.0-ASR-Flash

## Overview
Qwen-Audio-3.0-ASR-Flash (Model Studio id `qwen-audio-3.0-asr-flash`) is a non-real-time speech recognition model released on 2026-07-30; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes the June 2026 update of its ASR model as covering the seven traditional Chinese dialect groups (Mandarin, Wu, Xiang, Gan, Hakka, Min and Cantonese) and more than 20 regional Mandarin accents, tuned for the rhythm and classical expression of ancient Chinese poetry for heritage, education and audiobook work. Punctuation prediction and text normalisation convert numbers, dates and amounts to standard written forms. It supports 30 languages, among them English, Japanese, Korean, Vietnamese, Thai, Indonesian, Hindi, Arabic and major European languages, uses context, and transcribes audio of up to 5 minutes. The price is $0.000035 per second of audio in Singapore and $0.00003 in China (Beijing).

## Strengths
- Broad Chinese dialect coverage.
- Per-second pricing.

## Limitations
- 5 minutes per request.
- Superseded by Qwen-Audio-3.1-ASR-Flash.

## Good for
- Dialect-heavy Chinese clips and audiobooks.
