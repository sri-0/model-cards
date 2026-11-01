---
id: openai/text-embedding-3-small
name: Text Embedding 3 Small
owned_by: openai
type: embedding
description: OpenAI's low-cost third-generation text embedding model, returning 1536-dimensional vectors that the dimensions parameter can shorten at creation time.
aliases: [text-embedding-3-small, openai/text-embedding-3-small:batch, azure/text-embedding-3-small]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2024-01-25"
embedding_dimensions: 1536
mteb_score: 62.3
pricing:
  input: 0.02
  output: 0
sources:
  - https://openrouter.ai/openai/text-embedding-3-small
  - https://openrouter.ai/api/v1/embeddings/models
  - https://developers.openai.com/api/docs/models/text-embedding-3-small
  - https://developers.openai.com/api/docs/guides/embeddings
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Text Embedding 3 Small

## Overview
text-embedding-3-small is the smaller of OpenAI's two third-generation embedding models; OpenAI's changelog records both as released on 2024-01-25, together with the `dimensions` parameter. OpenRouter lists it in its embeddings catalogue at $0.02 per million input tokens, the same as OpenAI's list price, served by OpenAI and Azure; its `:batch` variant costs $0.01. OpenAI calls it an improved, more performant version of the ada embedding model. It takes text only and returns a 1536-dimensional vector by default, which `dimensions` can shorten. Maximum input is 8,192 tokens per OpenAI's embeddings guide (LiteLLM's catalogue records 8,191), counted with the `cl100k_base` encoding. The `mteb_score` is OpenAI's own figure from that guide, which does not name the MTEB version.

## Strengths
- 62.3% on MTEB in OpenAI's guide, against 61.0% for text-embedding-ada-002.
- About 62,500 pages per dollar (at roughly 800 tokens a page), the most of OpenAI's embedding models.
- Shortened vectors keep their concept-representing properties, so a smaller index is a parameter change, not a new model.

## Limitations
- Text only; the model page lists image, audio and video input as not supported.
- Lower MTEB score than text-embedding-3-large (64.6%).
- No published knowledge cutoff or deprecation date.
- Free-tier limits are 100 requests and 40,000 tokens per minute.

## Good for
- High-volume retrieval, clustering and classification where cost per token matters most.
- Vector stores with a dimension limit, using `dimensions` to fit.
- One embedding model across OpenAI, Azure OpenAI and OpenRouter.
