---
id: openai/text-davinci-003
name: text-davinci-003
owned_by: openai
type: llm
description: text-davinci-003 was OpenAI's last InstructGPT completion model in the GPT-3.5 series, the only one trained with reinforcement learning from human feedback, shut down on 4 January 2024.
aliases: [text-davinci-003]
context_length: 4097
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
knowledge_cutoff: "2021-06"
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://web.archive.org/web/20230603183535/https://platform.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20230603014855/https://platform.openai.com/docs/model-index-for-researchers
  - https://web.archive.org/web/20230314223727/https://help.openai.com/en/articles/6779149-how-do-text-davinci-002-and-text-davinci-003-differ
  - https://web.archive.org/web/20230108144707/https://openai.com/blog/gpt-3-edit-insert/
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# text-davinci-003

## Overview
Shut down: OpenAI announced on 6 July 2023 that older Completions models would be retired and shut text-davinci-003 down on 4 January 2024, naming `gpt-3.5-turbo-instruct` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id and the details come from OpenAI's archived 2023 docs. OpenAI's model index for researchers places it in the GPT-3.5 series (text and code from before Q4 2021) as an improvement on text-davinci-002, and lists it as the one InstructGPT variant trained with PPO, reinforcement learning against reward models built from human comparisons. `gpt-3.5-turbo-0301` was in turn described as an improvement on it, optimised for chat. It ran on the Completions endpoint with 4,097 tokens shared by prompt and completion, training data up to June 2021, and a price of $20 per million tokens.

## Strengths
- Higher-quality writing, more complex instructions and better long-form output than text-davinci-002, per OpenAI's release note, at the same price as other Davinci models.
- Could insert text between a prompt and a suffix as well as append to it.
- The most capable GPT-3 series model in OpenAI's 2023 Playground notes.

## Limitations
- Shut down; the named replacement `gpt-3.5-turbo-instruct` was itself shut down on 28 September 2026, with `gpt-5.6-terra` recommended.
- 4,097 tokens for prompt and output combined.
- OpenAI's 2023 docs put `gpt-3.5-turbo` at a tenth of its cost.
- Text in, text out only: no chat format, tools or images, and knowledge stops at June 2021.

## Good for
- Recognising the id in old code, prompts and logs before migrating them to a current model.
- Historical comparison of OpenAI's instruction-tuning methods.
