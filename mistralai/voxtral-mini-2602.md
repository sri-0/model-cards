---
id: mistralai/voxtral-mini-2602
name: Voxtral Mini Transcribe 2
owned_by: mistralai
type: llm
description: Voxtral Mini Transcribe 2 is Mistral AI's API-only batch speech-to-text model (version 26.02) with diarization, word timestamps and context biasing for recordings up to three hours.
aliases: [voxtral-mini-latest, mistral/voxtral-mini-2602, mistral/voxtral-mini-latest]
architecture:
  input_modalities: [audio]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2026-02-04"
sources:
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/voxtral-mini-transcribe-26-02
  - https://docs.mistral.ai/studio/audio/overview
  - https://docs.mistral.ai/studio/audio/speech_to_text/offline_transcription
  - https://mistral.ai/news/voxtral-transcribe-2
  - https://arxiv.org/abs/2602.11298
  - https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-10-16"
---

# Voxtral Mini Transcribe 2

## Overview
Voxtral Mini Transcribe 2 was announced on 2026-02-04 with the Voxtral Transcribe 2 release. OpenRouter does not list it and Mistral publishes no weights, so the id is Mistral's API id, voxtral-mini-2602, under the vendor prefix (alias voxtral-mini-latest). Mistral's models page lists it as Premier (API only) at version 26.02. It runs on the batch transcription endpoint (/v1/audio/transcriptions) at $0.003 per minute, accepts recordings up to three hours per request, and returns word-level timestamps, speaker diarization and context biasing of up to 100 custom terms. It covers the same 13 languages as Voxtral Mini 4B Realtime 2602. It replaces Voxtral Mini Transcribe (voxtral-mini-2507), deprecated on 2026-02-27 and retired on 2026-05-31.

## Strengths
- Mistral's Voxtral Realtime report gives it 5.90% average WER on FLEURS and 8.07% on Mozilla Common Voice, against 8.23% and 14.25% for Whisper and 7.95% and 12.85% for GPT-4o mini Transcribe; the announcement quotes about 4% on FLEURS.
- English: 7.27% short-form and 7.11% long-form average WER in the same report.
- Mistral says it beats GPT-4o mini Transcribe, Gemini 2.5 Flash, Assembly Universal and Deepgram Nova, and runs three times faster than ElevenLabs Scribe v2 at a fifth of the cost.

## Limitations
- No weights: Mistral's API, on-premise or private cloud deployments only.
- Timestamps cannot be combined with the language parameter; context biasing is tuned for English and experimental elsewhere.
- Overlapping speech is usually attributed to one speaker.
- No published context length, parameter count or Artificial Analysis results.

## Good for
- Batch transcription of meetings, calls and podcasts with speaker labels.
- Multilingual archives where per-minute pricing matters.
- Replacing the retired voxtral-mini-2507 transcription endpoint.
