---
id: openai/gpt-audio-1.5
name: GPT Audio 1.5
owned_by: openai
type: llm
description: GPT Audio 1.5 is OpenAI's current audio-in, audio-out model for the Chat Completions API, released in February 2026 and named as the replacement for gpt-audio, gpt-audio-mini and the GPT-4o audio previews.
aliases: [gpt-audio-1.5, azure/gpt-audio-1.5, azure/gpt-audio-1.5-2026-02-23]
context_length: 128000
max_output_tokens: 16384
capabilities: [tool_calling]
architecture:
  input_modalities: [text, audio]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-02-23"
knowledge_cutoff: "2024-09"
sources:
  - https://developers.openai.com/api/docs/models/gpt-audio-1.5
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/audio-chat-completions
  - https://artificialanalysis.ai/speech-to-speech
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Audio 1.5

## Overview
gpt-audio-1.5 was released to the Chat Completions API on 2026-02-23, alongside GPT-Realtime-1.5 (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; gpt-audio-1.5 is the only OpenAI snapshot, and LiteLLM lists an Azure deployment dated 2026-02-23. OpenAI's model page calls it the best voice model for audio in and audio out with Chat Completions. It takes text and audio, returns text and audio, and has a 128,000-token context window, 16,384 output tokens and a September 2024 knowledge cutoff. Text costs $2.50 input and $10 output per million tokens; audio costs $32 input and $64 output, the same as gpt-audio. OpenAI's Chat Completions audio guide uses it in its examples, and the deprecations page names it the replacement for gpt-audio, gpt-audio-mini, gpt-4o-audio and gpt-4o-mini-audio (shutting down 2027-01-20) and for gpt-4o-audio-preview, already shut down. It is not deprecated.

## Strengths
- Spoken input and spoken replies in ordinary Chat Completions requests, without a Realtime session.
- Streaming and function calling.
- A newer knowledge cutoff than gpt-audio (September 2024 against October 2023) at the same prices.
- 5,000 RPM and 450,000 TPM at Build, up to 30M TPM at Grow, with Batch queue limits listed.

## Limitations
- Chat Completions only; not served on the Responses or Realtime APIs.
- Audio tokens cost $32 and $64 per million against $2.50 and $10 for text.
- No prompt caching listed, unlike gpt-audio-mini.
- No published benchmarks; Artificial Analysis's speech-to-speech board (read 2026-11-01) does not list it.

## Good for
- Adding spoken replies to existing Chat Completions applications.
- Turn-based voice features where realtime latency is not needed.
- Migrations from gpt-audio, gpt-audio-mini or gpt-4o-audio-preview.
