---
id: qwen/qwen3-tts-instruct-flash
name: Qwen3-TTS-Instruct-Flash
owned_by: qwen
type: tts
description: "Qwen3-TTS-Instruct-Flash is a hosted Model Studio Qwen3 text-to-speech model that steers emotion and expression through natural-language instructions, with 25 instruction-adjustable Chinese and English voices."
aliases: [qwen3-tts-instruct-flash-2026-01-26]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2026-02-10"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-Instruct-Flash

## Overview
Status: Model Studio's current pricing page no longer lists qwen3-tts-instruct-flash; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. Qwen3-TTS-Instruct-Flash (Model Studio id `qwen3-tts-instruct-flash`, documented as equivalent to the `qwen3-tts-instruct-flash-2026-01-26` snapshot) appears in Model Studio's release table from 2026-02-10; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes it as a Qwen3-TTS-Flash model whose instruct variant controls the synthesis effect through natural language, giving emotional, context-appropriate speech, with 25 voices that accept instructions in Chinese and English. The archived pricing table lists Chinese (Mandarin), English, Spanish, Russian, Italian, French, Korean, Japanese, German and Portuguese output and up to 600 characters per request. It was priced at $0.115 per 10,000 characters in Singapore, with each Chinese character counted as two.

## Strengths
- Natural-language control of tone and emotion without cloning or design.
- Ten output languages.

## Limitations
- No longer listed for sale on Model Studio.
- 600 characters per request.

## Good for
- Interpreting older integrations that used qwen3-tts-instruct-flash.
