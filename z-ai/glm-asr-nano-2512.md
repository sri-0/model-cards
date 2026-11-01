---
id: z-ai/glm-asr-nano-2512
name: GLM-ASR-Nano-2512
owned_by: z-ai
type: llm
description: GLM-ASR-Nano-2512 is Z.ai's 1.5B open-weight (MIT) speech recognition model, tuned for Chinese dialects such as Cantonese and for very quiet speech, which Z.ai says beats OpenAI Whisper V3 on several benchmarks.
aliases: [zai-org/GLM-ASR-Nano-2512]
architecture:
  input_modalities: [audio, text]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-12-09"
sources:
  - https://huggingface.co/zai-org/GLM-ASR-Nano-2512
  - https://huggingface.co/api/models/zai-org/GLM-ASR-Nano-2512
  - https://huggingface.co/zai-org/GLM-ASR-Nano-2512/raw/main/config.json
  - https://github.com/zai-org/GLM-ASR
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# GLM-ASR-Nano-2512

## Overview
GLM-ASR-Nano-2512 is Z.ai's open-source speech recognition model with 1.5B parameters. Its Hugging Face repository was created on 2025-12-09, and no separate release date is stated. It is an audio-language model: the request carries an audio clip plus a text instruction such as "Please transcribe this audio into text", and it returns the transcript. Weights load in transformers 5 (installed from source) and can be served through SGLang's OpenAI-compatible chat endpoint; Z.ai notes that the weight format changed for that support, so copies downloaded before 2025-12-27 must be refreshed. OpenRouter does not list it; the id follows the Hugging Face repo `zai-org/GLM-ASR-Nano-2512` under the z-ai prefix. Weights are MIT-licensed.

## Strengths
- Z.ai reports the lowest average error rate (4.10) among comparable open-source models, with clear gains on Chinese benchmarks such as Wenet Meeting and AISHELL-1.
- Optimised for Cantonese and other dialects as well as Mandarin and English.
- Trained for whispered or very low-volume speech that other models often miss.
- Z.ai lists 17 languages with word error rates of 20% or less.

## Limitations
- Per-benchmark results are published only as an image, so individual scores cannot be quoted.
- SGLang needs its development Docker image, and vLLM support is promised but not yet documented.
- Z.ai's documentation does not link it to the paid `glm-asr-2512` API, which is documented as a separate model.

## Good for
- Self-hosted Chinese and Cantonese transcription.
- Noisy meetings and quiet or whispered speech.
- Small-footprint speech recognition on local hardware.
