---
id: openai/gpt-realtime-1.5
name: GPT Realtime 1.5
owned_by: openai
type: llm
description: GPT Realtime 1.5 is OpenAI's February 2026 speech-to-speech model for voice agents and customer support on the Realtime API, taking text, audio and images with a September 2024 knowledge cutoff.
aliases: [gpt-realtime-1.5, azure/gpt-realtime-1.5, azure/gpt-realtime-1.5-2026-02-23]
context_length: 32000
max_output_tokens: 4096
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, audio, image]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-02-23"
knowledge_cutoff: "2024-09"
sources:
  - https://developers.openai.com/api/docs/models/gpt-realtime-1.5
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/realtime-conversations
  - https://artificialanalysis.ai/speech-to-speech
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Realtime 1.5

## Overview
GPT-Realtime-1.5 was released to the Realtime API on 2026-02-23 (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; gpt-realtime-1.5 is the only OpenAI snapshot, and LiteLLM lists an Azure deployment dated 2026-02-23. OpenAI calls it its flagship audio model for voice agents and customer support. It takes text, audio and images, returns text and audio, and has a 32,000-token context window, 4,096 output tokens and a September 2024 knowledge cutoff. It runs only on /v1/realtime. Per million tokens it costs $4 input, $0.40 cached and $16 output for text; $32 input, $0.40 cached and $64 output for audio; and $5 input ($0.50 cached) for images, the same as gpt-realtime. OpenAI named it the replacement for gpt-4o-realtime-preview, which shut down on 2026-05-07. It is not deprecated.

## Strengths
- Artificial Analysis speech-to-speech board (read 2026-11-01): Speech to Speech Index 70.3, 81% on Big Bench Audio, 95.7% conversational dynamics, 38.8% agentic performance, 85.1% task success and 0.81 s to first audio, tied fastest among OpenAI entries; the board anchors its arena Elo on this model at 1000.
- Function calling and prompt caching.
- A newer knowledge cutoff than gpt-realtime (September 2024 against October 2023) at the same prices.

## Limitations
- 32,000-token context and 4,096 output tokens, against 128,000 and 32,000 for gpt-realtime-2 and 2.1.
- No configurable reasoning effort.
- Audio costs $32 and $64 per million tokens, eight and four times the text rates.
- Behind GPT-Realtime-2.1 High (75.2) and GPT-Live-1 (83.2 and 80.1) on the same board.
- Build-tier limits of 400 RPM and 200,000 TPM.

## Good for
- Low-latency voice agents and support lines on the Realtime API.
- Migrations from gpt-4o-realtime-preview.
- Voice sessions that mix speech with images.
