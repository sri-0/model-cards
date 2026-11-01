---
id: openai/code-cushman-001
name: code-cushman-001
owned_by: openai
type: llm
description: code-cushman-001 was OpenAI's faster, smaller Codex code model, formerly cushman-codex and mapped by OpenAI to the 12B Codex paper model, shut down on 23 March 2023.
aliases: [code-cushman-001, cushman-codex]
context_length: 2048
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://web.archive.org/web/20230610144645/https://platform.openai.com/docs/models/codex
  - https://web.archive.org/web/20221117105411/https://beta.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20230603014855/https://platform.openai.com/docs/model-index-for-researchers
  - https://web.archive.org/web/20221231201320/https://openai.com/blog/openai-codex/
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# code-cushman-001

## Overview
Shut down: OpenAI retired code-cushman-001 with its other Codex models on 23 March 2023; the deprecations page now gives `gpt-4o` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id, and OpenAI's archived Playground lists `cushman-codex` as its former name. OpenAI's model index for researchers maps it to Codex 12B from the July 2021 paper "Evaluating Large Language Models Trained on Code", calling it a stronger, multilingual version of that model; the 12B figure is the paper's and may differ slightly from the API model. OpenAI's 2022 docs described it as almost as capable as Davinci Codex but slightly faster, with requests of up to 2,048 tokens, and the 2023 docs list it as the earlier version of code-cushman-002. Codex models were trained on natural language and billions of lines of public GitHub code and were offered as a free trial.

## Strengths
- Lower latency than the Davinci Codex models; OpenAI suggested it for real-time applications.
- Most capable in Python and proficient in more than a dozen other languages, per OpenAI.
- One of the few API models OpenAI matched to a model in one of its papers.

## Limitations
- Shut down on OpenAI's API.
- Requests of up to 2,048 tokens, a quarter of code-davinci-002.
- OpenAI published no training-data cutoff for it.
- Text in, text out only.

## Good for
- Recognising the id or the `cushman-codex` name in old code and logs before migrating them.
- Historical comparison with the Codex 12B paper results.
