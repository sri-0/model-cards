---
id: openai/text-babbage-001
name: text-babbage-001
owned_by: openai
type: llm
description: text-babbage-001 was OpenAI's small InstructGPT completion model in the GPT-3 series, formerly babbage-instruct-beta, aimed at fast, cheap classification and shut down on 4 January 2024.
aliases: [text-babbage-001, babbage-instruct-beta]
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
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# text-babbage-001

## Overview
Shut down: OpenAI announced on 6 July 2023 that older Completions models would be retired and shut text-babbage-001 down on 4 January 2024, naming `gpt-3.5-turbo-instruct` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id, and OpenAI's archived Playground lists `babbage-instruct-beta` as its former name. OpenAI's model index for researchers lists it among the InstructGPT models trained with FeedME, supervised fine-tuning on human-written demonstrations and on model samples rated 7/7 by labellers. OpenAI's 2023 docs describe it as capable of straightforward tasks, very fast and lower cost, with a 2,049-token limit for prompt and completion and training data up to October 2019. It cost $0.50 per million tokens on the Completions endpoint.

## Strengths
- Listed for moderate classification and semantic search.
- OpenAI's 2022 docs said Babbage handled simple classification and was quite capable at ranking how well documents match search queries.
- A fortieth of the Davinci models' $20 per million tokens.

## Limitations
- Shut down; the named replacement `gpt-3.5-turbo-instruct` was itself shut down on 28 September 2026.
- Meant for straightforward tasks; OpenAI ranked it below Curie and Davinci in capability.
- 2,049 tokens for prompt and output combined.
- Knowledge stops at October 2019. Text in, text out only.

## Good for
- Recognising the id or its beta name in old code and logs before migrating them.
