---
id: mistralai/mistral-large-2512
name: Mistral Large 3 2512
owned_by: mistralai
type: llm
description: Mistral Large 3 is an Apache-2.0 open-weight mixture-of-experts model from Mistral AI with 675B total and 41B active parameters and image input.
aliases: [mistral-large-2512, mistral/mistral-large-2512, mistral/mistral-large-3, mistralai/Mistral-Large-3-675B-Instruct-2512]
context_length: 262144
max_output_tokens: 209715
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Apache-2.0
release_date: "2025-12-02"
pricing:
  input: 0.5
  output: 1.5
  cache_read: 0.05
benchmarks:
  intelligence_index: 9.3
  coding_index: 20.1
  agentic_index: 1
  omniscience_index: -39.6
  humanitys_last_exam: 4.2
  gpqa_diamond: 68
  scicode: 36.6
  terminal_bench_hard: 15.9
  terminal_bench_4: 0
  long_context_reasoning: 36
  ifbench: 36.2
  tau2_bench: 24.6
  mmmu_pro: 55.7
  output_tokens_per_second: 73.5
  time_to_first_token_seconds: 1.08
benchmark_variant: Mistral Large 3
sources:
  - https://openrouter.ai/mistralai/mistral-large-2512
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/mistral-large-3
  - https://docs.mistral.ai/getting-started/models
  - https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Mistral Large 3 2512

## Overview
Mistral Large 3 (API id mistral-large-2512) was released in December 2025. It is a granular mixture-of-experts language model with a 2.5B vision encoder, 41B active and 675B total parameters, and a 256K-token context window. It is an instruct model without a reasoning mode. Weights are on Hugging Face (mistralai/Mistral-Large-3-675B-Instruct-2512) in FP8, with NVFP4 and BF16 variants. Mistral states FP8 runs on a single node of B200s or H200s and NVFP4 on a single node of H100s or A100s.

## Strengths
- Permissive Apache-2.0 licence for commercial use and modification.
- Native function calling and JSON output. Mistral targets long-document understanding, assistants and enterprise knowledge work.
- Artificial Analysis rates it faster than average (73.5 output tokens per second, 1.08 s to first token) and fairly concise.

## Limitations
- Mistral notes it is not a dedicated reasoning model and lags vision-first models on multimodal tasks.
- Artificial Analysis Intelligence Index 9.3 (variant: Mistral Large 3), below average for comparable models. Agentic Index is 1.
- Large and complex to deploy on constrained hardware.
- Mistral recommends temperature below 0.1 for production, a small tool set, and images with an aspect ratio near 1:1.

## Good for
- Self-hosted general assistants that need a permissive licence.
- Retrieval-augmented systems and long-document question answering.
- Structured extraction and tool calling without reasoning overhead.
