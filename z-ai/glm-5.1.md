---
id: z-ai/glm-5.1
name: GLM 5.1
owned_by: z-ai
type: llm
description: GLM-5.1 is Z.ai's open-weight, text-only reasoning model (744B total, 40B active parameters) built for long-horizon agentic coding, with a 200K-token context window.
aliases: [glm-5.1, zai/glm-5.1, zai-org/GLM-5.1, zai-org/GLM-5.1-FP8]
context_length: 204800
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2026-04-07"
pricing:
  input: 0.966
  output: 3.036
  cache_read: 0.1794
benchmarks:
  intelligence_index: 26.1
  coding_index: 55.8
  agentic_index: 23.9
  omniscience_index: 0.8
  humanitys_last_exam: 30.1
  gpqa_diamond: 86.8
  scicode: 44.8
  terminal_bench_hard: 43.2
  terminal_bench_4: 2
  long_context_reasoning: 73.7
  ifbench: 76.3
  tau2_bench: 97.7
  output_tokens_per_second: 62.5
  time_to_first_token_seconds: 1.71
benchmark_variant: GLM-5.1 (Reasoning)
sources:
  - https://openrouter.ai/z-ai/glm-5.1
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-5-1
  - https://docs.z.ai/guides/llm/glm-5.1
  - https://huggingface.co/zai-org/GLM-5.1
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 5.1

## Overview
GLM-5.1 was released in April 2026. It takes text input and returns text, with a 200K-token context window and 128K max output per Z.ai. Z.ai says it can work on a single task for up to 8 hours, planning, executing and revising its approach, and that its general and coding performance is overall aligned with Claude Opus 4.6. Z.ai's docs list thinking-mode support; the Artificial Analysis figures below are for the reasoning mode. Weights are on Hugging Face as `zai-org/GLM-5.1` (with an FP8 build) under the MIT licence.

## Strengths
- Artificial Analysis places GLM-5.1 (Reasoning) among the leading models on its Intelligence Index (score 26, against a median of 18 for comparable open-weight models).
- Z.ai reports gains over GLM-5 on SWE-Bench Pro, NL2Repo and Terminal-Bench 2.0, and better persistence on long tasks.
- Tuned for agentic coding harnesses such as Claude Code, per Z.ai.
- Function calling, structured output, context caching and MCP on the Z.ai API.

## Limitations
- Text only.
- Context window is 200K tokens, smaller than GLM-5.2 and GLM-5.3.
- Artificial Analysis calls it expensive among open-weight models of its size and slower than average (about 62 tokens per second).
- Superseded by GLM-5.2 and GLM-5.3.

## Good for
- Long-running autonomous coding agents.
- Complex engineering optimisation tasks with many dependent steps.
- General assistance, multi-turn chat and creative writing, which Z.ai also lists.
- Self-hosted use under the MIT licence.
