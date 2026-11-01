---
id: minimax/speech-2.8-turbo
name: MiniMax Speech 2.8 Turbo
owned_by: minimax
type: tts
description: MiniMax Speech 2.8 Turbo is the faster, cheaper tier of Speech 2.8, with the same sound tags, 40 languages and voice cloning as speech-2.8-hd at $60 per million characters.
aliases: [speech-2.8-turbo]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-01-23"
sources:
  - https://platform.minimax.io/docs/guides/models-intro
  - https://platform.minimax.io/docs/faq/models
  - https://platform.minimax.io/docs/release-notes/models
  - https://platform.minimax.io/docs/api-reference/speech-t2a-http
  - https://platform.minimax.io/docs/guides/speech-t2a-websocket
  - https://platform.minimax.io/docs/guides/speech-t2a-async
  - https://platform.minimax.io/docs/guides/speech-voice-clone
  - https://platform.minimax.io/docs/pricing/overview
  - https://platform.minimax.io/docs/guides/rate-limits
  - https://www.minimax.io/news/minimax-speech-28
  - https://openrouter.ai/minimax/speech-2.8-turbo
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice
retrieved: "2026-11-01"
---

# MiniMax Speech 2.8 Turbo

## Overview
Speech 2.8 was released on 2026-01-23; MiniMax's pricing page describes `speech-2.8-turbo` as having the same capabilities as `speech-2.8-hd`, optimised for speed and cost. The id is OpenRouter's, which serves it on `/api/v1/audio/speech` (listed 2026-07-16, 45 preset voices, $0.00006 per character). It runs on the synchronous HTTP endpoint (`POST /v1/t2a_v2`, under 10,000 characters, optional streaming), the WebSocket and bidirectional WebSocket endpoints, where text can be streamed in at any granularity, and the asynchronous long-text API (up to 1M characters). It speaks 40 languages with system, cloned and designed voices, and supports the 19 Speech 2.8 sound tags (`(laughs)`, `(chuckle)`, `(breath)` and others), pause markers, pronunciation overrides, subtitles with word timestamps and `quality` text normalisation for non-streaming requests. Audio comes back as MP3, PCM, FLAC, WAV, Opus or G.711 at 8-44.1 kHz. Pay-as-you-go price is $60 per million characters; audio packages also cover it.

## Strengths
- Artificial Analysis Speech Arena (read 2026-11-01): Elo 1153, 31st of 100, ahead of every Speech 2.6 and Speech-02 model.
- 40% cheaper than speech-2.8-hd.
- Bidirectional streaming suits LLM output that arrives token by token.
- MiniMax's tagline for it is "seamless speed meets natural flow".

## Limitations
- 21 Elo below speech-2.8-hd on the same arena.
- Seven emotion presets; `fluent` and `whisper` are Speech 2.6 only.
- The 2.8 launch post gives no latency figure; the under-250 ms claim is from Speech 2.6's.
- Closed model; 60 requests per minute by default.

## Good for
- Voice agents and phone bots (G.711 output) that need natural fillers.
- High-volume narration where HD's price is hard to justify.
