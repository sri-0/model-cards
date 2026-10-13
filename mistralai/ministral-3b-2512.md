---
id: mistralai/ministral-3b-2512
name: Ministral 3 3B 2512
owned_by: mistralai
type: llm
description: Ministral 3 3B is the smallest model in Mistral AI's Ministral 3 family, an Apache-2.0 open-weight model with image input for edge and low-resource devices.
aliases: [ministral-3b-2512, mistral/ministral-3b-2512, mistralai/Ministral-3-3B-Instruct-2512]
context_length: 131072
max_output_tokens: 104857
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Apache-2.0
release_date: "2025-12-02"
pricing:
  input: 0.1
  output: 0.1
  cache_read: 0.01
benchmarks:
  intelligence_index: 4.8
  coding_index: 4.8
  agentic_index: 0.8
  omniscience_index: -64
  humanitys_last_exam: 5.4
  gpqa_diamond: 35.8
  scicode: 15.3
  terminal_bench_hard: 0
  terminal_bench_4: 0
  long_context_reasoning: 17
  ifbench: 26.8
  tau2_bench: 24.9
  mmmu_pro: 38.1
  output_tokens_per_second: 211.3
  time_to_first_token_seconds: 0.64
benchmark_variant: Ministral 3 3B
sources:
  - https://openrouter.ai/mistralai/ministral-3b-2512
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/ministral-3-3b
  - https://docs.mistral.ai/getting-started/models
  - https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Ministral 3 3B 2512

## Overview
Ministral 3 3B (API id ministral-3b-2512) was released in December 2025. It pairs a 3.4B language model with a 0.4B vision encoder. Mistral's model card lists a 256K-token context window, while OpenRouter lists 131,072 tokens for its endpoints. Weights are on Hugging Face (mistralai/Ministral-3-3B-Instruct-2512) in FP8 under Apache-2.0. Mistral says it fits in 8GB of VRAM in FP8, less if quantized further.

## Strengths
- Very fast: Artificial Analysis measured 211.3 output tokens per second and 0.64 s to first token (variant: Ministral 3 3B), and rates it highly concise.
- Small enough for edge devices and embedded systems.
- Native function calling, JSON output and image understanding, with a permissive licence.
- Low price on OpenRouter: $0.10 per million tokens for input and output.

## Limitations
- Low capability on Artificial Analysis: Intelligence Index 4.8, Coding Index 4.8, Agentic Index 0.8.
- Not suited to complex reasoning, coding or multi-step agent work.
- Mistral recommends temperature below 0.1 for production, a small tool set, and images close to a 1:1 aspect ratio.

## Good for
- Image captioning and text classification.
- Real-time translation and data extraction.
- Short content generation on low-resource hardware.
- Fine-tuning for a single narrow task.
