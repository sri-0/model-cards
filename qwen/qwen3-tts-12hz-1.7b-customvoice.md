---
id: qwen/qwen3-tts-12hz-1.7b-customvoice
name: Qwen3-TTS-12Hz-1.7B-CustomVoice
owned_by: qwen
type: tts
description: "Qwen3-TTS-12Hz-1.7B-CustomVoice is the Qwen team's 1.7B Apache-2.0 open-weight text-to-speech model with nine preset voices, natural-language control of timbre, emotion and prosody, streaming output and ten languages."
aliases: [Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: true
license: Apache-2.0
release_date: "2026-01-22"
sources:
  - https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice
  - https://huggingface.co/api/models/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice
  - https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/raw/main/config.json
  - https://github.com/QwenLM/Qwen3-TTS
  - https://arxiv.org/abs/2601.15621
  - https://artificialanalysis.ai/text-to-speech/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-12Hz-1.7B-CustomVoice

## Overview
Qwen3-TTS was released on 2026-01-22 (Hugging Face repo created 2026-01-21) with technical report arXiv 2601.15621. OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice. The family shares the Qwen3-TTS-Tokenizer-12Hz speech codec and a discrete multi-codebook language-model design without a diffusion transformer; its dual-track streaming can, per Qwen, emit the first audio packet after one input character, with end-to-end latency as low as 97 ms. This checkpoint speaks Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish and Italian with nine preset speakers, including Beijing and Sichuan dialect voices, and takes an optional natural-language instruction to steer timbre, emotion and prosody. Sibling repos cover voice design (1.7B-VoiceDesign), three-second voice cloning (1.7B-Base and 0.6B-Base) and a 0.6B-CustomVoice without instruction control. It runs with the `qwen-tts` package or vLLM-Omni, which the model card says supports offline inference only; Model Studio's DashScope real-time API serves hosted Qwen3-TTS.

## Strengths
- Qwen reports InstructTTSEval APS/DSD/RP of 83.0/77.8/61.2 in Chinese and 77.3/77.1/63.7 in English, above GPT-4o-mini-tts.
- Long-form generation WER of 2.36 (Chinese) and 2.81 (English) in Qwen's tests.
- Apache 2.0 licence.

## Limitations
- Gemini Flash and Gemini Pro score higher on InstructTTSEval in Qwen's own table.
- No cloning from reference audio; that needs the Base models.
- Artificial Analysis rates only the hosted Qwen3 TTS APIs, not these weights.

## Good for
- Self-hosted multilingual voice agents and narration with preset voices.
- Style-directed speech without recording reference audio.
