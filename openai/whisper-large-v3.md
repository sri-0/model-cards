---
id: openai/whisper-large-v3
name: Whisper Large V3
owned_by: openai
type: llm
description: Whisper large-v3 is OpenAI's 1.55B-parameter open-weight (Apache-2.0) speech recognition and speech-to-English translation model, released in November 2023 and trained on 5M hours of weakly and pseudo-labelled audio.
aliases: [whisper-large-v3, groq/whisper-large-v3, scaleway/openai/whisper-large-v3]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
  tokenizer: GPT
open_weights: true
license: Apache-2.0
release_date: "2023-11-06"
sources:
  - https://huggingface.co/openai/whisper-large-v3
  - https://huggingface.co/api/models/openai/whisper-large-v3
  - https://huggingface.co/openai/whisper-large-v3/raw/main/config.json
  - https://artificialanalysis.ai/speech-to-text
  - https://artificialanalysis.ai/speech-to-text/models/whisper
  - https://openrouter.ai/openai/whisper-large-v3
  - https://openrouter.ai/api/v1/models?output_modalities=transcription
  - https://openrouter.ai/api/v1/models/openai/whisper-large-v3/endpoints
  - https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions/methods/create
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Whisper Large V3

## Overview
Whisper large-v3 is the third large Whisper checkpoint. Artificial Analysis dates it to 2023-11-06; the Hugging Face repo openai/whisper-large-v3 was created on 2023-11-07 under Apache-2.0. OpenAI's own API does not serve it (whisper-1 is large-v2). OpenRouter lists it on its transcription API as openai/whisper-large-v3, routed to DeepInfra, Together and Groq; its model page gives $0.000008 per second. It keeps the large-v2 encoder-decoder design (32 encoder and 32 decoder layers, 1,550M parameters) but uses 128 mel bins instead of 80 and adds a Cantonese language token. Training used 1M hours of weakly labelled audio and 4M hours pseudo-labelled by large-v2, for 2 epochs. It transcribes in the source language or translates into English, detects the language, and returns sentence or word timestamps in transformers.

## Strengths
- The Hugging Face card reports 10% to 20% fewer errors than large-v2 across a wide range of languages.
- Artificial Analysis AA-WER v2 (read 2026-11-01): 4.1% on fal.ai (3.4% AA-AgentTalk, 2.4% VoxPopuli-Cleaned-AA, 7.0% Earnings22-Cleaned-AA) and 4.5% on Together AI at a 299.6 speed factor.
- Runs locally in transformers; torch.compile gives up to 4.5x speed-ups.

## Limitations
- A 30-second receptive field: longer audio needs sequential or chunked long-form decoding, and chunking costs up to 0.5% WER.
- Hosting matters: Artificial Analysis measures 10.1% on Replicate's build (29.2% on Earnings22) and 5.7% for Incredibly Fast Whisper.
- Can output words that were not spoken and repeat itself, more so in low-resource languages; accuracy varies by language, accent and speaker group.
- No speaker diarization, and not real-time out of the box.

## Good for
- Self-hosted multilingual transcription under a permissive licence.
- Batch subtitling with timestamps.
- Translating speech into English text.
