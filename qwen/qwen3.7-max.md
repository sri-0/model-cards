---
id: qwen/qwen3.7-max
name: Qwen3.7 Max
owned_by: qwen
type: llm
description: "Qwen3.7 Max is Alibaba's text-only hosted flagship of the Qwen3.7 series, built for agent-centric coding, office and long-horizon autonomous work with a 1M-token context, served on Model Studio as qwen3.7-max."
aliases: [qwen3.7-max, qwen3.7-max-2026-05-20, qwen3.7-max-2026-06-08, qwen3.7-max-2026-05-17, qwen3.7-max-preview]
context_length: 1000000
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
release_date: "2026-05-19"
pricing:
  input: 1.475
  output: 4.425
  cache_read: 0.295
  cache_write: 1.84375
benchmarks:
  intelligence_index: 29.5
  coding_index: 66
  agentic_index: 22.5
  omniscience_index: 13.5
  humanitys_last_exam: 40.5
  gpqa_diamond: 92.3
  scicode: 49.5
  terminal_bench_hard: 50.8
  terminal_bench_4: 1.5
  long_context_reasoning: 79
  ifbench: 80.5
  tau2_bench: 94.7
  output_tokens_per_second: 190.8
  time_to_first_token_seconds: 2.29
benchmark_variant: Qwen3.7 Max
sources:
  - https://openrouter.ai/qwen/qwen3.7-max
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-7-max
  - https://www.qwencloud.com/models/qwen3.7-max
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
retrieved: "2026-10-16"
---

# Qwen3.7 Max

## Overview
Qwen3.7 Max is the hosted flagship of Alibaba's Qwen3.7 series, released on 2026-05-19 according to Artificial Analysis, with no published weights. Qwen Cloud describes it as the largest and most capable Qwen3.7 model, designed for the agent-centric era with strengths in programming, office and productivity tasks and long-term autonomous execution, and notes that it currently offers a text-only interface. Alibaba Cloud Model Studio serves several snapshots: `qwen3.7-max-preview` (equivalent to `qwen3.7-max-2026-05-17`, thinking mode only), `qwen3.7-max-2026-05-20` (which the stable `qwen3.7-max` currently resolves to) and `qwen3.7-max-2026-06-08`; the text-generation page files Qwen3.7 Max under legacy models, no longer recommended, with Qwen3.8 Max as the current flagship. OpenRouter lists a 1,000,000-token context, 131,072-token output and text-only input, at $1.475 input, $4.425 output, $0.295 cache read and $1.84375 cache write per million tokens with no long-prompt tier; Qwen Cloud and Model Studio list $2.5 input and $7.5 output, with implicit caching at $0.5 and explicit cache creation at $3.125.

## Strengths
- Artificial Analysis (Qwen3.7 Max): Intelligence Index 29.5, Coding Index 66, Agentic Index 22.5, Omniscience 13.5, GPQA Diamond 92.3%, Humanity's Last Exam 40.5%, IFBench 80.5%, tau2-bench 94.7%, Terminal-Bench Hard 50.8%.
- Fast: 190.8 tokens per second and 2.29 s to first token in AA's test.
- Explicit prompt caching for repeated context, according to OpenRouter.

## Limitations
- Text input only; no image or video.
- Terminal-Bench 4.0 1.5% in AA's test.
- Legacy on Model Studio, with several snapshot ids to choose between.

## Good for
- Text-only coding and office-automation agents with long-horizon execution.
- High-throughput reasoning where output speed matters.
