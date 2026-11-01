---
id: openai/gpt-4o-mini-tts
name: GPT-4o Mini TTS
owned_by: openai
type: tts
description: GPT-4o Mini TTS is OpenAI's deprecated text-to-speech model built on GPT-4o Mini, with prompt-controlled delivery and 13 built-in voices on the Speech API, shutting down on 2027-01-06.
aliases: [gpt-4o-mini-tts, gpt-4o-mini-tts-2025-12-15, gpt-4o-mini-tts-2025-03-20, azure/gpt-4o-mini-tts]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2025-03-20"
sources:
  - https://developers.openai.com/api/docs/models/gpt-4o-mini-tts
  - https://developers.openai.com/api/docs/guides/text-to-speech
  - https://developers.openai.com/api/reference/resources/audio/subresources/speech/methods/create
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/blog/updates-audio-models
  - https://artificialanalysis.ai/text-to-speech/leaderboard
  - https://openrouter.ai/api/v1/models?output_modalities=speech
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o Mini TTS

## Overview
GPT-4o Mini TTS was added to the Audio API on 2025-03-20 (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. OpenAI describes it as a text-to-speech model built on GPT-4o Mini, with at most 2,000 input tokens; the Speech API caps input at 4,096 characters. Snapshots are gpt-4o-mini-tts-2025-03-20 and gpt-4o-mini-tts-2025-12-15, the default since 2026-01-13. It runs on /v1/audio/speech at $0.60 per million text input tokens and $12 per million audio output tokens. Output is mp3 by default, or opus, aac, flac, wav or pcm (24 kHz, 16-bit), streamed as raw audio or server-sent events, at speeds from 0.25 to 4.0. Language support follows Whisper's list, though the voices are optimised for English. OpenAI deprecated it on 2026-10-01; it shuts down on 2027-01-06, and OpenAI points users to gpt-realtime-2.1-mini on the Realtime API, which is not a Speech API model.

## Strengths
- An instructions field steers accent, emotional range, intonation, impressions, speed, tone and whispering; tts-1 and tts-1-hd ignore it.
- 13 built-in voices, with marin and cedar recommended, plus custom voices for eligible customers.
- OpenAI reports roughly 35% lower WER on Common Voice and FLEURS for the 2025-12-15 snapshot than the previous generation.

## Limitations
- Deprecated; shuts down on 2027-01-06.
- Short inputs: 4,096 characters per request, so long narration must be split.
- Artificial Analysis's text-to-speech leaderboard (read 2026-11-01) does not list it.
- Build-tier limits of 2,000 RPM and 150,000 TPM.

## Good for
- Existing Speech API integrations that need styled delivery until January 2027.
- Narration and spoken notifications with a consistent voice.
- Low-latency playback using wav or pcm streaming.
