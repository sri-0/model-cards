---
id: qwen/qwen3-omni-30b-a3b-instruct
name: Qwen3 Omni 30B A3B Instruct
owned_by: qwen
type: llm
description: Qwen3 Omni 30B A3B Instruct is Qwen's September 2025 open-weight (Apache-2.0) end-to-end omni-modal mixture-of-experts model that takes text, images, audio and video and answers in streaming text and natural speech.
aliases: [Qwen/Qwen3-Omni-30B-A3B-Instruct]
context_length: 65536
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text, audio]
open_weights: true
license: Apache-2.0
release_date: "2025-09-22"
benchmarks:
  gpqa_diamond: 62.0
  humanitys_last_exam: 4.6
  ifbench: 31.2
  long_context_reasoning: 0
  mmmu_pro: 55.5
  output_tokens_per_second: 95.6
  tau2_bench: 16.4
  terminal_bench_hard: 1.5
  time_to_first_token_seconds: 1.84
benchmark_variant: Qwen3 Omni 30B A3B Instruct
sources:
  - https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen3-Omni-30B-A3B-Instruct
  - https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-omni-30b-a3b-instruct
  - https://github.com/QwenLM/Qwen3-Omni
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 Omni 30B A3B Instruct

## Overview
Qwen3-Omni-30B-A3B-Instruct is the Instruct model of Qwen3-Omni, released on 2025-09-22 according to the Qwen3-Omni GitHub README (Artificial Analysis agrees; the Hugging Face repo was created 2025-09-20). OpenRouter does not list it; the id follows the Hugging Face repo. It is natively end-to-end: a mixture-of-experts Thinker reads text, images, audio and video, and a Talker streams speech with low latency. config.json gives the Thinker a 48-layer text model with 128 experts (8 active) and 65,536 positions, the context Artificial Analysis also lists; Hugging Face counts 35.3B parameters across all components. It handles 119 text languages, 19 speech input languages and 10 speech output languages, with three voices (Ethan, Chelsie and Aiden). In BF16 with transformers, Qwen gives a minimum of 78.85 GB of GPU memory for a 15-second video, and disable_talker() saves about 10 GB when speech is not needed. vLLM serving covers only the Thinker. Ollama does not list it.

## Strengths
- Qwen reports state of the art on 22 of 36 audio and audio-visual benchmarks and the best open-source result on 32.
- Qwen reports LibriSpeech clean/other WER 1.22/2.48, VoiceBench overall 85.5, MMMU 69.1, MathVista 75.9 and WorldSense 54.0.
- Artificial Analysis (Qwen3 Omni 30B A3B Instruct): GPQA Diamond 62%, MMMU-Pro 55.5%, 95.6 output tokens per second and 1.84 s to first token.
- Function calling from spoken requests, per Qwen's cookbook.

## Limitations
- Artificial Analysis long-context reasoning 0%, Terminal-Bench Hard 1.5%, tau2-bench 16.4% and Humanity's Last Exam 4.6%.
- Qwen's text table puts it below Qwen3-30B-A3B-Instruct-2507 on every benchmark except AIME25 (65.0 against 61.3).
- No reasoning mode; the Thinking release reasons but cannot speak.
- No published knowledge cutoff.

## Good for
- Voice assistants that listen and answer in speech.
- Speech recognition, speech translation and audio analysis in one model.
- Question answering over short videos with sound.
