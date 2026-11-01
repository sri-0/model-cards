---
id: minimax/speech-2.6-turbo
name: MiniMax Speech 2.6 Turbo
owned_by: minimax
type: tts
description: MiniMax Speech 2.6 Turbo is the low-latency, lower-cost tier of MiniMax's legacy Speech 2.6 text-to-speech line, aimed at voice agents, at $60 per million characters.
aliases: [speech-2.6-turbo]
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

# MiniMax Speech 2.6 Turbo

## Overview
Speech 2.6 was released on 2025-10-29; MiniMax describes `speech-2.6-turbo` as faster, more affordable and ideal for agents, and its model list tags it "ultimate value, low latency". OpenRouter does not list it; the id is MiniMax's API id under the `minimax/` prefix, as LiteLLM also uses. It is now a legacy model behind Speech 2.8 but is still served on the synchronous HTTP (`POST /v1/t2a_v2`), WebSocket, bidirectional WebSocket and asynchronous endpoints. The Speech 2.6 launch post claims end-to-end latency under 250 ms, direct reading of URLs, email addresses, phone numbers, dates and money, and Fluent LoRA for cloning from accented or disfluent recordings. It covers 40 languages, nine emotion presets including `fluent` and `whisper`, pause markers, pronunciation overrides, subtitles and `quality` text normalisation for non-streaming requests. Output is MP3, PCM, FLAC, WAV, Opus or G.711 at 8-44.1 kHz. Pay-as-you-go price is $60 per million characters; audio packages also cover it.

## Strengths
- Artificial Analysis Speech Arena (read 2026-11-01): Elo 1122, 37th of 100, five points below speech-2.6-hd.
- 40% cheaper than speech-2.6-hd.
- Reads structured entities from LLM output without a normalisation step, per MiniMax.

## Limitations
- No sound tags; those are Speech 2.8 only.
- 31 Elo below speech-2.8-turbo at the same $60 per million characters.
- Legacy status; no retirement date has been published.
- Closed model; 60 requests per minute by default.

## Good for
- Existing real-time voice agents built on Speech 2.6.
- Workloads that need the `whisper` preset at the lower price.
