---
id: openai/gpt-realtime-translate
name: GPT Realtime Translate
owned_by: openai
type: llm
description: GPT Realtime Translate is OpenAI's streaming speech-to-speech translation model, returning translated audio and transcript deltas on a dedicated Realtime translation endpoint at $0.034 per minute.
aliases: [gpt-realtime-translate, azure/gpt-realtime-translate]
context_length: 16000
max_output_tokens: 2000
architecture:
  input_modalities: [audio]
  output_modalities: [audio, text]
open_weights: false
license: proprietary
release_date: "2026-05-07"
knowledge_cutoff: "2024-09"
sources:
  - https://developers.openai.com/api/docs/models/gpt-realtime-translate
  - https://developers.openai.com/api/docs/guides/realtime-translation
  - https://developers.openai.com/api/docs/guides/speech-to-text
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://artificialanalysis.ai/speech-to-speech
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Realtime Translate

## Overview
OpenAI released GPT-Realtime-Translate on 2026-05-07 with GPT-Realtime-2 and GPT-Realtime-Whisper (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; gpt-realtime-translate is its only snapshot. OpenAI describes it as a streaming speech-to-speech translation model for live multilingual audio. It takes audio, returns translated audio and transcript deltas while the source audio is still arriving, and has a 16,000-token context window, 2,000 output tokens and a September 2024 knowledge cutoff. It runs only on /v1/realtime/translations, over WebRTC for browser media or WebSocket with 24 kHz PCM16 audio. The session acts as an interpreter rather than an assistant: it streams translated audio and transcript deltas instead of assistant turns or tool calls, there is no response.create, and each session translates into one target language set with session.update. It is priced by audio duration at $0.034 per minute. OpenAI names it as the replacement for /v1/audio/translations, which shuts down on 2027-02-26.

## Strengths
- Translated speech and subtitles from one continuous stream, with no turn lifecycle to manage.
- Works for listen-along (talks, livestreams, earnings calls) and conversational translation (one session per direction).
- Rate limits are set in minutes of audio: 200 per minute at Build, up to 850 at Grow.

## Limitations
- One output language per session; sessions scale with active speakers times target languages.
- Double the per-minute price of GPT Live Transcribe.
- Moving from /v1/audio/translations needs a new session-based integration, not just a new model id.
- OpenAI advises bilingual review of names, numbers, terminology and code-switching; no published accuracy figures, and Artificial Analysis's speech-to-speech board (read 2026-11-01) does not list it.

## Good for
- Live interpretation for calls, meetings, lessons and broadcasts.
- Replacing whisper-1 English translation before February 2027.
