---
id: mistralai/ministral-8b-2512
name: Ministral 3 8B 2512
owned_by: mistralai
type: llm
description: Ministral 3 8B is the mid-sized model in Mistral AI's Ministral 3 family, an Apache-2.0 open-weight model with image input for local and embedded use.
aliases: [ministral-8b-2512, mistral/ministral-8b-2512, mistralai/Ministral-3-8B-Instruct-2512]
context_length: 262144
max_output_tokens: 209715
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
  input: 0.15
  output: 0.15
  cache_read: 0.015
benchmarks:
  intelligence_index: 5.5
  coding_index: 9.7
  agentic_index: 0.6
  omniscience_index: -69
  humanitys_last_exam: 4.3
  gpqa_diamond: 47.1
  scicode: 20.7
  terminal_bench_hard: 4.5
  terminal_bench_4: 0
  long_context_reasoning: 25.7
  ifbench: 29.1
  tau2_bench: 26.6
  mmmu_pro: 46
  output_tokens_per_second: 106.7
  time_to_first_token_seconds: 0.78
benchmark_variant: Ministral 3 8B
sources:
  - https://openrouter.ai/mistralai/ministral-8b-2512
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/ministral-3-8b
  - https://docs.mistral.ai/getting-started/models
  - https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Ministral 3 8B 2512

## Overview
Ministral 3 8B (API id ministral-8b-2512) was released in December 2025. It pairs an 8.4B language model with a 0.4B vision encoder and has a 256K-token context window. Weights are on Hugging Face (mistralai/Ministral-3-8B-Instruct-2512) in FP8 under Apache-2.0. Mistral says it fits in 12GB of VRAM in FP8, less if quantized further.

## Strengths
- Runs within 12GB of VRAM at FP8, per Mistral, under a permissive licence.
- Native function calling, JSON output and image understanding.
- Multilingual, covering dozens of languages.
- Artificial Analysis rates it faster than average: 106.7 output tokens per second and 0.78 s to first token (variant: Ministral 3 8B).
- Low price on OpenRouter: $0.15 per million tokens for input and output.

## Limitations
- Low scores on Artificial Analysis: Intelligence Index 5.5, Coding Index 9.7, Agentic Index 0.6.
- Artificial Analysis rates it somewhat verbose for its class.
- Not a reasoning model in this instruct form. Not suited to complex coding or long agentic runs.
- Mistral recommends temperature below 0.1 for production, a small tool set, and images close to a 1:1 aspect ratio.

## Good for
- Local daily assistants and chat in constrained environments.
- Image and document description.
- Translation and short content generation.
- Narrow agentic tasks and fine-tuning.
