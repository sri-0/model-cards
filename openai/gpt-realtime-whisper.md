---
id: openai/gpt-realtime-whisper
name: GPT Realtime Whisper
owned_by: openai
type: llm
description: GPT Realtime Whisper is OpenAI's May 2026 streaming speech-to-text model for Realtime transcription sessions, priced by audio duration at $0.017 per minute and no longer the recommended starting model.
aliases: [gpt-realtime-whisper, azure/gpt-realtime-whisper]
context_length: 16000
max_output_tokens: 2000
architecture:
  input_modalities: [audio, text]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2026-05-07"
knowledge_cutoff: "2024-09"
sources:
  - https://developers.openai.com/api/docs/models/gpt-realtime-whisper
  - https://developers.openai.com/api/docs/guides/transcription
  - https://developers.openai.com/api/docs/guides/realtime-transcription
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://artificialanalysis.ai/speech-to-text/streaming
  - https://openrouter.ai/api/v1/models?output_modalities=transcription
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Realtime Whisper

## Overview
OpenAI released GPT-Realtime-Whisper on 2026-05-07 with GPT-Realtime-2 and GPT-Realtime-Translate (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; gpt-realtime-whisper is its only snapshot. OpenAI describes it as a streaming speech-to-text model for applications that need low-latency transcript deltas from live audio and want to tune latency against accuracy. It takes audio and text, returns text, and has a 16,000-token context window, 2,000 output tokens and a September 2024 knowledge cutoff. It runs only on Realtime transcription sessions (/v1/realtime/transcription_sessions) and is priced by audio duration at $0.017 per minute, the same as GPT Live Transcribe. OpenAI's transcription guide now recommends gpt-live-transcribe (released 2026-07-28) for new live integrations and says existing integrations can keep using gpt-realtime-whisper where supported. The model page shows no deprecation.

## Strengths
- Artificial Analysis streaming board (read 2026-11-01): AA-WER Streaming 4.5% (3.5% AA-AgentTalk, 2.8% VoxPopuli, 8.1% Earnings22), 0.78 s to the final transcript and 0.35 s to the first partial, slightly faster to final text than GPT Live Transcribe (0.86 s).
- Streaming transcript deltas as speech arrives.
- Rate limits are set in minutes of audio: 350 per minute at Build, up to 1,300 at Grow.

## Limitations
- Less accurate than GPT Live Transcribe on the same board (4.0%) at the same price; rank 26 of 47.
- Not the recommended model for new transcription integrations.
- Realtime sessions only: no file transcription endpoint.

## Good for
- Existing Realtime transcription integrations built on it in 2026.
- Live captions where final-transcript latency matters slightly more than accuracy.
