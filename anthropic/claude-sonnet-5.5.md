---
id: anthropic/claude-sonnet-5.5
name: Claude Sonnet 5.5
owned_by: anthropic
type: llm
description: Anthropic's current Sonnet model, released in September 2026, for everyday coding, agent and document work at a lower price than Opus.
aliases: [claude-sonnet-5-5, anthropic.claude-sonnet-5-5, anthropic/claude-sonnet-5-5]
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
release_date: "2026-09-28"
knowledge_cutoff: "2026-06"
pricing:
  input: 2
  output: 10
  cache_read: 0.1
  cache_write: 2.5
benchmarks:
  intelligence_index: 56
  omniscience_index: 32.3
  humanitys_last_exam: 55
  scicode: 61
  terminal_bench_4: 63.6
  long_context_reasoning: 82.7
  output_tokens_per_second: 135.5
  time_to_first_token_seconds: 441.68
benchmark_variant: Claude Sonnet 5.5 (Max, Default Fallback)
sources:
  - https://openrouter.ai/anthropic/claude-sonnet-5.5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-sonnet-5-5
  - https://platform.claude.com/docs/en/models/sonnet-5-5/overview
retrieved: "2026-10-14"
---

# Claude Sonnet 5.5

## Overview
Claude Sonnet 5.5 succeeds Claude Sonnet 5 as a direct upgrade in the Sonnet line. OpenRouter describes it as a model for well-scoped everyday work. It accepts text and image input, returns text, and has a 1M-token context window with up to 128K output tokens (300K on the Batch API with a beta header). Anthropic lists it as Active (latest), with retirement not sooner than September 28, 2027.

## Strengths
- Building features, fixing bugs, and producing documents, slides and spreadsheets, per OpenRouter.
- Writes and communicates more clearly than Sonnet 5, per OpenRouter.
- Artificial Analysis measured the Max variant at an Intelligence Index of 56.0 and about 135 output tokens per second, which it rates notably fast.
- List price is $2 input and $10 output per million tokens, with cache reads at $0.10.

## Limitations
- Adaptive thinking is on by default and the default effort is high. The lowest thinking setting is between_tools, which turns off up-front thinking and works only at high effort or below.
- Setting temperature, top_p or top_k to a non-default value returns a 400 error.
- Artificial Analysis rates it very verbose at Max: about 420M tokens for its Intelligence Index, against a median of 85M.
- At max effort, Artificial Analysis recorded a time to first token of about 442 seconds, which includes reasoning time before the first visible token.

## Good for
- Everyday coding agents: feature work, bug fixing and code changes of moderate scope.
- Producing documents, slides and spreadsheets.
- Agent loops that need to stay responsive, run at lower effort settings.
