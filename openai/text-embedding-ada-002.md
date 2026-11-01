---
id: openai/text-embedding-ada-002
name: Text Embedding Ada 002
owned_by: openai
type: embedding
description: text-embedding-ada-002 is OpenAI's December 2022 second-generation text embedding model, returning 1536-dimensional vectors, which replaced the five first-generation embedding model types and is now listed by OpenAI as an older model.
aliases: [text-embedding-ada-002, "openai/text-embedding-ada-002:batch", text-embedding-ada-002-v2, azure/text-embedding-ada-002, azure/eu/text-embedding-ada-002, azure/us/text-embedding-ada-002, github_copilot/text-embedding-ada-002, vercel_ai_gateway/openai/text-embedding-ada-002]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2022-12-15"
embedding_dimensions: 1536
mteb_score: 61.0
pricing:
  input: 0.1
  output: 0
sources:
  - https://openrouter.ai/openai/text-embedding-ada-002
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://developers.openai.com/api/docs/models/text-embedding-ada-002
  - https://developers.openai.com/api/docs/guides/embeddings
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://web.archive.org/web/2023/https://openai.com/blog/new-and-improved-embedding-model
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://github.com/MicrosoftDocs/azure-docs/blob/66b43614bc301725230b0d49ee867b5ae54e409c/articles/cognitive-services/openai/concepts/models.md
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Text Embedding Ada 002

## Overview
text-embedding-ada-002 was announced on 15 December 2022 as a single model replacing OpenAI's five first-generation embedding types (text similarity, text search query and document, code search text and code). OpenAI's catalogue now calls it an older embedding model, but it has no deprecation or shutdown date on the deprecations page. It takes text only and returns a 1536-dimensional vector; the third-generation `dimensions` parameter does not apply to it. OpenRouter lists it with an 8,192-token context at $0.10 per million input tokens, OpenAI's list price, and $0.05 for its `:batch` variant; OpenAI serves it on /v1/embeddings and Batch. Azure lists version 2 (8,192 tokens, parity with OpenAI's model) and an older version 1 (2,046 tokens), both with training data up to September 2021, and warns the two versions are not interchangeable. The `mteb_score` is OpenAI's own figure from its embeddings guide, which does not name the MTEB version.

## Strengths
- OpenAI's launch post says it outperformed all first-generation models on text search, code search and sentence similarity, and beat the old Davinci models at most tasks at a 99.8% lower price.
- Four times the first-generation context (8,192 against 2,048 tokens) and vectors one-eighth the size of davinci-001's.
- Widely supported: OpenAI, Azure, OpenRouter, GitHub Copilot and Vercel's gateway (LiteLLM catalogue).

## Limitations
- 61.0% on MTEB in OpenAI's guide, below text-embedding-3-small (62.3%) and text-embedding-3-large (64.6%), and 31.4 on MIRACL against 44.0 and 54.9 (Azure's table of OpenAI results).
- Five times text-embedding-3-small's price: 12,500 pages per dollar against 62,500.
- OpenAI said it did not beat text-similarity-davinci-001 on SentEval linear-probe classification.
- Moving to a third-generation model means generating new embeddings (Azure).

## Good for
- Existing vector stores built on 1536-dimensional ada-002 vectors.
- Applications pinned to Azure's version 2 deployment.
