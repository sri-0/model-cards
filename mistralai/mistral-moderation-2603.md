---
id: mistralai/mistral-moderation-2603
name: Mistral Moderation 2
owned_by: mistralai
type: llm
description: Mistral Moderation 2 is Mistral AI's free, API-only text moderation classifier of March 2026 with a 128k context and a jailbreaking category, and it backs Mistral's custom guardrails.
aliases: [mistral-moderation-2603, mistral/mistral-moderation-2603, mistral-moderation-2411]
context_length: 128000
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2026-03-01"
sources:
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mistral-moderation-26-03
  - https://docs.mistral.ai/models/mistral-moderation-24-11
  - https://docs.mistral.ai/studio/safety-moderation
  - https://docs.mistral.ai/inference/pricing
  - https://docs.mistral.ai/resources/changelogs
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mistral Moderation 2

## Overview
Mistral Moderation 2 (version 26.03, API id mistral-moderation-2603) is dated 1 March 2026 on Mistral's model page; the changelog records its release on 12 March 2026. OpenRouter does not list it and there are no weights, so the id is the vendor API id under the vendor prefix. It is a GA Premier classifier served on /v1/moderations and the batch API, with a 128k context, and Mistral's pricing page lists it as free. It replaces Mistral Moderation 24.11 (mistral-moderation-2411, 8k context, deprecated 31 March 2026 and retired 30 June 2026), whose id is an alias here. The raw-text endpoint scores single strings or small batches; the conversational endpoint scores chat turns. Each response gives per-category scores and flags against thresholds Mistral tuned on an internal test set. It is not a chat model and has no tool calling, reasoning, vision or structured output.

## Strengths
- Eleven categories: sexual, hate and discrimination, violence and threats, dangerous, criminal, self-harm, health, financial, law, PII and jailbreaking.
- Mistral describes strong results on complex multilingual data, including long multi-turn conversations.
- Backs custom guardrails (moderation_llm_v2) declared on chat completions, conversations or agents, with per-category thresholds and a 403 on a block, so no separate call is needed.
- Free on Mistral's API.

## Limitations
- Text only; Mistral's image-capable moderation model is the self-hosted Shieldstral 1.0.
- Guardrails apply to inputs only, not model outputs.
- Mistral says it will keep changing the underlying model, so policies built on raw category_scores may need recalibration.
- No published benchmark figures and no Artificial Analysis results.

## Good for
- Input and output screening around any model served through Mistral's API.
- Jailbreak detection on user prompts.
- Flagging requests for tailored medical, legal or financial advice.
