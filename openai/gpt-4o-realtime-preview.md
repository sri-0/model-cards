---
id: openai/gpt-4o-realtime-preview
name: GPT-4o Realtime Preview
owned_by: openai
type: llm
description: GPT-4o Realtime Preview was OpenAI's preview speech-to-speech model for the Realtime API beta, launched in October 2024 and shut down on 2026-05-07 in favour of gpt-realtime-1.5.
aliases: [gpt-4o-realtime-preview, gpt-4o-realtime-preview-2025-06-03, gpt-4o-realtime-preview-2024-12-17, gpt-4o-realtime-preview-2024-10-01, azure/gpt-4o-realtime-preview-2024-12-17, azure/gpt-4o-realtime-preview-2024-10-01]
context_length: 32000
max_output_tokens: 4096
capabilities: [tool_calling]
architecture:
  input_modalities: [text, audio]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2024-10-01"
knowledge_cutoff: "2023-10"
sources:
  - https://developers.openai.com/api/docs/models/gpt-4o-realtime-preview
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://artificialanalysis.ai/speech-to-speech
  - https://artificialanalysis.ai/models/gpt-4o-realtime-dec-24
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o Realtime Preview

## Overview
Shut down. OpenAI announced the deprecation of the gpt-4o-realtime-preview models in September 2025 and removed them on 2026-05-07, recommending gpt-realtime-1.5; the first snapshot, gpt-4o-realtime-preview-2024-10-01, had already shut down on 2025-10-10, and the Realtime API beta interface was removed on 2026-05-12. The model page remains for reference. OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. It arrived with the Realtime API on 2024-10-01 (OpenAI changelog), with later snapshots on 2024-12-17 (when WebRTC was added) and 2025-06-03, the last default. It responded to audio and text in realtime over WebRTC or WebSocket, returned text and audio, and had a 32,000-token context window, 4,096 output tokens and an October 2023 knowledge cutoff. Per million tokens it cost $5 input, $2.50 cached and $20 output for text, and $40 input, $2.50 cached and $80 output for audio.

## Strengths
- Function calling and prompt caching.
- Artificial Analysis's speech-to-speech board (read 2026-11-01) lists GPT-4o Realtime (Dec 2024) at 89.8% conversational dynamics and 27.9% agentic performance, with 1.49 s to first audio.

## Limitations
- Shut down; requests to it no longer work on OpenAI's API.
- No image input, unlike gpt-realtime and its successors.
- Audio cost $40 and $80 per million tokens, against $32 and $64 for gpt-realtime-1.5.
- AA gives the December 2024 snapshot no Big Bench Audio score or index.
- Knowledge stops at October 2023.

## Good for
- Interpreting logs and costs from Realtime beta integrations.
- Mapping old gpt-4o-realtime-preview ids to gpt-realtime-1.5 during migration.
