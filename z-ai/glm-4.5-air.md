---
id: z-ai/glm-4.5-air
name: GLM 4.5 Air
owned_by: z-ai
type: llm
description: GLM-4.5-Air is Z.ai's compact open-weight mixture-of-experts model (106B total, 12B active parameters) with switchable thinking and non-thinking modes and a 128K-token context window.
aliases: [glm-4.5-air, zai/glm-4.5-air, zai-org/GLM-4.5-Air, zai-org/GLM-4.5-Air-FP8]
context_length: 131072
max_output_tokens: 98304
capabilities: [tool_calling, reasoning]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, seed, stop, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2025-07-28"
knowledge_cutoff: "2024-12"
pricing:
  input: 0.13
  output: 0.85
  cache_read: 0.025
benchmarks:
  intelligence_index: 11.1
  omniscience_index: -61.5
  humanitys_last_exam: 7
  gpqa_diamond: 73.3
  terminal_bench_hard: 20.5
  long_context_reasoning: 46.7
  ifbench: 37.6
  tau2_bench: 46.5
  output_tokens_per_second: 77.6
  time_to_first_token_seconds: 2.37
benchmark_variant: GLM-4.5-Air
sources:
  - https://openrouter.ai/z-ai/glm-4.5-air
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-4-5-air
  - https://huggingface.co/zai-org/GLM-4.5-Air
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 4.5 Air

## Overview
GLM-4.5-Air was released in July 2025 as the lighter sibling of GLM-4.5 (355B total, 32B active). It takes text input and returns text. It is a hybrid reasoning model: thinking mode for complex reasoning and tool use, and non-thinking mode for fast replies, controlled with a `reasoning` `enabled` boolean on OpenRouter. Weights, including an FP8 build and base models, are on Hugging Face as `zai-org/GLM-4.5-Air` under the MIT licence, which allows commercial use. OpenRouter lists a knowledge cutoff of December 2024.

## Strengths
- Artificial Analysis places GLM-4.5-Air among the leading open-weight models of its size (Intelligence Index 11, marked as estimated, against a median of 8).
- Only 12B active parameters, so serving cost is low for its quality.
- Tool calling, with tool and reasoning parsers in Transformers, vLLM and SGLang.
- Low price on OpenRouter (0.13 USD input and 0.85 USD output per million tokens).

## Limitations
- Text only. No structured-output support listed on OpenRouter.
- Low Artificial Analysis Omniscience Index (-61.5) and Humanity's Last Exam score (7%), so factual recall and hard reasoning are limited.
- Slower than average output (about 78 tokens per second) per Artificial Analysis.
- Older generation, superseded by GLM-4.6 and later models.

## Good for
- Self-hosted agents on a few GPUs.
- Workloads that switch between quick replies and deeper reasoning.
- Commercial deployments needing a permissive licence.
