---
id: google/gemma-4-e2b-it
name: Gemma 4 E2B
owned_by: google
type: llm
description: Gemma 4 E2B is the smallest Gemma 4 model, an open-weight (Apache-2.0) multimodal model from Google DeepMind with 2.3B effective parameters (5.1B with embeddings) for phones and edge devices.
aliases: [google.gemma-4-e2b, google/gemma-4-E2B-it]
context_length: 128000
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-04-02"
benchmarks:
  intelligence_index: 7.8
  omniscience_index: -23.6
  humanitys_last_exam: 4.8
  gpqa_diamond: 43.3
  terminal_bench_hard: 3
  long_context_reasoning: 16.3
  ifbench: 38
  tau2_bench: 20.8
  mmmu_pro: 44.6
benchmark_variant: Gemma 4 E2B (Reasoning)
sources:
  - https://artificialanalysis.ai/models/gemma-4-e2b
  - https://huggingface.co/google/gemma-4-E2B-it
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Gemma 4 E2B

## Overview
Gemma 4 E2B was released on 2026-04-02 under Apache 2.0. It is not listed on OpenRouter; its id follows OpenRouter's naming of the Hugging Face repo `google/gemma-4-E2B-it`, and pricing and supported_parameters are absent for that reason. LiteLLM lists an Amazon Bedrock id for it (`google.gemma-4-e2b`). Per-Layer Embeddings keep the effective size at 2.3B while the total, with embedding tables, is 5.1B. It has 35 layers, a 512-token sliding window, a 128K context window, a ~150M vision encoder and a ~300M audio encoder, a configurable thinking mode and native function calling.

## Strengths
- Smallest footprint in the Gemma 4 family, aimed at high-end phones and edge devices.
- Text, image and audio input (Artificial Analysis also lists video).
- Artificial Analysis (Gemma 4 E2B, Reasoning variant): Intelligence Index 7.8 (estimated), which it rates above average for open models of its size; IFBench 38%, MMMU Pro 44.6%.

## Limitations
- Low scores on knowledge and hard reasoning: GPQA Diamond 43.3%, Humanity's Last Exam 4.8%, long-context reasoning 16.3%.
- Limited agent reliability: tau2-bench 20.8%, Terminal-Bench Hard 3%.
- No Artificial Analysis speed figures and no OpenRouter pricing.

## Good for
- On-device classification, routing and short answers.
- Speech or image triage on phones and embedded hardware.
- Fully offline features where memory is the main constraint.
