---
id: openai/gpt-rosalind-research
name: GPT-Rosalind
owned_by: openai
type: llm
description: GPT-Rosalind (API id gpt-rosalind-research) is OpenAI's life sciences reasoning model for biology, drug discovery and translational medicine, introduced in April 2026 and available only to approved organisations through a trusted-access programme.
aliases: [gpt-rosalind-research]
open_weights: false
license: proprietary
release_date: "2026-04-16"
sources:
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://web.archive.org/web/20261021124314/https://openai.com/index/introducing-gpt-rosalind/
  - https://web.archive.org/web/20261003193352/https://openai.com/gpt-rosalind/
  - https://web.archive.org/web/20261013202201/https://help.openai.com/en/articles/20001193-gpt-rosalind-for-life-sciences-research
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-Rosalind

## Overview
GPT-Rosalind is listed in OpenAI's model catalogue under Life sciences with the model id `gpt-rosalind-research`, linking to the pricing page rather than a model page. OpenRouter does not list it; the id is OpenAI's. OpenAI introduced it on 16 April 2026 as the first model in a life sciences series, built for chemistry, protein engineering and genomics and for tool use in multi-step scientific work, and named it after Rosalind Franklin. It started as a research preview for qualified US Enterprise customers in ChatGPT, Codex and the API. OpenAI's changelog made `gpt-rosalind-research` generally available through the trusted-access programme on 8 September 2026, and the announcement's 11 September update opened it to eligible organisations worldwide, with published pricing from 5 October 2026: 5 USD input, 0.50 cached input and 25 USD output per million tokens. OpenAI released GPT-6 Rosalind on 30 October 2026.

## Strengths
- OpenAI reports leading BixBench results among models with published scores, and wins over GPT-5.4 on 6 of 11 LABBench2 tasks, most clearly CloningQA.
- In a Dyno Therapeutics RNA test, best-of-ten submissions ranked above the 95th percentile of human experts on prediction.
- Works with the Codex Life Sciences Research plugin (more than 50 tools and data sources).

## Limitations
- Approved organisations only; API use is for internal research tools, not customer-facing or external commercial products.
- OpenAI publishes no context window, output limit, modalities or knowledge cutoff.
- No Artificial Analysis results.

## Good for
- Literature review, sequence-to-function work and experiment planning in governed research teams.
