---
id: openai/text-davinci-edit-001
name: text-davinci-edit-001
owned_by: openai
type: llm
description: text-davinci-edit-001 was OpenAI's GPT-3 model for the instruction-driven edits endpoint, released free in beta in March 2022 and shut down with that endpoint on 4 January 2024.
aliases: [text-davinci-edit-001]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2022-03-15"
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://web.archive.org/web/20220317012035/https://openai.com/blog/gpt-3-edit-insert/
  - https://web.archive.org/web/20221117105411/https://beta.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# text-davinci-edit-001

## Overview
Shut down: OpenAI announced on 6 July 2023 that the edit models and the `/v1/edits` endpoint would be retired and shut them down on 4 January 2024, recommending `/v1/chat/completions`; the deprecations page now gives `gpt-4o` as the replacement model. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id and the details come from OpenAI's archived docs and announcement. OpenAI released it on 15 March 2022 with the edits endpoint, a free public beta that changes existing text by following an instruction instead of continuing it. A request took an `input` text and an `instruction` such as "Fix the spelling mistakes", and could ask for several variants. OpenAI's 2022 docs pitched it for translating, editing and tweaking text, and the launch post showed it changing tone or structure, fixing spelling and generating text from an empty input. OpenAI's archived Playground capped edit requests at 4,001 tokens and offered no length, penalty, best-of, stop or log-probability settings in edit mode.

## Strengths
- Edits from a plain instruction, with no prompt engineering for the rewrite.
- Free to use during the beta, per OpenAI.
- Worked on empty inputs too, giving completion-like generation.

## Limitations
- Shut down, together with the `/v1/edits` endpoint.
- OpenAI labelled text editing alpha in its 2022 docs and the endpoint beta.
- Few controls: no length limit, stop sequences or log probabilities in the Playground's edit mode.
- OpenAI published no training-data cutoff for it. Text in, text out only.

## Good for
- Recognising the id and `/v1/edits` calls in old code before moving them to a chat model.
