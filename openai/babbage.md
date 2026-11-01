---
id: openai/babbage
name: babbage
owned_by: openai
type: llm
description: babbage was a small original GPT-3 base model on OpenAI's API, a completion model without instruction tuning aimed at classification and search, shut down on 4 January 2024.
aliases: [babbage]
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
  - https://web.archive.org/web/20221231070937/https://openai.com/blog/openai-api/
  - https://web.archive.org/web/20230101110545/https://openai.com/blog/instruction-following/
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# babbage

## Overview
Shut down: after a 6 July 2023 notice, OpenAI shut `babbage` down on 4 January 2024, naming `babbage-002` as the replacement; `babbage-002` was itself shut down on 28 September 2026, with `gpt-5.6-terra` recommended. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id, and the details below come from its archived docs. The OpenAI API opened in private beta on 11 June 2020 running models with weights from the GPT-3 family. OpenAI's model index for researchers maps `babbage` to the GPT-3 paper's 1B model, with the caveat that the API model may differ slightly. OpenAI's 2023 docs describe it as capable of straightforward tasks, very fast, and lower cost, with a 2,049-token limit for prompt and completion and training data up to October 2019. By then GPT-3.5 had superseded the base GPT-3 models, but they were still the only ones open to fine-tuning. It cost $0.50 per million tokens on the Completions endpoint; fine-tuning cost $0.60 per million training tokens and $2.40 per million usage tokens.

## Strengths
- OpenAI's docs listed it for moderate classification and semantic search.
- The 2022 docs said Babbage was quite capable at ranking how well documents match search queries.

## Limitations
- Shut down, and models fine-tuned on it through the legacy `/v1/fine-tunes` endpoint stopped working on the same date.
- No instruction tuning; OpenAI said GPT-3 models had to be coaxed with carefully engineered prompts, and its Playground recommended the newer GPT-3 models.
- 2,049 tokens for prompt and output combined. Knowledge stops at October 2019. Text in, text out only.

## Good for
- Recognising the id in old code, logs and fine-tuned model names before migrating them.
- Cheap fine-tuning experiments of the 2020 to 2023 era, now only of historical interest.