---
id: minimax/speech-02-hd
name: MiniMax Speech-02 HD
owned_by: minimax
type: tts
description: MiniMax Speech-02 HD is MiniMax's April 2025 autoregressive text-to-speech model with zero-shot voice cloning from a learnable speaker encoder, now legacy, covering 24 languages at $100 per million characters.
aliases: [speech-02-hd]
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

# MiniMax Speech-02 HD

## Overview
The Speech-02 series (`speech-02-hd`, `speech-02-turbo`) was released on 2025-04-02. OpenRouter does not list it; the id is MiniMax's API id under the `minimax/` prefix, as LiteLLM also uses. MiniMax's launch post describes an autoregressive Transformer co-trained with a learnable speaker encoder, which extracts timbre from reference audio for zero-shot cloning, and says Speech-02-HD reached first place on both the Artificial Analysis Speech Arena and the Hugging Face TTS Arena at the time. The launch post claimed 32 languages; MiniMax's models page now gives 24, and the API notes that the Speech-01 and Speech-02 series lack Persian, Filipino and Tamil. MiniMax files it under legacy models but still serves it on the synchronous HTTP (`POST /v1/t2a_v2`), WebSocket, bidirectional WebSocket and asynchronous endpoints, with seven emotion presets, pause markers, pronunciation overrides and subtitles. Output is MP3, PCM, FLAC, WAV, Opus or G.711 at 8-44.1 kHz. Pay-as-you-go price is $100 per million characters; audio packages also cover it.

## Strengths
- Strong cloning similarity, MiniMax's headline claim for the series.
- Artificial Analysis Speech Arena (read 2026-11-01): Elo 1108, 41st of 100, still ahead of Speech-02-Turbo.
- Served on the same endpoints and request format as MiniMax's newer speech models.

## Limitations
- Fewer languages than Speech 2.6 and 2.8 (24 against 40).
- No sound tags, no `fluent` or `whisper` presets, and `quality` text normalisation does not apply.
- 66 Elo below speech-2.8-hd at the same price; its first-place ranking is long gone.
- Legacy status; no retirement date has been published.

## Good for
- Existing integrations tuned to Speech-02 voices.
- Clone-heavy workloads in the 24 supported languages.
