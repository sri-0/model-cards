---
id: openai/gpt-realtime-mini
name: GPT Realtime Mini
owned_by: openai
type: llm
description: GPT Realtime Mini is OpenAI's cost-efficient speech-to-speech model for the Realtime API, released at DevDay 2025 and deprecated in favour of gpt-realtime-2.1-mini, shutting down on 2027-01-20.
aliases: [gpt-realtime-mini, gpt-realtime-mini-2025-12-15, gpt-realtime-mini-2025-10-06, azure/gpt-realtime-mini, azure/gpt-realtime-mini-2025-10-06]
context_length: 32000
max_output_tokens: 4096
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image, audio]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2025-10-06"
knowledge_cutoff: "2023-10"
sources:
  - https://developers.openai.com/api/docs/models/gpt-realtime-mini
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/realtime-conversations
  - https://developers.openai.com/blog/updates-audio-models
  - https://artificialanalysis.ai/speech-to-speech
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Realtime Mini

## Overview
gpt-realtime-mini was released at OpenAI DevDay on 2025-10-06 for more cost-efficient speech-to-speech (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. Its snapshots are gpt-realtime-mini-2025-10-06, shut down on 2026-07-23, and gpt-realtime-mini-2025-12-15, the default since 2026-01-13. OpenAI describes it as a cost-efficient version of GPT-Realtime that responds to audio and text over WebRTC, WebSocket or SIP; the model page lists image input as well. It has a 32,000-token context window, 4,096 output tokens and an October 2023 knowledge cutoff, and runs only on /v1/realtime. Per million tokens it costs $0.60 input, $0.06 cached and $2.40 output for text; $10 input, $0.30 cached and $20 output for audio; and $0.80 input ($0.08 cached) for images. OpenAI deprecated it on 2026-07-20; it shuts down on 2027-01-20, replaced by gpt-realtime-2.1-mini.

## Strengths
- Audio at roughly a third of gpt-realtime's price ($10 and $20 against $32 and $64 per million tokens).
- OpenAI reports the 2025-12-15 snapshot gained 18.6 points in instruction following and 12.9 points in tool-calling accuracy over the previous snapshot on its internal evaluations.
- Function calling and prompt caching; Build-tier limits of 400 RPM and 200,000 TPM, up to 20,000 RPM and 15M TPM.

## Limitations
- Deprecated; shuts down on 2027-01-20.
- Artificial Analysis's speech-to-speech board (read 2026-11-01) covers only the shut-down October snapshot: Speech to Speech Index 56.1, 64% on Big Bench Audio and 15.1% agentic performance, against 69.1, 83% and 30.4% for gpt-realtime; time to first audio is 0.81 s.
- Sessions are capped at 60 minutes.
- Not on Chat Completions or Responses; gpt-audio-mini serves Chat Completions.

## Good for
- High-volume voice agents where audio token cost dominates.
- SIP telephony bots with tool calls.
- Bridging Realtime integrations until a move to gpt-realtime-2.1-mini.
