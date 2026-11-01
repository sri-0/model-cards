---
id: qwen/qwen-audio-3.1-tts-plus
name: Qwen-Audio-3.1-TTS-Plus
owned_by: qwen
type: tts
description: "Qwen-Audio-3.1-TTS-Plus is Alibaba's current quality-first hosted text-to-speech model on Model Studio, with instruction and tag control of emotion, tone, persona, pace and volume, voice cloning and design, and wide Chinese dialect coverage."
aliases: [qwen-audio-3.1-tts-plus]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2026-10-21"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/tts-model
  - https://www.alibabacloud.com/help/en/model-studio/qwen-tts
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://www.qwencloud.com/models/qwen-audio-3.1-tts-plus
  - https://artificialanalysis.ai/text-to-speech/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.1-TTS-Plus

## Overview
Qwen-Audio-3.1-TTS-Plus (Model Studio id `qwen-audio-3.1-tts-plus`) is the speech synthesis model Model Studio now recommends for audiobooks, dubbing, brand voices and content production; no weights are published. OpenRouter does not list it; the id is the DashScope model id. Model Studio lists it from 2026-10-21 in Singapore and Beijing; Artificial Analysis dates it 2026-09-24. Model Studio and Qwen Cloud describe it as supporting multiple minority languages and Chinese dialects with authentic dialect pronunciation, streaming synthesis, free-style instructions and fine-grained tags for emotion, tone, persona, speaking rate and volume, and voice cloning that is more robust to noise and reverberation in the reference audio. It offers system voices, cloned voices and designed voices; cloned voices speak Mandarin and 20 other Chinese varieties plus English, Japanese, Korean, Russian, French, German, Portuguese, Thai, Indonesian, Vietnamese, Spanish, Italian, Malaysian, Filipino and Arabic, while designed voices cover Mandarin and English. The Singapore price is $0.30 per 10,000 characters, with each Chinese character counted as two.

## Strengths
- Artificial Analysis text-to-speech arena: Elo 1305, third behind Eleven v4 Turbo (1336) and Eleven v4 (1334), and the highest Alibaba entry.
- Fine control of delivery through instructions, tags and SSML.

## Limitations
- Closed weights; Model Studio regions only.
- 50% dearer per character than Qwen-Audio-3.0-TTS-Plus.
- Designed voices are limited to Mandarin and English.

## Good for
- Audiobooks, film and video dubbing and character performance.
- Brand voices in Chinese dialects or other supported languages.
