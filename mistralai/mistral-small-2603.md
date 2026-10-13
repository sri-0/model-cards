---
id: mistralai/mistral-small-2603
name: Mistral Small 4
owned_by: mistralai
type: llm
description: Mistral Small 4 is an Apache-2.0 open-weight mixture-of-experts model from Mistral AI (119B total, 6.5B active) that unifies instruct, reasoning and coding with image input.
aliases: [mistral-small-2603, mistral/mistral-small-2603, mistralai/Mistral-Small-4-119B-2603]
context_length: 262144
max_output_tokens: 209715
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, reasoning_effort, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Apache-2.0
release_date: "2026-03-16"
pricing:
  input: 0.15
  output: 0.6
  cache_read: 0.015
benchmarks:
  intelligence_index: 11.3
  coding_index: 26.6
  agentic_index: 0.8
  omniscience_index: -30.4
  humanitys_last_exam: 9.9
  gpqa_diamond: 76.9
  scicode: 38.8
  terminal_bench_hard: 17.4
  terminal_bench_4: 0
  long_context_reasoning: 49.7
  ifbench: 48.2
  tau2_bench: 41.2
  mmmu_pro: 56.8
  output_tokens_per_second: 155.5
  time_to_first_token_seconds: 0.81
benchmark_variant: Mistral Small 4 (Reasoning)
sources:
  - https://openrouter.ai/mistralai/mistral-small-2603
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/mistral-small-4
  - https://docs.mistral.ai/getting-started/models
  - https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Mistral Small 4

## Overview
Mistral Small 4 (API id mistral-small-2603) was released in March 2026. It is a mixture-of-experts model with 128 experts (4 active), 119B total and 6.5B activated parameters, a 256K-token context window, and text and image input. It merges three Mistral lines in one model: Instruct, Magistral (reasoning) and Devstral (coding). Reasoning is set per request with reasoning_effort ("none" or "high"). Weights are on Hugging Face (mistralai/Mistral-Small-4-119B-2603), with EAGLE and NVFP4 companion checkpoints.

## Strengths
- Artificial Analysis measured 155.5 output tokens per second and 0.81 s to first token on Mistral Small 4 (Reasoning), and rates it highly concise.
- Low cost on OpenRouter: $0.15 input and $0.60 output per million tokens.
- Mistral reports 40% lower end-to-end completion time and 3x more requests per second than Mistral Small 3.
- Native function calling and JSON output under the Apache-2.0 licence.

## Limitations
- Modest scores on Artificial Analysis (Mistral Small 4 (Reasoning)): Intelligence Index 11.3, Coding Index 26.6, Agentic Index 0.8.
- All 119B parameters must be loaded even though only 6.5B are active per token.
- With reasoning_effort "none" it behaves like Mistral Small 3.2 in style, so complex tasks need "high".

## Good for
- General chat assistants and document parsing or extraction.
- Low-cost coding and research assistants.
- Fine-tuning for specialised tasks under a permissive licence.
- Replacing Mistral Small 3.2 and Magistral Small deployments.
