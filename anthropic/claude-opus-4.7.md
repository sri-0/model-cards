---
id: anthropic/claude-opus-4.7
name: Claude Opus 4.7
owned_by: anthropic
type: llm
description: Anthropic Opus model released in April 2026 for long-running asynchronous agents, now a legacy model.
aliases: [claude-opus-4-7, anthropic.claude-opus-4-7, anthropic/claude-opus-4-7]
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
release_date: "2026-04-16"
knowledge_cutoff: "2026-01"
pricing:
  input: 5
  output: 25
  cache_read: 0.5
  cache_write: 6.25
benchmarks:
  intelligence_index: 40.7
  coding_index: 73.6
  agentic_index: 38.6
  omniscience_index: 27.3
  humanitys_last_exam: 42.3
  gpqa_diamond: 91.4
  terminal_bench_hard: 51.5
  long_context_reasoning: 78.7
  ifbench: 58.6
  tau2_bench: 88.6
  mmmu_pro: 78.8
  output_tokens_per_second: 52.2
  time_to_first_token_seconds: 22.49
benchmark_variant: Claude Opus 4.7 (Max)
sources:
  - https://openrouter.ai/anthropic/claude-opus-4.7
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-opus-4-7
  - https://platform.claude.com/docs/en/models/opus-4-7/overview
retrieved: "2026-10-14"
---

# Claude Opus 4.7

## Overview
Claude Opus 4.7 followed Opus 4.6 and was built for long-running, asynchronous agents. OpenRouter says it is stronger on complex multi-step tasks and more reliable in extended agentic workflows than Opus 4.6. It accepts text, image and file input, returns text, and has a 1M-token context window with up to 128K output tokens (300K on the Batch API with a beta header). Anthropic lists it as Active (legacy), with retirement not sooner than April 16, 2027. Its knowledge cutoff is January 2026.

## Strengths
- Asynchronous agent pipelines where tasks unfold over time: large codebases, multi-stage debugging and end-to-end project orchestration.
- Knowledge work such as drafting documents, building presentations and analysing data.
- Coherence across very long outputs and extended sessions, per OpenRouter.
- Artificial Analysis measured the Max variant at an Intelligence Index of 40.7, a Coding Index of 73.6, 91.4% on GPQA Diamond and 78.8% on MMMU-Pro.

## Limitations
- Artificial Analysis marks its Intelligence Index value for this model as estimated.
- List price is $5 input and $25 output per million tokens. Artificial Analysis rates it particularly expensive and notably slow, at about 52 output tokens per second.
- Thinking is adaptive. The default effort is high.
- OpenRouter publishes a migration guide for users moving from earlier Opus versions, so prompts tuned for older models may need changes.

## Good for
- Existing integrations validated on Opus 4.7.
- Asynchronous coding agents and multi-stage debugging.
- Document and image-heavy analysis where newer Opus models have not yet been tested.
