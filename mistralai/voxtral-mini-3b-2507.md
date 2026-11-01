---
id: mistralai/voxtral-mini-3b-2507
name: Voxtral Mini 3B 2507
owned_by: mistralai
type: llm
description: Voxtral Mini is Mistral AI's 4.7B-parameter open-weight (Apache-2.0) audio and text model built on Ministral 3B for transcription, translation and audio understanding, now deprecated on Mistral's API.
aliases: [mistralai/Voxtral-Mini-3B-2507, voxtral-mini-2507, mistral.voxtral-mini-3b-2507]
context_length: 32768
capabilities: [structured_output]
architecture:
  input_modalities: [text, audio]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-07-15"
sources:
  - https://huggingface.co/mistralai/Voxtral-Mini-3B-2507
  - https://huggingface.co/api/models/mistralai/Voxtral-Mini-3B-2507
  - https://huggingface.co/mistralai/Voxtral-Mini-3B-2507/raw/main/config.json
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/voxtral-mini-25-07
  - https://docs.mistral.ai/models/voxtral-mini-transcribe-25-07
  - https://mistral.ai/news/voxtral
  - https://arxiv.org/abs/2507.13264
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-10-16"
---

# Voxtral Mini 3B 2507

## Overview
Voxtral Mini (API id voxtral-mini-2507) was announced on 2025-07-15 with Voxtral Small. OpenRouter does not list it; the id follows the Hugging Face repo mistralai/Voxtral-Mini-3B-2507. Mistral's paper counts 4.7B parameters: a 3.6B language decoder from Ministral 3B, 400M of text embeddings, a 640M audio encoder and a 25M adapter. The model card gives a 32k-token context (the config says 131,072), 30 minutes of audio for transcription or 40 for understanding, and automatic language detection across English, Spanish, French, Portuguese, Hindi, German, Dutch and Italian. Mistral's API served the same id for chat with audio and, as Voxtral Mini Transcribe, on the transcriptions endpoint. Both were deprecated on 2026-02-27 and retired on 2026-05-31 in favour of Voxtral Mini Transcribe 2; the weights remain on Hugging Face.

## Strengths
- Mistral's paper: 3.77% WER on FLEURS English (3.61% in transcription mode) against Whisper large-v3's 4.00%, and 10.22% on Mozilla Common Voice English against 22.91%.
- FLEURS speech translation: 49.7 BLEU en-fr and 49.6 de-en, close to GPT-4o mini Audio.
- Runs in about 9.5 GB of GPU memory in bf16.
- Audio question answering and summarisation without a separate ASR stage; 85.6% on AU Bench.

## Limitations
- Retired from Mistral's API; new integrations should use Voxtral Mini Transcribe 2 or the realtime model.
- No system prompt support, and no function calling documented at this size.
- Weaker than Voxtral Small on understanding: 47.6% on spoken MMLU against 74.3%.
- Needs vLLM 0.10.0 or transformers 4.54.0 or later with mistral-common 1.8.1 or later.

## Good for
- Local or edge transcription of European languages and Hindi.
- Existing self-hosted Voxtral Mini pipelines.
- Low-cost audio summarisation where a 32k context is enough.
