---
id: qwen/qwen-audio-3.1-tts-next
name: Qwen-Audio-3.1-TTS-Next
owned_by: qwen
type: tts
description: "Qwen-Audio-3.1-TTS-Next is Alibaba hosted unified audio generation model on Model Studio, producing speech, dialogue, podcasts, sound effects and ambient soundscapes in one pass from text, timestamps and reference audio."
architecture:
  input_modalities: [text, audio]
  output_modalities: [audio]
open_weights: false
license: proprietary
release_date: "2026-09-21"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-audio-3-1-tts-next
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/audio-generation
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Audio-3.1-TTS-Next

## Overview
Qwen-Audio-3.1-TTS-Next (Model Studio id `qwen-audio-3.1-tts-next`) is an AudioGen model that Model Studio released on 2026-09-21 in China (Beijing) and 2026-10-22 in Singapore, and lists under audio generation on its models page; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Going beyond speech-only TTS, it generates complete audio in a single pass from text, timestamps and reference audio, combining speech, sound effects and ambient sound for multilingual TTS, single-speaker speech, multi-speaker dialogue, podcasts, cinematic soundscapes and sound effects. It supports Chinese and English, takes up to three reference clips of up to 30 seconds and 10 MB each (WAV, MP3 or OGG Opus), and returns non-streaming WAV, MP3 or PCM of up to 240 seconds for podcasts or 120 seconds otherwise. It is billed by tokens: $0.93 input and $1.87 output per million tokens in Singapore.

## Strengths
- Speech and sound design in one request, with timing control.
- Consistent voice identity from reference clips, per Model Studio.

## Limitations
- Chinese and English only.
- Non-streaming, with output capped at two to four minutes.

## Good for
- Podcasts, short-form video and game audio with sound effects.
