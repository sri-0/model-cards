---
id: anthropic/claude-fable-5
name: Claude Fable 5
owned_by: anthropic
type: llm
description: Anthropic's previous Fable-tier Claude model, released in June 2026 and now a legacy model succeeded by Claude Fable 5.1.
aliases: [claude-fable-5, anthropic.claude-fable-5]
context_length: 1000000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, reasoning_effort, response_format, stop, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: Claude
open_weights: false
license: proprietary
release_date: "2026-06-09"
knowledge_cutoff: "2026-01"
pricing:
  input: 10
  output: 50
  cache_read: 1
  cache_write: 12.5
benchmarks:
  intelligence_index: 49.6
  coding_index: 76.5
  agentic_index: 50.7
  omniscience_index: 43.3
  humanitys_last_exam: 55.5
  gpqa_diamond: 92.6
  scicode: 61
  terminal_bench_hard: 62.9
  terminal_bench_4: 42.4
  long_context_reasoning: 82.3
  ifbench: 63.5
  tau2_bench: 98.5
  output_tokens_per_second: 66.1
  time_to_first_token_seconds: 129.27
benchmark_variant: Claude Fable 5 (Max, Opus 4.8 Fallback)
sources:
  - https://openrouter.ai/anthropic/claude-fable-5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-fable-5
  - https://platform.claude.com/docs/en/models/fable-5/overview
retrieved: "2026-10-14"
---

# Claude Fable 5

## Overview
Claude Fable 5 is described by OpenRouter as a Mythos-class model from Anthropic, built for autonomous knowledge work and coding. It is aimed at long-running, complex and asynchronous tasks that previously required frequent human check-ins. It accepts text, image and file input, returns text, and has a 1M-token context window with up to 128K output tokens. Anthropic lists it as Active (legacy), with retirement not sooner than June 9, 2027. Claude Fable 5.1 is its successor at the same per-token price.

## Strengths
- End-to-end work that would take a person hours, days or weeks, including ambiguous, highly multi-step problems, per OpenRouter.
- Self-corrects through verification loops on well-scoped tasks, per OpenRouter.
- Artificial Analysis measured its Max configuration (with Opus 4.8 as fallback) at an Intelligence Index of 49.6, a Coding Index of 76.5 and 98.5% on tau2-bench.

## Limitations
- List price is $10 input and $50 output per million tokens, with cache reads at $1. Artificial Analysis rates it particularly expensive.
- Slower than average per Artificial Analysis, at about 66 output tokens per second. The measured time to first token of about 129 seconds at max effort includes reasoning time.
- Adaptive thinking is always on. The default effort is high.
- Knowledge cutoff is January 2026.

## Good for
- Existing deployments that are pinned to Fable 5.
- Long asynchronous agent tasks and multi-step knowledge work.
- New work is better started on Fable 5.1.
