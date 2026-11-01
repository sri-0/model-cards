---
id: qwen/qwen3-tts-vc-realtime-2026-01-15
name: Qwen3-TTS-VC-Realtime 2026-01-15
owned_by: qwen
type: tts
description: "Qwen3-TTS-VC-Realtime is Alibaba's hosted real-time Qwen3 text-to-speech model for voices cloned through Model Studio's voice-enrollment service, across ten languages; this card covers its 2026-01-15 and 2025-11-27 snapshots."
aliases: [qwen3-tts-vc-realtime-2025-11-27]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2025-11-27"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://artificialanalysis.ai/text-to-speech/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-VC-Realtime 2026-01-15

## Overview
Status: Model Studio's current pricing and speech synthesis pages no longer list Qwen3-TTS-VC-Realtime; archived pricing pages show its snapshots on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for them. Qwen3-TTS-VC-Realtime has only dated ids: `qwen3-tts-vc-realtime-2025-11-27` (released 2025-11-27) and `qwen3-tts-vc-realtime-2026-01-15` (released 2026-01-14), the newer of which is the card id. No weights are published and OpenRouter does not list it. Model Studio describes it as a Qwen3-TTS-Flash real-time speech synthesis model for voices replicated by the voice-enrollment service, keeping the same timbre across languages and adapting tone to the text; it supports cloned voices only, not the default voices. The pricing page lists Chinese (Mandarin), English, Spanish, Russian, Italian, French, Korean, Japanese, German and Portuguese, while the release table says 11 languages. It was priced at $0.13 per 10,000 characters in Singapore and $0.143353 in China (Beijing), with each Chinese character counted as two.

## Strengths
- Real-time streaming synthesis in a cloned voice.
- Artificial Analysis lists it (as Qwen3 TTS, Qwen3-TTS-VC-Realtime) on Alibaba Cloud and DeepInfra.

## Limitations
- AA text-to-speech arena Elo 929, near the bottom of its list and far below Qwen-Audio-3.1-TTS-Plus (1305).
- No longer listed for sale on Model Studio; cloned voices only.

## Good for
- Interpreting older real-time integrations built on these snapshots.
