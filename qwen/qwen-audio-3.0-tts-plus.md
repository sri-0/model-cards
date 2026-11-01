---
id: qwen/qwen-audio-3.0-tts-plus
name: Qwen-Audio-3.0-TTS Plus
owned_by: qwen
type: tts
description: "Qwen-Audio-3.0-TTS-Plus is Alibaba's hosted quality-first text-to-speech model on Model Studio, with instruction and tag control of emotion, tone and pace, voice cloning and design, and wide Chinese dialect coverage."
aliases: [qwen-audio-3.0-tts-plus, qwen/qwen-audio-3.0-tts-plus-20260723]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-07-14"
sources:
  - https://openrouter.ai/qwen/qwen-audio-3.0-tts-plus
  - https://openrouter.ai/api/v1/models/qwen/qwen-audio-3.0-tts-plus/endpoints
  - https://openrouter.ai/api/v1/models
  - https://www.alibabacloud.com/help/en/model-studio/tts-model
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://artificialanalysis.ai/text-to-speech/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.0-TTS Plus

## Overview
Qwen-Audio-3.0-TTS-Plus (Model Studio id `qwen-audio-3.0-tts-plus`) is Alibaba's hosted speech synthesis model for quality-first work; no weights are published. OpenRouter lists it as `qwen/qwen-audio-3.0-tts-plus` (added 2026-07-23), served by Alibaba through the DashScope Speech Synthesizer API with two voices exposed there. Model Studio released it on 2026-07-14 for real-time and non-real-time synthesis. Against the previous version, Model Studio says it covers more low-resource languages and Chinese dialects, follows free-style instructions and fine-grained tags for emotion, tone, character, speaking rate, volume and style, and holds up better in noisy and reverberant conditions. The Qwen-Audio-TTS family offers system voices, voice cloning and voice design; cloned voices speak Chinese (Mandarin, Cantonese, Shanghainese, Sichuanese and 17 other varieties), English, Japanese, Korean, Russian, French, German, Portuguese, Thai, Indonesian, Vietnamese, Spanish, Italian, Malaysian, Filipino and Arabic. The price is $20 per million characters on OpenRouter and $0.20 per 10,000 characters on Model Studio (Singapore), where each Chinese character counts as two.

## Strengths
- Artificial Analysis text-to-speech arena: Elo 1269, behind Qwen-Audio-3.1-TTS-Plus (1305) and the leader Eleven v4 Turbo (1336); AA groups it in its CosyVoice TTS family.
- Audiobooks, dubbing and brand voices, per Model Studio.

## Limitations
- Superseded: Model Studio now recommends qwen-audio-3.1-tts-plus.
- Designed voices are limited to Mandarin and English.
- Closed weights.

## Good for
- Narration and dubbing that needs Chinese dialects.
- Brand voices built by cloning or voice design.
