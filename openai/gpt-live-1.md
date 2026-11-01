---
id: openai/gpt-live-1
name: GPT-Live 1
owned_by: openai
type: llm
description: GPT-Live 1 is OpenAI's full-duplex voice model on the Live API, generally available since September 2026, which listens and speaks at once and delegates reasoning and tools to a separate backend model or agent.
aliases: [gpt-live-1, azure/gpt-live-1]
capabilities: [tool_calling]
architecture:
  input_modalities: [audio, text]
  output_modalities: [audio, text]
open_weights: false
license: proprietary
release_date: "2026-09-10"
knowledge_cutoff: "2025-07"
sources:
  - https://developers.openai.com/api/docs/models/gpt-live-1
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/live
  - https://developers.openai.com/api/docs/guides/live-conversations
  - https://artificialanalysis.ai/speech-to-speech
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-Live 1

## Overview
GPT-Live 1 became generally available on 2026-09-10 (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; gpt-live-1 is the only snapshot. It is a full-duplex voice model: it can listen while speaking and hands reasoning and tool use to a backend through delegation, either Responses delegation (OpenAI runs a chosen Responses model) or client delegation (any model or agent the application runs). It takes audio and text, returns audio and text, does not accept images or video, and has a July 2025 knowledge cutoff; OpenAI publishes no context window. It runs on /v1/live/sessions. Voice sessions cost $0.05 per minute of session duration, billed per second; backend model and tool usage is billed separately. Rate limits are concurrent sessions: 50 at Build, 300 at Launch and 500 at Grow, with no free tier.

## Strengths
- Artificial Analysis speech-to-speech board (read 2026-11-01): GPT-Live-1 (Astra, medium) scores a Speech to Speech Index of 83.2 with 74.5% agentic performance, and (Sol, low) 80.1 with arena Elo 1037, the two highest OpenAI entries; both are single trials.
- The backend keeps working when the caller interrupts.
- 21 extra Live voices in English (including Australian, British, Irish and Southern US styles), Portuguese, German, French, Hindi, Japanese and Korean, plus voices created from a text description.
- Partner integrations for LiveKit, Twilio, Telnyx, Bandwidth and Daily/Pipecat.

## Limitations
- No structured outputs, fine-tuning or predicted outputs.
- Time to first audio of 1.24 to 1.34 s on AA, slower than most Realtime API entries (0.81 to 1.22 s).
- Total cost depends on the delegated backend, billed on top of the per-minute rate.

## Good for
- Phone and app conversations that need tools or long-running backend tasks.
- Replacing Realtime voice agents with a split voice and reasoning design.
