---
id: z-ai/glm-5.3
name: GLM 5.3
owned_by: z-ai
type: llm
description: GLM-5.3 is Z.ai's open-weight, text-only reasoning model (753B total, 40B active parameters) for software engineering and long-horizon agent tasks, with a 1M-token context window.
aliases: [glm-5.3, zai/glm-5.3, zai-org/GLM-5.3, zai-org/GLM-5.3-BF16]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, parallel_tool_calls, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: GLM-5.3 License
release_date: "2026-08-18"
pricing:
  input: 0.079
  output: 4.8
  cache_read: 0.059
benchmarks:
  intelligence_index: 44.8
  coding_index: 74.8
  agentic_index: 53.1
  omniscience_index: 14.3
  humanitys_last_exam: 42.3
  gpqa_diamond: 91.7
  scicode: 59
  terminal_bench_4: 41.9
  long_context_reasoning: 79.7
  output_tokens_per_second: 66.9
  time_to_first_token_seconds: 3.32
benchmark_variant: GLM-5.3 (Max)
sources:
  - https://openrouter.ai/z-ai/glm-5.3
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-5-3
  - https://docs.z.ai/guides/llm/glm-5.3
  - https://huggingface.co/zai-org/GLM-5.3
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 5.3

## Overview
GLM-5.3 was released in August 2026. Z.ai says it uses the same base model as GLM-5.2, with all gains coming from post-training. It takes text input only and returns text. Z.ai documents a 1M-token context window and 128K max output. Reasoning is always on and cannot be disabled; `reasoning_effort` accepts `low`, `high` and `max` (default `max`). Weights are on Hugging Face as `zai-org/GLM-5.3` under the GLM-5.3 License, and the model README lists SGLang, vLLM and Transformers among supported serving frameworks.

## Strengths
- Artificial Analysis places GLM-5.3 (Max) among the leading models on its Intelligence Index (score 45, against a median of 18 for comparable open-weight models).
- Z.ai reports a 50% gain over GLM-5.2 on its internal Z.ai Code Bench and stronger cybersecurity results (CyberGym, exploitation benchmarks).
- Tool calling, structured output and context caching on the Z.ai API.
- Short time to first token (about 3.3 seconds on the Max variant).

## Limitations
- Text only. No image input.
- Artificial Analysis calls it expensive among open-weight models of its size, slower than average (about 67 tokens per second) and very verbose.
- Very large: self-hosting needs multi-GPU infrastructure for 753B parameters.
- Applications that set `thinking.type: "disabled"` fail; Z.ai says to switch to `enabled` with `low` effort.

## Good for
- Complex coding and terminal-based agent work.
- Long-horizon, multi-step agent tasks over large contexts.
- Security research workflows such as vulnerability discovery.
- Self-hosted deployments that need a strong open-weight model.
