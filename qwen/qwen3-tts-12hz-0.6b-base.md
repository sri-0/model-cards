---
id: qwen/qwen3-tts-12hz-0.6b-base
name: Qwen3-TTS-12Hz-0.6B-Base
owned_by: qwen
type: tts
description: "Qwen3-TTS-12Hz-0.6B-Base is the Qwen team's compact 0.6B Apache-2.0 open-weight voice-cloning text-to-speech model, which speaks new text in a voice taken from about three seconds of reference audio and can be fine-tuned."
aliases: [Qwen/Qwen3-TTS-12Hz-0.6B-Base]
architecture:
  input_modalities: [text, audio]
  output_modalities: [speech]
open_weights: true
license: Apache-2.0
release_date: "2026-01-22"
sources:
  - https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base
  - https://huggingface.co/api/models/Qwen/Qwen3-TTS-12Hz-0.6B-Base
  - https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base
  - https://github.com/QwenLM/Qwen3-TTS
  - https://arxiv.org/abs/2601.15621
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-12Hz-0.6B-Base

## Overview
Qwen3-TTS-12Hz-0.6B-Base was released on 2026-01-22 with the rest of the Qwen3-TTS series (Hugging Face repo created 2026-01-21), with technical report arXiv 2601.15621. OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-TTS-12Hz-0.6B-Base. Its model card says the family was trained on over 5 million hours of speech in 10 languages. Qwen documents it as directly usable for speech: like the 1.7B Base model, `generate_voice_clone` speaks new text in the voice of a reference clip (`ref_audio`) with its transcript (`ref_text`), from as little as three seconds of audio, or from the speaker embedding alone with `x_vector_only_mode=True`. Qwen also lists it as a base for fine-tuning. It speaks Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish and Italian with streaming output and takes no style instructions. It uses the same Qwen3-TTS-Tokenizer-12Hz codec and dual-track streaming design as the larger models and runs with the `qwen-tts` package or vLLM-Omni.

## Strengths
- Qwen reports Seed-TTS zero-shot WER of 0.92 (Chinese) and 1.32 (English), still ahead of CosyVoice 3 (1.45) and MiniMax-Speech (1.65) in English.
- Multilingual cloning WER of 1.15 in Chinese and 0.84 in English in Qwen's tests.
- 0.6B parameters, against 1.7B for the larger Base model.

## Limitations
- Higher Seed-TTS WER than the 1.7B Base (0.77 and 1.24).
- No instruction control of emotion or style.
- Embedding-only cloning without a transcript lowers quality, per Qwen.

## Good for
- Voice cloning where a smaller model is preferred.
- Lightweight fine-tuning experiments.
