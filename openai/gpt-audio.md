---
id: openai/gpt-audio
name: GPT Audio
owned_by: openai
type: llm
description: GPT Audio is OpenAI's first generally available audio model for the Chat Completions API, taking and returning text and speech, deprecated in favour of gpt-audio-1.5 and shutting down on 2027-01-20.
aliases: [gpt-audio, gpt-audio-2025-08-28, azure/gpt-audio, azure/gpt-audio-2025-08-28]
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
knowledge_cutoff: "2023-10"
pricing:
  input: 2.5
  output: 10
sources:
  - https://openrouter.ai/openai/gpt-audio
  - https://openrouter.ai/api/v1/models
  - https://developers.openai.com/api/docs/models/gpt-audio
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/guides/audio-chat-completions
  - https://artificialanalysis.ai/speech-to-speech
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Audio

## Overview
OpenAI calls gpt-audio its first generally available audio model: it accepts audio input and produces audio output on the Chat Completions REST API. Its only snapshot is gpt-audio-2025-08-28; OpenAI's docs give no separate release date. OpenRouter lists it as openai/gpt-audio. It takes text and audio, returns text and audio, and has a 128,000-token context window, 16,384 output tokens and an October 2023 knowledge cutoff. Text costs $2.50 input and $10 output per million tokens; audio costs $32 input and $64 output per million tokens, on both OpenAI and OpenRouter. OpenAI deprecated it on 2026-07-20; it shuts down on 2027-01-20, replaced by gpt-audio-1.5, which OpenAI's Chat Completions audio guide now uses in its examples.

## Strengths
- Spoken input and spoken replies in ordinary Chat Completions requests, with no Realtime session to manage.
- Streaming and function calling per OpenAI; OpenRouter also passes structured outputs, logprobs and seed.
- Higher default limits than the Realtime models: 5,000 RPM and 450,000 TPM at Build, up to 30M TPM at Grow.

## Limitations
- Deprecated; shuts down on 2027-01-20.
- Chat Completions only: not served on the Responses or Realtime APIs.
- Audio tokens cost $32 and $64 per million against $2.50 and $10 for text.
- Knowledge stops at October 2023.
- No published benchmarks; Artificial Analysis's speech-to-speech board (read 2026-11-01) does not list it.

## Good for
- Adding spoken replies to an existing Chat Completions application.
- Turn-based voice features where realtime latency is not needed.
- Existing integrations until they move to gpt-audio-1.5.
