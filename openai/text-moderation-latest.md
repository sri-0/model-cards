---
id: openai/text-moderation-latest
name: text-moderation
owned_by: openai
type: llm
description: text-moderation-latest was OpenAI's automatically upgraded alias for its free text-only moderation classifier, last pointing to text-moderation-007, shut down on 27 October 2025 in favour of omni-moderation.
aliases: [text-moderation-latest, text-moderation-007]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
knowledge_cutoff: "2021-09"
sources:
  - https://developers.openai.com/api/docs/models/text-moderation-latest
  - https://developers.openai.com/api/docs/models/text-moderation-stable
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/moderation
  - https://github.com/openai/openai-python/blob/ece795f0c2dde3f483f9af9126d4c98adf789a8a/src/openai/types/moderation_create_params.py
  - https://github.com/openai/openai-python/blob/main/src/openai/types/moderation_model.py
  - https://web.archive.org/web/2022/https://openai.com/blog/new-and-improved-content-moderation-tooling/
  - https://arxiv.org/abs/2208.03274
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# text-moderation

## Overview
Shut down: OpenAI retired `text-moderation-latest`, its snapshot `text-moderation-007` and `text-moderation-stable` on 27 October 2025, after notifying developers on 28 April 2025, and names `omni-moderation` as the replacement. OpenRouter does not list it; the id is OpenAI's API id. It was the default model of the free moderation endpoint (/v1/moderations), a text-only classifier that flagged harmful content by category. OpenAI's SDK described it as automatically upgraded over time so callers always got the most accurate model; its final default snapshot was text-moderation-007, which this card also covers. OpenAI's model page gives text input and output, 32,768 max output tokens (the changelog added `max_tokens` to the moderation models on 16 October 2023) and a 1 September 2021 knowledge cutoff. The endpoint launched on 10 August 2022, scoring sexual, hateful, violent and self-harm content; OpenAI described the training approach in a paper on undesired content detection (arXiv 2208.03274).

## Strengths
- Free to call.
- Rolled forward automatically, so it tracked OpenAI's newest text moderation model without code changes.
- Built on OpenAI's taxonomy and active-learning pipeline for rare categories, per the paper.

## Limitations
- Shut down and no longer accessible.
- Text only; its successor added image input and, per OpenAI's changelog, two new text-only harm categories and more accurate scores.
- Automatic upgrades meant custom policies built on `category_scores` could need recalibration; OpenAI's moderation guide gives that warning for its continuously upgraded endpoint.

## Good for
- Recognising the id in old moderation pipelines and logs.
- Mapping legacy calls to omni-moderation-latest.
