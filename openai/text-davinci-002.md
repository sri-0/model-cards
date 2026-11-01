---
id: openai/text-davinci-002
name: text-davinci-002
owned_by: openai
type: llm
description: text-davinci-002 was OpenAI's March 2022 InstructGPT completion model, built on code-davinci-002 with supervised fine-tuning, and shut down on 4 January 2024.
aliases: [text-davinci-002]
context_length: 4097
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2022-03-15"
knowledge_cutoff: "2021-06"
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://web.archive.org/web/20230603183535/https://platform.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20221117105411/https://beta.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20230603014855/https://platform.openai.com/docs/model-index-for-researchers
  - https://web.archive.org/web/20220317012035/https://openai.com/blog/gpt-3-edit-insert/
  - https://web.archive.org/web/20230314223727/https://help.openai.com/en/articles/6779149-how-do-text-davinci-002-and-text-davinci-003-differ
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# text-davinci-002

## Overview
Shut down: OpenAI announced on 6 July 2023 that older Completions models would be retired and shut text-davinci-002 down on 4 January 2024, naming `gpt-3.5-turbo-instruct` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id and the details come from OpenAI's archived docs. OpenAI released it on 15 March 2022 as the latest GPT-3 version, alongside code-davinci-002 and the new insert capability. OpenAI's model index for researchers places it in the GPT-3.5 series as an InstructGPT model based on code-davinci-002, trained with FeedME: supervised fine-tuning on human-written demonstrations and on model samples rated 7/7 by labellers. The 2023 docs describe it as similar to text-davinci-003 but trained with supervised fine-tuning instead of reinforcement learning, with 4,097 tokens (4,000 per request in the 2022 docs) and training data up to June 2021. It cost $20 per million tokens on the Completions endpoint.

## Strengths
- The most capable GPT-3 model in OpenAI's 2022 docs, able to do any task the other GPT-3 models could, often with less context.
- Inserting completions within text, using a prompt and a suffix.
- Twice the context of the earlier 2,049-token GPT-3 models.

## Limitations
- Shut down; the named replacement `gpt-3.5-turbo-instruct` was itself shut down on 28 September 2026.
- text-davinci-003 superseded it with better writing and longer output at the same price.
- Text in, text out only: no chat format, tools or images, and knowledge stops at June 2021.

## Good for
- Recognising the id in old code, prompts and logs before migrating them.
- Historical comparison of OpenAI's FeedME and PPO instruction tuning.
