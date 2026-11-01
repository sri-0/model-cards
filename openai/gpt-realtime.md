---
id: openai/gpt-realtime
name: GPT Realtime
owned_by: openai
type: llm
description: GPT Realtime is OpenAI's first generally available speech-to-speech model for the Realtime API, taking text, audio and images over WebRTC, WebSocket or SIP, deprecated in favour of gpt-realtime-2.1 and shutting down on 2027-01-20.
aliases: [gpt-realtime, gpt-realtime-2025-08-28, azure/gpt-realtime, azure/gpt-realtime-2025-08-28]
context_length: 32000
max_output_tokens: 4096
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, audio, image]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2025-08-28"
knowledge_cutoff: "2023-10"
sources:
  - https://developers.openai.com/api/docs/models/gpt-realtime
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/realtime
  - https://developers.openai.com/api/docs/guides/realtime-conversations
  - https://developers.openai.com/blog/realtime-api
  - https://artificialanalysis.ai/speech-to-speech
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Realtime

## Overview
gpt-realtime shipped with the general availability of the Realtime API on 2025-08-28 (OpenAI changelog); its only snapshot is gpt-realtime-2025-08-28. OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. OpenAI calls it its first general-availability realtime model, responding to audio and text in realtime over WebRTC, WebSocket or SIP; it also accepts images. The model page gives a 32,000-token context window, 4,096 output tokens and an October 2023 knowledge cutoff (OpenAI's Realtime developer notes say 32,768 tokens). It runs only on /v1/realtime. Per million tokens it costs $4 input, $0.40 cached and $16 output for text; $32 input, $0.40 cached and $64 output for audio; and $5 input ($0.50 cached) for images. OpenAI deprecated it on 2026-07-20; it shuts down on 2027-01-20, replaced by gpt-realtime-2.1.

## Strengths
- Artificial Analysis speech-to-speech board (read 2026-11-01), GPT Realtime (Aug '25): Speech to Speech Index 69.1, 83% on Big Bench Audio, 30.4% agentic performance, 89.4% task success, arena Elo 967 and 0.98 s to first audio.
- Function calling and prompt caching.
- Ten voices; OpenAI recommends marin or cedar.
- Image input in a voice session, which the Realtime guide lists for gpt-realtime and gpt-realtime-2 only.

## Limitations
- Deprecated; shuts down on 2027-01-20.
- Audio costs $32 and $64 per million tokens, eight and four times the text rates.
- Sessions last at most 60 minutes, and the voice cannot change once audio has been produced.
- Not on Chat Completions or Responses; Chat Completions audio uses gpt-audio models instead.
- Behind gpt-realtime-2.1 High on the same board (index 75.2, 96% Big Bench Audio).

## Good for
- Voice agents already built on the Realtime API that cannot move to gpt-realtime-2.1 before 2027.
- SIP telephony with tool calls.
- Sessions that mix speech with screenshots or photos.
