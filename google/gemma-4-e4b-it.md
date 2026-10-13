---
id: google/gemma-4-e4b-it
name: Gemma 4 E4B
owned_by: google
type: llm
description: Gemma 4 E4B is Google DeepMind's small open-weight (Apache-2.0) multimodal model with 4.5B effective parameters (8B with embeddings), designed for laptops and mobile devices.
aliases: [google/gemma-4-E4B-it]
context_length: 128000
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-04-03"
benchmarks:
  intelligence_index: 8.9
  omniscience_index: -19.7
  humanitys_last_exam: 3.8
  gpqa_diamond: 57.6
  scicode: 24.4
  terminal_bench_hard: 8.3
  terminal_bench_4: 0
  long_context_reasoning: 32
  ifbench: 44.2
  tau2_bench: 20.8
  mmmu_pro: 51.4
  output_tokens_per_second: 27.6
  time_to_first_token_seconds: 1
benchmark_variant: Gemma 4 E4B (Reasoning)
sources:
  - https://artificialanalysis.ai/models/gemma-4-e4b
  - https://huggingface.co/google/gemma-4-E4B-it
retrieved: "2026-10-14"
---

# Gemma 4 E4B

## Overview
Gemma 4 E4B was released on 2026-04-03 under Apache 2.0. It is not listed on OpenRouter; its id follows OpenRouter's naming of the Hugging Face repo `google/gemma-4-E4B-it`, and pricing and supported_parameters are absent for that reason. The "E" means effective parameters: Per-Layer Embeddings give each decoder layer its own small embedding table, so the total with embeddings is 8B while the effective count is 4.5B. It has 42 layers, a 128K context window, a ~150M vision encoder and a ~300M audio encoder, a configurable thinking mode and native function calling.

## Strengths
- Built for on-device use with text, image and audio input (Artificial Analysis also lists video).
- Artificial Analysis (Gemma 4 E4B, Reasoning variant): Intelligence Index 8.9 (estimated), which it rates above average for open models of its size; GPQA Diamond 57.6%, MMMU Pro 51.4%.
- 1 s to first token.

## Limitations
- Artificial Analysis rates it notably slow on the provider it measured: 27.6 output tokens per second.
- Half the context of the larger Gemma 4 models (128K versus 256K).
- Limited on harder work: long-context reasoning 32%, tau2-bench 20.8%, 0% on Terminal-Bench 4.
- No OpenRouter listing, so no provider pricing in this card.

## Good for
- Offline assistants on laptops and phones.
- Speech and image understanding with a small memory footprint.
- Simple tool-calling and classification tasks at the edge.
