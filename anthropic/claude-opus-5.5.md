---
id: anthropic/claude-opus-5.5
name: Claude Opus 5.5
owned_by: anthropic
type: llm
description: Anthropic's current Opus model, released in September 2026, for long-running agentic coding, analysis and knowledge work.
aliases: [claude-opus-5-5, anthropic.claude-opus-5-5, anthropic/claude-opus-5-5]
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
release_date: "2026-09-22"
knowledge_cutoff: "2026-06"
pricing:
  input: 4
  output: 20
  cache_read: 0.2
  cache_write: 5
benchmarks:
  intelligence_index: 57.6
  omniscience_index: 46.4
  humanitys_last_exam: 61.4
  scicode: 66.9
  terminal_bench_4: 59.6
  long_context_reasoning: 84.7
  mmmu_pro: 87.7
  output_tokens_per_second: 95.1
  time_to_first_token_seconds: 683.9
benchmark_variant: Claude Opus 5.5 (Max, Default Fallback)
sources:
  - https://openrouter.ai/anthropic/claude-opus-5.5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-opus-5-5
  - https://platform.claude.com/docs/en/models/opus-5-5/overview
retrieved: "2026-10-14"
---

# Claude Opus 5.5

## Overview
Claude Opus 5.5 is the current model in Anthropic's Opus line and succeeds Claude Opus 5. Anthropic positions it for long-running agentic coding and knowledge work. It accepts text and image input, returns text, and has a 1M-token context window with up to 128K output tokens (300K on the Batch API with a beta header). Anthropic lists it as Active (latest), with retirement not sooner than September 22, 2027.

## Strengths
- Multi-step changes in large codebases, code review and bug finding, according to OpenRouter's description.
- Financial and scientific analysis, and reading dense charts, diagrams and screenshots.
- Per OpenRouter, it finishes comparable tasks in fewer steps and tokens than Opus 5, and is more careful to state only figures and sources it can back up.
- Artificial Analysis measured the Max variant at an Intelligence Index of 57.6 and about 95 output tokens per second, which it rates faster than average.

## Limitations
- Adaptive thinking is always on and cannot be turned off. Effort is the only depth control. The default effort is medium.
- At max effort, Artificial Analysis recorded a time to first token of about 684 seconds. This figure includes reasoning time before the first visible token.
- Artificial Analysis rates it very verbose: about 260M tokens to run its Intelligence Index, against a median of 85M.
- List price is $4 input and $20 output per million tokens, which Artificial Analysis rates above the median for comparable models.

## Good for
- Long agentic coding sessions and repository-wide changes.
- Analysis of documents, charts and screenshots where the accuracy of figures matters.
- Tasks that need more depth than a Sonnet-class model, with lower effort for latency-sensitive work.
