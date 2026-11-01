---
id: openai/gpt-4o-audio-preview
name: GPT-4o Audio Preview
owned_by: openai
type: llm
description: GPT-4o Audio Preview was OpenAI's preview audio-in, audio-out model for the Chat Completions API, released in October 2024 and shut down on 2026-05-07 in favour of gpt-audio-1.5.
aliases: [gpt-4o-audio-preview, gpt-4o-audio-preview-2025-06-03, gpt-4o-audio-preview-2024-12-17, gpt-4o-audio-preview-2024-10-01, azure/gpt-4o-audio-preview-2024-12-17]
context_length: 128000
max_output_tokens: 16384
capabilities: [tool_calling]
architecture:
  input_modalities: [text, audio]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2024-10-17"
knowledge_cutoff: "2023-10"
sources:
  - https://developers.openai.com/api/docs/models/gpt-4o-audio-preview
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://artificialanalysis.ai/speech-to-speech
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o Audio Preview

## Overview
Shut down. OpenAI announced the deprecation of the gpt-4o-audio-preview models in September 2025 and removed them on 2026-05-07, recommending gpt-audio-1.5; the first snapshot, gpt-4o-audio-preview-2024-10-01, had already shut down on 2025-10-10. The model page remains for reference. OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. OpenAI released it on 2024-10-17 for Chat Completions with audio input and output, using the same underlying model as the Realtime API (OpenAI changelog); later snapshots were 2024-12-17 and 2025-06-03, the last default. It took text and audio, returned text and audio, and had a 128,000-token context window, 16,384 output tokens and an October 2023 knowledge cutoff. Text cost $2.50 input and $10 output per million tokens; audio cost $40 input and $80 output.

## Strengths
- Streaming and function calling on Chat Completions.
- 5,000 RPM and 450,000 TPM at Build, up to 30M TPM at Grow.
- Artificial Analysis's speech-to-speech board (read 2026-11-01) lists a "GPT-4o audio chatcompletions" entry at 54% on Big Bench Audio.

## Limitations
- Shut down; requests to it no longer work on OpenAI's API.
- Audio cost more than its successors: $40 and $80 per million tokens against $32 and $64 for gpt-audio-1.5.
- That AA entry takes 3.38 s to first audio and has no index score.
- Knowledge stops at October 2023.

## Good for
- Interpreting logs and costs from integrations built on the preview.
- Mapping old gpt-4o-audio-preview ids to gpt-audio-1.5 during migration.
