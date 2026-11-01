---
id: openai/gpt-rosalind-discovery
name: GPT-Rosalind Discovery
owned_by: openai
type: llm
description: gpt-rosalind-discovery is an OpenAI life sciences model id that appears only in OpenAI's pricing table for Rosalind models, at the same price as gpt-rosalind-research, with access limited to approved research organisations.
aliases: [gpt-rosalind-discovery, "chatgpt/gpt-rosalind-discovery"]
open_weights: false
license: proprietary
sources:
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/models/all
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-Rosalind Discovery

## Overview
`gpt-rosalind-discovery` is listed in the Life sciences models table of OpenAI's pricing page, next to `gpt-6-rosalind` and `gpt-rosalind-research`. OpenRouter does not list it, OpenAI's model catalogue and changelog do not mention it, and OpenAI has no model page for it; the id is OpenAI's pricing-page id and the name here is formed from it. The pricing page gives 5 USD input, 0.50 cached input and 25 USD output per million tokens, the same as `gpt-rosalind-research`, with no cache-write or long-context rates. It says access is limited to approved internal research through the GPT-Rosalind trusted-access programme. LiteLLM lists it for the OpenAI API and, as `chatgpt/gpt-rosalind-discovery`, for its ChatGPT-subscription provider on the Responses endpoint.

## Strengths
- Priced at a third of GPT-6 Rosalind's 15 USD input and 75 USD output per million tokens.

## Limitations
- No public description: what sets it apart from `gpt-rosalind-research` is undocumented.
- No published context window, output limit, modalities, knowledge cutoff or release date.
- Approved organisations only.
- No Artificial Analysis results.

## Good for
- Recognising the id in approved Rosalind deployments and billing records.
