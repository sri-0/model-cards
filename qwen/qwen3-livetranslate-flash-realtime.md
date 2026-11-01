---
id: qwen/qwen3-livetranslate-flash-realtime
name: Qwen3-LiveTranslate-Flash-Realtime
owned_by: qwen
type: llm
description: "Qwen3-LiveTranslate-Flash-Realtime is the real-time version of Alibaba hosted Qwen3-LiveTranslate-Flash, a simultaneous audio and video interpretation model built on Qwen3-Omni that understands 19 languages and speaks 10."
aliases: [qwen3-livetranslate-flash-realtime-2025-09-22]
context_length: 53248
max_output_tokens: 4096
capabilities: [vision]
architecture:
  input_modalities: [audio, image]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2025-09-23"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-LiveTranslate-Flash-Realtime

## Overview
Status: Model Studio's current pricing page no longer lists qwen3-livetranslate-flash-realtime; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. Qwen3-LiveTranslate-Flash-Realtime (Model Studio id `qwen3-livetranslate-flash-realtime`, documented as equivalent to `qwen3-livetranslate-flash-realtime-2025-09-22`) appears in Model Studio's release table from 2025-09-23 in China (Beijing) and 2025-09-24 in Singapore; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes a high-precision, responsive multilingual simultaneous interpretation model for audio and video, built on Qwen3-Omni with cross-language and cross-modal alignment and visual enhancement, that understands 19 languages and speaks 10, including 8 Chinese dialects. The archived models page gives a 53,248-token context with 49,152 input and 4,096 output tokens. Singapore prices per million tokens were $10 audio input, $1.30 image input, $10 text output and $38 audio output.

## Strengths
- Live interpretation with spoken output.

## Limitations
- No longer listed for sale; Qwen3.5 and Qwen3.8 LiveTranslate replace it.
- Higher prices than its successors.

## Good for
- Interpreting older real-time translation integrations.
