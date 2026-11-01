---
id: openai/tts-1-hd
name: TTS-1 HD
owned_by: openai
type: tts
description: TTS-1 HD is OpenAI's deprecated quality-optimised text-to-speech model from November 2023, with nine voices at $30 per million characters on the Speech API, shutting down on 2027-01-06.
aliases: [tts-1-hd, tts-1-hd-1106, azure/tts-1-hd]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2023-11-06"
sources:
  - https://developers.openai.com/api/docs/models/tts-1-hd
  - https://developers.openai.com/api/docs/guides/text-to-speech
  - https://developers.openai.com/api/reference/resources/audio/subresources/speech/methods/create
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://artificialanalysis.ai/text-to-speech/leaderboard
  - https://openrouter.ai/api/v1/models?output_modalities=speech
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# TTS-1 HD

## Overview
TTS-1 HD arrived with OpenAI's text-to-speech API on 2023-11-06 (OpenAI changelog; Artificial Analysis gives the same date). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; tts-1-hd is the only snapshot. OpenAI describes it as optimised for high-quality text-to-speech, at higher latency than tts-1. It runs on /v1/audio/speech at $30 per million characters, accepts up to 4,096 characters per request, and offers nine voices: alloy, ash, coral, echo, fable, onyx, nova, sage and shimmer. Output is mp3 by default, or opus, aac, flac, wav or pcm, with speed from 0.25 to 4.0 and chunked audio streaming. OpenAI deprecated it on 2026-10-01; it shuts down on 2027-01-06, and OpenAI points users to gpt-realtime-2.1-mini on the Realtime API.

## Strengths
- Artificial Analysis Speech Arena (provider voices, read 2026-11-01): Elo 1106 (95% interval 1095 to 1117) over 3,949 samples, rank 42, the highest-ranked OpenAI model there.
- Higher quality than tts-1, per OpenAI.
- 2,500 RPM at Build, rising to 10,000 RPM at Grow.

## Limitations
- Deprecated; shuts down on 2027-01-06.
- Twice the price of tts-1.
- No instructions field for tone or style, and no server-sent-event streaming (both are gpt-4o-mini-tts only).
- Nine voices against 13 for gpt-4o-mini-tts.
- No free-tier rate limit is listed.
- Voices are optimised for English.

## Good for
- Narration and recorded prompts where quality matters more than latency.
- Existing integrations until January 2027.
