---
id: openai/code-davinci-001
name: code-davinci-001
owned_by: openai
type: llm
description: code-davinci-001 was the first Davinci-sized Codex code model on OpenAI's API, formerly davinci-codex, superseded by code-davinci-002 and shut down on 23 March 2023.
aliases: [code-davinci-001, davinci-codex]
context_length: 8001
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
knowledge_cutoff: "2021-06"
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://web.archive.org/web/20230610144645/https://platform.openai.com/docs/models/codex
  - https://web.archive.org/web/20221231201320/https://openai.com/blog/openai-codex/
  - https://web.archive.org/web/20230506030828/https://help.openai.com/en/articles/5480054-understanding-codex-training-data-and-outputs
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# code-davinci-001

## Overview
Shut down: OpenAI retired code-davinci-001 with its other Codex models on 23 March 2023; the deprecations page now gives `gpt-4o` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id, and OpenAI's archived Playground lists `davinci-codex` as its former name. OpenAI opened Codex to API developers in private beta on 10 August 2021, free during the initial period, describing it as a descendant of GPT-3 trained on natural language and billions of lines of public source code, including public GitHub repositories. OpenAI's 2023 docs list code-davinci-001 as the earlier version of code-davinci-002, with 8,001 tokens and training data up to June 2021; the Playground instead described its per-request limit as 4,096 tokens, double the usual 2,048. It could translate natural language to code as well as complete code.

## Strengths
- Most capable in Python and proficient in more than a dozen other languages, per OpenAI.
- OpenAI's launch post gave Codex a 14KB memory for Python code against GPT-3's 4KB.
- OpenAI's help centre reported that more than 99% of Codex output did not match its training data.

## Limitations
- Shut down on OpenAI's API, and superseded by code-davinci-002 before that.
- OpenAI's own sources disagree on its token limit (8,001 or 4,096).
- Knowledge stops at June 2021. Text in, text out only.

## Good for
- Recognising the id or the `davinci-codex` name in old code and logs before migrating them.
