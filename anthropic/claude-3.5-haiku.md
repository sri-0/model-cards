---
id: anthropic/claude-3.5-haiku
name: Claude 3.5 Haiku
owned_by: anthropic
type: llm
description: Anthropic's late-2024 fast, low-cost model that surpassed Claude 3 Opus on many evaluations, retired from the Claude API on February 19, 2026.
aliases: [claude-3-5-haiku-20241022, claude-3-5-haiku-latest, "anthropic.claude-3-5-haiku-20241022-v1:0", "us.anthropic.claude-3-5-haiku-20241022-v1:0", "eu.anthropic.claude-3-5-haiku-20241022-v1:0", "claude-3-5-haiku@20241022", claude-3-5-haiku]
context_length: 200000
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2024-10-22"
knowledge_cutoff: "2024-07"
benchmarks:
  gpqa_diamond: 40.8
  humanitys_last_exam: 3.6
  ifbench: 42.8
  long_context_reasoning: 27.3
  mmmu_pro: 45.6
  tau2_bench: 24.6
  terminal_bench_hard: 2.3
benchmark_variant: Claude 3.5 Haiku
sources:
  - https://artificialanalysis.ai/models/claude-3-5-haiku
  - https://www.anthropic.com/news/3-5-models-and-computer-use
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deprecations/partner-models
  - https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/v0.69.0/src/anthropic/types/model.py
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Claude 3.5 Haiku

## Overview
Claude 3.5 Haiku (Claude Haiku 3.5 in Anthropic's current docs) was announced on October 22, 2024, the release date Artificial Analysis records, and shipped later that month on the Claude API, Amazon Bedrock and Vertex AI, first text-only, with image input to follow. Anthropic called it the next generation of its fastest model, surpassing Claude 3 Opus on many intelligence benchmarks. OpenRouter no longer lists it, so the id follows OpenRouter's naming style; the Claude API id is `claude-3-5-haiku-20241022`, with the alias `claude-3-5-haiku-latest`. Anthropic deprecated it on December 19, 2025 and retired it from the Claude API on February 19, 2026, naming `claude-haiku-4-5-20251001` as the replacement. Anthropic's docs still list it on Claude Models on Google Cloud (Google managed) as `claude-3-5-haiku@20241022`, but Google's deprecations page says it shut down on July 5, 2026. Anthropic's price, revised on December 3, 2024, is $0.80 input and $4 output per million tokens, with cache writes at $1 (5 minutes) or $1.60 (1 hour) and cache reads at $0.08. Artificial Analysis lists a 200K-token context window and a July 2024 knowledge cutoff, as does Google.

## Strengths
- 40.6% on SWE-bench Verified at launch, per Anthropic, ahead of the original Claude 3.5 Sonnet.
- Low latency, better instruction following and more accurate tool use, which Anthropic aimed at user-facing products and sub-agent tasks.
- Artificial Analysis measured 40.8% on GPQA Diamond, 45.6% on MMMU-Pro and 42.8% on IFBench.

## Limitations
- Retired on the Claude API and, per Google, on Google Cloud.
- No extended thinking.
- Weak as an agent by current standards: 24.6% on tau2-bench and 2.3% on Terminal-Bench Hard, per Artificial Analysis.
- 200K context window.

## Good for
- Checking old results and prompts written for it.
- New work belongs on Claude Haiku 4.5, Anthropic's named replacement, or Claude Haiku 5.5.
