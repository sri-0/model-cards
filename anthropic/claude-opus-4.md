---
id: anthropic/claude-opus-4
name: Claude 4 Opus
owned_by: anthropic
type: llm
description: Anthropic's Claude Opus 4, its May 2025 flagship hybrid reasoning model for coding and long-running agent tasks, retired from the Claude API on June 15, 2026.
aliases: [claude-opus-4-20250514, claude-opus-4-0, claude-4-opus-20250514, "anthropic.claude-opus-4-20250514-v1:0", "us.anthropic.claude-opus-4-20250514-v1:0", "eu.anthropic.claude-opus-4-20250514-v1:0", "claude-opus-4@20250514"]
context_length: 200000
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-05-22"
knowledge_cutoff: "2025-01"
benchmarks:
  gpqa_diamond: 79.6
  humanitys_last_exam: 12.3
  ifbench: 53.7
  long_context_reasoning: 69.3
  tau2_bench: 73.4
  terminal_bench_hard: 31.1
benchmark_variant: Claude 4 Opus (Reasoning)
sources:
  - https://artificialanalysis.ai/models/claude-4-opus
  - https://www.anthropic.com/news/claude-4
  - https://www.anthropic.com/transparency
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://platform.claude.com/docs/en/build-with-claude/effort
  - https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy
  - https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
  - https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/v0.69.0/src/anthropic/types/model.py
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Claude 4 Opus

## Overview
Claude Opus 4 (Artificial Analysis lists it as Claude 4 Opus) was released on May 22, 2025 as Anthropic's most powerful model of that generation, a hybrid with near-instant responses and an extended thinking mode. OpenRouter no longer lists it, so the id follows OpenRouter's naming style; the Claude API id is `claude-opus-4-20250514`, with the alias `claude-opus-4-0`. Anthropic deprecated it on April 14, 2026 and retired it from the Claude API on June 15, 2026, naming `claude-opus-4-8` as the replacement. Its pricing page lists it as retired except on Claude Models on Google Cloud (Google managed), where the id is `claude-opus-4@20250514`. Anthropic priced it at $15 input and $75 output per million tokens, with cache writes at $18.75 (5 minutes) or $30 (1 hour) and cache reads at $1.50. Artificial Analysis lists a 200K-token context window. Anthropic's transparency hub gives a reliable knowledge cutoff of January 2025 and a training data cutoff of March 2025.

## Strengths
- 72.5% on SWE-bench Verified (79.4% with parallel test-time compute) and 43.2% on Terminal-bench, per Anthropic.
- Extended thinking with tool use, parallel tool calls, and memory files when given local file access.
- Artificial Analysis measured the Reasoning variant at 79.6% on GPQA Diamond, 73.4% on tau2-bench, 69.3% on AA-LCR and 31.1% on Terminal-Bench Hard.

## Limitations
- Retired on the Claude API and absent from Anthropic's current Bedrock model tables.
- Three times the price of Opus 4.5 through Opus 5.
- 200K context window; thinking needs a manual token budget and the effort parameter does not support it.
- Long thinking is summarised by a smaller model; raw chains of thought needed Anthropic's Developer Mode.

## Good for
- Google Cloud deployments pinned to the dated id.
- Reproducing results that cited Opus 4; Anthropic recommends Claude Opus 4.8 instead.
