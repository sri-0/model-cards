---
id: qwen/qwen-omni-turbo
name: Qwen-Omni-Turbo
owned_by: qwen
type: llm
description: "Qwen-Omni-Turbo is Alibaba earlier hosted Qwen multimodal understanding and generation model on Model Studio, taking text, image, speech and video input and streaming text and speech with four voices."
aliases: [qwen-omni-turbo-latest, qwen-omni-turbo-2025-03-26, qwen-omni-turbo-0326, qwen-omni-turbo-2025-01-19, qwen-omni-turbo-0119]
context_length: 32768
max_output_tokens: 2048
capabilities: [vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2025-02-14"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Omni-Turbo

## Overview
Status: Model Studio's current pricing page no longer lists qwen-omni-turbo; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. Qwen-Omni-Turbo (Model Studio id `qwen-omni-turbo`, documented as equivalent to `qwen-omni-turbo-2025-03-26`, also `qwen-omni-turbo-0326`) first appears in Model Studio's release table on 2025-02-14 in China (Beijing), with an earlier `qwen-omni-turbo-2025-01-19` (0119) snapshot and a Singapore launch on 2025-07-18; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes a multimodal understanding and generation model that takes text, image, speech and video input, including mixed input, streams text and speech together, and offers four natural dialogue voices. The archived models page gives a 32,768-token context with 30,720 input and 2,048 output tokens, non-thinking only. Singapore prices per million tokens were $0.07 text, $4.44 audio and $0.21 image or video input, and $0.27, $0.63 or $8.89 output for text after text-only input, text after multimodal input, and text plus audio.

## Strengths
- Very low text price for an omni model.

## Limitations
- No longer listed for sale on Model Studio.
- Only 2,048 output tokens.

## Good for
- Interpreting older omni integrations; Qwen3.5 and Qwen3.8 Omni replace it.
