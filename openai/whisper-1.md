---
id: openai/whisper-1
name: Whisper 1
owned_by: openai
type: llm
description: whisper-1 is OpenAI's deprecated speech-to-text API model, powered by the open-source Whisper large-v2 checkpoint, offering transcription, translation to English, subtitles and word timestamps until it shuts down on 2027-02-26.
aliases: [whisper-1, azure/whisper-1, openai/whisper-large-v2]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
  tokenizer: GPT
open_weights: true
license: Apache-2.0
release_date: "2022-12-08"
sources:
  - https://developers.openai.com/api/docs/models/whisper-1
  - https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions/methods/create
  - https://developers.openai.com/api/docs/guides/speech-to-text
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/blog/updates-audio-models
  - https://huggingface.co/openai/whisper-large-v2
  - https://huggingface.co/api/models/openai/whisper-large-v2
  - https://huggingface.co/openai/whisper-large-v2/raw/main/config.json
  - https://artificialanalysis.ai/speech-to-text
  - https://artificialanalysis.ai/speech-to-text/models/whisper
  - https://openrouter.ai/openai/whisper-1
  - https://openrouter.ai/api/v1/models?output_modalities=transcription
  - https://openrouter.ai/api/v1/models/openai/whisper-1/endpoints
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Whisper 1

## Overview
whisper-1 is OpenAI's API id for Whisper. OpenAI's transcription reference says it is powered by its open-source Whisper V2 model, published on Hugging Face as openai/whisper-large-v2 (1,550M parameters, 80 mel bins, Apache-2.0), so this card is separate from Whisper large-v3 and large-v3-turbo. Artificial Analysis lists it as Whisper Large v2 served by OpenAI and dates that model to 2022-12-08. OpenRouter lists it on its transcription API as openai/whisper-1. It serves /v1/audio/transcriptions and /v1/audio/translations (English output only), takes files up to 25 MB in mp3, mp4, mpeg, mpga, m4a, wav or webm, and covers 98 languages with uneven accuracy. OpenAI charges $0.006 per minute; OpenRouter's model page gives $0.0001 per second, billed to the nearest second. OpenAI deprecated it on 2026-08-26; it and the translations endpoint shut down on 2027-02-26, replaced by gpt-transcribe or gpt-live-transcribe, and by gpt-realtime-translate for translation.

## Strengths
- Artificial Analysis AA-WER v2 (read 2026-11-01): 4.1% on OpenAI's API, with 3.2% on AA-AgentTalk, 2.8% on VoxPopuli-Cleaned-AA and 7.0% on Earnings22-Cleaned-AA, at $6.00 per 1,000 minutes.
- The large-v2 Hugging Face card reports 3.0% WER on LibriSpeech test-clean.
- The only OpenAI model that accepts timestamp_granularities (word or segment timestamps in verbose_json); also returns text, srt and vtt.
- Speech translation into English.

## Limitations
- Deprecated; shuts down on 2027-02-26.
- No streaming, and prompts are capped at 224 tokens.
- Median speed factor of 28.5 on Artificial Analysis, the slowest of OpenAI's transcription models there (36.6 to 45.7 for the others).
- OpenAI reports about 90% fewer hallucinations on noisy audio for gpt-4o-mini-transcribe-2025-12-15 than for Whisper v2.
- Default limits: 3 RPM and 200 RPD on the free tier, 2,500 RPM at Build.

## Good for
- Subtitles and word-level timestamps until February 2027.
- Translating recorded speech into English text.
- Self-hosting the same checkpoint from openai/whisper-large-v2.
