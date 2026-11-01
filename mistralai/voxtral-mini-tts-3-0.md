---
id: mistralai/voxtral-mini-tts-3-0
name: Voxtral TTS 3
owned_by: mistralai
type: tts
description: Voxtral TTS 3 is Mistral AI's API-only text-to-speech model of October 2026, with preset voices, zero-shot and professional voice cloning, inline emotion and pace tags, and 35 languages.
aliases: [voxtral-mini-tts-3, voxtral-mini-tts-realtime-3-0, voxtral-mini-tts-realtime-3, voxtral-mini-tts-realtime-latest, mistral/voxtral-mini-tts-3-0, mistral/voxtral-mini-tts-3]
context_length: 4096
max_output_tokens: 3276
architecture:
  input_modalities: [text]
  output_modalities: [speech]
  tokenizer: Mistral
open_weights: false
license: proprietary
release_date: "2026-10-20"
sources:
  - https://openrouter.ai/mistralai/voxtral-mini-tts-3-0
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/voxtral-mini-tts-3-0
  - https://docs.mistral.ai/studio/audio/overview
  - https://docs.mistral.ai/studio/audio/text-to-speech/overview
  - https://docs.mistral.ai/studio/audio/specs-and-limits/limits
  - https://docs.mistral.ai/studio/audio/specs-and-limits/languages
  - https://docs.mistral.ai/studio/audio/migrate-from-voxtral-2
  - https://docs.mistral.ai/inference/pricing
  - https://docs.mistral.ai/resources/changelogs
  - https://mistral.ai/news/voxtral-3
  - https://artificialanalysis.ai/text-to-speech/models
  - https://huggingface.co/mistralai
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Voxtral TTS 3

## Overview
Voxtral TTS 3 (version 3.0, API id voxtral-mini-tts-3-0, alias voxtral-mini-tts-3) was released on 2026-10-20 with the Voxtral 3 family and is in Public Preview. OpenRouter lists it under Mistral's API id, with a 4,096-token context; there are no weights. It runs on /v1/audio/speech at $13 per million characters. Its streaming mode, Voxtral TTS Realtime 3 (voxtral-mini-tts-realtime-3-0), shares the model page and is an alias here. It covers 35 languages and more than 50 dialects, with preset voices in 22 of them, zero-shot cloning from an MP3 or WAV clip of a few seconds to a few minutes, and Pro Voice adaptation from 30 minutes of audio. Delivery is steered with 34 emotion tags, slow and fast pace tags, phoneme hints and expressiveness. It outputs MP3, WAV (24 kHz), PCM, FLAC or Opus, about 90 ms to first audio. It replaces Voxtral TTS 26.03 (voxtral-mini-tts-2603), deprecated on 2026-10-31 and retiring on 2027-04-30. Mistral says voxtral-mini-tts-latest moves to this model within a month of general availability, so that alias stays on the 26.03 card for now.

## Strengths
- Artificial Analysis's TTS leaderboard gives it a quality ELO of 1,223, against 1,090 for Voxtral TTS 26.03 and 1,334 for Eleven v4.
- Mistral says it costs less than OpenAI TTS-1, Deepgram, ElevenLabs Flash and Gemini Flash.
- Contextual TTS conditions delivery on earlier conversation audio.

## Limitations
- No weights; Public Preview; style instructions are not available at launch.
- The voice sets the language: 13 of the 35 languages have no preset voice and need a cloned one.
- Unknown emotion or pace tags are ignored without an error.

## Good for
- Voice agent replies matching the tone of a call.
- Branded voices through cloning or Pro Voice.
- Multilingual narration on a budget.
