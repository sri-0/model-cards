---
id: meta/muse-voice-transcribe-1.0
name: Muse Voice Transcribe 1.0
owned_by: meta
type: llm
description: Muse Voice Transcribe 1.0 is Meta's proprietary streaming and file speech-to-text model with built-in endpointing, speaker diarisation and keyword biasing across 25 languages.
aliases: [muse-voice-transcribe-1.0]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-09-03"
sources:
  - https://openrouter.ai/meta/muse-voice-transcribe-1.0
  - https://openrouter.ai/api/v1/models
  - https://dev.meta.ai/models/muse-voice-transcribe
  - https://dev.meta.ai/docs/speech-to-text
  - https://dev.meta.ai/docs/api-reference/voice/transcribe
  - https://dev.meta.ai/docs/models
  - https://dev.meta.ai/docs/pricing-rate-limits
  - https://dev.meta.ai/resources/blog/meet-muse-voice-transcribe-streaming-speech-to-text
  - https://artificialanalysis.ai/speech-to-text/streaming
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Muse Voice Transcribe 1.0

## Overview
Muse Voice Transcribe 1.0 (`muse-voice-transcribe-1.0`) is Meta's speech-to-text model, launched on Meta Model API in the week of September 3, 2026 as Meta's first real-time audio perception model. It runs over a realtime WebSocket (`wss://api.meta.ai/v1/asr/realtime`, sessions up to 60 minutes, raw 16-bit mono PCM at 24 or 16 kHz) or a file endpoint (`POST /v1/asr/transcribe`, mono 16-bit PCM WAV at 16 or 24 kHz, up to 10 minutes); OpenRouter serves it on `/api/v1/audio/transcriptions`. Modes are push-to-talk (default), endpointing and diarisation. It returns punctuated text with turn-level timestamps and speaker labels, in 25 languages with code-switching, language hints and keyword biasing. Price: $0.18 per hour of audio ($3.00 per 1,000 minutes) on Meta Model API, billed in whole seconds, and $0.00005 per second on OpenRouter; failed and rate-limited requests are not billed.

## Strengths
- Artificial Analysis streaming leaderboard on 2026-11-01: an AA-WER streaming index of 3.06%, fifth of 47 entries, with about 0.16 s to the final transcript. Meta said it ranked first by word error rate at launch.
- Speaker attribution for 20+ speakers and end-of-speech detection inside the model, with no separate diarisation pass.
- Adaptive delay, trained with reinforcement learning, trades latency against accuracy per word.
- Zero data retention costs the same as Standard mode.

## Limitations
- No word-level timestamps, confidence scores, sound-event or emotion detection, and no speech synthesis.
- Files must be converted to WAV first; the realtime socket takes only raw PCM.
- Keywords bias recognition but do not guarantee spelling, and speaker labels are only valid within a session.
- Limits of 256 concurrent streams and 16,000 streams per hour per team; API-only.

## Good for
- Voice agents that need fast turn detection.
- Meeting and call transcription with speaker labels.
- Live captions and dictation in the 25 supported languages.
