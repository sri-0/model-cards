---
id: openai/gpt-live-transcribe
name: GPT Live Transcribe
owned_by: openai
type: llm
description: GPT Live Transcribe is OpenAI's recommended low-latency streaming speech-to-text model for live audio in Realtime transcription sessions, with tunable delay, keyword hints and multiple language hints at $0.017 per minute.
aliases: [gpt-live-transcribe, azure/gpt-live-transcribe]
architecture:
  input_modalities: [audio, text]
  output_modalities: [transcription]
open_weights: false
license: proprietary
release_date: "2026-07-28"
sources:
  - https://developers.openai.com/api/docs/models/gpt-live-transcribe
  - https://developers.openai.com/api/docs/guides/transcription
  - https://developers.openai.com/api/docs/guides/realtime-transcription
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://artificialanalysis.ai/speech-to-text/streaming
  - https://openrouter.ai/api/v1/models?output_modalities=transcription
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Live Transcribe

## Overview
OpenAI released GPT Live Transcribe on 2026-07-28 alongside GPT Transcribe (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; gpt-live-transcribe is its only snapshot. OpenAI's transcription guide recommends it for microphones, calls and other live streams, and names it with gpt-transcribe as the replacement for the transcription models that shut down on 2027-02-26. It runs only on Realtime transcription sessions (/v1/realtime/transcription_sessions) over WebRTC or WebSocket, takes 24 kHz PCM audio, and returns transcript deltas as speech arrives plus a final transcript when the application commits each turn. Sessions accept a prompt, keyword hints, a languages list and a delay setting from minimal to xhigh that trades latency for accuracy. OpenAI charges $0.017 per minute of audio.

## Strengths
- Artificial Analysis streaming board (read 2026-11-01): AA-WER Streaming 4.0% (2.8% AA-AgentTalk, 2.6% VoxPopuli, 7.7% Earnings22), 0.86 s to the final transcript and 0.37 s to the first partial, ahead of GPT Realtime Whisper's 4.5%.
- Delay levels let one model serve live captions and higher-accuracy streams.
- Keyword and multiple-language hints that can change mid-session.

## Limitations
- No word timestamps, speaker labels, confidence scores or detected-language output.
- Server VAD and semantic VAD are not supported: the client must detect speech ends and commit turns.
- Rank 21 of 47 on the streaming board; MAI-Transcribe-2-Streaming leads at 2.5%.
- Nearly four times gpt-transcribe's per-minute price.
- Build-tier limits of 2,000 RPM and 210,000 TPM.

## Good for
- Live captions for calls, meetings and broadcasts.
- Voice front ends that need text while the speaker is still talking.
- Migrating realtime transcription off gpt-4o-transcribe before February 2027.
