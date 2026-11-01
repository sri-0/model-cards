---
id: anthropic/claude-3-haiku
name: Claude 3 Haiku
owned_by: anthropic
type: llm
description: The smallest and fastest model of Anthropic's March 2024 Claude 3 family, retired from the Claude API on April 20, 2026 and left on Amazon Bedrock in three Asia-Pacific regions until November 13, 2026.
aliases: [claude-3-haiku-20240307, "anthropic.claude-3-haiku-20240307-v1:0", "claude-3-haiku@20240307", claude-3-haiku]
context_length: 200000
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2024-03-13"
knowledge_cutoff: "2023-08"
benchmarks:
  gpqa_diamond: 37.4
  humanitys_last_exam: 4.1
  ifbench: 36.1
  long_context_reasoning: 27.7
  mmmu_pro: 30.8
  tau2_bench: 21.1
  terminal_bench_hard: 0.8
benchmark_variant: Claude 3 Haiku
sources:
  - https://artificialanalysis.ai/models/claude-3-haiku
  - https://www.anthropic.com/news/claude-3-haiku
  - https://www.anthropic.com/news/claude-3-family
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/partner-models
  - https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/v0.90.0/src/anthropic/types/model.py
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Claude 3 Haiku

## Overview
Claude 3 Haiku (Claude Haiku 3 in Anthropic's current docs) is the smallest model of the Claude 3 family that Anthropic announced on March 4, 2024, the release date Artificial Analysis records. Anthropic released it on the Claude API and Amazon Bedrock on March 13, 2024, with Vertex AI to follow. OpenRouter no longer lists it, so the id follows OpenRouter's naming style; the Claude API id is `claude-3-haiku-20240307`. Anthropic deprecated it on February 19, 2026 and retired it from the Claude API on April 20, 2026, naming `claude-haiku-4-5-20251001` as the replacement. Google shut down `claude-3-haiku` on August 23, 2026. AWS ended it on Bedrock on September 10, 2026 in most regions and lists November 13, 2026 for ap-northeast-2, ap-south-1 and ap-southeast-1. Anthropic's launch price was $0.25 input and $1.25 output per million tokens, with a 200K-token context window. Artificial Analysis and Google both give an August 2023 knowledge cutoff.

## Strengths
- Speed: Anthropic said it reads about 21K tokens (around 30 pages) per second for prompts under 32K tokens, three times faster than its peers for most workloads.
- Image input and function calling, per Google's model card.
- Artificial Analysis measured 37.4% on GPQA Diamond, 30.8% on MMMU-Pro and 36.1% on IFBench.

## Limitations
- Retired on the Claude API and Google Cloud; the last Bedrock regions end on November 13, 2026.
- No extended thinking.
- Very weak at agent work: 21.1% on tau2-bench and 0.8% on Terminal-Bench Hard, per Artificial Analysis.
- 200K context window.

## Good for
- Bedrock workloads in those three regions until November 13, 2026.
- Reproducing 2024 results; Anthropic recommends Claude Haiku 4.5 instead.
