---
id: qwen/qwen3-asr-flash-filetrans
name: Qwen3-ASR-Flash-Filetrans
owned_by: qwen
type: llm
description: "Qwen3-ASR-Flash-Filetrans is the large-file asynchronous transcription version of Alibaba hosted Qwen3-ASR-Flash on Model Studio, for audio files of up to 12 hours with sentence or word timestamps."
aliases: [qwen3-asr-flash-filetrans-2025-11-17]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2025-11-17"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-asr-flash-filetrans
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/qwen-speech-recognition
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-ASR-Flash-Filetrans

## Overview
Qwen3-ASR-Flash-Filetrans (Model Studio id `qwen3-asr-flash-filetrans`, with snapshot `qwen3-asr-flash-filetrans-2025-11-17`) is the large-file transcription version of Qwen3-ASR-Flash (qwen/qwen3-asr-flash), released on 2025-11-17 in China (Beijing) and 2025-11-18 in Singapore; no weights are published under this id and OpenRouter does not list it, so the id is the DashScope model id. It shares Qwen3-ASR-Flash's LLM-based recognition with automatic language detection. Jobs are submitted asynchronously and polled for the result; a file can be up to 2 GB and 12 hours, or 2 hours with speaker diarisation. Timestamps are always on through the DashScope asynchronous call, at sentence level by default or word level with `enable_words` for Chinese, English, Japanese, Korean, German, French, Spanish, Italian, Portuguese and Russian. Results arrive as a downloadable JSON file whose URL lasts 24 hours. The price is $0.000035 per second of audio in Singapore and $0.000032 in China (Beijing).

## Strengths
- Long recordings in one job.
- Word-level timestamps in ten languages.

## Limitations
- No streaming results; the task must be polled.
- Model Studio now recommends Qwen-Audio-3.1-ASR-Flash-Filetrans.

## Good for
- Meeting, interview and call recordings.
