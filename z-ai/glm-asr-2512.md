---
id: z-ai/glm-asr-2512
name: GLM-ASR-2512
owned_by: z-ai
type: llm
description: GLM-ASR-2512 is Z.ai's API-only speech recognition model for Mandarin, Chinese dialects, English and dozens of other languages, with hotword lists and streaming transcription.
aliases: [glm-asr-2512]
architecture:
  input_modalities: [audio]
  output_modalities: [text]
open_weights: false
release_date: "2025-12-10"
sources:
  - https://docs.z.ai/guides/audio/glm-asr-2512
  - https://docs.z.ai/api-reference/audio/audio-transcriptions
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.bigmodel.cn/cn/guide/models/sound-and-video/glm-asr-2512
  - https://docs.bigmodel.cn/cn/update/new-releases
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# GLM-ASR-2512

## Overview
GLM-ASR-2512 is Z.ai's cloud speech recognition model, launched on Zhipu's platform on 2025-12-10. OpenRouter does not list it and there is no Hugging Face repository; the id is Z.ai's API id `glm-asr-2512`, called on `/api/paas/v4/audio/transcriptions` with streaming or non-streaming output. It accepts `.wav` or `.mp3` files up to 25 MB and 30 seconds, an optional `prompt` with earlier transcript text as context (under 8,000 characters recommended) and up to 100 `hotwords` for names and domain terms. Z.ai prices it at $0.03 per million tokens, about $0.0024 per minute of audio. Z.ai does not say whether it is related to the open-weight GLM-ASR-Nano-2512, whose Hugging Face repository was created a day earlier.

## Strengths
- Z.ai reports a character error rate of 0.0717 in its latest competitive evaluation.
- Languages: Mandarin plus Sichuanese, Cantonese, Min Nan and Wu; American and British English; and dozens of others, including French, German, Japanese, Korean, Spanish and Arabic.
- Handles mixed Chinese-English speech, commands, industry terms and colloquial speech, per Z.ai.
- Very low price per minute.

## Limitations
- 30-second limit per request, so longer recordings must be split and stitched with the `prompt` context.
- Weights are not published; self-hosting needs GLM-ASR-Nano-2512 instead.
- No independent benchmark; Artificial Analysis's speech-to-text leaderboard does not list it.

## Good for
- Voice input, meeting minutes and live captions in Chinese and English.
- Call-centre quality checks and medical dictation with custom vocabularies.
