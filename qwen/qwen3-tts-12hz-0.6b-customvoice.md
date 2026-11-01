---
id: qwen/qwen3-tts-12hz-0.6b-customvoice
name: Qwen3-TTS-12Hz-0.6B-CustomVoice
owned_by: qwen
type: tts
description: "Qwen3-TTS-12Hz-0.6B-CustomVoice is the Qwen team's compact 0.6B Apache-2.0 open-weight text-to-speech model with nine preset voices, streaming output and ten languages, without the 1.7B model's instruction control."
aliases: [Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: true
license: Apache-2.0
release_date: "2026-01-22"
sources:
  - https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice
  - https://huggingface.co/api/models/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice
  - https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice
  - https://github.com/QwenLM/Qwen3-TTS
  - https://arxiv.org/abs/2601.15621
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-12Hz-0.6B-CustomVoice

## Overview
Qwen3-TTS-12Hz-0.6B-CustomVoice was released on 2026-01-22 with the rest of the Qwen3-TTS series (Hugging Face repo created 2026-01-21), with technical report arXiv 2601.15621. OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice. It is the smaller counterpart of Qwen3-TTS-12Hz-1.7B-CustomVoice (qwen/qwen3-tts-12hz-1.7b-customvoice), with the same nine preset speakers: Vivian, Serena and Uncle_Fu (Chinese), Dylan (Beijing dialect), Eric (Sichuan dialect), Ryan and Aiden (English), Ono_Anna (Japanese) and Sohee (Korean). Each speaker can speak any of the ten supported languages (Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish and Italian), though Qwen recommends each speaker's native language. Qwen's model table marks streaming but not instruction control for this size. It uses the Qwen3-TTS-Tokenizer-12Hz codec and dual-track streaming design, calls `generate_custom_voice` with a speaker and language, and runs with the `qwen-tts` package or vLLM-Omni.

## Strengths
- Qwen reports target-speaker WER of 0.94 in Chinese and 1.19 in English, below GPT-4o-Audio Preview (3.52 and 2.20).
- 0.6B parameters, against 1.7B for the larger CustomVoice model.
- Apache 2.0 licence.

## Limitations
- No instruction control of tone, emotion or prosody.
- Slightly higher WER than the 1.7B model (0.90 and 0.90).
- No voice cloning or voice design.

## Good for
- Lightweight self-hosted narration and voice agents with preset voices.
- Deployments where instruction control is not needed.
