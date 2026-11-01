---
id: minimax/speech-2.8-hd
name: MiniMax Speech 2.8 HD
owned_by: minimax
type: tts
description: MiniMax Speech 2.8 HD is MiniMax's current highest-quality text-to-speech model, adding inline sound tags such as (laughs) and (breath) to 40-language synthesis with voice cloning, at $100 per million characters.
aliases: [speech-2.8-hd]
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
  - https://openrouter.ai/minimax/speech-2.8-hd
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice
retrieved: "2026-11-01"
---

# MiniMax Speech 2.8 HD

## Overview
Speech 2.8 was released on 2026-01-23 in HD and Turbo tiers; `speech-2.8-hd` is the quality tier. The id is OpenRouter's, which serves it on `/api/v1/audio/speech` (listed 2026-07-16, 45 preset voices, $0.0001 per character). MiniMax serves it through synchronous HTTP (`POST /v1/t2a_v2`, under 10,000 characters, optional streaming), WebSocket and bidirectional WebSocket endpoints, and an asynchronous API for up to 1M characters per request. It covers 40 languages with system, cloned (10 s to 5 min of source audio) and text-designed voices, and returns MP3, PCM, FLAC, WAV, Opus or G.711 audio at 8-44.1 kHz, mono or stereo. New in 2.8 are sound tags: 19 interjections such as `(laughs)`, `(sighs)` and `(breath)` written inline. Pause markers, pinyin, IPA and Jyutping pronunciation overrides, sentence or word timestamps, and LLM-assisted text normalisation (`quality` mode, non-streaming) are also available. Pay-as-you-go price is $100 per million characters, sync or async; cloning costs $1.5 and voice design $3 per voice, charged on first use. Audio packages also cover it.

## Strengths
- The highest-ranked MiniMax model on Artificial Analysis's Speech Arena (read 2026-11-01): Elo 1174, 27th of 100.
- Sound tags add laughs, breaths and hesitations without post-processing.
- MiniMax says cloning needs only a 10-second sample, output is free of background noise, and Mandarin-Japanese accent bleed is fixed.
- A US West endpoint (`api-uw.minimax.io`) cuts time to first audio.

## Limitations
- Seven emotion presets; `fluent` and `whisper` are Speech 2.6 only.
- Costs two-thirds more than speech-2.8-turbo ($60 per million), which AA scores 21 Elo lower.
- Closed model with no self-hosted option; 60 requests per minute by default.
- `quality` normalisation does not apply to streaming or WebSocket requests.

## Good for
- Narration, audiobooks and dubbing where breathing and laughter matter.
- Long-form synthesis through the asynchronous API.
