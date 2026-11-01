---
id: anthropic/claude-mythos-5.1
name: Claude Mythos 5.1
owned_by: anthropic
type: llm
description: The same underlying model as Claude Fable 5.1, served under its own id with more permissive cyber and life-sciences safeguards to organisations verified through Anthropic's access programs.
aliases: [claude-mythos-5-1, anthropic.claude-mythos-5-1, us.anthropic.claude-mythos-5-1, global.anthropic.claude-mythos-5-1]
context_length: 1000000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2026-09-01"
knowledge_cutoff: "2026-06"
sources:
  - https://platform.claude.com/docs/en/models/mythos-5-1/overview
  - https://platform.claude.com/docs/en/models/fable-5-1/migration-guide
  - https://platform.claude.com/docs/en/models/overview
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://platform.claude.com/docs/en/build-with-claude/thinking
  - https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback
  - https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
  - https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed
  - https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
  - https://www.anthropic.com/claude-fable-and-mythos-5-1
  - https://www.anthropic.com/claude/mythos
  - https://www.anthropic.com/claude/fable
  - https://www.anthropic.com/transparency
  - https://support.claude.com/en/articles/14604842
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Claude Mythos 5.1

## Overview
Claude Mythos 5.1 shares its underlying model with Claude Fable 5.1 (card `anthropic/claude-fable-5.1`); Anthropic calls them "the same model, but with different levels of safeguards". Released on September 1, 2026, it is offered only through Anthropic's Cyber and Life Sciences Verification Programs, currently to US organisations, and powers Claude Security. OpenRouter does not list it, so the id is Anthropic's API id `claude-mythos-5-1` under the vendor prefix; it is also on Amazon Bedrock, Google Cloud (Google managed) and Microsoft Foundry. Anthropic charges $10 input and $50 output per million tokens, $12.50 (5 minutes) or $20 (1 hour) for cache writes, $0.25 for cache reads, and half price for batches. It has a 1M-token context window, 128K maximum output, always-on adaptive thinking (default effort `high`), and June 2026 reliable and training-data cutoffs. Status is Active (verification required), with retirement not sooner than September 1, 2027. It succeeds Claude Mythos 5. Artificial Analysis has no page for it.

## Strengths
- 60.9% on Terminal-Bench 4.0 against 55.8% for Fable 5.1; Anthropic rates its cyber capabilities the strongest of any model it has released.
- Penetration testing, exploit generation and binary-based vulnerability scanning, which Fable 5.1's safeguards redirect to Opus models.
- Reads Fable 5.1, Mythos 5 and Opus 5 thinking blocks, so conversations move onto it intact.

## Limitations
- Needs verification and 30-day data retention; zero data retention only if Anthropic authorises it.
- Keeps Mythos 5's biology safeguards and can return a `refusal` stop reason callers must handle.
- Forced tool choice returns a 400 error, and editing earlier turns invalidates thinking blocks.
- Not on Claude Platform on AWS, which serves Fable 5.1.

## Good for
- Verified security teams and life-sciences researchers whose work Fable 5.1's safeguards interrupt; others should use Claude Fable 5.1, with the same specifications and pricing.
