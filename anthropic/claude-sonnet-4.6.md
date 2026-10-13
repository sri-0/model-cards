---
id: anthropic/claude-sonnet-4.6
name: Claude Sonnet 4.6
owned_by: anthropic
type: llm
description: Anthropic Sonnet model released in February 2026 for coding, agents and professional work, now a legacy model succeeded by Sonnet 5 and Sonnet 5.5.
aliases: [claude-sonnet-4-6, anthropic.claude-sonnet-4-6, anthropic/claude-sonnet-4-6]
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
release_date: "2026-02-17"
knowledge_cutoff: "2025-08"
pricing:
  input: 3
  output: 15
  cache_read: 0.3
  cache_write: 3.75
benchmarks:
  intelligence_index: 30.1
  coding_index: 63
  agentic_index: 31.8
  omniscience_index: 12.2
  humanitys_last_exam: 33.6
  gpqa_diamond: 87.5
  scicode: 50.1
  terminal_bench_hard: 53
  terminal_bench_4: 3
  long_context_reasoning: 80
  ifbench: 56.6
  tau2_bench: 75.7
  mmmu_pro: 73.3
  output_tokens_per_second: 58.8
  time_to_first_token_seconds: 102.68
benchmark_variant: Claude Sonnet 4.6 (Max)
sources:
  - https://openrouter.ai/anthropic/claude-sonnet-4.6
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-sonnet-4-6-adaptive
  - https://platform.claude.com/docs/en/models/sonnet-4-6/overview
retrieved: "2026-10-14"
---

# Claude Sonnet 4.6

## Overview
Claude Sonnet 4.6 was Anthropic's most capable Sonnet-class model at release, aimed at coding, agents and professional work. It accepts text, image and file input, returns text, and has a 1M-token context window with up to 128K output tokens (300K on the Batch API with a beta header). Anthropic lists it as Active (legacy), with retirement not sooner than February 17, 2027. Its reliable knowledge cutoff is August 2025 and its training data cutoff is January 2026.

## Strengths
- Coding and agentic work. Artificial Analysis measured the Max variant at an Intelligence Index of 30.1, a Coding Index of 63.0 and 53% on Terminal-Bench Hard.
- Long-context work: 80% on Artificial Analysis's long-context reasoning test.
- OpenRouter lists temperature, top_p and top_k among its supported parameters.
- Widely served. OpenRouter routes it to five providers.

## Limitations
- Thinking is adaptive. Anthropic marks the older extended thinking mode as deprecated on this model. The default effort is high.
- List price is $3 input and $15 output per million tokens, which is higher than the later Sonnet 5 and Sonnet 5.5 ($2 and $10). Artificial Analysis rates it somewhat expensive.
- Artificial Analysis rates it slower than average (about 59 output tokens per second) and very verbose at Max. The measured time to first token of about 103 seconds at max effort includes reasoning time.

## Good for
- Existing integrations validated on Sonnet 4.6.
- Coding and agent workloads that have not been re-tested on a newer Sonnet.
- Long-context document tasks within a 1M-token window.
