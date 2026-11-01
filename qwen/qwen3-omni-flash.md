---
id: qwen/qwen3-omni-flash
name: Qwen3-Omni-Flash
owned_by: qwen
type: llm
description: "Qwen3-Omni-Flash is Alibaba's hosted Qwen3 omni-modal hybrid thinking model on Model Studio, a Thinker-Talker mixture-of-experts that takes text with an image, audio or video and returns text or streamed speech; Model Studio now lists it as legacy."
aliases: [qwen3-omni-flash-2025-12-01, qwen3-omni-flash-2025-09-15, qwen3-omni-flash-0915]
context_length: 65536
max_output_tokens: 16384
capabilities: [reasoning, vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2025-09-17"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-omni
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://github.com/QwenLM/Qwen3-Omni
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-Omni-Flash

## Overview
Status: Model Studio's visual understanding page lists "qwen3-omni-flash and its snapshots" among legacy models that are no longer recommended; it is still on the pricing page. Qwen3-Omni-Flash (Model Studio id `qwen3-omni-flash`) is served in China (Beijing) and Singapore with no published weights; OpenRouter does not list it, so the id is the DashScope model id. The first snapshot, `qwen3-omni-flash-2025-09-15` (also `qwen3-omni-flash-0915`), appeared on 2025-09-17; the stable id, listed with the `qwen3-omni-flash-2025-12-01` snapshot on 2025-12-04, is documented as equivalent to that snapshot. Model Studio describes a Thinker-Talker mixture-of-experts that understands text, images, audio and video and generates speech, with text interaction in 119 languages and speech in 20. The Qwen-Omni guide gives 19 speech input and output languages and dialects (11 languages, 8 Chinese dialects) and limits a request to text plus one other modality, up to 20 minutes of audio or 150 seconds of video. Thinking is switched with `enable_thinking`; audio output needs non-thinking mode and streaming. The context is 65,536 tokens with 16,384 output tokens (49,152 input without thinking; 16,384 input and 32,768 reasoning tokens with it). The Qwen3-Omni open-weight README links this API as the hosted Qwen3-Omni-Flash, but Model Studio does not say it shares weights with Qwen3-Omni-30B-A3B. Singapore prices per million tokens: $0.43 text, $3.81 audio and $0.78 image or video input; $1.66 text output for text-only input, $3.06 for multimodal input, and $15.11 for audio output.

## Strengths
- One model for thinking and spoken replies.
- Text input at $0.43 per million tokens, close to Qwen3.5-Omni-Flash ($0.40).

## Limitations
- No web search, and only one non-text modality per request.
- Model Studio rates its audio-video descriptions below Qwen3.5-Omni.

## Good for
- Existing voice and media integrations built on qwen3-omni-flash.
