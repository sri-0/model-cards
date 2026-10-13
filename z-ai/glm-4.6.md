---
id: z-ai/glm-4.6
name: GLM 4.6
owned_by: z-ai
type: llm
description: GLM-4.6 is Z.ai's open-weight, text-only model (357B total, 32B active parameters) for coding, reasoning and agent work, with a 200K-token context window.
aliases: [glm-4.6, zai/glm-4.6, zai-org/GLM-4.6, zai-org/GLM-4.6-FP8]
context_length: 204800
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2025-09-30"
knowledge_cutoff: "2025-03"
pricing:
  input: 0.5
  output: 2
  cache_read: 0.1
benchmarks:
  intelligence_index: 18.5
  coding_index: 45.8
  omniscience_index: -41.9
  humanitys_last_exam: 14.5
  gpqa_diamond: 78
  terminal_bench_hard: 25
  long_context_reasoning: 54
  ifbench: 43.4
  tau2_bench: 70.5
  output_tokens_per_second: 35.1
  time_to_first_token_seconds: 3.1
benchmark_variant: GLM-4.6 (Reasoning)
sources:
  - https://openrouter.ai/z-ai/glm-4.6
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-4-6-reasoning
  - https://docs.z.ai/guides/llm/glm-4.6
  - https://huggingface.co/zai-org/GLM-4.6
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 4.6

## Overview
GLM-4.6 was released in September 2025 as the successor to GLM-4.5. It takes text input and returns text. Z.ai expanded the context window from 128K to 200K tokens and reports better coding, reasoning, tool use during inference, search agents and writing. Weights are on Hugging Face as `zai-org/GLM-4.6` (with an FP8 build) under the MIT licence. OpenRouter lists a knowledge cutoff of March 2025. The Artificial Analysis figures below are for the reasoning mode.

## Strengths
- Artificial Analysis rates GLM-4.6 (Reasoning) slightly above average on its Intelligence Index (score 19, marked as estimated, against a median of 18 for comparable open-weight models).
- Z.ai reports better real-world coding in Claude Code, Cline, Roo Code and Kilo Code, including front-end page generation.
- Tool calling and structured output.
- Permissive MIT licence and widely supported by open-source serving stacks.

## Limitations
- Text only.
- Artificial Analysis measured it as notably slow (about 35 tokens per second) and somewhat expensive for open-weight models of its size.
- Low Artificial Analysis Omniscience Index (-41.9), so expect weak factual recall without retrieval.
- Superseded by GLM-4.7 and the GLM-5 series.
- Self-hosting needs multi-GPU infrastructure for 357B parameters.

## Good for
- Self-hosted coding agents where an established, MIT-licensed model is preferred.
- Tool-using and search-based agents.
- Writing and role-play tasks, which Z.ai also lists.
