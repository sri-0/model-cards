---
id: openai/gpt-audio-mini
name: GPT Audio Mini
owned_by: openai
type: llm
description: GPT Audio Mini is the cost-efficient version of OpenAI's GPT Audio for speech in and out on the Chat Completions API, released at DevDay 2025 and shutting down on 2027-01-20.
aliases: [gpt-audio-mini, gpt-audio-mini-2025-12-15, gpt-audio-mini-2025-10-06, azure/gpt-audio-mini, azure/gpt-audio-mini-2025-10-06]
context_length: 128000
max_output_tokens: 16384
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p]
architecture:
  input_modalities: [text, audio]
  output_modalities: [text, audio]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-10-06"
knowledge_cutoff: "2023-10"
pricing:
  input: 0.6
  output: 2.4
sources:
  - https://openrouter.ai/openai/gpt-audio-mini
  - https://openrouter.ai/api/v1/models
  - https://developers.openai.com/api/docs/models/gpt-audio-mini
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/blog/updates-audio-models
  - https://artificialanalysis.ai/speech-to-speech
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Audio Mini

## Overview
gpt-audio-mini was released at OpenAI DevDay on 2025-10-06 alongside gpt-realtime-mini for more cost-efficient speech-to-speech (OpenAI changelog). OpenRouter lists it as openai/gpt-audio-mini. OpenAI describes it as a cost-efficient version of GPT Audio that accepts audio inputs and outputs on the Chat Completions API. The snapshots are gpt-audio-mini-2025-10-06, shut down on 2026-07-23, and gpt-audio-mini-2025-12-15, the default since 2026-01-13. It has a 128,000-token context window, 16,384 output tokens and an October 2023 knowledge cutoff. OpenAI charges $0.60 input and $2.40 output per million text tokens and $10 input and $20 output per million audio tokens; OpenRouter lists audio at the text rates, $0.60 and $2.40. OpenAI deprecated it on 2026-07-20; it shuts down on 2027-01-20, replaced by gpt-audio-1.5.

## Strengths
- About a quarter of gpt-audio's text price and under a third of its audio price at OpenAI's rates.
- OpenAI says the 2025-12-15 snapshot was optimised for tool calling and instruction following and has an upgraded decoder for more natural voices and steadier custom voices.
- Function calling and prompt caching; 5,000 RPM and 450,000 TPM at Build, up to 30M TPM at Grow.

## Limitations
- Deprecated; shuts down on 2027-01-20.
- Chat Completions only, for speech-to-speech where real-time interaction is not required.
- OpenRouter's audio price differs from OpenAI's list price; check the bill on each route.
- No published benchmarks; Artificial Analysis's speech-to-speech board (read 2026-11-01) does not list it.
- Knowledge stops at October 2023.

## Good for
- Low-cost spoken replies in Chat Completions applications.
- Voice features that need tool calls but not streaming audio sessions.
- Pinning gpt-audio-mini-2025-12-15 until a move to gpt-audio-1.5.
