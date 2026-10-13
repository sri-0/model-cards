---
id: meta/muse-spark-1.3-contributor
name: Muse Spark 1.3 Contributor
owned_by: meta
type: llm
description: Muse Spark 1.3 Contributor is a low-cost tier of Meta's Muse Spark 1.3 multimodal reasoning model whose prompts and outputs may be used to improve Meta's products.
aliases: [muse-spark-1.3-contributor]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, reasoning_effort, repetition_penalty, response_format, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image, video, file]
  output_modalities: [text]
  tokenizer: Other
open_weights: false
license: proprietary
pricing:
  input: 0.1
  output: 0.2
  cache_read: 0.002
sources:
  - https://openrouter.ai/meta/muse-spark-1.3-contributor
  - https://openrouter.ai/api/v1/models
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Muse Spark 1.3 Contributor

## Overview
OpenRouter describes Muse Spark 1.3 Contributor as "the cost-efficient contributor tier" of Meta's multimodal reasoning model, aimed at experimentation, learning, and early-stage agentic, multi-agent and coding workflows. It is served through Meta's API. It takes text, images, video and files, returns text, and OpenRouter lists a 1,048,576-token context window. The defining condition of the tier: prompts and outputs may be used to improve Meta's products.

## Strengths
- Very low price on OpenRouter: $0.10 input, $0.20 output and $0.002 cached input per million tokens, against $1.25 and $4.25 for standard Muse Spark 1.3.
- Same listed features as Muse Spark 1.3 on OpenRouter: tool calling, reasoning with effort control, vision and structured outputs.
- Designed to track information across extended tasks, work through conflicting inputs and ask for clarification or confirmation.

## Limitations
- Prompts and outputs may be used by Meta. Do not send confidential, personal, customer or regulated data.
- No separate Artificial Analysis benchmarks. The sources do not say whether quality matches standard Muse Spark 1.3, so do not assume it does.
- Proprietary and API-only; not usable in a network-isolated deployment.

## Good for
- Prototyping and learning with public or synthetic data.
- Early-stage agent, multi-agent and coding experiments where cost matters more than data control.
- Trying Muse Spark behaviour before moving to the standard tier.
