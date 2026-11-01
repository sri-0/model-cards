---
id: qwen/qwen3-tts-12hz-1.7b-voicedesign
name: Qwen3-TTS-12Hz-1.7B-VoiceDesign
owned_by: qwen
type: tts
description: "Qwen3-TTS-12Hz-1.7B-VoiceDesign is the Qwen team's 1.7B Apache-2.0 open-weight text-to-speech model that creates a voice from a natural-language description, with streaming output and ten languages."
aliases: [Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign]
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: true
license: Apache-2.0
release_date: "2026-01-22"
sources:
  - https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign
  - https://huggingface.co/api/models/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign
  - https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice
  - https://github.com/QwenLM/Qwen3-TTS
  - https://arxiv.org/abs/2601.15621
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-TTS-12Hz-1.7B-VoiceDesign

## Overview
Qwen3-TTS-12Hz-1.7B-VoiceDesign was released on 2026-01-22 with the rest of the Qwen3-TTS series (Hugging Face repo created 2026-01-21), with technical report arXiv 2601.15621. OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign. It shares the family design: the Qwen3-TTS-Tokenizer-12Hz codec, a discrete multi-codebook language model without a diffusion transformer, and dual-track streaming with end-to-end latency as low as 97 ms. Instead of preset speakers, `generate_voice_design` takes the target text plus a natural-language `instruct` that describes the voice, such as gender, age, timbre and emotion. It speaks Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish and Italian, and supports streaming and instruction control. Qwen documents a design-then-clone workflow: synthesise a short reference clip with this model, then pass it to a Base model's `create_voice_clone_prompt` to reuse the designed voice consistently across many lines. It runs with the `qwen-tts` package or vLLM-Omni (offline inference only, per the model card).

## Strengths
- Qwen reports InstructTTSEval APS/DSD/RP of 85.2/81.1/65.1 in Chinese and 82.9/82.4/68.4 in English, above Mimo-Audio-7B-Instruct and VoiceSculptor, and above Hume on English DSD and RP.
- Apache 2.0 licence.

## Limitations
- Released in 1.7B only; the 0.6B line has no voice design model.
- Qwen suggests the Base model's clone prompt when one designed voice must stay consistent across many lines.
- Artificial Analysis does not list these weights.

## Good for
- Creating character and brand voices for games, animation or agents without recordings.
- Producing reference clips for voice cloning.
