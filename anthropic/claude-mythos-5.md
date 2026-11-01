---
id: anthropic/claude-mythos-5
name: Claude Mythos 5
owned_by: anthropic
type: llm
description: The same underlying model as Claude Fable 5, served under its own id with Fable's cyber safeguards lifted to verified organisations, now succeeded by Claude Mythos 5.1.
aliases: [claude-mythos-5, anthropic.claude-mythos-5, us.anthropic.claude-mythos-5]
context_length: 1000000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2026-06-09"
knowledge_cutoff: "2026-01"
sources:
  - https://platform.claude.com/docs/en/models/mythos-5/overview
  - https://platform.claude.com/docs/en/models/fable-5-1/migration-guide
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://platform.claude.com/docs/en/build-with-claude/thinking
  - https://platform.claude.com/docs/en/build-with-claude/effort
  - https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
  - https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
  - https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
  - https://www.anthropic.com/news/claude-fable-5-mythos-5
  - https://www.anthropic.com/claude/mythos
  - https://www.anthropic.com/transparency
  - https://support.claude.com/en/articles/14604842
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Claude Mythos 5

## Overview
Claude Mythos 5 shares its underlying model with Claude Fable 5 (card `anthropic/claude-fable-5`). Both were released on June 9, 2026: Fable 5 for general use with cyber, biology and chemistry safeguards, and Mythos 5 with the cyber safeguards lifted, deployed through Project Glasswing with the US government as the upgrade to Claude Mythos Preview. Anthropic suspended access to both on June 12, 2026 and restored it on July 1, 2026. OpenRouter does not list it, so the id is Anthropic's API id `claude-mythos-5` under the vendor prefix; it is also on Amazon Bedrock, Google Cloud (Google managed) and Microsoft Foundry. Anthropic charges $10 input and $50 output per million tokens, $12.50 (5 minutes) or $20 (1 hour) for cache writes, $1 for cache reads, and half price for batches. It has a 1M-token context window, 128K maximum output, always-on adaptive thinking (default effort `high`), and January 2026 reliable and training-data cutoffs. Status is Active (verification required), with retirement not sooner than June 9, 2027; Anthropic names Claude Mythos 5.1 as the current Mythos model. Artificial Analysis has no page for it, so no benchmarks are recorded.

## Strengths
- With it, Anthropic's protein design experts sped up parts of drug design about tenfold, and its scientists preferred its molecular biology hypotheses about 80% of the time.
- Cyber requests that Fable 5 hands to Claude Opus 4.8 are answered by the model itself.

## Limitations
- Superseded: Mythos 5.1 reads its thinking blocks, but not the reverse.
- Biology and chemistry safeguards stayed on at launch.
- 30-day data retention is required and Priority Tier is not supported.
- Cache reads cost $1, four times Mythos 5.1's rate.

## Good for
- Verified deployments pinned to Mythos 5 that have not yet migrated; new verified work should start on Claude Mythos 5.1.
