---
id: mistralai/voxtral-mini-transcribe-realtime-3-0
name: Voxtral Mini Transcribe Realtime 3
owned_by: mistralai
type: llm
description: Voxtral Mini Transcribe Realtime 3 is Mistral AI's API-only streaming speech-to-text model of October 2026 for voice agents, with a configurable 80 ms to 2.4 s delay, end-of-turn detection, diarization and context biasing.
aliases: [voxtral-mini-transcribe-realtime-3, voxtral-mini-transcribe-realtime-latest, mistral/voxtral-mini-transcribe-realtime-3-0, mistral/voxtral-mini-transcribe-realtime-3]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2026-10-20"
sources:
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/voxtral-mini-transcribe-realtime-3-0
  - https://docs.mistral.ai/studio/audio/overview
  - https://docs.mistral.ai/studio/audio/speech-to-text/overview
  - https://docs.mistral.ai/studio/audio/specs-and-limits/limits
  - https://docs.mistral.ai/studio/audio/specs-and-limits/languages
  - https://docs.mistral.ai/studio/audio/migrate-from-voxtral-2
  - https://docs.mistral.ai/studio/audio/voice-agents/overview
  - https://docs.mistral.ai/inference/pricing
  - https://docs.mistral.ai/resources/changelogs
  - https://mistral.ai/news/voxtral-3
  - https://huggingface.co/mistralai
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Voxtral Mini Transcribe Realtime 3

## Overview
Voxtral Mini Transcribe Realtime 3 (version 3.0, API id voxtral-mini-transcribe-realtime-3-0, aliases voxtral-mini-transcribe-realtime-3 and voxtral-mini-transcribe-realtime-latest) was released on 2026-10-20 with the Voxtral 3 family and is in Public Preview. OpenRouter does not list it and there are no public weights, so the id is Mistral's API id under the vendor prefix. It streams audio over a WebSocket and returns text as people speak, at $0.008 per minute. The streaming delay is set per session to any value from 80 to 1,200 ms, or 2,400 ms. It adds end-of-turn detection from acoustic and semantic cues, realtime diarization with up to eight speaker reference clips, and context biasing; the docs list 45 languages and dialects. It is the listening stage of Mistral's Voice Agents SDK, billed at $0.04 per minute with Mistral Small 4 and $0.08 with larger models. It replaces voxtral-mini-transcribe-realtime-2602, deprecated on 2026-10-31 and retiring on 2027-04-30.

## Strengths
- On Mistral's 35-language FLEURS chart it scores 5.7% WER at a 2,400 ms delay, 6.0% at 960 ms, 6.4% at 480 ms and 7.4% at 240 ms, against 5.8% for Microsoft AI Transcribe 2 Streaming, 8.4% for GPT Live Transcribe and 8.7% for Scribe v2 Realtime. Gemini 3.5 Realtime Transcribe scored 4.2%.
- One session covers transcription, turn detection, diarization and biasing.
- Mistral says its voice agent pipeline completes a turn in under a second.

## Limitations
- Diarization and turn detection cannot share a session; setting both returns an error.
- Realtime segments carry speaker labels but no start or end times.
- Settings lock once audio starts; a later session.update returns an error.
- No public weights, published context length or parameter count; Public Preview only.

## Good for
- Voice agents and phone bots that need end-of-turn detection.
- Live captions with a tunable latency and accuracy trade-off.
- Migrating voxtral-mini-transcribe-realtime-2602 sessions.
