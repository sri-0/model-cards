---
id: qwen/qwen-audio-3.0-tts-flash
name: Qwen-Audio-3.0-TTS Flash
owned_by: qwen
type: tts
description: "Qwen-Audio-3.0-TTS-Flash is Alibaba's hosted low-latency text-to-speech model on Model Studio, with first audio within 200 ms, instruction and tag control of emotion and pace, voice cloning and design."
aliases: [qwen-audio-3.0-tts-flash, qwen/qwen-audio-3.0-tts-flash-20260723]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-07-14"
sources:
  - https://openrouter.ai/qwen/qwen-audio-3.0-tts-flash
  - https://openrouter.ai/api/v1/models/qwen/qwen-audio-3.0-tts-flash/endpoints
  - https://openrouter.ai/api/v1/models
  - https://www.alibabacloud.com/help/en/model-studio/tts-model
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://artificialanalysis.ai/text-to-speech/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.0-TTS Flash

## Overview
Qwen-Audio-3.0-TTS-Flash (Model Studio id `qwen-audio-3.0-tts-flash`) is Alibaba's hosted speech synthesis model for real-time use; no weights are published. OpenRouter lists it as `qwen/qwen-audio-3.0-tts-flash` (added 2026-07-23), served by Alibaba through the DashScope Speech Synthesizer API with two voices exposed there. Model Studio released it on 2026-07-14 and says it keeps first-packet latency within 200 ms. Against the previous version it covers more low-resource languages and Chinese dialects, follows free-style instructions and fine-grained tags for emotion, tone, character, speaking rate, volume and style, and is more robust in noisy and reverberant conditions. The Qwen-Audio-TTS family offers system voices, voice cloning and voice design. Cloned voices speak Mandarin and 20 other Chinese varieties, English, Japanese, Korean, Russian, French, German, Portuguese, Thai, Indonesian, Vietnamese, Spanish, Italian, Malaysian, Filipino and Arabic. The price is $15 per million characters on OpenRouter and $0.15 per 10,000 characters on Model Studio (Singapore), where each Chinese character counts as two.

## Strengths
- Low first-audio latency for interactive use.
- A quarter cheaper than Qwen-Audio-3.0-TTS-Plus.

## Limitations
- Artificial Analysis lists no arena score for it.
- Superseded: Model Studio now recommends qwen-audio-3.1-tts-flash for real-time use.
- Designed voices are limited to Mandarin and English.

## Good for
- Voice assistants, real-time dialogue and customer service.
- Interactive voice apps that need Chinese dialects.
