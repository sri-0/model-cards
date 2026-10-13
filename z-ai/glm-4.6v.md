---
id: z-ai/glm-4.6v
name: GLM 4.6V
owned_by: z-ai
type: llm
description: GLM-4.6V is Z.ai's open-weight multimodal model (about 108B total, 12B active parameters) for visual understanding with native function calling, with a 128K-token context window.
aliases: [glm-4.6v, zai-org/GLM-4.6V]
context_length: 131072
max_output_tokens: 32768
capabilities: [tool_calling, reasoning, vision]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [image, text, video]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2025-12-08"
pricing:
  input: 0.3
  output: 0.9
  cache_read: 0.055
benchmarks:
  intelligence_index: 11.2
  omniscience_index: -26.9
  humanitys_last_exam: 9.6
  gpqa_diamond: 71.9
  terminal_bench_hard: 14.4
  long_context_reasoning: 48.7
  ifbench: 30.1
  tau2_bench: 31.6
  mmmu_pro: 48.6
  output_tokens_per_second: 85.8
  time_to_first_token_seconds: 3.22
benchmark_variant: GLM-4.6V (Reasoning)
sources:
  - https://openrouter.ai/z-ai/glm-4.6v
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-4-6v-reasoning
  - https://docs.z.ai/guides/vlm/glm-4.6v
  - https://huggingface.co/zai-org/GLM-4.6V
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 4.6V

## Overview
GLM-4.6V was released in December 2025. It accepts images, video, files and text and returns text, with a 128K-token context window. Z.ai says it is the first GLM-V model with native function calling, linking visual perception to tool execution. OpenRouter describes support for complex page layouts and charts as visual input, interleaved image-text generation and UI reconstruction. Weights are on Hugging Face as `zai-org/GLM-4.6V` under the MIT licence. Z.ai also offers lighter FlashX and Flash tiers of the series.

## Strengths
- Artificial Analysis places GLM-4.6V (Reasoning) among the leading open-weight models of its size (Intelligence Index 11, marked as estimated, against a median of 8).
- Vision input with tool calling in one model.
- Moderate price (0.3 USD input and 0.9 USD output per million tokens on OpenRouter).
- About 86 tokens per second per Artificial Analysis.

## Limitations
- Smaller context window (128K) and max output (32,768 tokens on OpenRouter) than recent text GLM models.
- Weaker agentic and instruction-following scores than text GLM models: Artificial Analysis tau2-bench is 31.6% and IFBench 30.1%.
- Slightly slower than average output per Artificial Analysis.
- Z.ai's newer GLM-5.3-Flash also accepts images and video.

## Good for
- Document, chart and screenshot understanding.
- Visual agents that must call tools based on what they see.
- UI reconstruction from images.
- Self-hosted multimodal deployments of moderate size.
