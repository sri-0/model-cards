---
id: anthropic/claude-sonnet-5
name: Claude Sonnet 5
owned_by: anthropic
type: llm
description: Anthropic's previous Sonnet model, released in June 2026 and now a legacy model succeeded by Claude Sonnet 5.5.
aliases: [claude-sonnet-5, anthropic.claude-sonnet-5]
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
release_date: "2026-06-30"
knowledge_cutoff: "2026-01"
pricing:
  input: 2
  output: 10
  cache_read: 0.2
  cache_write: 2.5
benchmarks:
  intelligence_index: 38.2
  coding_index: 71.5
  agentic_index: 43.6
  omniscience_index: 16.4
  humanitys_last_exam: 41.3
  gpqa_diamond: 91.1
  scicode: 54.3
  terminal_bench_4: 14.1
  long_context_reasoning: 82
  mmmu_pro: 77.3
  output_tokens_per_second: 81.7
  time_to_first_token_seconds: 170.91
benchmark_variant: Claude Sonnet 5 (Max)
sources:
  - https://openrouter.ai/anthropic/claude-sonnet-5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-sonnet-5
  - https://platform.claude.com/docs/en/models/sonnet-5/overview
retrieved: "2026-10-14"
---

# Claude Sonnet 5

## Overview
Claude Sonnet 5 was Anthropic's Sonnet-class model for coding, agents and professional work before Claude Sonnet 5.5. It supports adaptive thinking with selectable effort (low, medium, high, xhigh and max), text, image and file input, and a 1M-token context window with up to 128K output tokens. Anthropic lists it as Active (legacy), with retirement not sooner than June 30, 2027. Its knowledge cutoff is January 2026.

## Strengths
- Coding, agent and professional work, per OpenRouter.
- Artificial Analysis measured the Max variant at an Intelligence Index of 38.2, a Coding Index of 71.5, 91.1% on GPQA Diamond and 82% on its long-context reasoning test.
- List price is $2 input and $10 output per million tokens, which Artificial Analysis rates moderately priced.
- Up to 300K output tokens on the Batch API with a beta header.

## Limitations
- Setting temperature, top_p or top_k to a non-default value returns a 400 error.
- It uses an updated tokenizer, so token counts differ from older Claude models.
- It includes real-time cyber safeguards that block certain high-risk dual-use activities, which can affect security-related requests.
- Artificial Analysis rates it slower than average (about 82 output tokens per second) and very verbose at Max. The measured time to first token of about 171 seconds at max effort includes reasoning time.

## Good for
- Existing integrations that are pinned to Sonnet 5.
- Coding agents and professional tasks at a moderate price.
- New work is better started on Sonnet 5.5, which has the same list price.
