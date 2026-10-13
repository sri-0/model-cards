---
id: google/gemma-4-12b-it
name: Gemma 4 12B
owned_by: google
type: llm
description: Gemma 4 12B (Unified) is Google DeepMind's 11.95B-parameter dense open-weight (Apache-2.0) model that takes text, image and audio input without separate encoders.
aliases: [google/gemma-4-12B-it]
context_length: 262144
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-06-03"
benchmarks:
  intelligence_index: 14.2
  omniscience_index: -52.7
  humanitys_last_exam: 15.7
  gpqa_diamond: 75.3
  terminal_bench_hard: 18.2
  long_context_reasoning: 63.7
  ifbench: 73.5
  tau2_bench: 36.3
  mmmu_pro: 69.7
  output_tokens_per_second: 111.6
  time_to_first_token_seconds: 2.49
benchmark_variant: Gemma 4 12B (Reasoning)
sources:
  - https://artificialanalysis.ai/models/gemma-4-12b
  - https://huggingface.co/google/gemma-4-12B-it
retrieved: "2026-10-14"
---

# Gemma 4 12B

## Overview
Gemma 4 12B Unified was released on 2026-06-03 under Apache 2.0. It is not listed on OpenRouter; its id follows OpenRouter's naming of the Hugging Face repo `google/gemma-4-12B-it`, and pricing and supported_parameters are absent for that reason. "Unified" means encoder-free: image patches and audio waveforms are projected straight into the language model's embedding space, so one decoder-only transformer handles every modality. It has 48 layers, a 256K context window, a configurable thinking mode, native function calling and system-role support.

## Strengths
- Text, image and audio input in one model (Artificial Analysis also lists video), aimed at consumer devices and local execution.
- The whole model can be fine-tuned in one pass, according to Google.
- Artificial Analysis (Gemma 4 12B, Reasoning variant): Intelligence Index 14.2 (estimated), IFBench 73.5%, GPQA Diamond 75.3%, MMMU Pro 69.7%, long-context reasoning 63.7%.
- Fast output: 111.6 tokens per second.

## Limitations
- No OpenRouter listing, so this card has no provider pricing or parameter list.
- 2.49 s to first token, slower to start than the larger Gemma 4 models in Artificial Analysis' tests.
- Omniscience index of -52.7; verify factual answers.
- Terminal-Bench Hard 18.2% and tau2-bench 36.3%, so expect limited reliability on long agent tasks.

## Good for
- Local multimodal assistants that need speech or audio input.
- Image and document understanding on a single consumer GPU.
- Fine-tuning projects that want one model for all modalities.
