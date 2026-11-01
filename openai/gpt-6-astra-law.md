---
id: openai/gpt-6-astra-law
name: GPT-6 Astra Law
owned_by: openai
type: llm
description: gpt-6-astra-law is the API id of Astra for Law, OpenAI's configuration of GPT-6 Astra with a legal search index and instructions for legal analysis and writing, announced on 17 September 2026 for selected law firms.
aliases: [gpt-6-astra-law, "chatgpt/gpt-6-astra-law"]
open_weights: false
license: proprietary
release_date: "2026-09-17"
sources:
  - https://developers.openai.com/api/docs/pricing
  - https://web.archive.org/web/20261021182542/https://openai.com/index/astra-for-law/
  - https://web.archive.org/web/20260922172430/https://help.openai.com/en/articles/20001528-astra-for-law
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-6 Astra Law

## Overview
Astra for Law, announced on 17 September 2026, is not a separate model: OpenAI describes it as GPT-6 Astra combined with settings, tools and context for professional legal work, chiefly a legal search index and custom instructions for legal analysis and writing. It appears as "GPT-6 Astra Law" in the ChatGPT model picker and as `gpt-6-astra-law` in the API. OpenRouter does not list it and OpenAI has no model page for it; the id comes from OpenAI's announcement and pricing page. The index covers U.S. case law, statutes, regulations, court rules and administrative decisions across more than 230 million URLs, updated daily, including Free Law Project's CourtListener collection. Access started with selected U.S. law firms through Trusted Access in ChatGPT and Codex, for lawyers and people they supervise, with the API to follow; Harvey and Legora are named API customers. The pricing page lists 10 USD input, 1 USD cached input and 50 USD output per million tokens, promotional until at least 31 December 2026. LiteLLM lists 922,000 input and 128,000 output tokens and standard and pro reasoning modes.

## Strengths
- OpenAI reports 54.0% on 200 questions from Vals AI's Legal Research Bench at the highest reasoning effort, against 38.7% for GPT-6 Astra with web search alone.
- 24% more reference cases found on case-law questions (OpenAI's figures).
- Zero Data Retention on the API for eligible firms.

## Limitations
- Trusted-access law firms only.
- The index covers U.S. law only; OpenAI says to review answers and cited sources before relying on them.
- No Artificial Analysis results.

## Good for
- U.S. legal research and drafting by approved firms and legal technology products.
