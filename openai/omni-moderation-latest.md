---
id: openai/omni-moderation-latest
name: omni-moderation
owned_by: openai
type: llm
description: omni-moderation-latest is OpenAI's free moderation model, classifying text and images against 13 harm categories on the moderation endpoint or inline with generated responses.
aliases: [omni-moderation-latest, omni-moderation-2024-09-26]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2024-09-26"
sources:
  - https://developers.openai.com/api/docs/models/omni-moderation-latest
  - https://developers.openai.com/api/docs/guides/moderation
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# omni-moderation

## Overview
omni-moderation-latest was released on 2024-09-26 as OpenAI's new moderation model, supporting images as well as text, adding two text-only harm categories and giving more accurate scores (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API alias under the vendor prefix; it points to the snapshot omni-moderation-2024-09-26. OpenAI calls it its most capable moderation model. It is free, runs on /v1/moderations and Batch, and since 2026-06-04 can also score a Responses or Chat Completions request's input and output when a moderation object is passed. Results give a flagged boolean plus categories and category_scores for 13 categories: harassment, harassment/threatening, hate, hate/threatening, illicit, illicit/violent, self-harm, self-harm/intent, self-harm/instructions, sexual, sexual/minors, violence and violence/graphic. It replaced the text-moderation models, shut down on 2025-10-27.

## Strengths
- No charge for moderation calls.
- Six categories (the three self-harm ones, sexual, violence and violence/graphic) also score images, up to 20 MB per file.
- Inline moderation avoids a second request; tool-call arguments and outputs in the conversation are covered.

## Limitations
- Harassment, hate, illicit and sexual/minors categories are text only and score 0 for image-only input.
- Does not classify audio.
- OpenAI may upgrade the underlying model, so thresholds on category_scores can need recalibration.
- Not designed for detecting child sexual abuse material.
- Rate limits are low at the bottom tiers: 250 RPM, 5,000 RPD and 10,000 TPM free; 500 RPM and 20,000 TPM at Build.

## Good for
- Screening user prompts and uploaded images before they reach a model.
- Logging and routing generated output to human review.
- Policy checks in pipelines that cannot pay per call.
