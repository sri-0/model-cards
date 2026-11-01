---
id: anthropic/claude-sonnet-4
name: Claude 4 Sonnet
owned_by: anthropic
type: llm
description: Anthropic's Claude Sonnet 4, the May 2025 mid-tier hybrid reasoning model that succeeded Claude Sonnet 3.7, retired from the Claude API on June 15, 2026.
aliases: [claude-sonnet-4-20250514, claude-sonnet-4-0, claude-4-sonnet-20250514, "anthropic.claude-sonnet-4-20250514-v1:0", "global.anthropic.claude-sonnet-4-20250514-v1:0", "us.anthropic.claude-sonnet-4-20250514-v1:0", "eu.anthropic.claude-sonnet-4-20250514-v1:0", "apac.anthropic.claude-sonnet-4-20250514-v1:0", "claude-sonnet-4@20250514"]
context_length: 1000000
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-05-22"
knowledge_cutoff: "2025-01"
benchmarks:
  gpqa_diamond: 77.7
  humanitys_last_exam: 10.7
  ifbench: 54.7
  long_context_reasoning: 70.3
  mmmu_pro: 61.8
  tau2_bench: 64.6
  terminal_bench_hard: 31.1
benchmark_variant: Claude 4 Sonnet (Reasoning)
sources:
  - https://artificialanalysis.ai/models/claude-4-sonnet
  - https://www.anthropic.com/news/claude-4
  - https://claude.com/blog/1m-context
  - https://www.anthropic.com/transparency
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://platform.claude.com/docs/en/build-with-claude/effort
  - https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy
  - https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/v0.69.0/src/anthropic/types/model.py
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Claude 4 Sonnet

## Overview
Claude Sonnet 4 (Artificial Analysis lists it as Claude 4 Sonnet) was released on May 22, 2025 alongside Claude Opus 4 as a significant upgrade to Claude Sonnet 3.7, a hybrid with near-instant responses and an extended thinking mode. OpenRouter no longer lists it, so the id follows OpenRouter's naming style; the Claude API id is `claude-sonnet-4-20250514`, with the alias `claude-sonnet-4-0`. Anthropic deprecated it on April 14, 2026 and retired it from the Claude API on June 15, 2026, naming `claude-sonnet-5-5` as the replacement. Anthropic's pricing page lists it as retired except on Amazon Bedrock and Claude Models on Google Cloud (Google managed), but AWS gives its Bedrock end-of-life as October 14, 2026 in the 23 regions it names. Anthropic priced it at $3 input and $15 output per million tokens, with cache reads at $0.30. Artificial Analysis lists a 1M-token context window, from the long-context beta Anthropic opened on August 12, 2025 at $6 input and $22.50 output above 200K tokens; Anthropic's Bedrock and Google Cloud pages give 200K. Reliable knowledge cutoff January 2025, training data cutoff March 2025.

## Strengths
- 72.7% on SWE-bench Verified (80.2% with parallel test-time compute), per Anthropic.
- Extended thinking with tool use and parallel tool calls, as on Opus 4.
- Artificial Analysis measured the Reasoning variant at 77.7% on GPQA Diamond, 64.6% on tau2-bench, 70.3% on AA-LCR and 31.1% on Terminal-Bench Hard.

## Limitations
- Retired on the Claude API and past end-of-life in the Bedrock regions AWS lists.
- Anthropic said at launch that it does not match Opus 4 in most domains.
- Thinking needs a manual token budget; the effort parameter does not support it.

## Good for
- Google Cloud deployments pinned to `claude-sonnet-4@20250514`.
- Reproducing results that cited Sonnet 4; Anthropic recommends Claude Sonnet 5.5 instead.
