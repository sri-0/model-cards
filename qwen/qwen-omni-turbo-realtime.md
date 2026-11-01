---
id: qwen/qwen-omni-turbo-realtime
name: Qwen-Omni-Turbo-Realtime
owned_by: qwen
type: llm
description: "Qwen-Omni-Turbo-Realtime is the real-time version of Alibaba earlier hosted Qwen-Omni-Turbo on Model Studio, for live audio interaction with mixed text, image and video input and streamed speech output."
aliases: [qwen-omni-turbo-realtime-latest, qwen-omni-turbo-realtime-2025-05-08]
context_length: 32768
max_output_tokens: 2048
capabilities: [vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2025-05-08"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Omni-Turbo-Realtime

## Overview
Status: Model Studio's current pricing page no longer lists qwen-omni-turbo-realtime; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. Qwen-Omni-Turbo-Realtime (Model Studio id `qwen-omni-turbo-realtime`, documented as equivalent to `qwen-omni-turbo-realtime-2025-05-08`, with a `-latest` alias) appears in Model Studio's release table from 2025-05-08 in China (Beijing) and 2025-08-14 in Singapore; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes it as the real-time version of Qwen's multimodal understanding and generation model for live audio interaction: it understands audio together with text, images and video, and streams speech and text with four natural voices. The archived models page gives a 32,768-token context with 30,720 input and 2,048 output tokens. Singapore prices per million tokens were $0.27 text, $4.44 audio and $0.84 image input, and $1.07, $2.52 or $8.89 output for text after text-only input, text after multimodal input, and text plus audio.

## Strengths
- Live voice interaction with visual context.

## Limitations
- No longer listed for sale on Model Studio.
- Only 2,048 output tokens and four voices.

## Good for
- Interpreting older real-time voice integrations.
