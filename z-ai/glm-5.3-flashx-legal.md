---
id: z-ai/glm-5.3-flashx-legal
name: GLM-5.3-FlashX-Legal
owned_by: z-ai
type: llm
description: GLM-5.3-FlashX-Legal (GLM-Legal) is Z.ai's legal-domain version of GLM-5.3-FlashX, trained for legal research, contract review and drafting, available by application to selected enterprise customers.
aliases: [glm-5.3-flashx-legal]
capabilities: [tool_calling, reasoning, vision, structured_output]
architecture:
  input_modalities: [text, image, video, file]
  output_modalities: [text]
open_weights: false
sources:
  - https://docs.z.ai/guides/vlm/glm-5.3-flash
  - https://docs.z.ai/guides/overview/overview
  - https://docs.z.ai/guides/overview/pricing
  - https://huggingface.co/api/models?author=zai-org
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# GLM-5.3-FlashX-Legal

## Overview
GLM-5.3-FlashX-Legal, also called GLM-Legal, is Z.ai's model for professional legal work. OpenRouter does not list it and no weights are on Hugging Face; the id is Z.ai's API id `glm-5.3-flashx-legal`. Z.ai documents it on the GLM-5.3-Flash page, which gives the three model codes (`glm-5.3-flash`, `glm-5.3-flashx`, `glm-5.3-flashx-legal`) shared settings: a 1M-token context, image and video input, thinking that cannot be disabled, function calling, context caching and structured output. The legal model adds legal-domain mid-training on large legal datasets, then reinforcement learning in tens of thousands of task environments modelled on real legal workflows. API access is limited to selected enterprise customers who apply. Z.ai's price list matches GLM-5.3-FlashX: $0.37 input, $0.075 cached input and $1.25 output per million tokens.

## Strengths
- On the Harvey LAB legal-agent benchmark, Z.ai reports a 19.2% all-criteria pass rate, 12.5 points above the base model and the best open-source result in that evaluation.
- Cross-checks contracts, registry records and litigation files; analyses issues; reviews clauses across negotiation rounds; drafts documents.
- Designed to work with legal MCP services for laws, cases and company data, and Word drafting and revision tools with tracked changes.

## Limitations
- Gated: only selected enterprise customers can call it, after applying.
- No release date, parameter count or weights published; Artificial Analysis does not test it.
- A 19.2% pass rate means most Harvey LAB tasks are still not fully solved.

## Good for
- Law firms and legal teams running agent workflows for research, due diligence and contract review.
- First drafts of legal documents for professional review.
