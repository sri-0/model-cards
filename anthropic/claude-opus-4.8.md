---
id: anthropic/claude-opus-4.8
name: Claude Opus 4.8
owned_by: anthropic
type: llm
description: Anthropic Opus model released in May 2026 for long-horizon agents and knowledge work, now a legacy model behind Claude Opus 5 and Opus 5.5.
aliases: [claude-opus-4-8, anthropic.claude-opus-4-8, anthropic/claude-opus-4-8]
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
release_date: "2026-05-28"
knowledge_cutoff: "2026-01"
pricing:
  input: 5
  output: 25
  cache_read: 0.5
  cache_write: 6.25
benchmarks:
  intelligence_index: 41.8
  coding_index: 74.3
  agentic_index: 41.9
  omniscience_index: 28.8
  humanitys_last_exam: 48.7
  gpqa_diamond: 92
  scicode: 54.4
  terminal_bench_hard: 58.3
  terminal_bench_4: 21.7
  long_context_reasoning: 77.7
  ifbench: 62.2
  tau2_bench: 94.4
  output_tokens_per_second: 60.4
  time_to_first_token_seconds: 59.81
benchmark_variant: Claude Opus 4.8 (Max)
sources:
  - https://openrouter.ai/anthropic/claude-opus-4.8
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-opus-4-8
  - https://platform.claude.com/docs/en/models/opus-4-8/overview
retrieved: "2026-10-14"
---

# Claude Opus 4.8

## Overview
Claude Opus 4.8 was the most capable generally available Opus model when it was released. OpenRouter describes it as suited to highly autonomous agents, long-horizon agentic work, knowledge work and memory-driven tasks where coherence over long sessions matters. It accepts text, image and file input, returns text, and has a 1M-token context window with up to 128K output tokens (300K on the Batch API with a beta header). Anthropic lists it as Active (legacy), with retirement not sooner than May 28, 2027. Its knowledge cutoff is January 2026.

## Strengths
- Multi-step reasoning, complex coding and end-to-end project orchestration, including large codebases and multi-stage debugging.
- Knowledge work such as drafting documents, building presentations and analysing data, with quality held across very long outputs.
- Artificial Analysis measured the Max variant at an Intelligence Index of 41.8, a Coding Index of 74.3, 94.4% on tau2-bench and 58.3% on Terminal-Bench Hard.

## Limitations
- List price is $5 input and $25 output per million tokens. Artificial Analysis rates it particularly expensive.
- Artificial Analysis rates it slower than average (about 60 output tokens per second) and very verbose at Max. The measured time to first token of about 60 seconds at max effort includes reasoning time.
- Thinking is adaptive. The default effort is high.

## Good for
- Deployments already validated on Opus 4.8.
- Long-running asynchronous agent pipelines.
- Long documents, presentations and data analysis where newer Opus models have not yet been tested.
