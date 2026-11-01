---
id: qwen/qwen-audio-3.1-tts-flash
name: Qwen-Audio-3.1-TTS-Flash
owned_by: qwen
type: tts
description: "Qwen-Audio-3.1-TTS-Flash is Alibaba's current low-latency hosted text-to-speech model on Model Studio for voice assistants and customer service, with streaming synthesis, instruction and tag control, voice cloning and design, and the widest language list of Model Studio's TTS models."
aliases: [qwen-audio-3.1-tts-flash]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2026-10-12"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/tts-model
  - https://www.alibabacloud.com/help/en/model-studio/qwen-tts
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://www.qwencloud.com/models/qwen-audio-3.1-tts-flash
  - https://artificialanalysis.ai/text-to-speech/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.1-TTS-Flash

## Overview
Qwen-Audio-3.1-TTS-Flash (Model Studio id `qwen-audio-3.1-tts-flash`) is the speech synthesis model Model Studio now recommends for voice assistants, real-time conversation and customer service; no weights are published. OpenRouter does not list it; the id is the DashScope model id. Model Studio lists it from 2026-10-12. It supports streaming synthesis, a range of system voices, free-style instructions and fine-grained emotion and paralinguistic tags for tone, persona, speaking rate and volume, plus voice cloning (more robust to noisy, reverberant reference audio, per Qwen Cloud) and voice design. Cloned voices speak Mandarin and 20 other Chinese varieties, English, Japanese, Korean, Russian, French, German, Portuguese, Thai, Indonesian, Vietnamese, Spanish, Italian, Malaysian, Filipino and Arabic, and for this model Model Studio lists 51 more for cloned voices, from Bulgarian and Dutch to Swahili and Ukrainian. Unlike the rest of the Qwen-Audio-TTS family it is billed by tokens: $0.23 per million input tokens and $1.87 per million output tokens in Singapore.

## Strengths
- Widest language list of Model Studio's TTS models.
- Low-latency real-time synthesis with the same controls as the Plus model.

## Limitations
- Artificial Analysis lists no arena score for it.
- Closed weights; designed voices cover Mandarin and English only.
- Token billing makes costs harder to compare with per-character TTS prices.

## Good for
- Multilingual voice agents and call-centre bots.
- Real-time speech in less common languages.
