---
id: qwen/qwen-audio-3.1-asr-flash-message
name: Qwen-Audio-3.1-ASR-Flash-Message
owned_by: qwen
type: llm
description: "Qwen-Audio-3.1-ASR-Flash-Message is Alibaba hosted generative speech recognition model on Model Studio for voice messages and voice input, with incremental streaming, hotwords, context-aware recognition, optional polishing and dialect-to-Mandarin output."
capabilities: [structured_output]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2026-09-21"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-1-asr-flash-message
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.1-ASR-Flash-Message

## Overview
Qwen-Audio-3.1-ASR-Flash-Message (Model Studio id `qwen-audio-3.1-asr-flash-message`) is a generative speech recognition model released on 2026-09-21 and listed on Model Studio's models page for real-time recognition; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio optimises it for voice messages, voice input and enterprise use: it supports Chinese, English and other languages, with extra tuning for Indonesian, Japanese, Thai, Filipino, Vietnamese, Korean and Malay. It offers incremental streaming transcription, P0 and P1 hotwords, text normalisation, recognition informed by earlier transcripts and business context, optional native text polishing, and structured output. It is steadier with several speakers, background talk, far-field audio and noise, detects the language or takes a target language, and can keep Chinese dialects as spoken or convert them to standard Mandarin. It is billed by tokens: $0.93 input and $0.70 output per million tokens in Singapore, at 1,200 requests per minute.

## Strengths
- Context and hotwords for domain terms.
- Dialect-to-Mandarin conversion.

## Limitations
- Higher input price than the non-real-time Qwen-Audio-3.1-ASR-Flash.

## Good for
- Chat voice messages and dictation in Southeast Asian languages.
