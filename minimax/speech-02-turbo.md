---
id: minimax/speech-02-turbo
name: MiniMax Speech-02 Turbo
owned_by: minimax
type: tts
description: MiniMax Speech-02 Turbo is the low-latency, lower-cost tier of MiniMax's legacy Speech-02 text-to-speech series, with zero-shot voice cloning across 24 languages at $60 per million characters.
aliases: [speech-02-turbo]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2025-04-02"
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
  - https://www.minimax.io/news/minimax-speech-02
  - https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# MiniMax Speech-02 Turbo

## Overview
`speech-02-turbo` was released on 2025-04-02 with `speech-02-hd`. OpenRouter does not list it; the id is MiniMax's API id under the `minimax/` prefix, as LiteLLM also uses. MiniMax's model list describes it as having superior rhythm and stability with low latency, and its speech guides add enhanced multilingual capability. The series uses an autoregressive Transformer with a learnable speaker encoder for zero-shot voice cloning, per MiniMax's launch post. It covers 24 languages (the API notes that the Speech-01 and Speech-02 series lack Persian, Filipino and Tamil), seven emotion presets, pause markers, pronunciation overrides and subtitles. MiniMax files it under legacy models but still serves it on the synchronous HTTP (`POST /v1/t2a_v2`, under 10,000 characters), WebSocket, bidirectional WebSocket and asynchronous (up to 1M characters) endpoints. Output is MP3, PCM, FLAC, WAV, Opus or G.711 at 8-44.1 kHz. Pay-as-you-go price is $60 per million characters; audio packages also cover it.

## Strengths
- 40% cheaper than speech-02-hd.
- Same endpoints, request format and cloning workflow as MiniMax's newer speech models.
- Artificial Analysis Speech Arena (read 2026-11-01): Elo 1091, 47th of 100.

## Limitations
- The lowest arena score of the six speech models in MiniMax's model list, 17 Elo below speech-02-hd.
- 24 languages against 40 for Speech 2.6 and 2.8.
- No sound tags, no `fluent` or `whisper` presets, no `quality` text normalisation.
- Legacy status; speech-2.8-turbo costs the same and scores 62 Elo higher.

## Good for
- Existing low-cost integrations tuned to Speech-02 voices.
- Simple read-aloud tasks in the 24 supported languages.
