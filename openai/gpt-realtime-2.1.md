---
id: openai/gpt-realtime-2.1
name: GPT Realtime 2.1
owned_by: openai
type: llm
description: GPT Realtime 2.1 is OpenAI's July 2026 update to GPT Realtime 2, a reasoning speech-to-speech model for the Realtime API with better alphanumeric recognition, silence and noise handling and interruption behaviour.
aliases: [gpt-realtime-2.1, azure/gpt-realtime-2.1]
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
  - https://developers.openai.com/api/docs/models/gpt-realtime-2.1
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/realtime
  - https://artificialanalysis.ai/speech-to-speech
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Realtime 2.1

## Overview
GPT-Realtime-2.1 was released on 2026-07-06 with GPT-Realtime-2.1 mini (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; gpt-realtime-2.1 is the only snapshot. OpenAI describes it as an update to GPT-Realtime-2 with improved alphanumeric recognition, silence and noise handling, and interruption behaviour, keeping configurable reasoning effort and tool use. It takes text, audio and images, returns text and audio, and has a 128,000-token context window, 32,000 output tokens and a September 2024 knowledge cutoff. It runs only on /v1/realtime, and OpenAI's Realtime getting-started guide uses it in its example. Per million tokens it costs $4 input, $0.40 cached and $24 output for text; $32 input, $0.40 cached and $64 output for audio; and $5 input ($0.50 cached) for images. OpenAI's deprecations name it the replacement for gpt-realtime and gpt-4o-realtime, which shut down on 2027-01-20.

## Strengths
- Artificial Analysis speech-to-speech board (read 2026-11-01): GPT-Realtime-2.1 High scores a Speech to Speech Index of 75.2 (two trials), the highest Realtime API model there, with 96% on Big Bench Audio, 45.7% agentic performance, 91.5% task success and 1.21 s to first audio.
- The Minimal setting keeps an index of 70.7 and 87% on Big Bench Audio with 0.97 s to first audio.
- Function calling, prompt caching and image input.

## Limitations
- Higher reasoning effort raises latency and output tokens, per OpenAI.
- Text output costs $24 per million tokens and audio $32 input and $64 output.
- GPT-Live-1 scores higher on the same board (83.2 and 80.1), and agentic performance stays below 50%.
- Build-tier limits of 400 RPM and 200,000 TPM.

## Good for
- New speech-to-speech agents on the Realtime API.
- Calls with spoken letters and numbers or background noise, where OpenAI reports the 2.1 improvements.
- Migrations from gpt-realtime before its 2027 shutdown.
