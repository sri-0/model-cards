---
id: qwen/qwen3-tts-vd-realtime-2026-01-15
name: Qwen3-TTS-VD-Realtime 2026-01-15
owned_by: qwen
type: tts
description: "Qwen3-TTS-VD-Realtime is Alibaba's hosted real-time Qwen3 text-to-speech model for voices created from text descriptions by Model Studio's voice-design service, across ten languages; this card covers its 2026-01-15 and 2025-12-16 snapshots."
aliases: [qwen3-tts-vd-realtime-2025-12-16]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2025-12-12"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-VD-Realtime 2026-01-15

## Overview
Status: Model Studio's current pricing and speech synthesis pages no longer list Qwen3-TTS-VD-Realtime; archived pricing pages show its snapshots on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for them. Qwen3-TTS-VD-Realtime has only dated ids: `qwen3-tts-vd-realtime-2025-12-16` (listed from 2025-12-12) and `qwen3-tts-vd-realtime-2026-01-15` (listed from 2026-01-14), the newer of which is the card id. No weights are published and OpenRouter does not list it. Model Studio describes it as a real-time speech synthesis model for voices designed by the qwen3-voice-design service from a text description, keeping one voice across languages and adapting tone to the text; it supports designed voices only, not the default voices. The pricing page lists Chinese (Mandarin), English, Spanish, Russian, Italian, French, Korean, Japanese, German and Portuguese, while the release table says 11 languages. It was priced at $0.143353 per 10,000 characters in Singapore and China (Beijing), with each Chinese character counted as two.

## Strengths
- Real-time streaming synthesis in a designed voice.
- No reference recording needed.

## Limitations
- No longer listed for sale on Model Studio.
- Designed voices only.
- Artificial Analysis publishes no score under these ids.

## Good for
- Interpreting older real-time integrations built on these snapshots.
