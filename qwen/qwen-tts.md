---
id: qwen/qwen-tts
name: Qwen-TTS
owned_by: qwen
type: tts
description: "Qwen-TTS is the first Qwen speech synthesis model on Model Studio, for Chinese, English and mixed-language text with adaptive tone and streaming output."
aliases: [qwen-tts-latest, qwen-tts-2025-04-10, qwen-tts-2025-05-22]
context_length: 8192
max_output_tokens: 7680
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2025-04-20"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-TTS

## Overview
Status: Model Studio's current pricing page no longer lists qwen-tts or its snapshots; `qwen-tts-latest` is on the archived 2026-10-07 pricing page but not on 2026-10-13, and the deprecation page names no date for them. Qwen-TTS (Model Studio id `qwen-tts`) appears in Model Studio's release table from 2025-04-20 with the `qwen-tts-2025-04-10` snapshot, which the stable id was documented as equivalent to; `qwen-tts-latest` followed the newest snapshot, and a `qwen-tts-2025-05-22` snapshot followed. No weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio calls it the first speech synthesis model in the Qwen series, for Chinese, English and mixed input, with tone that adapts to the text, natural voice quality and streaming output. The archived models page gives an 8,192-token context with 512 input and 7,680 output tokens, billed by tokens with 50 tokens per second of audio; the archived pricing page lists qwen-tts-latest at $0.23 input and $1.434 output per million tokens in China (Beijing).

## Strengths
- Mixed Chinese and English text in one request.
- Streaming output.

## Limitations
- No longer listed for sale on Model Studio.
- Only 512 input tokens per request.

## Good for
- Interpreting older integrations that used qwen-tts.
