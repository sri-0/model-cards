---
id: openai/text-davinci-001
name: text-davinci-001
owned_by: openai
type: llm
description: text-davinci-001 was OpenAI's first Davinci-sized InstructGPT completion model, formerly davinci-instruct-beta-v3, trained with FeedME supervised fine-tuning and shut down on 4 January 2024.
aliases: [text-davinci-001, davinci-instruct-beta-v3]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://web.archive.org/web/20230603014855/https://platform.openai.com/docs/model-index-for-researchers
  - https://web.archive.org/web/20230101110545/https://openai.com/blog/instruction-following/
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# text-davinci-001

## Overview
Shut down: OpenAI announced on 6 July 2023 that older Completions models would be retired and shut text-davinci-001 down on 4 January 2024, naming `gpt-3.5-turbo-instruct` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id, and OpenAI's archived Playground lists `davinci-instruct-beta-v3` as its former name. OpenAI's model index for researchers groups it with text-davinci-002, text-curie-001 and text-babbage-001 as InstructGPT models trained with FeedME: supervised fine-tuning on human-written demonstrations and on model samples rated 7/7 by labellers. OpenAI's 27 January 2022 post made its InstructGPT models, by then in beta on the API for more than a year, the default language models on the API. The Playground called it an older version of the most capable GPT-3 model that could do any task the other GPT-3 models could, often with less context, and applied the default 2,049-token limit to it. It cost $20 per million tokens on the Completions endpoint.

## Strengths
- OpenAI's January 2022 post found its InstructGPT models much better than GPT-3 at following user intentions, and less prone to making up facts.
- Listed for complex intent, cause and effect, creative generation, search and summarisation for an audience.

## Limitations
- Shut down; the named replacement `gpt-3.5-turbo-instruct` was itself shut down on 28 September 2026.
- Superseded by text-davinci-002 and text-davinci-003, both with twice the context.
- OpenAI published no training-data cutoff for it in the sources read.
- Text in, text out only.

## Good for
- Recognising the id or its beta name in old code and logs before migrating them.
