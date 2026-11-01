---
id: qwen/qwen3-tts-flash
name: Qwen3-TTS-Flash
owned_by: qwen
type: tts
description: "Qwen3-TTS-Flash is Alibaba's hosted Qwen3 text-to-speech model on Model Studio with 17 expressive system voices, ten languages and eight Chinese dialects besides Mandarin, billed per character."
aliases: [qwen3-tts-flash-2025-11-27, qwen3-tts-flash-2025-09-18, dashscope/qwen3-tts-flash]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2025-09-16"
sources:
  - https://www.qwencloud.com/models/qwen3-tts-flash
  - https://www.alibabacloud.com/help/en/model-studio/tts-model
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://artificialanalysis.ai/text-to-speech/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-Flash

## Overview
Qwen3-TTS-Flash (Model Studio id `qwen3-tts-flash`) is the hosted, non-real-time member of Model Studio's Qwen3-TTS family; no weights are published. OpenRouter does not list it; the id is the DashScope model id. Model Studio's release table lists the first snapshot, `qwen3-tts-flash-2025-09-18`, from 2025-09-16, and the stable id together with its `qwen3-tts-flash-2025-11-27` snapshot from 2025-11-27; Artificial Analysis dates it 2025-09-22. Qwen Cloud describes it as a low-latency, stable synthesis model with 17 expressive voices that keep their character across languages and adjust tone to the text. System voices speak Chinese (Mandarin and the Beijing, Shanghainese, Sichuan, Nanjing, Shaanxi, Hokkien, Tianjin and Cantonese varieties, depending on voice), English, German, Italian, Portuguese, Spanish, Japanese, Korean, French and Russian. It has no cloned or designed voices; Model Studio serves those through separate Qwen3-TTS voice-clone and voice-design ids, and serves `qwen3-tts-flash-realtime` (qwen/qwen3-tts-flash-realtime, $0.13 per 10,000 characters) separately for real-time use. The Singapore price is $0.10 per 10,000 characters, with output free.

## Strengths
- Low price per character.
- Dialect voices for Beijing, Shanghai, Sichuan, Cantonese and other varieties.

## Limitations
- Artificial Analysis text-to-speech arena: Elo 941, far below Qwen-Audio-3.1-TTS-Plus (1305).
- System voices only.
- Model Studio now recommends the Qwen-Audio-3.1-TTS models.

## Good for
- Low-cost batch narration with preset voices.
- Existing integrations built on qwen3-tts-flash.
