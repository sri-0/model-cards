---
id: meta/muse-spark-1.3
name: Muse Spark 1.3
owned_by: meta
type: llm
description: Muse Spark 1.3 is Meta's proprietary multimodal reasoning model for long-running agentic, multi-agent and coding workflows.
aliases: [muse-spark-1.3]
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
release_date: "2026-09-02"
pricing:
  input: 1.25
  output: 4.25
  cache_read: 0.15
benchmarks:
  intelligence_index: 48.1
  coding_index: 75.8
  agentic_index: 55.5
  omniscience_index: 25
  humanitys_last_exam: 48.7
  gpqa_diamond: 93.5
  scicode: 58.8
  terminal_bench_4: 33.3
  long_context_reasoning: 83
  output_tokens_per_second: 127.3
  time_to_first_token_seconds: 41.68
benchmark_variant: Muse Spark 1.3 (Max)
sources:
  - https://openrouter.ai/meta/muse-spark-1.3
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/muse-spark-1-3
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Muse Spark 1.3

## Overview
Muse Spark is a model line in Meta's Muse family. Version 1.3 was released on 2026-09-02 and is served through Meta's API; the weights are not published. It takes text, images, video and files as input, returns text, and OpenRouter lists a 1,048,576-token context window with up to 943,718 output tokens. Meta's open-weight Muse Glimmer 30B is distilled from Muse Spark.

## Strengths
- Designed to keep track of information across extended tasks, work through conflicting inputs, and ask for clarification or confirmation when needed, with an emphasis on concise execution (OpenRouter description).
- Strong independent scores. Artificial Analysis (Muse Spark 1.3, Max variant): Intelligence Index 48.1, coding index 75.8, agentic index 55.5, GPQA Diamond 93.5%.
- Fast output: 127.3 tokens per second at Max.
- Priced at $1.25 input and $4.25 output per million tokens on OpenRouter, which Artificial Analysis rates as competitive.

## Limitations
- Proprietary and API-only; it cannot be run locally.
- Verbose at Max effort: 170M tokens to run the Intelligence Index against a median of 85M.
- Time to first token at Max is 41.68 s, so lower effort settings suit interactive use better.
- A cheaper Contributor tier exists, but its prompts and outputs may be used by Meta (see `meta/muse-spark-1.3-contributor`).

## Good for
- Coding agents and multi-agent orchestration.
- Long agentic sessions that need a very large context.
- Multimodal analysis of images, video and documents.
