---
id: anthropic/claude-sonnet-4.5
name: Claude Sonnet 4.5
owned_by: anthropic
type: llm
description: Anthropic Sonnet model released in September 2025 for agents and coding, deprecated and scheduled to retire on November 30, 2026.
aliases: [claude-sonnet-4-5-20250929, claude-sonnet-4-5, "anthropic.claude-sonnet-4-5-20250929-v1:0", "claude-sonnet-4-5@20250929", anthropic/claude-sonnet-4-5]
context_length: 1000000
max_output_tokens: 64000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: Claude
open_weights: false
license: proprietary
release_date: "2025-09-29"
knowledge_cutoff: "2025-01"
pricing:
  input: 3
  output: 15
  cache_read: 0.3
  cache_write: 3.75
benchmarks:
  intelligence_index: 20.7
  coding_index: 52.1
  agentic_index: 15.8
  omniscience_index: -0.1
  humanitys_last_exam: 17.8
  gpqa_diamond: 83.4
  scicode: 45.7
  terminal_bench_hard: 35.6
  terminal_bench_4: 0
  long_context_reasoning: 72.3
  ifbench: 57.3
  tau2_bench: 78.1
  mmmu_pro: 68.7
  output_tokens_per_second: 47.4
  time_to_first_token_seconds: 18.07
benchmark_variant: Claude 4.5 Sonnet (Reasoning)
sources:
  - https://openrouter.ai/anthropic/claude-sonnet-4.5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-4-5-sonnet-thinking
  - https://platform.claude.com/docs/en/models/sonnet-4-5/overview
retrieved: "2026-10-14"
---

# Claude Sonnet 4.5

## Overview
Claude Sonnet 4.5 is a Sonnet model that OpenRouter describes as optimised for real-world agents and coding workflows, with extended autonomous operation. Anthropic deprecated it on September 30, 2026 and lists retirement on November 30, 2026. Anthropic lists a 200K-token context window and 64K maximum output, while OpenRouter lists a 1M-token context. It accepts text, image and file input and returns text. Its reliable knowledge cutoff is January 2025 and its training data cutoff is July 2025.

## Strengths
- Tool orchestration, speculative parallel execution, and context and memory management, per OpenRouter.
- Awareness of token usage across tool calls, which helps in multi-context and long-running workflows.
- System design, code security and specification adherence, per OpenRouter.
- Artificial Analysis measured the Reasoning variant at an Intelligence Index of 20.7, a Coding Index of 52.1 and 78.1% on tau2-bench, and rates it fairly concise.

## Limitations
- Deprecated. Plan to move to a current Sonnet model before November 30, 2026.
- On OpenRouter, prompts over 200,000 tokens cost more: $6 input and $22.50 output per million tokens, against $3 and $15 below that size.
- Anthropic lists its thinking mode as extended, not adaptive, and the effort parameter as not supported.
- Artificial Analysis rates it notably slow, at about 47 output tokens per second, and recorded 0% on Terminal-Bench 4.0.

## Good for
- Existing agent and coding integrations until they are migrated.
- Software engineering, security review, financial analysis and research agents, as OpenRouter lists.
