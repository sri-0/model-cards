---
id: openai/gpt-5.5-cyber
name: GPT-5.5 Cyber
owned_by: openai
type: llm
description: GPT-5.5-Cyber is OpenAI's more permissive and more capable cybersecurity model of the GPT-5.5 generation, released in full on 22 June 2026 to verified defenders through a limited trusted-access release.
aliases: [gpt-5.5-cyber, gpt-5.5-cyber-preview]
open_weights: false
license: proprietary
release_date: "2026-06-22"
sources:
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/models/gpt-5.6-cyber
  - https://web.archive.org/web/20261020235309/https://openai.com/index/daybreak-securing-the-world/
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.5 Cyber

## Overview
GPT-5.5-Cyber is an approval-only OpenAI model for advanced, authorised cybersecurity work. OpenRouter does not list it and OpenAI has no model page for it; the id `gpt-5.5-cyber` comes from OpenAI's pricing page, which lists it under Cyber models at 12.50 USD input, 1.25 cached input and 75 USD output per million tokens, with no cache-write or long-context rates. LiteLLM also lists `gpt-5.5-cyber-preview` at the same price. OpenAI's Daybreak post of 22 June 2026 says an initial permissive-only preview came first, aimed at cutting unnecessary refusals, and the full version followed through a continued limited release to trusted defenders. OpenAI says it keeps GPT-5.5's general-purpose intelligence and long-task ability, and that the US Center for AI Standards and Innovation (CAISI) ran pre-deployment testing on it. The deprecations page does not list it, but OpenAI now calls GPT-5.6 Cyber its most advanced cyber model.

## Strengths
- OpenAI reports 85.6% on CyberGym in single-model evaluations, against 81.8% for GPT-5.5, the highest it had measured from one model.
- 39.5% on ExploitGym against 25.95% for GPT-5.5, and 69.8% on SEC-bench Pro against 63.1% (OpenAI's figures).

## Limitations
- For verified defenders only, with stronger verification, monitoring, scoped controls and review; OpenAI says most defenders should start with GPT-5.5 under Trusted Access for Cyber.
- No published context window, output limit, modalities or knowledge cutoff.
- 2.5 times GPT-5.5's 5 USD input and 30 USD output prices (OpenAI's comparison table).
- No Artificial Analysis results.

## Good for
- Approved teams finding, reproducing and patching vulnerabilities.
- Recognising the id in Daybreak deployments set up before GPT-5.6 Cyber.
