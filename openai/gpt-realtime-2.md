---
id: openai/gpt-realtime-2
name: GPT Realtime 2
owned_by: openai
type: llm
description: GPT Realtime 2 is OpenAI's May 2026 realtime voice model with configurable reasoning effort, stronger instruction following and more reliable tool use for speech-to-speech agents on the Realtime API.
aliases: [gpt-realtime-2, azure/gpt-realtime-2]
context_length: 128000
max_output_tokens: 32000
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, audio, image]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-05-07"
knowledge_cutoff: "2024-09"
sources:
  - https://developers.openai.com/api/docs/models/gpt-realtime-2
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/realtime-conversations
  - https://artificialanalysis.ai/speech-to-speech
  - https://artificialanalysis.ai/text-to-speech/leaderboard
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Realtime 2

## Overview
GPT-Realtime-2 was released on 2026-05-07 as a realtime voice model with configurable reasoning for speech-to-speech agents, alongside gpt-realtime-translate and gpt-realtime-whisper (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; gpt-realtime-2 is the only snapshot. OpenAI describes it as its most capable realtime voice model, with stronger instruction following and more reliable tool use. It takes text, audio and images, returns text and audio, supports reasoning tokens, and has a 128,000-token context window, 32,000 output tokens and a September 2024 knowledge cutoff. It runs only on /v1/realtime. Per million tokens it costs $4 input, $0.40 cached and $24 output for text; $32 input, $0.40 cached and $64 output for audio; and $5 input ($0.50 cached) for images. It is not deprecated; gpt-realtime-2.1 is its update.

## Strengths
- Artificial Analysis speech-to-speech board (read 2026-11-01): GPT-Realtime-2 (High) scores a Speech to Speech Index of 73.6, 97% on Big Bench Audio, 39.8% agentic performance and 89.8% task success, with 1.14 s to first audio.
- Four times gpt-realtime-1.5's context and nearly eight times its output limit.
- Function calling, prompt caching and image input.

## Limitations
- Higher reasoning effort raises latency and output tokens, per OpenAI; the Minimal setting drops to an index of 63.3 and 72% on Big Bench Audio (one trial).
- Text output costs $24 per million tokens, against $16 for gpt-realtime-1.5.
- Arena Elo of 920 on the speech-to-speech board, below gpt-realtime-1.5's anchor of 1000; Elo 1073 on AA's text-to-speech arena.
- Superseded by gpt-realtime-2.1, which improves alphanumeric recognition, noise handling and interruptions.

## Good for
- Voice agents that need multi-step reasoning and tool calls.
- Long sessions that exceed 32,000 tokens.
