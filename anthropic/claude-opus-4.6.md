---
id: anthropic/claude-opus-4.6
name: Claude Opus 4.6
owned_by: anthropic
type: llm
description: Anthropic Opus model released in February 2026 for coding and long-running professional tasks, now a legacy model.
aliases: [claude-opus-4-6, anthropic.claude-opus-4-6-v1, anthropic/claude-opus-4-6]
context_length: 1000000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, reasoning_effort, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p, verbosity]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: Claude
open_weights: false
license: proprietary
release_date: "2026-02-05"
knowledge_cutoff: "2025-05"
pricing:
  input: 5
  output: 25
  cache_read: 0.5
  cache_write: 6.25
benchmarks:
  intelligence_index: 31.9
  omniscience_index: 13.7
  humanitys_last_exam: 39.9
  gpqa_diamond: 89.6
  terminal_bench_hard: 46.2
  long_context_reasoning: 78
  ifbench: 53.1
  tau2_bench: 92.1
  mmmu_pro: 75.4
  output_tokens_per_second: 42.7
  time_to_first_token_seconds: 23.31
benchmark_variant: Claude Opus 4.6 (Max)
sources:
  - https://openrouter.ai/anthropic/claude-opus-4.6
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-opus-4-6-adaptive
  - https://platform.claude.com/docs/en/models/opus-4-6/overview
retrieved: "2026-10-14"
---

# Claude Opus 4.6

## Overview
Claude Opus 4.6 is an Opus model built, per OpenRouter, for agents that operate across whole workflows rather than single prompts. It accepts text, image and file input, returns text, and has a 1M-token context window with up to 128K output tokens (300K on the Batch API with a beta header). Anthropic lists it as Active (legacy), with retirement not sooner than February 5, 2027. Its reliable knowledge cutoff is May 2025 and its training data cutoff is August 2025.

## Strengths
- Large codebases, complex refactors and multi-step debugging that unfolds over time.
- Problem decomposition and reliability on hard engineering tasks, per OpenRouter.
- Documents, plans and analyses that are close to final in a single pass, with coherence across long outputs.
- Artificial Analysis measured the Max variant at an Intelligence Index of 31.9, 89.6% on GPQA Diamond and 92.1% on tau2-bench.

## Limitations
- Artificial Analysis marks its Intelligence Index value for this model as estimated.
- Thinking is adaptive. Anthropic marks the older extended thinking mode as deprecated on this model. The default effort is high.
- Its knowledge is older than that of later Opus models.
- List price is $5 input and $25 output per million tokens. Artificial Analysis rates it particularly expensive and notably slow, at about 43 output tokens per second.

## Good for
- Technical design, migration planning and end-to-end project execution, as OpenRouter suggests.
- Existing deployments that have been validated on Opus 4.6.
- Long coding sessions where a newer Opus model is not available.
