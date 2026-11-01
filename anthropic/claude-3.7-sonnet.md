---
id: anthropic/claude-3.7-sonnet
name: Claude 3.7 Sonnet
owned_by: anthropic
type: llm
description: Anthropic's February 2025 model, which it called the first hybrid reasoning model on the market, retired from the Claude API on February 19, 2026 and left on Amazon Bedrock in two regions until November 13, 2026.
aliases: [claude-3-7-sonnet-20250219, claude-3-7-sonnet-latest, "anthropic.claude-3-7-sonnet-20250219-v1:0", "us.anthropic.claude-3-7-sonnet-20250219-v1:0", "eu.anthropic.claude-3-7-sonnet-20250219-v1:0", claude-3-7-sonnet]
context_length: 200000
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-02-24"
knowledge_cutoff: "2024-10"
benchmarks:
  gpqa_diamond: 77.2
  humanitys_last_exam: 9.7
  ifbench: 48.3
  tau2_bench: 54.7
  terminal_bench_hard: 21.2
benchmark_variant: Claude 3.7 Sonnet (Reasoning)
sources:
  - https://artificialanalysis.ai/models/claude-3-7-sonnet
  - https://www.anthropic.com/news/claude-3-7-sonnet
  - https://www.anthropic.com/transparency
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://platform.claude.com/docs/en/build-with-claude/effort
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/partner-models
  - https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/v0.69.0/src/anthropic/types/model.py
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Claude 3.7 Sonnet

## Overview
Claude 3.7 Sonnet (Claude Sonnet 3.7 in Anthropic's current docs) was released on February 24, 2025 as what Anthropic called the first hybrid reasoning model on the market: it answers directly or, in extended thinking mode, self-reflects first, and API callers set a thinking budget up to its 128K-token output limit. OpenRouter no longer lists it, so the id follows OpenRouter's naming style; the Claude API id is `claude-3-7-sonnet-20250219`, with the alias `claude-3-7-sonnet-latest`. Anthropic deprecated it on October 28, 2025 and retired it from the Claude API on February 19, 2026; the deprecations page names `claude-sonnet-5-5` as the replacement. Google shut down `claude-3-7-sonnet` on May 11, 2026, and AWS lists its Bedrock end-of-life as November 13, 2026 in ap-south-1 and eu-west-2. Anthropic priced it at $3 input and $15 output per million tokens in both modes, with thinking tokens billed as output. Artificial Analysis lists a 200K-token context window. Anthropic's transparency hub gives a knowledge cutoff of October 2024; Google's model card says November 2024.

## Strengths
- 63.7% on SWE-bench Verified, or 70.3% with Anthropic's high-compute scaffolding, on the 489 tasks its infrastructure could run.
- Its thinking is visible to the user, and Anthropic reported 45% fewer unnecessary refusals than its predecessor.
- Artificial Analysis measured the Reasoning variant at 77.2% on GPQA Diamond, 54.7% on tau2-bench and 21.2% on Terminal-Bench Hard.

## Limitations
- Retired on the Claude API and Google Cloud; Bedrock access ends on November 13, 2026.
- Anthropic optimised it less for maths and computer-science competition problems than for real-world tasks.
- Manual thinking budget only; no adaptive thinking or effort parameter.
- 200K context window.

## Good for
- Bedrock workloads in ap-south-1 or eu-west-2 that must run until November 13, 2026.
- Reproducing early-2025 results; Anthropic recommends Claude Sonnet 5.5 instead.
