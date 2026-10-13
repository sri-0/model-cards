---
id: mistralai/ministral-14b-2512
name: Ministral 3 14B 2512
owned_by: mistralai
type: llm
description: Ministral 3 14B is the largest model in Mistral AI's Ministral 3 family, an Apache-2.0 open-weight 14B model with image input built for local and edge deployment.
aliases: [ministral-14b-2512, mistral/ministral-14b-2512, mistralai/Ministral-3-14B-Instruct-2512]
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
  input: 0.2
  output: 0.2
  cache_read: 0.02
benchmarks:
  intelligence_index: 6
  coding_index: 14.4
  agentic_index: 1.1
  omniscience_index: -66.4
  humanitys_last_exam: 4.6
  gpqa_diamond: 57.2
  scicode: 23.8
  terminal_bench_hard: 4.5
  terminal_bench_4: 0
  long_context_reasoning: 26.3
  ifbench: 32
  tau2_bench: 27.2
  mmmu_pro: 49.8
  output_tokens_per_second: 56.1
  time_to_first_token_seconds: 1.08
benchmark_variant: Ministral 3 14B
sources:
  - https://openrouter.ai/mistralai/ministral-14b-2512
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/ministral-3-14b
  - https://docs.mistral.ai/getting-started/models
  - https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Ministral 3 14B 2512

## Overview
Ministral 3 14B (API id ministral-14b-2512) was released in December 2025. It combines a 13.5B language model with a 0.4B vision encoder and has a 256K-token context window. Weights are on Hugging Face (mistralai/Ministral-3-14B-Instruct-2512) in FP8 under Apache-2.0. Mistral says it fits in 24GB of VRAM in FP8, less if quantized further, and performs comparably to Mistral Small 3.2 24B.

## Strengths
- Runs locally within 24GB of VRAM at FP8, per Mistral.
- Native function calling and JSON output, plus image understanding.
- Supports dozens of languages, including English, French, German, Chinese, Japanese, Korean and Arabic.
- Low price on OpenRouter: $0.20 per million tokens for both input and output.

## Limitations
- Low scores on Artificial Analysis (variant: Ministral 3 14B): Intelligence Index 6, Coding Index 14.4, Agentic Index 1.1.
- Artificial Analysis rates it slower than average on the measured provider: 56.1 output tokens per second, 1.08 s to first token.
- Not a reasoning model in this instruct form.
- Mistral recommends temperature below 0.1 for production, a small tool set, and images close to a 1:1 aspect ratio.

## Good for
- Private chat assistants in constrained or offline environments.
- Local agentic use with a limited tool set.
- Fine-tuning and specialisation on modest hardware.
- Image and document description at low cost.
