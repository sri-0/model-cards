---
id: openai/gpt-6-luna-decisions
name: GPT-6 Luna Decisions
owned_by: openai
type: llm
description: GPT-6 Luna Decisions is GPT-6 Luna served through OpenAI's Decisions API, which returns typed, probabilistic answers (predicates, choices and scores) about text, JSON and images instead of generated text.
aliases: [openai/gpt-6-luna-decisions-20261006]
context_length: 1050000
max_output_tokens: 945000
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [decisions]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-10-06"
knowledge_cutoff: "2026-05"
pricing:
  input: 0.1
  output: 0
  cache_read: 0
  cache_write: 0
sources:
  - https://openrouter.ai/openai/gpt-6-luna-decisions
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models/openai/gpt-6-luna-decisions-20261006/endpoints
  - https://developers.openai.com/api/docs/guides/decisions
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/models/gpt-6-luna
retrieved: "2026-11-01"
---

# GPT-6 Luna Decisions

## Overview
OpenRouter lists GPT-6 Luna Decisions as GPT-6 Luna served through OpenAI's Decisions API, on its `/api/alpha/decisions` endpoint. It is not a separate model: OpenAI's API calls it with `model: "gpt-6-luna"` on `POST /v1/decisions`, the only model that endpoint supports, and the GPT-6 Luna card covers the model itself. The API was released in beta on 6 October 2026 and became generally available on 22 October 2026. A request carries shared `input` (a string, or messages with text, images, JSON via `input_json`, and tool calls with their outputs) and 1 to 400 named `questions`. Each question is a `predicate` (probability from 0 to 1 that a condition holds), a `choice` (one supplied value, with per-option probabilities and a confidence) or a `score` (2 to 10 ordered levels, returned as a probability-weighted average). Answers can also be refusals. OpenAI says it answers about 10 times faster than the Responses API. OpenRouter gives a 1,050,000-token context and the knowledge cutoff is GPT-6 Luna's 18 May 2026.

## Strengths
- Uncached input costs 0.10 USD per million tokens and output is free (OpenAI and OpenRouter).
- Typed, probabilistic answers for classifying content, routing requests and prioritising work, with no text to parse.
- Prompt caching of shared input (prefix of at least 1,024 tokens), Zero Data Retention and HIPAA eligibility, and native use from GPT-Live.

## Limitations
- Cannot generate text or JSON objects; OpenAI points to Structured Outputs for that.
- No files, audio or `file_id` inputs; dependent questions need separate requests.
- OpenRouter lists cache reads and writes at 0, while OpenAI bills cache writes at GPT-6 Luna's rates. OpenRouter also lists 0.01 USD per web search.
- No Artificial Analysis results for this API.

## Good for
- Content classification, request routing and rubric scoring at high volume.
