---
id: openai/text-curie-001
name: text-curie-001
owned_by: openai
type: llm
description: text-curie-001 was OpenAI's mid-sized InstructGPT completion model in the GPT-3 series, formerly curie-instruct-beta-v2, priced at a tenth of Davinci and shut down on 4 January 2024.
aliases: [text-curie-001, curie-instruct-beta-v2]
context_length: 2049
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
knowledge_cutoff: "2019-10"
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://web.archive.org/web/20230603183535/https://platform.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20221117105411/https://beta.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20230603014855/https://platform.openai.com/docs/model-index-for-researchers
  - https://web.archive.org/web/20230101110545/https://openai.com/blog/instruction-following/
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# text-curie-001

## Overview
Shut down: OpenAI announced on 6 July 2023 that older Completions models would be retired and shut text-curie-001 down on 4 January 2024, naming `gpt-3.5-turbo-instruct` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id, and OpenAI's archived Playground lists `curie-instruct-beta-v2` as its former name. OpenAI's model index for researchers lists it among the InstructGPT models trained with FeedME, supervised fine-tuning on human-written demonstrations and on model samples rated 7/7 by labellers; OpenAI's 27 January 2022 post made such InstructGPT models the API's default. OpenAI's 2023 docs describe it as very capable, faster and lower cost than Davinci, with a 2,049-token limit for prompt and completion and training data up to October 2019. It cost $2 per million tokens on the Completions endpoint, a tenth of the Davinci models.

## Strengths
- Listed for language translation, complex classification, sentiment and summarisation.
- OpenAI's 2022 docs said Curie could do many of Davinci's tasks faster and at a tenth of the cost, and handled question answering and general service chatbots well.

## Limitations
- Shut down; the named replacement `gpt-3.5-turbo-instruct` was itself shut down on 28 September 2026.
- 2,049 tokens for prompt and output combined, half of text-davinci-002 and text-davinci-003.
- OpenAI's docs said Davinci was stronger at analysing complicated text.
- Knowledge stops at October 2019. Text in, text out only.

## Good for
- Recognising the id or its beta name in old code and logs before migrating them.
