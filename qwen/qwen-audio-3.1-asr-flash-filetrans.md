---
id: qwen/qwen-audio-3.1-asr-flash-filetrans
name: Qwen-Audio-3.1-ASR-Flash-Filetrans
owned_by: qwen
type: llm
description: "Qwen-Audio-3.1-ASR-Flash-Filetrans is Alibaba current hosted offline long-audio transcription model on Model Studio, with dialect recognition, hotwords, speaker separation and dialect ASR/AST output."
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2026-09-21"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-1-asr-flash-filetrans
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/asr-model
  - https://www.alibabacloud.com/help/en/model-studio/qwen-speech-recognition
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.1-ASR-Flash-Filetrans

## Overview
Qwen-Audio-3.1-ASR-Flash-Filetrans (Model Studio id `qwen-audio-3.1-asr-flash-filetrans`) is an end-to-end offline speech recognition model released on 2026-09-21 and listed on Model Studio's models page for file transcription; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio calls it the preferred choice for long audio: it handles multilingual speech and Chinese dialects from many regions with high-precision transcription, hotword and context enhancement, speaker separation, punctuation prediction and text normalisation, stays stable in noisy environments, and supports controllable dialect output as transcription (ASR) or translation (AST). Jobs run asynchronously on files of up to 2 GB and 12 hours, or 2 hours with speaker diarisation, with timestamps. It is billed by tokens: $0.15 input and $0.47 output per million tokens in Singapore.

## Strengths
- Long recordings with speaker separation.
- Robust in noisy audio, per Model Studio.

## Limitations
- No streaming results; the task must be polled.
- Token billing is harder to compare with per-second ASR prices.

## Good for
- Meetings, content production and call analysis.
