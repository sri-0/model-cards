---
id: qwen/qwen3-livetranslate-flash
name: Qwen3-LiveTranslate-Flash
owned_by: qwen
type: llm
description: "Qwen3-LiveTranslate-Flash is Alibaba hosted audio and video file translation model on Model Studio, translating speech across 18 languages into text, synthesised speech or both, using video frames as context."
aliases: [qwen3-livetranslate-flash-2025-12-01]
capabilities: [vision]
architecture:
  input_modalities: [audio, video]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2025-12-04"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-livetranslate-flash
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-LiveTranslate-Flash

## Overview
Qwen3-LiveTranslate-Flash (Model Studio id `qwen3-livetranslate-flash`, with snapshot `qwen3-livetranslate-flash-2025-12-01`) translates audio and video files and appears in Model Studio's release table from 2025-12-04; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. It covers 18 languages, accepts audio or video and returns translated text, synthesised audio or both through the OpenAI-compatible streaming API, with source and target languages set in `translation_options` (omitting the source enables automatic detection). For video, frames give context, for example telling a medical mask from a masquerade mask. Output speech uses preset voices such as Cherry. Singapore prices per million tokens: $1.577 audio input, $0.631 image input, $1.577 text output and $6.308 audio output.

## Strengths
- Speech-to-speech translation of recorded media in one call.
- Visual context improves word choice.

## Limitations
- File-based only; real-time use needs the LiveTranslate realtime models.
- 18 languages.

## Good for
- Dubbing and subtitling recorded video.
