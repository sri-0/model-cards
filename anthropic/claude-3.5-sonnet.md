---
id: anthropic/claude-3.5-sonnet
name: Claude 3.5 Sonnet
owned_by: anthropic
type: llm
description: Anthropic's 2024 mid-tier model in two snapshots, June 2024 and the October 2024 upgrade that introduced computer use, retired from the Claude API on October 28, 2025.
aliases: [claude-3-5-sonnet-20241022, claude-3-5-sonnet-20240620, claude-3-5-sonnet-latest, "anthropic.claude-3-5-sonnet-20241022-v2:0", "anthropic.claude-3-5-sonnet-20240620-v1:0", "us.anthropic.claude-3-5-sonnet-20241022-v2:0", "us.anthropic.claude-3-5-sonnet-20240620-v1:0", "eu.anthropic.claude-3-5-sonnet-20241022-v2:0", "eu.anthropic.claude-3-5-sonnet-20240620-v1:0", "claude-3-5-sonnet@20240620", claude-3-5-sonnet-v2, claude-3-5-sonnet]
context_length: 200000
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2024-10-22"
knowledge_cutoff: "2024-04"
benchmarks:
  gpqa_diamond: 59.9
  humanitys_last_exam: 3.7
benchmark_variant: "Claude 3.5 Sonnet (Oct '24)"
sources:
  - https://artificialanalysis.ai/models/claude-35-sonnet
  - https://artificialanalysis.ai/models/claude-35-sonnet-june-24
  - https://www.anthropic.com/news/3-5-models-and-computer-use
  - https://www.anthropic.com/news/claude-3-5-sonnet
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/partner-models
  - https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/v0.69.0/src/anthropic/types/model.py
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Claude 3.5 Sonnet

## Overview
Claude 3.5 Sonnet (Claude Sonnet 3.5 in Anthropic's current docs) exists as two snapshots that share this card: `claude-3-5-sonnet-20240620`, released June 21, 2024 as the first of the 3.5 family, and the upgraded `claude-3-5-sonnet-20241022` of October 22, 2024, which added the computer use beta. The frontmatter dates and benchmarks are the October snapshot's. OpenRouter no longer lists it, so the id follows OpenRouter's naming style. Anthropic deprecated both on August 13, 2025 and retired them from the Claude API on October 28, 2025; the deprecations page names `claude-sonnet-5-5` as the replacement. Google shut down `claude-3-5-sonnet-v2` and `claude-3-5-sonnet` on February 19, 2026. AWS lists Bedrock end-of-life for both as November 13, 2026 in ap-northeast-2, ap-south-1 and ap-southeast-1. Anthropic priced it at $3 input and $15 output per million tokens, with a 200K-token context window. Artificial Analysis gives an April 2024 knowledge cutoff for both snapshots; Google's model card gives August 2024 for the October one.

## Strengths
- The October snapshot raised SWE-bench Verified from 33.4% to 49.0% and TAU-bench retail from 62.6% to 69.2%, per Anthropic, and scored 14.9% on OSWorld with screenshots only.
- The June snapshot ran at twice the speed of Claude 3 Opus and was Anthropic's strongest vision model at the time, notably on charts and graphs.
- Artificial Analysis measured the October snapshot at 59.9% on GPQA Diamond, against 56.0% for June.

## Limitations
- Retired on the Claude API and Google Cloud; Bedrock access ends on November 13, 2026.
- No extended thinking.
- Anthropic called computer use experimental, at times cumbersome and error-prone, with scrolling, dragging and zooming still difficult.
- 200K context window.

## Good for
- Bedrock workloads in those three regions that must run until November 13, 2026.
- Reproducing 2024 results; Anthropic recommends Claude Sonnet 5.5 instead.
