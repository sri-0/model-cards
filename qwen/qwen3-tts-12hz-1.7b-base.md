---
id: qwen/qwen3-tts-12hz-1.7b-base
name: Qwen3-TTS-12Hz-1.7B-Base
owned_by: qwen
type: tts
description: "Qwen3-TTS-12Hz-1.7B-Base is the Qwen team's 1.7B Apache-2.0 open-weight voice-cloning text-to-speech model, which speaks new text in a voice taken from about three seconds of reference audio and serves as the base for fine-tuning."
aliases: [Qwen/Qwen3-TTS-12Hz-1.7B-Base]
architecture:
  input_modalities: [text, audio]
  output_modalities: [speech]
open_weights: true
license: Apache-2.0
release_date: "2026-01-22"
sources:
  - https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base
  - https://huggingface.co/api/models/Qwen/Qwen3-TTS-12Hz-1.7B-Base
  - https://github.com/QwenLM/Qwen3-TTS
  - https://arxiv.org/abs/2601.15621
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-12Hz-1.7B-Base

## Overview
Qwen3-TTS-12Hz-1.7B-Base was released on 2026-01-22 with the rest of the Qwen3-TTS series (Hugging Face repo created 2026-01-21), with technical report arXiv 2601.15621. OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-TTS-12Hz-1.7B-Base. Qwen documents it as directly usable for speech: `generate_voice_clone` takes the text to speak plus a reference clip (`ref_audio`, a path, URL, base64 or array) and its transcript (`ref_text`), and Qwen says three seconds of audio is enough. With `x_vector_only_mode=True` it uses only the speaker embedding and needs no transcript, at some cost to quality, and `create_voice_clone_prompt` builds a reusable prompt for many lines. Qwen also names it the starting point for fine-tuning other Qwen3-TTS models. It speaks Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish and Italian with streaming output, but takes no style instructions. It runs with the `qwen-tts` package or vLLM-Omni (offline inference only, per the model card).

## Strengths
- Qwen reports Seed-TTS zero-shot WER of 0.77 (Chinese) and 1.24 (English), the lowest English figure in its table, ahead of CosyVoice 3 (1.45) and MiniMax-Speech (1.65).
- Multilingual cloning WER of 0.93 in Chinese and 0.93 in English in Qwen's tests, well below the MiniMax and ElevenLabs figures there.
- Apache 2.0 licence.

## Limitations
- No instruction control of emotion or style.
- CosyVoice 3 has a lower Chinese Seed-TTS WER (0.71).
- Embedding-only cloning without a transcript lowers quality, per Qwen.

## Good for
- Self-hosted cloning of a known speaker's voice.
- Fine-tuning a custom Qwen3-TTS voice.
