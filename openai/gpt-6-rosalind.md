---
id: openai/gpt-6-rosalind
name: GPT-6 Rosalind
owned_by: openai
type: llm
description: GPT-6 Rosalind is OpenAI's newest life sciences model, released on 30 October 2026 to organisations approved for Rosalind Research, combining specialised biological reasoning with scientific tool use.
aliases: [gpt-6-rosalind, "chatgpt/gpt-6-rosalind"]
open_weights: false
license: proprietary
release_date: "2026-10-30"
sources:
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/pricing
  - https://web.archive.org/web/20261021124314/https://openai.com/index/introducing-gpt-rosalind/
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-6 Rosalind

## Overview
GPT-6 Rosalind was released on 30 October 2026. OpenAI's changelog says it brings specialised biological reasoning with scientific tool use to complex life sciences research, and that access is for organisations approved for Rosalind Research through the trusted-access programme, for internal research by authorised users. OpenRouter does not list it and OpenAI has no model page for it yet; the id `gpt-6-rosalind` comes from the changelog and the pricing page. The pricing page lists it first among the Rosalind models at 15 USD input, 1.50 cached input and 75 USD output per million tokens, with cache writes at 18.75 (30 minutes) or 37.50 (12 hours) and long-context rates of 30 input, 3 cached and 112.50 output. Regional processing adds 10%. OpenAI had said eligible organisations would keep getting the latest Rosalind models. LiteLLM lists 922,000 input and 128,000 output tokens, function calling, reasoning, vision and structured output, and a `chatgpt/gpt-6-rosalind` Responses route; OpenAI has not published these limits.

## Strengths
- OpenAI's latest model for biology and drug-discovery reasoning.
- Built for tool-heavy research workflows.

## Limitations
- Approved organisations only, for internal research.
- Three times the price of `gpt-rosalind-research`.
- No OpenAI model page, benchmark results or knowledge cutoff yet, and no Artificial Analysis results.

## Good for
- Approved life sciences teams moving up from GPT-Rosalind for complex research.
