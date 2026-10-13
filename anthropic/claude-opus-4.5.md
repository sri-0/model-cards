---
id: anthropic/claude-opus-4.5
name: Claude Opus 4.5
owned_by: anthropic
type: llm
description: Anthropic Opus model released in November 2025 for software engineering and agentic workflows, now a legacy model with a 200K context window.
aliases: [claude-opus-4-5-20251101, claude-opus-4-5, "anthropic.claude-opus-4-5-20251101-v1:0", "claude-opus-4-5@20251101", anthropic/claude-opus-4-5]
context_length: 200000
max_output_tokens: 64000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, verbosity]
architecture:
  input_modalities: [file, image, text]
  output_modalities: [text]
  tokenizer: Claude
open_weights: false
license: proprietary
release_date: "2025-11-24"
knowledge_cutoff: "2025-05"
pricing:
  input: 5
  output: 25
  cache_read: 0.5
  cache_write: 6.25
benchmarks:
  intelligence_index: 29.1
  omniscience_index: 14
  humanitys_last_exam: 30.1
  gpqa_diamond: 86.6
  terminal_bench_hard: 47
  long_context_reasoning: 77.3
  ifbench: 58
  tau2_bench: 89.5
  mmmu_pro: 74
  output_tokens_per_second: 54.3
  time_to_first_token_seconds: 19.2
benchmark_variant: Claude Opus 4.5 (Reasoning)
sources:
  - https://openrouter.ai/anthropic/claude-opus-4.5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-opus-4-5-thinking
  - https://platform.claude.com/docs/en/models/opus-4-5/overview
retrieved: "2026-10-14"
---

# Claude Opus 4.5

## Overview
Claude Opus 4.5 is a reasoning model that OpenRouter describes as optimised for complex software engineering, agentic workflows and long-horizon computer use. It accepts text, image and file input and returns text. Anthropic lists a 200K-token context window and 64K maximum output. Its status is Active (legacy), with retirement not sooner than November 24, 2026. Its reliable knowledge cutoff is May 2025 and its training data cutoff is August 2025.

## Strengths
- Tool use, context management and coordinated multi-agent setups, per OpenRouter.
- Autonomous research, debugging, multi-step planning, and spreadsheet and browser manipulation.
- Improved robustness to prompt injection compared with earlier Opus models, per OpenRouter.
- Effort levels let callers trade speed, depth and token use. OpenRouter exposes this through its verbosity parameter (low, medium, high).
- Artificial Analysis measured the Reasoning variant at an Intelligence Index of 29.1, 89.5% on tau2-bench and 47% on Terminal-Bench Hard.

## Limitations
- Artificial Analysis marks its Intelligence Index value for this model as estimated.
- Anthropic lists its thinking mode as extended rather than adaptive.
- The 200K context window is smaller than the 1M window of later Opus models.
- List price is $5 input and $25 output per million tokens. Artificial Analysis rates it particularly expensive and notably slow, at about 54 output tokens per second.
- Retirement can occur from November 24, 2026.

## Good for
- Existing integrations validated on Opus 4.5 that have not yet moved to a newer model.
- Computer-use and browser automation agents.
- Software engineering tasks that fit within 200K tokens.
