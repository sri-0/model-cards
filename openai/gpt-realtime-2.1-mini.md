---
id: openai/gpt-realtime-2.1-mini
name: GPT Realtime 2.1 Mini
owned_by: openai
type: llm
description: GPT Realtime 2.1 Mini is OpenAI's distilled reasoning speech-to-speech model for faster, lower-cost voice agents on the Realtime API, released in July 2026 and named as the replacement for its older mini voice and text-to-speech models.
aliases: [gpt-realtime-2.1-mini, azure/gpt-realtime-2.1-mini]
context_length: 128000
max_output_tokens: 32000
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, audio, image]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-07-06"
knowledge_cutoff: "2024-09"
sources:
  - https://developers.openai.com/api/docs/models/gpt-realtime-2.1-mini
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/text-to-speech
  - https://artificialanalysis.ai/speech-to-speech
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Realtime 2.1 Mini

## Overview
GPT-Realtime-2.1 mini was released on 2026-07-06 with GPT-Realtime-2.1 as a faster, lower-cost distilled reasoning model for realtime voice applications (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; gpt-realtime-2.1-mini is the only snapshot. It accepts text, audio and images over WebRTC, WebSocket or SIP, returns text and audio, supports reasoning tokens and improves alphanumeric recognition over GPT-Realtime-2. It has a 128,000-token context window, 32,000 output tokens and a September 2024 knowledge cutoff, and runs only on /v1/realtime. Per million tokens it costs $0.60 input, $0.06 cached and $2.40 output for text; $10 input, $0.30 cached and $20 output for audio; and $0.80 input ($0.08 cached) for images, the same as gpt-realtime-mini. OpenAI's deprecations name it the replacement for gpt-realtime-mini and gpt-4o-mini-realtime (shutting down 2027-01-20) and for tts-1, tts-1-hd and gpt-4o-mini-tts (shutting down 2027-01-06).

## Strengths
- Four times gpt-realtime-mini's context window and nearly eight times its output limit at the same prices.
- Artificial Analysis speech-to-speech board (read 2026-11-01): GPT-Realtime-2.1 Mini High reaches 75% on Big Bench Audio and 29.4% agentic performance; the Minimal setting answers in 0.85 s.
- Function calling, prompt caching and image input.

## Limitations
- The Minimal setting scores a Speech to Speech Index of 54.4, 63% on Big Bench Audio, 76.7% task success and arena Elo 840, the lowest OpenAI index on the board.
- The High setting takes 4.28 s to first audio.
- Not a /v1/audio/speech model: replacing the TTS models means moving to Realtime sessions.

## Good for
- High-volume voice agents where audio cost dominates.
- Replacing gpt-realtime-mini or the Speech API TTS models.
