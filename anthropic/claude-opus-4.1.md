---
id: anthropic/claude-opus-4.1
name: Claude Opus 4.1
owned_by: anthropic
type: llm
description: Anthropic's August 2025 update to Claude Opus 4 for agentic coding and reasoning, retired from the Claude API on August 5, 2026 but still listed by OpenRouter and, per Anthropic, on Amazon Bedrock and Google Cloud.
aliases: [claude-opus-4-1-20250805, claude-opus-4-1, "anthropic.claude-opus-4-1-20250805-v1:0", "us.anthropic.claude-opus-4-1-20250805-v1:0", "claude-opus-4-1@20250805", anthropic/claude-4.1-opus-20250805, "anthropic/claude-opus-4.1:batch"]
context_length: 200000
max_output_tokens: 32000
capabilities: [tool_calling, reasoning, vision]
supported_parameters: [include_reasoning, max_tokens, reasoning, stop, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [image, text, file]
  output_modalities: [text]
  tokenizer: Claude
open_weights: false
license: proprietary
release_date: "2025-08-05"
knowledge_cutoff: "2025-01"
pricing:
  input: 15
  output: 75
  cache_read: 1.5
  cache_write: 18.75
benchmarks:
  gpqa_diamond: 80.9
  humanitys_last_exam: 12.5
  ifbench: 55.4
  long_context_reasoning: 76.0
  mmmu_pro: 67.9
  tau2_bench: 71.4
  terminal_bench_hard: 34.3
benchmark_variant: Claude 4.1 Opus (Reasoning)
sources:
  - https://openrouter.ai/anthropic/claude-opus-4.1
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-4-1-opus
  - https://www.anthropic.com/news/claude-opus-4-1
  - https://www.anthropic.com/transparency
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://platform.claude.com/docs/en/models/overview
  - https://platform.claude.com/docs/en/build-with-claude/effort
  - https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy
  - https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/v0.90.0/src/anthropic/types/model.py
retrieved: "2026-11-01"
---

# Claude Opus 4.1

## Overview
Claude Opus 4.1 is the August 5, 2025 upgrade to Claude Opus 4 on agentic tasks, real-world coding and reasoning, at the same price. Anthropic deprecated it on June 5, 2026 and retired it from the Claude API on August 5, 2026, naming `claude-opus-4-8` as the replacement. Its pricing page lists it as retired except on Amazon Bedrock and Claude Models on Google Cloud (Google managed); AWS lists its Bedrock end-of-life as January 8, 2027 in us-east-1, us-east-2 and us-west-2. OpenRouter still lists it with a 200K-token context window and 32K maximum output, at $15 input and $75 output per million tokens. Anthropic charges $18.75 (5 minutes) or $30 (1 hour) for cache writes and $1.50 for cache reads. The knowledge cutoff is OpenRouter's (January 31, 2025); Artificial Analysis gives March 2025; Anthropic's current docs state none.

## Strengths
- 74.5% on SWE-bench Verified, per Anthropic, with better research and data analysis, especially detail tracking and agentic search.
- GitHub reported notable gains in multi-file code refactoring; Rakuten found it pinpoints exact corrections in large codebases without unnecessary changes.
- Artificial Analysis measured the Reasoning variant at 80.9% on GPQA Diamond, 71.4% on tau2-bench, 76.0% on AA-LCR and 34.3% on Terminal-Bench Hard.

## Limitations
- Retired on the Claude API; only Bedrock, Google Cloud and OpenRouter still serve it.
- Thinking is manual extended thinking with a token budget; Anthropic's effort parameter does not support this model.
- 200K context window, a fifth of later Opus models.
- On Bedrock its ARN-versioned id can reject API version 2026-10-21, so SDKs must stay pinned to an earlier release.

## Good for
- Integrations validated on Opus 4.1 that cannot yet move.
- Reproducing 2025 results that cited this model; Anthropic recommends Claude Opus 4.8 instead.
