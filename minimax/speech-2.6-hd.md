---
id: minimax/speech-2.6-hd
name: MiniMax Speech 2.6 HD
owned_by: minimax
type: tts
description: MiniMax Speech 2.6 HD is MiniMax's October 2025 high-quality text-to-speech model, now legacy, with 40 languages, direct reading of URLs, numbers and dates, Fluent LoRA cloning and the only fluent and whisper emotion presets.
aliases: [speech-2.6-hd]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2025-10-29"
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
  - https://www.minimax.io/news/minimax-speech-26
  - https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# MiniMax Speech 2.6 HD

## Overview
Speech 2.6 was released on 2025-10-29 in HD and Turbo tiers; `speech-2.6-hd` is the quality tier. OpenRouter does not list it; the id is MiniMax's API id under the `minimax/` prefix, as LiteLLM also uses. MiniMax now files it under legacy models behind Speech 2.8 but still serves it on the synchronous HTTP (`POST /v1/t2a_v2`), WebSocket, bidirectional WebSocket and asynchronous endpoints. MiniMax's launch post claims end-to-end latency under 250 ms, direct reading of URLs, email addresses, phone numbers, dates and money without pre-processing, and Fluent LoRA, which keeps a cloned voice's timbre while producing fluent speech from accented or disfluent recordings. It covers 40 languages with system, cloned and designed voices, pause markers, pronunciation overrides, subtitles and `quality` text normalisation for non-streaming requests. Output is MP3, PCM, FLAC, WAV, Opus or G.711 at 8-44.1 kHz. Pay-as-you-go price is $100 per million characters; audio packages also cover it.

## Strengths
- The only MiniMax models with `fluent` and `whisper` emotion presets, alongside the seven shared ones.
- Fluent LoRA for cloning from imperfect source audio.
- Artificial Analysis Speech Arena (read 2026-11-01): Elo 1127, 36th of 100.

## Limitations
- No sound tags; those are Speech 2.8 only.
- 47 Elo below speech-2.8-hd at the same $100 per million characters.
- Legacy status; no retirement date has been published.
- Closed model; 60 requests per minute by default.

## Good for
- Existing integrations that rely on the `whisper` or `fluent` presets.
- Cloning voices from non-native or disfluent recordings.
