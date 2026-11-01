---
id: openai/code-cushman-002
name: code-cushman-002
owned_by: openai
type: llm
description: code-cushman-002 was the later version of OpenAI's faster Cushman Codex code model, listed as deprecated in OpenAI's 2023 docs and shut down on 23 March 2023.
aliases: [code-cushman-002]
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
  - https://web.archive.org/web/20230603/https://openaiapi-site.azureedge.net/public-assets/d/73e99b463e/static/js/main.e66f2f5a.js
retrieved: "2026-11-01"
---

# code-cushman-002

## Overview
Shut down: OpenAI retired code-cushman-002 with its other Codex models on 23 March 2023; the deprecations page now gives `gpt-4o` as the replacement. OpenRouter does not list it and OpenAI no longer has a model page; the id is OpenAI's API id and the details come from OpenAI's archived June 2023 docs, which list it among the deprecated Codex models. Those docs describe it as almost as capable as Davinci Codex but slightly faster, a speed advantage that may suit real-time applications, with requests of up to 2,048 tokens and no training-data date; code-cushman-001 is listed as its earlier version. OpenAI's archived Playground code allowed it in the insert mode, alongside code-davinci-002 and text-davinci-003, and capped its requests at 8,001 tokens, which disagrees with the docs. Codex models were descendants of GPT-3, trained on natural language and billions of lines of public GitHub code.

## Strengths
- Lower latency than the Davinci Codex models, per OpenAI's description.
- Code insertion between a prompt and a suffix in the Playground.
- Most capable in Python and proficient in more than a dozen other languages, as OpenAI said of all Codex models.

## Limitations
- Shut down on OpenAI's API.
- OpenAI's sources disagree on its token limit (2,048 or 8,001).
- No published training-data cutoff, announcement or benchmark results.

## Good for
- Recognising the id in old code and logs before migrating them.
