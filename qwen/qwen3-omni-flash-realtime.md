---
id: qwen/qwen3-omni-flash-realtime
name: Qwen3-Omni-Flash-Realtime
owned_by: qwen
type: llm
description: "Qwen3-Omni-Flash-Realtime is the real-time version of Alibaba hosted Qwen3-Omni-Flash on Model Studio, a Thinker-Talker mixture-of-experts for live voice and video conversation with text and speech output."
aliases: [qwen3-omni-flash-realtime-2025-12-01, qwen3-omni-flash-realtime-2025-09-15]
context_length: 65536
max_output_tokens: 16384
capabilities: [vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2025-09-17"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/realtime
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-Omni-Flash-Realtime

## Overview
Status: Model Studio's current pricing page lists only the `qwen3-omni-flash-realtime-2025-09-15` snapshot; the stable id and the 2025-12-01 snapshot are on the archived 2026-10-07 pricing page but not on 2026-10-13. Qwen3-Omni-Flash-Realtime (Model Studio id `qwen3-omni-flash-realtime`) is the real-time version of Qwen3-Omni-Flash (qwen/qwen3-omni-flash); no weights are published and OpenRouter does not list it, so the id is the DashScope model id. The 2025-09-15 snapshot appeared on 2025-09-17 and the stable id, documented as equivalent to the 2025-12-01 snapshot, on 2025-12-04. Model Studio describes a Thinker-Talker mixture-of-experts that understands text, images, audio and video and generates speech, with text interaction in 119 languages and speech in 20. The archived models page gives a 65,536-token context with 49,152 input and 16,384 output tokens. The 2025-09-15 snapshot costs, per million tokens in Singapore, $0.52 text, $4.57 audio and $0.94 image input, and $1.99, $3.67 or $18.13 output for text after text-only input, text after multimodal input, and text plus audio.

## Strengths
- Live voice and video dialogue with spoken replies.
- Text in 119 languages, per Model Studio.

## Limitations
- Most ids are no longer listed for sale.
- Small 65,536-token context.

## Good for
- Interpreting older real-time voice integrations on Qwen3-Omni-Flash.
