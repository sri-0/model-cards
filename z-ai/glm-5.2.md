---
id: z-ai/glm-5.2
name: GLM 5.2
owned_by: z-ai
type: llm
description: GLM-5.2 is Z.ai's open-weight, text-only reasoning model (753B total, 40B active parameters) for long-horizon agent work and project-scale coding, with a 1M-token context window.
aliases: [glm-5.2, zai/glm-5.2, zai-org/GLM-5.2, zai-org/GLM-5.2-FP8]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, parallel_tool_calls, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2026-06-16"
pricing:
  input: 0.06
  output: 7
  cache_read: 0.059
benchmarks:
  intelligence_index: 33.7
  coding_index: 68.8
  agentic_index: 38.4
  omniscience_index: 4.4
  humanitys_last_exam: 41.1
  gpqa_diamond: 89.5
  scicode: 51.2
  terminal_bench_hard: 50.8
  terminal_bench_4: 1
  long_context_reasoning: 78.3
  ifbench: 73.3
  tau2_bench: 99.1
  output_tokens_per_second: 83.6
  time_to_first_token_seconds: 2.97
benchmark_variant: GLM-5.2 (Max)
sources:
  - https://openrouter.ai/z-ai/glm-5.2
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-5-2
  - https://docs.z.ai/guides/llm/glm-5.2
  - https://huggingface.co/zai-org/GLM-5.2
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 5.2

## Overview
GLM-5.2 was released in June 2026 and is the base model that GLM-5.3 was later post-trained from. It takes text input and returns text. Z.ai documents a 1M-token context window and 128K max output. The model README describes a new IndexShare attention design that cuts per-token FLOPs by 2.9x at 1M context. On OpenRouter, reasoning efforts `high` and `xhigh` are supported, with `xhigh` mapping to maximum reasoning. Weights are on Hugging Face as `zai-org/GLM-5.2` (with an FP8 build) under the MIT licence.

## Strengths
- Artificial Analysis places GLM-5.2 (Max) among the leading models on its Intelligence Index (score 34, against a median of 18 for comparable open-weight models).
- Faster than average output on the Max variant (about 84 tokens per second) and a short time to first token (about 3 seconds).
- Z.ai positions it for project-level codebase work: keeping module boundaries, API contracts and earlier decisions across long tasks.
- Function calling, structured output, context caching and MCP integration on the Z.ai API.

## Limitations
- Text only.
- Artificial Analysis calls it expensive among open-weight models of its size and somewhat verbose.
- Superseded by GLM-5.3, which shares the same base model.
- Self-hosting requires multi-GPU infrastructure for 753B parameters.

## Good for
- Reading and refactoring whole codebases within one context.
- Long-running, multi-step engineering and automation tasks.
- Self-hosted deployments under a permissive MIT licence.
