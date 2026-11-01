---
id: qwen/qwen3-asr-0.6b
name: Qwen3 ASR 0.6B
owned_by: qwen
type: llm
description: "Qwen3-ASR-0.6B is the compact Apache-2.0 open-weight model of the Qwen3-ASR family, identifying and transcribing 30 languages and 22 Chinese dialects in streaming or offline mode, tuned for throughput over peak accuracy."
aliases: [Qwen/Qwen3-ASR-0.6B, Qwen/Qwen3-ASR-0.6B-hf, qwen/qwen3-asr-0.6b-20260813]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2026-01-29"
sources:
  - https://openrouter.ai/qwen/qwen3-asr-0.6b
  - https://openrouter.ai/api/v1/models/qwen/qwen3-asr-0.6b/endpoints
  - https://openrouter.ai/api/v1/models
  - https://huggingface.co/Qwen/Qwen3-ASR-0.6B
  - https://huggingface.co/api/models/Qwen/Qwen3-ASR-0.6B
  - https://huggingface.co/api/models/Qwen/Qwen3-ASR-0.6B-hf
  - https://arxiv.org/abs/2601.21337
  - https://github.com/QwenLM/Qwen3-ASR
  - https://artificialanalysis.ai/speech-to-text/non-streaming
retrieved: "2026-11-01"
---

# Qwen3 ASR 0.6B

## Overview
Qwen3-ASR-0.6B was released on 2026-01-29 (Hugging Face repo created 2026-01-28) alongside Qwen3-ASR-1.7B, with technical report arXiv 2601.21337. OpenRouter lists it as `qwen/qwen3-asr-0.6b` (added 2026-08-13), served by DeepInfra, at $0.000003 per second of audio as shown on its model page. Like the 1.7B model it builds on Qwen3-Omni's audio understanding, identifies the language and transcribes 30 languages and 22 Chinese dialects, handles streaming and offline inference and long audio in one model, and transcribes singing and songs with background music. Qwen positions it as the accuracy-efficiency trade-off, reaching 2,000 times throughput at a concurrency of 128. It loads through the `qwen-asr` package (transformers or vLLM backends), and Qwen/Qwen3-ASR-0.6B-hf is the Transformers-native checkpoint. Qwen3-ForcedAligner-0.6B adds timestamps for up to 5 minutes of speech.

## Strengths
- Qwen's offline WER: LibriSpeech 2.11/4.55 (clean/other), Fleurs-en 4.39, GigaSpeech 8.88, Tedlium 3.85 (better than the 1.7B model's 4.50), WenetSpeech 5.97/6.88 (net/meeting).
- Very high batch throughput for bulk transcription.

## Limitations
- Less accurate than Qwen3-ASR-1.7B on most of Qwen's sets; average WER over LibriSpeech, Fleurs-en and Fleurs-zh is 3.48 offline and 4.40 streaming, against 2.69 and 3.33.
- Artificial Analysis lists it but has published no WER.

## Good for
- High-volume transcription where cost and speed matter.
- Multilingual captioning with Chinese dialects.
