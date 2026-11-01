---
id: openai/gpt-4o-mini-realtime-preview
name: GPT-4o Mini Realtime Preview
owned_by: openai
type: llm
description: GPT-4o Mini Realtime Preview was OpenAI's smaller preview speech-to-speech model for the Realtime API, released in December 2024 and shut down on 2026-05-07 in favour of gpt-realtime-mini.
aliases: [gpt-4o-mini-realtime-preview, gpt-4o-mini-realtime-preview-2024-12-17, azure/gpt-4o-mini-realtime-preview-2024-12-17]
context_length: 16000
max_output_tokens: 4096
capabilities: [tool_calling]
architecture:
  input_modalities: [text, audio]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2024-12-17"
knowledge_cutoff: "2023-10"
sources:
  - https://developers.openai.com/api/docs/models/gpt-4o-mini-realtime-preview
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/deprecations
  - https://artificialanalysis.ai/speech-to-speech
  - https://artificialanalysis.ai/models/gpt-4o-mini-realtime-dec-24
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o Mini Realtime Preview

## Overview
Shut down. OpenAI announced the deprecation of the gpt-4o-mini-realtime-preview model in September 2025 and removed it on 2026-05-07, recommending gpt-realtime-mini, which itself shuts down on 2027-01-20 in favour of gpt-realtime-2.1-mini. The model page remains for reference. OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. Its only snapshot was gpt-4o-mini-realtime-preview-2024-12-17; Artificial Analysis dates it to 2024-12-17. OpenAI described it as a preview of the GPT-4o-Mini Realtime model, responding to audio and text in realtime over WebRTC or WebSocket. It returned text and audio, and had a 16,000-token context window, 4,096 output tokens and an October 2023 knowledge cutoff. Per million tokens it cost $0.60 input, $0.30 cached and $2.40 output for text, and $10 input, $0.30 cached and $20 output for audio.

## Strengths
- A quarter of gpt-4o-realtime-preview's audio price ($10 and $20 against $40 and $80 per million tokens).
- Function calling and prompt caching.
- Artificial Analysis's speech-to-speech board (read 2026-11-01) lists GPT-4o mini Realtime (Dec 2024) at 69% on Big Bench Audio with 1.27 s to first audio.

## Limitations
- Shut down; requests to it no longer work on OpenAI's API.
- Its named replacement, gpt-realtime-mini, is itself deprecated.
- Half the context of gpt-4o-realtime-preview (16,000 against 32,000 tokens), and no image input.
- No index score on AA's board.
- Knowledge stops at October 2023.

## Good for
- Interpreting logs and costs from Realtime beta integrations.
- Mapping old ids during a move to gpt-realtime-2.1-mini.
