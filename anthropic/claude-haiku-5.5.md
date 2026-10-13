---
id: anthropic/claude-haiku-5.5
name: Claude Haiku 5.5
owned_by: anthropic
type: llm
description: Anthropic's smallest and fastest current Claude model, released in October 2026, for high-volume, latency-sensitive work.
aliases: [claude-haiku-5-5, anthropic.claude-haiku-5-5, anthropic/claude-haiku-5-5]
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
release_date: "2026-10-07"
knowledge_cutoff: "2026-06"
pricing:
  input: 0.1
  output: 0.5
  cache_read: 0.01
  cache_write: 0.125
benchmarks:
  intelligence_index: 43.4
  omniscience_index: 10.7
  humanitys_last_exam: 44.4
  scicode: 55
  terminal_bench_4: 32.8
  long_context_reasoning: 82.7
  output_tokens_per_second: 236.4
  time_to_first_token_seconds: 314.69
benchmark_variant: Claude Haiku 5.5 (Max)
sources:
  - https://openrouter.ai/anthropic/claude-haiku-5.5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-haiku-5-5
  - https://platform.claude.com/docs/en/models/haiku-5-5/overview
retrieved: "2026-10-14"
---

# Claude Haiku 5.5

## Overview
Claude Haiku 5.5 succeeds Claude Haiku 4.5. Anthropic positions it for classification, extraction, routing and subagent tasks, and OpenRouter adds summarization and browser use. It accepts text and image input, returns text, and has a 1M-token context window with up to 128K output tokens. It is the first Haiku model with adjustable effort. Anthropic lists it as Active (latest), with retirement not sooner than October 7, 2027.

## Strengths
- Stronger coding, computer use and knowledge work than Haiku 4.5, per OpenRouter.
- Low price: $0.10 input and $0.50 output per million tokens for prompts up to 100,000 tokens, with cache reads at $0.01.
- Artificial Analysis measured the Max variant at an Intelligence Index of 43.4, well above the median of 13 for models in its price range, and about 236 output tokens per second.

## Limitations
- Prompts over 100,000 tokens are billed at a higher tier: $0.50 input, $2.50 output and $0.05 cache read per million tokens.
- Adaptive thinking is on by default and the default effort is medium. OpenRouter notes thinking can be turned off at low, medium and high effort.
- Omit temperature, top_p and top_k. Some values return a 400 error.
- Artificial Analysis rates it very verbose at Max (about 440M tokens for its Intelligence Index, against a median of 95M). Its measured time to first token of about 315 seconds at max effort includes reasoning time.

## Good for
- Classification, extraction and routing at volume.
- Subagents inside larger agent systems.
- Summarization and browser-use tasks where cost and latency matter more than peak depth.
