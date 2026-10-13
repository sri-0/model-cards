---
id: z-ai/glm-5
name: GLM 5
owned_by: z-ai
type: llm
description: GLM-5 is Z.ai's open-weight, text-only foundation model (744B total, 40B active parameters) for systems engineering and long-horizon agent tasks, with a 200K-token context window.
aliases: [glm-5, zai/glm-5, zai-org/GLM-5, zai-org/GLM-5-FP8]
context_length: 204800
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2026-02-11"
pricing:
  input: 0.6
  output: 1.92
  cache_read: 0.12
benchmarks:
  intelligence_index: 27.9
  omniscience_index: 0.3
  humanitys_last_exam: 29.3
  gpqa_diamond: 82
  terminal_bench_hard: 43.2
  long_context_reasoning: 75.7
  ifbench: 72.3
  tau2_bench: 98.2
  output_tokens_per_second: 79.8
  time_to_first_token_seconds: 1.51
benchmark_variant: GLM-5 (Reasoning)
sources:
  - https://openrouter.ai/z-ai/glm-5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-5
  - https://docs.z.ai/guides/llm/glm-5
  - https://huggingface.co/zai-org/GLM-5
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 5

## Overview
GLM-5 was released in February 2026. The model README says it scales from GLM-4.5's 355B parameters (32B active) to 744B (40B active), raises pre-training data from 23T to 28.5T tokens, and adds DeepSeek Sparse Attention to lower deployment cost. It takes text input and returns text, with a 200K-token context window and 128K max output per Z.ai. Z.ai's docs list thinking-mode support; the Artificial Analysis figures below are for the reasoning mode. Weights are on Hugging Face as `zai-org/GLM-5` (with an FP8 build) under the MIT licence.

## Strengths
- Artificial Analysis places GLM-5 (Reasoning) among the leading models on its Intelligence Index (score 28, marked as estimated, against a median of 18 for comparable open-weight models).
- Faster than average output (about 80 tokens per second) and a short time to first token (about 1.5 seconds).
- Z.ai compares its real-world coding usability to Claude Opus 4.5.
- Function calling, structured output and context caching on the Z.ai API.

## Limitations
- Text only.
- Artificial Analysis calls it somewhat expensive among open-weight models of its size.
- Superseded by GLM-5.1, GLM-5.2 and GLM-5.3.
- Self-hosting requires multi-GPU infrastructure for 744B parameters.

## Good for
- Agentic coding across front-end, back-end and data tasks.
- Multi-stage agent work that needs planning and self-checking.
- Role-play and long-form script writing, which Z.ai also lists.
- Self-hosted deployments under the MIT licence.
