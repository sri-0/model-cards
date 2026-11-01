---
id: qwen/qwen3.8-omni-flash
name: Qwen3.8 Omni Flash
owned_by: qwen
type: llm
description: "Qwen3.8 Omni Flash is Alibaba's hosted omni-modal reasoning model that takes text, image, audio and video input and returns text, built on the Qwen3.8-Flash-Next architecture with a 1M-token context and native long-form audio-video understanding."
aliases: [qwen3.8-omni-flash]
context_length: 1000000
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
pricing:
  input: 0.15
  output: 0.47
  cache_read: 0.016
sources:
  - https://openrouter.ai/qwen/qwen3.8-omni-flash
  - https://openrouter.ai/api/v1/models
  - https://www.qwencloud.com/models/qwen3.8-omni-flash
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-8-omni-flash
  - https://www.alibabacloud.com/help/en/model-studio/omni
  - https://www.alibabacloud.com/help/en/model-studio/qwen-omni
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
retrieved: "2026-10-16"
---

# Qwen3.8 Omni Flash

## Overview
Qwen3.8 Omni Flash is Alibaba's hosted omni-modal reasoning model, served through Alibaba Cloud Model Studio and Qwen Cloud (`qwen3.8-omni-flash`) with no published weights; OpenRouter listed it on 2026-09-21. Qwen Cloud says it is built on the Qwen3.8-Flash-Next architecture and is the first Qwen model designed around agentic capability with native audio and video understanding. OpenRouter lists text, image, audio and video input with text output; the separate `qwen3.8-omni-flash-realtime` handles speech output. Model Studio's Qwen-Omni guide gives the input limits: audio up to 3 hours and 2 GB per file (WAV, MP3, AAC, AMR, 3GP and others) with 2-channel or 4-channel ambisonic spatial audio via `use_multichannel` and speech in 113 languages and dialects; video up to 2 hours and 2 GB, 64 files, visual and audio billed separately; up to 2,048 images. The context is 1M tokens (991,808 max input without thinking, 983,616 with, 131,072 max output). Thinking is on by default with `reasoning_effort` from none to max (default xhigh) and `preserve_thinking` on; JSON mode is supported but not JSON schema; a `web_search` built-in tool is available. Pricing is $0.15 input, $0.47 output and $0.016 cached input per million tokens on OpenRouter and Qwen Cloud.

## Strengths
- Audio-video analysis and summarisation, video editing and production, audio-video dialogue, coding, knowledge work and GUI interaction, per Qwen Cloud and OpenRouter.
- Long-form multimedia that combines speech, sound and visual context, plus spatial audio.
- Same low price as Qwen3.8 Flash.

## Limitations
- Text output only; no speech synthesis.
- Artificial Analysis figures are not recorded in this card, and no release date is published.
- No JSON schema structured output; function calling is supported.

## Good for
- Meeting, podcast and video summarisation and search.
- Agents that watch screens or video and listen to audio.
