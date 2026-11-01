---
id: mistralai/voxtral-small-transcribe-3-0
name: Voxtral Small Transcribe 3
owned_by: mistralai
type: llm
description: Voxtral Small Transcribe 3 is Mistral AI's flagship API-only batch speech-to-text model of October 2026, with speaker diarization, segment timestamps and context biasing across 50 languages.
aliases: [voxtral-small-transcribe-3, voxtral-small-transcribe-latest, mistral/voxtral-small-transcribe-3-0, mistral/voxtral-small-transcribe-3]
context_length: 65536
max_output_tokens: 52428
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
  tokenizer: Mistral
open_weights: false
license: proprietary
release_date: "2026-10-20"
sources:
  - https://openrouter.ai/mistralai/voxtral-small-transcribe-3-0
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/voxtral-small-transcribe-3-0
  - https://docs.mistral.ai/studio/audio/overview
  - https://docs.mistral.ai/studio/audio/speech-to-text/overview
  - https://docs.mistral.ai/studio/audio/specs-and-limits/limits
  - https://docs.mistral.ai/studio/audio/specs-and-limits/languages
  - https://docs.mistral.ai/studio/audio/migrate-from-voxtral-2
  - https://docs.mistral.ai/inference/pricing
  - https://docs.mistral.ai/resources/changelogs
  - https://mistral.ai/news/voxtral-3
  - https://artificialanalysis.ai/speech-to-text/non-streaming
  - https://huggingface.co/mistralai
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Voxtral Small Transcribe 3

## Overview
Voxtral Small Transcribe 3 (version 3.0, API id voxtral-small-transcribe-3-0, aliases voxtral-small-transcribe-3 and voxtral-small-transcribe-latest) was released on 2026-10-20 with the Voxtral 3 family and is in Public Preview. OpenRouter lists it under Mistral's API id; there are no public weights. Mistral publishes no parameter count. It is the higher-accuracy offline model on /v1/audio/transcriptions at $0.004 per minute, with the same features as Voxtral Mini Transcribe 3: diarization with segment timestamps, context biasing and 50 languages, including the 24 official EU languages. Mistral's migration guide names it the replacement for voxtral-small-2507 transcription. The model page also lists translation, speech Q&A, summarisation and function calling, but the audio docs say it is transcription-only at launch and send audio chat to voxtral-small-latest. OpenRouter and the limits page give 65,536 tokens shared by the audio and context_bias; the model page says 32k.

## Strengths
- Artificial Analysis measured an AA WER Index of 2.09%, third-lowest on its non-streaming leaderboard behind Fun-Realtime-ASR-preview (1.73%) and MAI-Transcribe-2 (2.04%), at a median speed factor of 62.
- Mistral reports the best cpWER in its diarization chart, 18.4%, ahead of Pyannote Precision 3 (19.0%) and Microsoft AI Transcribe 2 (20.3%), and 4.0-4.1% macro-average WER over 45 FLEURS languages.
- Earnings-22 keyphrase recall rises from 81.4% to 94.6% with context biasing, per Mistral.

## Limitations
- No public weights; Public Preview only.
- Segment timestamps only; word timestamps return a 400 error.
- No translation, Q&A or summarisation through this id at launch.
- Costs more than Mini; Mistral suggests switching only when custom vocabulary does not fix Mini's errors.

## Good for
- The most accurate batch transcription and diarization on Mistral's API.
- Multilingual archives, including low-resource Asian and Indic languages.
- Earnings calls and technical recordings where key terms must be right.
