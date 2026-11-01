---
id: mistralai/voxtral-mini-4b-realtime-2602
name: Voxtral Mini 4B Realtime 2602
owned_by: mistralai
type: llm
description: Voxtral Mini 4B Realtime is Mistral AI's 4.4B-parameter open-weight (Apache-2.0) streaming speech-to-text model, served on Mistral's API as Voxtral Mini Transcribe Realtime.
aliases: [mistralai/Voxtral-Mini-4B-Realtime-2602, voxtral-mini-transcribe-realtime-2602, voxtral-mini-realtime-latest, mistral/voxtral-mini-transcribe-realtime-2602, mistral/voxtral-mini-transcribe-realtime-latest, mistral/voxtral-mini-realtime-2602, mistral/voxtral-mini-realtime-latest]
context_length: 131072
architecture:
  input_modalities: [audio]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-02-04"
sources:
  - https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602
  - https://huggingface.co/api/models/mistralai/Voxtral-Mini-4B-Realtime-2602
  - https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602/raw/main/config.json
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/voxtral-mini-transcribe-realtime-26-02
  - https://docs.mistral.ai/studio/audio/speech_to_text/realtime_transcription
  - https://mistral.ai/news/voxtral-transcribe-2
  - https://arxiv.org/abs/2602.11298
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-10-16"
---

# Voxtral Mini 4B Realtime 2602

## Overview
Voxtral Mini 4B Realtime was announced on 2026-02-04 in the Voxtral Transcribe 2 release. OpenRouter does not list it; the id follows the Hugging Face repo mistralai/Voxtral-Mini-4B-Realtime-2602, past 2,000,000 downloads when read. Mistral's API serves it as Voxtral Mini Transcribe Realtime (voxtral-mini-transcribe-realtime-2602) over a websocket at wss://api.mistral.ai/v1/audio/transcriptions/realtime for $0.006 per minute. A 970M causal audio encoder feeds a 3.4B decoder fine-tuned from Ministral 3 3B, 4.4B parameters in total, both with sliding-window attention for unbounded streaming. The transcription delay is configurable from 80 ms to 2.4 s; Mistral recommends 480 ms. The config's 131,072-token context is about three hours of audio at one token per 80 ms. It covers 13 languages: English, Chinese, Hindi, Spanish, Arabic, French, Portuguese, Russian, German, Japanese, Korean, Italian and Dutch.

## Strengths
- Mistral's model card reports 8.72% average WER on FLEURS at 480 ms delay (6.73% at 2.4 s), against 5.90% for the offline Voxtral Mini Transcribe 2.
- The technical report gives 7.70% on FLEURS at 960 ms, ahead of Whisper (8.23%) and Scribe v2 Realtime (8.34%).
- Runs on one GPU with 16 GB or more in BF16; ExecuTorch, MLX, Rust and C community ports exist.
- Supported in vLLM's realtime endpoint (/v1/realtime) and transformers 5.2.0 or later.

## Limitations
- Transcription only: no translation, audio question answering or chat.
- Accuracy drops as delay shrinks: 12.60% FLEURS WER at 160 ms.
- Arabic (22.53%) and Korean (15.74%) are the weakest languages at 480 ms.
- Mistral's realtime API does not support speaker diarization.

## Good for
- Live captions, meeting transcription and voice assistants that need sub-second text.
- On-device or private transcription on one 16 GB GPU.
- Streaming front ends where a batch model is too slow.
