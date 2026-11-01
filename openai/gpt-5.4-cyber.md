---
id: openai/gpt-5.4-cyber
name: GPT-5.4 Cyber
owned_by: openai
type: llm
description: GPT-5.4-Cyber was OpenAI's cyber-permissive fine-tune of GPT-5.4 for verified defenders in the top Trusted Access for Cyber tiers, introduced on 14 April 2026 and shut down on 1 October 2026.
aliases: [gpt-5.4-cyber]
open_weights: false
license: proprietary
release_date: "2026-04-14"
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://web.archive.org/web/20261001052046/https://openai.com/index/scaling-trusted-access-for-cyber-defense/
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# GPT-5.4 Cyber

## Overview
Shut down: OpenAI deprecated `gpt-5.4-cyber` on 11 September 2026 and removed it from the API on 1 October 2026, telling users to move to the most capable cyber model available to them. OpenRouter does not list it and OpenAI has no model page for it; the id comes from OpenAI's deprecations page. OpenAI introduced it on 14 April 2026, when it widened Trusted Access for Cyber (launched in February 2026) to thousands of verified individuals and hundreds of teams and added higher access tiers. Customers in the highest tiers got GPT-5.4-Cyber, a version of GPT-5.4 fine-tuned for extra cyber capability and fewer capability restrictions. OpenAI says it lowers the refusal boundary for legitimate security work and adds binary reverse engineering, so analysts can examine compiled software for malware, vulnerabilities and robustness without the source code. Rollout started with vetted security vendors, organisations and researchers.

## Strengths
- Fewer refusals than GPT-5.4 on dual-use defensive work.
- Binary reverse engineering for compiled software.

## Limitations
- Shut down; requests to the id fail.
- Highest-tier verified defenders only; OpenAI warned of limits on no-visibility uses such as Zero Data Retention, especially through third-party platforms.
- OpenAI published no context window, output limit, price or knowledge cutoff for it.
- No Artificial Analysis results.

## Good for
- Recognising the id in security tooling set up between April and October 2026.
- Planning a move to GPT-5.6 Cyber or another current cyber model.
