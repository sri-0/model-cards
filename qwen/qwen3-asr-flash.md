---
id: qwen/qwen3-asr-flash
name: Qwen3-ASR-Flash
owned_by: qwen
type: llm
description: "Qwen3-ASR-Flash is Alibaba hosted LLM-based multilingual speech recognition model on Model Studio, with automatic language detection and Chinese dialect support for short audio, billed per second."
aliases: [qwen3-asr-flash-2025-09-08, qwen3-asr-flash-2026-02-10, qwen3-asr-flash-us, qwen3-asr-flash-2025-09-08-us]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2025-09-08"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-asr-flash
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://www.alibabacloud.com/help/en/model-studio/qwen-speech-recognition
  - https://artificialanalysis.ai/speech-to-text/non-streaming
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-ASR-Flash

## Overview
Qwen3-ASR-Flash (Model Studio id `qwen3-asr-flash`) is a hosted speech recognition model released on 2025-09-08 in China (Beijing) and 2025-09-16 in Singapore; it has `-us` ids for the US (Virginia) region and a `qwen3-asr-flash-2026-02-10` snapshot, and the archived pricing page documents the stable id as equivalent to `qwen3-asr-flash-2025-09-08`. No weights are published under this id and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes an LLM-based model trained on tens of millions of hours of audio that detects the language and transcribes accurately in noisy conditions; the archived models page lists Chinese (Mandarin, Sichuanese, Minnan, Wu and Cantonese) and 25 other languages. Synchronous calls take up to 5 minutes or 10 MB of audio, with streaming results. The price is $0.000035 per second of audio in Singapore and US (Virginia) and $0.000032 in China (Beijing).

## Strengths
- Artificial Analysis speech-to-text leaderboard: AA-WER 4.1% for Qwen3 ASR Flash, which AA lists as a 1.7B open-weight model (see qwen/qwen3-asr-1.7b).
- Automatic language detection.

## Limitations
- 5 minutes or 10 MB per request; longer files need qwen3-asr-flash-filetrans.
- Model Studio now recommends the Qwen-Audio-3.1-ASR models.

## Good for
- Short multilingual clips, voice notes and commands.
