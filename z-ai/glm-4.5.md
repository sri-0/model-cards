---
id: z-ai/glm-4.5
name: GLM 4.5
owned_by: z-ai
type: llm
description: GLM-4.5 is Z.ai's July 2025 open-weight (MIT) flagship, a 355B-total, 32B-active mixture-of-experts model for agents and coding with switchable thinking and a 128K-token context.
aliases: [glm-4.5, glm-4.5-x, zai/glm-4.5, zai/glm-4.5-x, zai-org/GLM-4.5, zai-org/GLM-4.5-FP8]
context_length: 131072
max_output_tokens: 98304
capabilities: [tool_calling, reasoning]
supported_parameters: [include_reasoning, max_tokens, reasoning, response_format, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2025-07-28"
knowledge_cutoff: "2024-12"
pricing:
  input: 0.6
  output: 2.2
  cache_read: 0.11
benchmarks:
  gpqa_diamond: 78.2
  humanitys_last_exam: 13.0
  ifbench: 44.1
  long_context_reasoning: 52.7
  tau2_bench: 43.0
  terminal_bench_hard: 22.0
benchmark_variant: GLM-4.5 (Reasoning)
sources:
  - https://openrouter.ai/z-ai/glm-4.5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-4-5
  - https://huggingface.co/zai-org/GLM-4.5
  - https://huggingface.co/api/models/zai-org/GLM-4.5
  - https://huggingface.co/zai-org/GLM-4.5/raw/main/config.json
  - https://docs.z.ai/guides/llm/glm-4.5
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.bigmodel.cn/cn/guide/models/text/glm-4.5
  - https://docs.bigmodel.cn/cn/update/new-releases
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GLM 4.5

## Overview
GLM-4.5 launched on 2025-07-28 alongside the smaller GLM-4.5-Air. Z.ai describes a mixture-of-experts model with 355B total and 32B active parameters (160 routed experts, 8 per token), pre-trained on 15T tokens and then tuned for code, reasoning and agents. It is a hybrid reasoning model: `thinking.type` switches between thinking and instant replies, with dynamic thinking on by default. Z.ai documents a 128K context and 96K maximum output, text only. Weights, an FP8 build and a base model are on Hugging Face under MIT. `glm-4.5-x` is Z.ai's high-speed tier ($2.2 input and $8.9 output per million tokens), which Z.ai says exceeds 100 tokens per second. Zhipu's China platform says GLM-4.5 and GLM-4.5-X will soon be retired in favour of GLM-4.7, and OpenRouter lists an expiration date of 2026-12-31.

## Strengths
- Z.ai reports an average of 63.2 across 12 benchmarks, third among the models it compared at launch.
- Built for agents: function calling, structured output and context caching on Z.ai's API, with tool and reasoning parsers in vLLM and SGLang.
- Z.ai released its 52-task Claude Code evaluation trajectories (CC-Bench) for reproduction.

## Limitations
- Artificial Analysis marks it deprecated, succeeded by GLM-4.6; on GLM-4.5 (Reasoning) it measured 13% on Humanity's Last Exam and 43% on tau2-bench.
- Text only.
- Self-hosting needs 8 H100s in FP8, or 16 for the full 128K context, per Z.ai.

## Good for
- Existing GLM-4.5 integrations, including Claude Code-style coding agents, until retirement.
- Self-hosted agent workloads that need a permissive licence.
