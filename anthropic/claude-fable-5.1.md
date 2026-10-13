---
id: anthropic/claude-fable-5.1
name: Claude Fable 5.1
owned_by: anthropic
type: llm
description: Anthropic's highest-priced current Claude model, released in September 2026, succeeding Claude Fable 5 for agentic coding and long-running knowledge work.
aliases: [claude-fable-5-1, anthropic.claude-fable-5-1, anthropic/claude-fable-5-1]
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
release_date: "2026-09-01"
knowledge_cutoff: "2026-06"
pricing:
  input: 10
  output: 50
  cache_read: 0.25
  cache_write: 12.5
benchmarks:
  intelligence_index: 53.4
  coding_index: 81.6
  agentic_index: 57.9
  omniscience_index: 43.5
  humanitys_last_exam: 59.1
  gpqa_diamond: 93.7
  scicode: 63.1
  terminal_bench_4: 52
  long_context_reasoning: 85.3
  output_tokens_per_second: 69.6
  time_to_first_token_seconds: 243.75
benchmark_variant: Claude Fable 5.1 (Max, Default Fallback)
sources:
  - https://openrouter.ai/anthropic/claude-fable-5.1
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-fable-5-1
  - https://platform.claude.com/docs/en/models/fable-5-1/overview
retrieved: "2026-10-14"
---

# Claude Fable 5.1

## Overview
Claude Fable 5.1 succeeds Claude Fable 5 in Anthropic's top price tier. OpenRouter says the largest gains over Fable 5 are in agentic coding, long-running agentic workflows and knowledge work. It accepts text and image input, returns text, and has a 1M-token context window with up to 128K output tokens. Anthropic lists it as Active (latest), with retirement not sooner than September 1, 2027.

## Strengths
- Long code refactors, front-end and visual code generation, per OpenRouter.
- Finance and analysis tasks, per OpenRouter.
- Artificial Analysis measured the Max variant at an Intelligence Index of 53.4, a Coding Index of 81.6, an Agentic Index of 57.9 and 93.7% on GPQA Diamond.
- Cache reads cost $0.25 per million tokens.

## Limitations
- List price is $10 input and $50 output per million tokens. Artificial Analysis rates it particularly expensive for its class.
- Artificial Analysis rates it slower than average, at about 70 output tokens per second.
- At max effort, the measured time to first token was about 244 seconds. This includes reasoning time before the first visible token.
- Adaptive thinking is always on. The default effort is high.
- Very verbose at Max: about 190M tokens for the Intelligence Index, against a median of 85M.

## Good for
- Difficult coding and analysis work where output quality matters more than cost or latency.
- Long refactors and front-end code generation.
- Long-running agent workflows that produce finance or analysis deliverables.
