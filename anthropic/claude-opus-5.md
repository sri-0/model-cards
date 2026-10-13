---
id: anthropic/claude-opus-5
name: Claude Opus 5
owned_by: anthropic
type: llm
description: Anthropic's previous Opus model, released in July 2026 and now a legacy model succeeded by Claude Opus 5.5.
aliases: [claude-opus-5, anthropic.claude-opus-5]
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
release_date: "2026-07-24"
knowledge_cutoff: "2026-05"
pricing:
  input: 5
  output: 25
  cache_read: 0.5
  cache_write: 6.25
benchmarks:
  intelligence_index: 50.8
  coding_index: 78
  agentic_index: 56.5
  omniscience_index: 37.1
  humanitys_last_exam: 54.9
  gpqa_diamond: 93.2
  scicode: 56.4
  terminal_bench_4: 49
  long_context_reasoning: 79.3
  mmmu_pro: 84.7
  output_tokens_per_second: 56.3
  time_to_first_token_seconds: 85.14
benchmark_variant: Claude Opus 5 (Max)
sources:
  - https://openrouter.ai/anthropic/claude-opus-5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-opus-5
  - https://platform.claude.com/docs/en/models/opus-5/overview
retrieved: "2026-10-14"
---

# Claude Opus 5

## Overview
Claude Opus 5 was Anthropic's flagship Opus model for demanding reasoning, coding and long-horizon agentic work until Claude Opus 5.5 replaced it. It accepts text and image input, returns text, and has a 1M-token context window with up to 128K output tokens (300K on the Batch API with a beta header). Anthropic lists it as Active (legacy), with retirement not sooner than July 24, 2027. Its knowledge cutoff is May 2026.

## Strengths
- End-to-end software tasks, code review and bug finding, per OpenRouter.
- Visual analysis of charts and documents, and complex office deliverables.
- Coordinating parallel subagents, with steady instruction following and tool use over long tasks.
- Stays effective at lower effort settings when latency and token use matter, per OpenRouter.
- Artificial Analysis measured the Max variant at an Intelligence Index of 50.8, a Coding Index of 78.0 and an Agentic Index of 56.5.

## Limitations
- List price is $5 input and $25 output per million tokens, higher than Opus 5.5. Artificial Analysis rates it particularly expensive.
- Artificial Analysis rates it notably slow (about 56 output tokens per second) and very verbose at Max. The measured time to first token of about 85 seconds at max effort includes reasoning time.
- Adaptive thinking is on by default. The default effort is high.

## Good for
- Workloads already tuned and validated on Opus 5.
- Agent systems that coordinate parallel subagents.
- Chart, document and office-deliverable work. New work is better started on Opus 5.5.
