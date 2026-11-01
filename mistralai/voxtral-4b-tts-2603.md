---
id: mistralai/voxtral-4b-tts-2603
name: Voxtral 4B TTS 2603
owned_by: mistralai
type: tts
description: Voxtral TTS is Mistral AI's 4B-parameter open-weight (CC-BY-NC-4.0) text-to-speech model with zero-shot voice cloning, streaming output and nine languages.
aliases: [mistralai/Voxtral-4B-TTS-2603, voxtral-mini-tts-2603, voxtral-mini-tts-latest, mistral/voxtral-mini-tts-2603, mistral/voxtral-mini-tts-latest]
architecture:
  input_modalities: [text]
  output_modalities: [audio]
open_weights: true
license: CC-BY-NC-4.0
release_date: "2026-03-23"
sources:
  - https://huggingface.co/mistralai/Voxtral-4B-TTS-2603
  - https://huggingface.co/api/models/mistralai/Voxtral-4B-TTS-2603
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/voxtral-tts-26-03
  - https://docs.mistral.ai/studio/audio/overview
  - https://docs.mistral.ai/studio/audio/text_to_speech/speech
  - https://mistral.ai/news/voxtral-tts
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-10-16"
---

# Voxtral 4B TTS 2603

## Overview
Voxtral TTS (version 26.03, API id voxtral-mini-tts-2603, alias voxtral-mini-tts-latest) was announced on 2026-03-23. OpenRouter does not list it; the id follows the Hugging Face repo mistralai/Voxtral-4B-TTS-2603. Built on Ministral 3 3B, it pairs a 3.4B autoregressive decoder with a 390M flow-matching acoustic transformer and a 300M audio codec at 12.5 Hz. It produces 24 kHz audio in WAV, PCM, FLAC, MP3, AAC or Opus for English, French, Spanish, German, Italian, Portuguese, Dutch, Arabic and Hindi, ships 20 preset voices, and clones a voice from a short reference clip without a transcript (two to three seconds per Mistral's docs). Mistral's API serves it on /v1/audio/speech at $16 per million characters. Weights and bundled reference voices are CC BY-NC 4.0, so self-hosting is non-commercial.

## Strengths
- Mistral's human evaluations: preferred over ElevenLabs Flash v2.5 on naturalness, on par with ElevenLabs v3, and chosen in 68.4% of voice-customisation comparisons.
- 70 ms latency and a 0.103 real-time factor at concurrency 1 on one H200 (Mistral, vLLM-Omni 0.18.0).
- Cross-lingual voice transfer and emotion steering (neutral, happy, sarcastic and similar).
- Runs on one GPU with 16 GB or more in BF16.

## Limitations
- Non-commercial licence for the weights; commercial use goes through Mistral's paid API.
- Native generation covers two minutes of audio; Mistral recommends prompts under 300 words.
- Serving needs vllm-omni 0.18.0 and mistral-common 1.10.0 or later; no transformers path is documented.
- API requests can be refused by content moderation (HTTP 403).

## Good for
- Voice agents and call-centre bots that need fast first audio.
- Multilingual narration with one consistent cloned voice.
- Research and internal prototypes where a non-commercial licence is acceptable.
