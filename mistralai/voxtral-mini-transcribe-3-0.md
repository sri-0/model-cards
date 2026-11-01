---
id: mistralai/voxtral-mini-transcribe-3-0
name: Voxtral Mini Transcribe 3
owned_by: mistralai
type: llm
description: Voxtral Mini Transcribe 3 is Mistral AI's API-only 4B batch speech-to-text model of October 2026, with speaker diarization, segment timestamps and context biasing across 50 languages.
aliases: [voxtral-mini-transcribe-3, voxtral-mini-transcribe-latest, mistral/voxtral-mini-transcribe-3-0, mistral/voxtral-mini-transcribe-3]
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
  - https://openrouter.ai/mistralai/voxtral-mini-transcribe-3-0
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/voxtral-mini-transcribe-3-0
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

# Voxtral Mini Transcribe 3

## Overview
Voxtral Mini Transcribe 3 (version 3.0, API id voxtral-mini-transcribe-3-0, aliases voxtral-mini-transcribe-3 and voxtral-mini-transcribe-latest) was released on 2026-10-20 with the Voxtral 3 family and is in Public Preview. OpenRouter lists it under Mistral's API id; Mistral publishes no weights. Mistral's announcement gives it 4B parameters. It transcribes recorded files on /v1/audio/transcriptions at $0.0035 per minute, with speaker diarization, segment timestamps, context biasing from key terms or free-form text, and language detection across 50 languages. OpenRouter and Mistral's limits page give a 65,536-token window shared by the audio and the context_bias list; the model page says 32k. It replaces Voxtral Mini Transcribe 2 (voxtral-mini-2602), deprecated on 2026-10-31 and retiring on 2027-04-30.

## Strengths
- Artificial Analysis measured an AA WER Index of 2.22% (VoxPopuli, Earnings-22 and AgentTalk), against 3.59% for Voxtral Mini Transcribe 2, at a median speed factor of 76.
- Mistral reports 18.6% cpWER on its diarization set (AMI, Switchboard, CallHome, AISHELL-4) against 30.9% for Voxtral Mini Transcribe 2, and 4.5-4.6% macro-average WER over 45 FLEURS languages.
- Mistral's model page says it ranks third on FLEURS multilingual transcription and English diarization, ahead of Gemini 3.5 Transcribe, while staying small enough for resource-constrained deployments.

## Limitations
- No public weights: Mistral's API, or a self-deployment arranged with Mistral.
- Public Preview, not general availability.
- Segment timestamps only; requesting word timestamps returns a 400 error.
- Offline only, with no turn detection; live audio needs Voxtral Mini Transcribe Realtime 3.
- Requests over the context window fail with a 400 error rather than being cut.

## Good for
- Batch transcription of calls, meetings and podcasts with speaker labels.
- Domain vocabulary through context biasing, without fine-tuning.
- Moving voxtral-mini-2602 integrations that do not need word timestamps.
