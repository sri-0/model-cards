---
id: openai/text-ada-001
name: text-ada-001
owned_by: openai
type: llm
description: text-ada-001 was the smallest, fastest and cheapest instruction-following completion model in OpenAI's GPT-3 series, formerly ada-instruct-beta, shut down on 4 January 2024.
aliases: [text-ada-001, ada-instruct-beta]
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
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# text-ada-001

## Overview
Shut down: OpenAI announced on 6 July 2023 that older Completions models would be retired and shut text-ada-001 down on 4 January 2024, naming `gpt-3.5-turbo-instruct` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id, and OpenAI's archived Playground lists `ada-instruct-beta` as its former name. OpenAI's 2023 docs describe it as capable of very simple tasks, usually the fastest model in the GPT-3 series and the lowest cost, with a 2,049-token limit for prompt and completion and training data up to October 2019. It cost $0.40 per million tokens on the Completions endpoint. Unlike text-davinci-001, text-curie-001 and text-babbage-001, it is not in the FeedME row of OpenAI's model index for researchers, and the sources read do not say how it was tuned.

## Strengths
- Listed for parsing text, simple classification, address correction and keywords.
- OpenAI's 2022 docs said Ada suited creative tasks where creativity matters more than precision, and generating large amounts of test data such as names and addresses.
- The cheapest GPT-3 completion model, at a fiftieth of Davinci's price.

## Limitations
- Shut down; the named replacement `gpt-3.5-turbo-instruct` was itself shut down on 28 September 2026.
- OpenAI pitched Ada at tasks that need little nuance and said it often did better with more context.
- 2,049 tokens for prompt and output combined.
- Knowledge stops at October 2019. Text in, text out only.

## Good for
- Recognising the id or its beta name in old code and logs before migrating them.
