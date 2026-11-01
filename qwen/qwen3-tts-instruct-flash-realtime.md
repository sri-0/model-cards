---
id: qwen/qwen3-tts-instruct-flash-realtime
name: Qwen3-TTS-Instruct-Flash-Realtime
owned_by: qwen
type: tts
description: "Qwen3-TTS-Instruct-Flash-Realtime is the real-time version of Model Studio Qwen3 instruction-controlled text-to-speech, steering emotion and expression through natural language with its default voices only."
aliases: [qwen3-tts-instruct-flash-realtime-2026-01-22]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2026-01-21"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-Instruct-Flash-Realtime

## Overview
Status: Model Studio's current pricing page no longer lists qwen3-tts-instruct-flash-realtime; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. Qwen3-TTS-Instruct-Flash-Realtime (Model Studio id `qwen3-tts-instruct-flash-realtime`, documented as equivalent to the `qwen3-tts-instruct-flash-realtime-2026-01-22` snapshot) appears in Model Studio's release table from 2026-01-21; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes it as a real-time Qwen3-TTS-Flash model whose instruct variant controls the synthesis effect through natural language, with 25 voices that accept instructions in Chinese and English. Qwen real-time synthesis takes streaming text and returns streaming audio. It uses the default voices only, not cloned or designed voices. The archived pricing table lists Chinese (Mandarin), English, Spanish, Russian, Italian, French, Korean, Japanese, German and Portuguese output at $0.143 per 10,000 characters in Singapore, with each Chinese character counted as two.

## Strengths
- Instruction-controlled delivery in a streaming session.
- Ten output languages.

## Limitations
- No longer listed for sale on Model Studio.
- Default voices only.

## Good for
- Interpreting older real-time integrations that used this id.
