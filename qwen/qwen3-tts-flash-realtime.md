---
id: qwen/qwen3-tts-flash-realtime
name: Qwen3-TTS-Flash-Realtime
owned_by: qwen
type: tts
description: "Qwen3-TTS-Flash-Realtime is Alibaba's hosted real-time Qwen3 text-to-speech model on Model Studio, with streaming text input and audio output, 17 expressive system voices, ten languages and Chinese dialects."
aliases: [qwen3-tts-flash-realtime-2025-11-27, qwen3-tts-flash-realtime-2025-09-18]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2025-09-16"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/tts-model
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-Flash-Realtime

## Overview
Qwen3-TTS-Flash-Realtime (Model Studio id `qwen3-tts-flash-realtime`) is the real-time member of Model Studio's Qwen3-TTS family; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio lists the first snapshot, `qwen3-tts-flash-realtime-2025-09-18`, from 2025-09-16 and the `2025-11-27` snapshot, to which the stable id is documented as equivalent, from 2025-11-27. Model Studio calls it Tongyi's real-time speech synthesis foundation model with 17 expressive voices, low latency, consistent voices across languages and tone that adapts to the text. Qwen real-time synthesis accepts streaming text and returns streaming audio, adjusting speaking rate to content and punctuation. It uses system voices only, with no cloned or designed voices. Voices speak Chinese (Mandarin plus Beijing, Shanghai, Sichuan, Nanjing, Shaanxi, Minnan, Tianjin and Cantonese varieties), English, Spanish, Russian, Italian, French, Korean, Japanese, German and Portuguese. It is still on Model Studio's pricing page at $0.13 per 10,000 characters in Singapore and $0.143353 in China (Beijing), with each Chinese character counted as two and output free. No source ties it to the non-real-time qwen3-tts-flash (qwen/qwen3-tts-flash), so it has its own card.

## Strengths
- Streaming text in and audio out for live voice applications.
- Dialect voices for several Chinese regions.

## Limitations
- System voices only.
- Model Studio now recommends Qwen-Audio-3.1-TTS-Flash for real-time use.
- Artificial Analysis publishes no score under this id.

## Good for
- Voice assistants that speak LLM output as it streams.
- Existing integrations built on qwen3-tts-flash-realtime.
