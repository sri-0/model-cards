---
id: anthropic/claude-mythos-preview
name: Claude Mythos Preview
owned_by: anthropic
type: llm
description: Anthropic's first Mythos-class model, an invitation-only research preview for defensive cybersecurity released through Project Glasswing in April 2026 and deprecated on June 9, 2026 in favour of Claude Mythos 5.
aliases: [claude-mythos-preview, anthropic.claude-mythos-preview, us.anthropic.claude-mythos-preview, apac.anthropic.claude-mythos-preview, au.anthropic.claude-mythos-preview]
context_length: 1000000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2026-04-07"
sources:
  - https://www.anthropic.com/glasswing
  - https://www.anthropic.com/transparency
  - https://www.anthropic.com/news/claude-fable-5-mythos-5
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://platform.claude.com/docs/en/build-with-claude/context-windows
  - https://platform.claude.com/docs/en/build-with-claude/thinking
  - https://platform.claude.com/docs/en/build-with-claude/effort
  - https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
  - https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
  - https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
  - https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/src/anthropic/types/model.py
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Claude Mythos Preview

## Overview
Claude Mythos Preview is the first Mythos-class model, a tier Anthropic places above Opus. Anthropic announced it with Project Glasswing on April 7, 2026 and gave it only to invited partners for defensive cybersecurity, with no plan for general availability. OpenRouter does not list it, so the id is Anthropic's API id `claude-mythos-preview` under the vendor prefix. Partners reach it on the Claude API, Amazon Bedrock (us-east-1 only, from an allowlisted AWS account), Google Cloud and Microsoft Foundry. After the usage credits Anthropic committed to Glasswing, the price is $25 input and $125 output per million tokens. It has a 1M-token context window, 128K maximum output, adaptive thinking on by default, and the newer tokenizer that produces about 30% more tokens for the same text. Anthropic deprecated it on June 9, 2026, with retirement to be announced, and offered Glasswing users Claude Mythos 5 as the upgrade; Claude Mythos 5.1 is now the current Mythos model. Anthropic publishes no knowledge cutoff for it, and Artificial Analysis has no page for it.

## Strengths
- Anthropic reports 93.9% on SWE-bench Verified, 77.8% on SWE-bench Pro, 82.0% on Terminal-Bench 2.0, 94.6% on GPQA Diamond and 79.6% on OSWorld-Verified.
- 83.1% on CyberGym against 66.6% for Claude Opus 4.6; Anthropic says it found thousands of zero-day vulnerabilities, including in every major operating system and web browser.
- Accepts manual extended thinking with a token budget as well as adaptive thinking, unlike Mythos 5.

## Limitations
- Invitation only, for defensive cybersecurity, with real-time classifier guards.
- Deprecated, and Mythos 5 costs less than half as much.
- Thinking cannot be turned off, the `xhigh` effort level is unavailable, and non-default temperature, top_p or top_k values return a 400 error.

## Good for
- Glasswing workloads validated on it that have not yet moved to Claude Mythos 5.1.
