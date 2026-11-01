---
id: voyageai/voyage-3-large
name: voyage-3-large
owned_by: voyageai
type: embedding
description: Voyage AI's previous-generation flagship general-purpose and multilingual text embedding model, with a 32,000-token input and 1024-dimensional default output; still served but superseded by voyage-4-large.
aliases: [voyage-3-large, voyage/voyage-3-large]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
release_date: "2025-01-07"
embedding_dimensions: 1024
sources:
  - https://docs.voyageai.com/docs/embeddings
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2025/01/07/voyage-3-large/
  - https://blog.voyageai.com/2026/01/15/voyage-4/
  - https://openrouter.ai/api/v1/embeddings/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# voyage-3-large

## Overview
voyage-3-large is a previous-generation model: Voyage AI lists it among earlier models still available through its API, and voyage-4-large (2026-01-15) is the current flagship. It was announced on 2025-01-07, and voyage-3.5 was later distilled from it. OpenRouter does not list it; the id is Voyage's API id under the voyageai prefix. Input is up to 32,000 tokens per text, with up to 1,000 texts and 120K tokens per request. Output is 1024 dimensions by default, or 256, 512 or 2048 through Matryoshka learning, as float, int8, uint8, binary or ubinary. Voyage's pricing page lists it among older models at $0.18 per million tokens, with no free tokens. Voyage published no MTEB score; its launch evaluation covered 100 datasets in eight domains, including 62 multilingual datasets in 26 languages, by NDCG@10.

## Strengths
- Voyage reported average leads of 9.74% over OpenAI's text-embedding-3-large and 20.71% over Cohere's embed-english-v3.0.
- Int8 at 1024 dimensions scored only 0.31% below full precision at 2048 with eight times less storage.
- At 512-dimension binary, 1/200 of OpenAI's float storage, it still led text-embedding-3-large by 1.16%.

## Limitations
- voyage-4-large is more accurate at a lower price ($0.12 against $0.18), per Voyage.
- Older-model pricing with no free tokens.
- Text only; proprietary.

## Good for
- Existing indexes built on voyage-3-large.
- Storage-constrained retrieval with quantised vectors.
- Pipelines pinned to a known model version.
