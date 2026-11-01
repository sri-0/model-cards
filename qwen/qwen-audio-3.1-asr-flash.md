---
id: qwen/qwen-audio-3.1-asr-flash
name: Qwen-Audio-3.1-ASR-Flash
owned_by: qwen
type: llm
description: "Qwen-Audio-3.1-ASR-Flash is Alibaba current hosted short-audio speech recognition model on Model Studio, with multilingual and Chinese dialect recognition, classical poetry tuning, dialect ASR/AST output, polishing and role-based multi-speaker transcription."
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2026-09-21"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-1-asr-flash
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/asr-model
  - https://www.alibabacloud.com/help/en/model-studio/qwen-speech-recognition
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.1-ASR-Flash

## Overview
Qwen-Audio-3.1-ASR-Flash (Model Studio id `qwen-audio-3.1-asr-flash`) is the non-real-time short-audio recognition model Model Studio lists on its models page, released on 2026-09-21; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio says it handles multilingual speech and Chinese dialects from many regions, is tuned for the rhythm and classical expression of ancient Chinese poetry, adds context enhancement, punctuation prediction and text normalisation, and supports controllable dialect output as transcription (ASR) or translation (AST), native transcription polishing and industrial multi-speaker, role-based transcription. Synchronous calls take audio of up to 5 minutes, with streaming or non-streaming results. Unlike Qwen3-ASR-Flash it is billed by tokens: $0.15 input and $0.47 output per million tokens in Singapore, at 600 requests per minute.

## Strengths
- Dialect and classical Chinese recognition.
- Speaker roles and text polishing built in.

## Limitations
- 5 minutes per request; long files need the Filetrans model.
- Token billing is harder to compare with per-second ASR prices.

## Good for
- Short multilingual and dialect clips, including cultural and educational audio.
