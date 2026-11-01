---
id: qwen/qwen3-asr-1.7b
name: Qwen3 ASR 1.7B
owned_by: qwen
type: llm
description: "Qwen3-ASR-1.7B is the Qwen team's Apache-2.0 open-weight speech recognition model built on Qwen3-Omni, identifying and transcribing 30 languages and 22 Chinese dialects in streaming or offline mode, including singing and songs with background music."
aliases: [Qwen/Qwen3-ASR-1.7B, Qwen/Qwen3-ASR-1.7B-hf, qwen/qwen3-asr-1.7b-20260813]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2026-01-29"
sources:
  - https://openrouter.ai/qwen/qwen3-asr-1.7b
  - https://openrouter.ai/api/v1/models/qwen/qwen3-asr-1.7b/endpoints
  - https://openrouter.ai/api/v1/models
  - https://huggingface.co/Qwen/Qwen3-ASR-1.7B
  - https://huggingface.co/api/models/Qwen/Qwen3-ASR-1.7B
  - https://huggingface.co/Qwen/Qwen3-ASR-1.7B-hf
  - https://arxiv.org/abs/2601.21337
  - https://github.com/QwenLM/Qwen3-ASR
  - https://artificialanalysis.ai/speech-to-text/non-streaming
  - https://www.alibabacloud.com/help/en/model-studio/qwen-speech-recognition
retrieved: "2026-11-01"
---

# Qwen3 ASR 1.7B

## Overview
Qwen3-ASR-1.7B was released on 2026-01-29 (Hugging Face repo created 2026-01-28) with technical report arXiv 2601.21337. OpenRouter lists it as `qwen/qwen3-asr-1.7b` (added 2026-08-13), served by DeepInfra, at $0.000008 per second of audio as shown on its model page. Built on the audio understanding of Qwen3-Omni, it identifies the language and transcribes 30 languages and 22 Chinese dialects, plus regional English accents, with one model for streaming and offline inference and for long audio. It also transcribes singing and songs with background music. Qwen3-ForcedAligner-0.6B adds timestamps for up to 5 minutes of speech in 11 languages. The `qwen-asr` package has transformers and vLLM backends, vLLM also serves an OpenAI-compatible transcription API, and Qwen/Qwen3-ASR-1.7B-hf is the Transformers-native checkpoint (transformers 5.13.0 or later). Qwen points to the DashScope API for hosted use; Model Studio's synchronous Qwen3-ASR-Flash takes up to 5 minutes or 10 MB of audio per request.

## Strengths
- Qwen's offline WER: LibriSpeech 1.63/3.38 (clean/other), Fleurs-en 3.35, GigaSpeech 8.45, CommonVoice-en 7.39, ahead of Whisper-large-v3 except on LibriSpeech clean.
- Artificial Analysis lists Qwen3 ASR Flash as a 1.7B open-weight model with an AA-WER of 4.1% (AA-STT 3.1%, VoxPopuli 4.0%, Earnings-22 6.2%); the leader scores 1.7% across 62 models.
- Streaming costs little: average WER over LibriSpeech, Fleurs-en and Fleurs-zh is 2.69 offline and 3.33 streaming.

## Limitations
- AA's separate Qwen3 ASR 1.7B entry has no WER yet.
- GPT-4o-Transcribe is ahead on Fleurs-en (2.40) and LibriSpeech clean (1.39) in Qwen's table.
- Timestamps need the separate aligner model.

## Good for
- Self-hosted multilingual and Chinese-dialect transcription.
- Lyrics and noisy media transcription.
