---
id: openai/text-moderation-stable
name: text-moderation-stable
owned_by: openai
type: llm
description: text-moderation-stable was OpenAI's slower-moving alias for its free text-only moderation classifier, updated only with advance notice, shut down on 27 October 2025 in favour of omni-moderation.
aliases: [text-moderation-stable]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
knowledge_cutoff: "2021-09"
sources:
  - https://developers.openai.com/api/docs/models/text-moderation-stable
  - https://developers.openai.com/api/docs/models/text-moderation-latest
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://github.com/openai/openai-python/blob/ece795f0c2dde3f483f9af9126d4c98adf789a8a/src/openai/types/moderation_create_params.py
  - https://github.com/openai/openai-python/blob/main/src/openai/types/moderation_model.py
  - https://web.archive.org/web/2022/https://openai.com/blog/new-and-improved-content-moderation-tooling/
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# text-moderation-stable

## Overview
Shut down: OpenAI retired `text-moderation-stable` on 27 October 2025, together with `text-moderation-latest` and `text-moderation-007`, after notifying developers on 28 April 2025, and names `omni-moderation` as the replacement. OpenRouter does not list it; the id is OpenAI's API id. It was the second model id of the free text-only moderation endpoint (/v1/moderations), which launched on 10 August 2022 to flag sexual, hateful, violent and self-harm content. OpenAI's SDK described the difference: `text-moderation-latest` (the default) upgraded automatically, while for `text-moderation-stable` OpenAI gave advance notice before updating the model, and its accuracy could be slightly lower. At shutdown both OpenAI model pages listed the same default snapshot, text-moderation-007, which sits on the text-moderation-latest card. The page gives text input and output, 32,768 max output tokens and a 1 September 2021 knowledge cutoff.

## Strengths
- Free to call.
- More predictable than the latest alias: OpenAI gave advance notice before updating the underlying model.

## Limitations
- Shut down and no longer accessible.
- OpenAI said its accuracy could be slightly lower than text-moderation-latest.
- Text only; omni-moderation-latest added image input, two new text-only harm categories and more accurate scores, per OpenAI's changelog.

## Good for
- Recognising the id in old moderation pipelines that pinned the stable alias.
- Mapping legacy calls to omni-moderation-latest.
