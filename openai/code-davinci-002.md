---
id: openai/code-davinci-002
name: code-davinci-002
owned_by: openai
type: llm
description: code-davinci-002 was OpenAI's most capable Codex model and the base model of the GPT-3.5 series, released in March 2022 with code insertion and shut down by early 2024.
aliases: [code-davinci-002]
context_length: 8001
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
  - https://web.archive.org/web/20230610144645/https://platform.openai.com/docs/models/codex
  - https://web.archive.org/web/20230603183535/https://platform.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20221117105411/https://beta.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20230603014855/https://platform.openai.com/docs/model-index-for-researchers
  - https://web.archive.org/web/20220317012035/https://openai.com/blog/gpt-3-edit-insert/
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# code-davinci-002

## Overview
Shut down: OpenAI's deprecations page lists code-davinci-002 twice, once with the Codex models shut down on 23 March 2023 (replacement now given as `gpt-4o`) and once with the base GPT models shut down on 4 January 2024 (replacement `gpt-3.5-turbo-instruct`, no price listed); it gives no reason for the two dates. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id and the details come from OpenAI's archived docs. OpenAI released it on 15 March 2022 as the latest Codex version, alongside text-davinci-002 and the insert capability. OpenAI's model index for researchers names it the base model of the GPT-3.5 series (text and code from before Q4 2021), good for pure code completion, with text-davinci-002 built on it. The 2023 docs call it the most capable Codex model, particularly good at translating natural language to code, with 8,001 tokens (8,000 in the 2022 docs) and training data up to June 2021. Codex models were trained on natural language and billions of lines of public GitHub code and were offered as a free trial.

## Strengths
- Most capable in Python and proficient in more than a dozen languages, including JavaScript, Go, Perl, PHP, Ruby, Swift, TypeScript, SQL and Shell, per OpenAI's docs.
- Inserted code between a prompt and a suffix, not only at the end.
- About twice the context of text-davinci-002.

## Limitations
- Shut down on OpenAI's API.
- A base model, which OpenAI recommended for pure code completion; text-davinci-002 was the instruction-tuned model built on it.
- Knowledge stops at June 2021. Text in, text out only.

## Good for
- Recognising the id in old code and logs before migrating them.
- Historical study of the base model behind text-davinci-002 and text-davinci-003.
