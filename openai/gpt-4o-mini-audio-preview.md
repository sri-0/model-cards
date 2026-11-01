---
id: openai/gpt-4o-mini-audio-preview
name: GPT-4o Mini Audio Preview
owned_by: openai
type: llm
description: GPT-4o Mini Audio Preview was OpenAI's smaller preview audio-in, audio-out model for the Chat Completions API, shut down on 2026-05-07 in favour of gpt-audio-mini.
aliases: [gpt-4o-mini-audio-preview, gpt-4o-mini-audio-preview-2024-12-17, azure/gpt-4o-mini-audio-preview-2024-12-17]
context_length: 128000
max_output_tokens: 16384
capabilities: [tool_calling]
architecture:
  input_modalities: [text, audio]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
knowledge_cutoff: "2023-10"
sources:
  - https://developers.openai.com/api/docs/models/gpt-4o-mini-audio-preview
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o Mini Audio Preview

## Overview
Shut down. OpenAI announced the deprecation of the gpt-4o-mini-audio-preview model in September 2025 and removed it on 2026-05-07, recommending gpt-audio-mini, which itself shuts down on 2027-01-20 in favour of gpt-audio-1.5. The model page remains for reference. OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. OpenAI described it as a preview release of the smaller GPT-4o Audio model for audio input or output through the REST API; its only snapshot was gpt-4o-mini-audio-preview-2024-12-17, and OpenAI's docs give no separate release date. It ran on Chat Completions, took text and audio, returned text and audio, and had a 128,000-token context window, 16,384 output tokens and an October 2023 knowledge cutoff. Text cost $0.15 input and $0.60 output per million tokens; audio cost $10 input and $20 output.

## Strengths
- Far cheaper than gpt-4o-audio-preview: $0.15 against $2.50 for text input, and a quarter of its audio prices.
- Streaming and function calling.
- High default limits: 5,000 RPM and 2M TPM at Build, up to 30,000 RPM and 150M TPM at Grow, plus a free tier of 3 RPM, 200 RPD and 40,000 TPM.

## Limitations
- Shut down; requests to it no longer work on OpenAI's API.
- Its named replacement, gpt-audio-mini, is itself deprecated.
- No Artificial Analysis results.
- Knowledge stops at October 2023.

## Good for
- Interpreting logs and costs from integrations built on the preview.
- Mapping old ids during a move to gpt-audio-1.5.
