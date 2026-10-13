---
id: z-ai/glm-4.7
name: GLM 4.7
owned_by: z-ai
type: llm
description: GLM-4.7 is Z.ai's open-weight, text-only model (357B total, 32B active parameters) for agentic coding and multi-step reasoning, with a 200K-token context window.
aliases: [glm-4.7, zai/glm-4.7, zai-org/GLM-4.7, zai-org/GLM-4.7-FP8]
context_length: 204800
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_a, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2025-12-22"
pricing:
  input: 0.6
  output: 2.2
  cache_read: 0.11
benchmarks:
  intelligence_index: 22.2
  coding_index: 45.3
  omniscience_index: -36.4
  humanitys_last_exam: 27.4
  gpqa_diamond: 85.9
  terminal_bench_hard: 31.8
  long_context_reasoning: 71
  ifbench: 67.9
  tau2_bench: 95.9
  output_tokens_per_second: 42.6
  time_to_first_token_seconds: 2.1
benchmark_variant: GLM-4.7 (Reasoning)
sources:
  - https://openrouter.ai/z-ai/glm-4.7
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-4-7
  - https://docs.z.ai/guides/llm/glm-4.7
  - https://huggingface.co/zai-org/GLM-4.7
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 4.7

## Overview
GLM-4.7 was released in December 2025 as the successor to GLM-4.6. It takes text input and returns text, with a 200K-token context window and 128K max output per Z.ai. Z.ai lists multiple thinking modes, and the model README says it "supports thinking before acting" in agent frameworks such as Claude Code, Kilo Code, Cline and Roo Code. Weights are on Hugging Face as `zai-org/GLM-4.7` (with an FP8 build) under the MIT licence. The OpenRouter API lists an expiration date of 2026-12-31 for this model on OpenRouter.

## Strengths
- Artificial Analysis rates GLM-4.7 (Reasoning) above average on its Intelligence Index (score 22, marked as estimated, against a median of 18 for comparable open-weight models).
- Z.ai reports gains over GLM-4.6 on SWE-bench, SWE-bench Multilingual, Terminal Bench 2.0 and Humanity's Last Exam.
- Z.ai highlights cleaner web UI and slide generation, and better tool use.
- Function calling, structured output and context caching on the Z.ai API.

## Limitations
- Text only.
- Artificial Analysis measured it as notably slow (about 43 tokens per second) and somewhat expensive for open-weight models of its size.
- Scheduled to leave OpenRouter after 2026-12-31. Newer GLM-5 models are available.
- Self-hosting needs multi-GPU infrastructure for 357B parameters.

## Good for
- Agentic coding inside tools such as Claude Code or Cline.
- Front-end and UI generation.
- Self-hosted coding assistants under a permissive licence.
