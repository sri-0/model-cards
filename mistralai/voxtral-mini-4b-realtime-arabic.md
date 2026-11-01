---
id: mistralai/voxtral-mini-4b-realtime-arabic
name: Voxtral Mini 4B Realtime Arabic
owned_by: mistralai
type: llm
description: Voxtral Mini 4B Realtime Arabic is Mistral AI's 4.4B-parameter open-weight (Apache-2.0) streaming speech-to-text model, fine-tuned from Voxtral Mini 4B Realtime for Modern Standard Arabic, Arabic dialects and code-switching.
aliases: [mistralai/Voxtral-Mini-4B-Realtime-Arabic]
context_length: 131072
architecture:
  input_modalities: [audio]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-10-08"
sources:
  - https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-Arabic
  - https://huggingface.co/api/models/mistralai/Voxtral-Mini-4B-Realtime-Arabic
  - https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-Arabic/raw/main/config.json
  - https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602
  - https://docs.mistral.ai/getting-started/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-10-16"
---

# Voxtral Mini 4B Realtime Arabic

## Overview
Voxtral Mini 4B Realtime Arabic appeared on Hugging Face on 2026-10-08 (repository creation date); Mistral has published no announcement and docs.mistral.ai lists no API id. OpenRouter does not list it; the id follows the Hugging Face repo mistralai/Voxtral-Mini-4B-Realtime-Arabic. It fine-tunes Voxtral Mini 4B Realtime 2602 (about 4.4B parameters, BF16), streaming 16 kHz audio with a configurable delay. Language tags cover Modern Standard Arabic and fifteen dialect codes from the Maghreb to the Gulf, with training focused on code-switching. Mistral co-developed it with Morocco's Ministère de la Transition Numérique et de la Réforme Administrative (MTNRA) under the partnership signed in January 2026. The README states an Apache 2.0 licence; the Hugging Face metadata has no licence tag. The config gives a 131,072-token context.

## Strengths
- Mistral reports 8.82% average character error rate across seven Arabic benchmarks at a 480 ms delay, within 0.91 points of its offline Voxtral Transcribe Arabic (7.91%).
- Two new benchmarks, ISMA and Darija in the Wild, built with MTNRA, target real-world dialect audio.
- Code-switching also improved for languages outside the training focus, per Mistral.
- Deploys like the base model: vLLM's /v1/realtime websocket, transformers 5.2.0 or later, or a community ONNX build for WebGPU.

## Limitations
- Arabic only; Mistral points other languages to Voxtral Mini 4B Realtime 2602.
- Per-benchmark scores are published as images with a custom normalisation.
- No Mistral API endpoint, pricing or announcement yet.
- Transcription only, with no translation or audio chat.

## Good for
- Live captioning and voice interfaces for Arabic dialect speakers.
- Call-centre and public-service transcription in Morocco and the wider Arab world.
- Code-switched Arabic conversations that general models mis-transcribe.
