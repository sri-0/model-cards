---
id: voyageai/voyage-3.5-lite
name: voyage-3.5-lite
owned_by: voyageai
type: embedding
description: Voyage AI's previous-generation low-cost text embedding model, released with voyage-3.5, with a 32,000-token input and 1024-dimensional default output; still served but superseded by voyage-4-lite.
aliases: [voyage-3.5-lite, voyage/voyage-3.5-lite]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
release_date: "2025-05-20"
embedding_dimensions: 1024
sources:
  - https://docs.voyageai.com/docs/embeddings
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2025/05/20/voyage-3-5/
  - https://openrouter.ai/api/v1/embeddings/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# voyage-3.5-lite

## Overview
voyage-3.5-lite is a previous-generation model: Voyage AI lists it among earlier models still served by its API, describing it as optimised for latency and cost, and recommends the Voyage 4 family, including voyage-4-lite, for new work. It was announced on 2025-05-20 with voyage-3.5. OpenRouter does not list it; the id is Voyage's API id under the voyageai prefix. Input is up to 32,000 tokens per text, with up to 1,000 texts and 1M tokens per request. Output is 1024 dimensions by default, or 256, 512 or 2048 through Matryoshka learning, as float, int8, uint8, binary or ubinary. Voyage's pricing page lists it among older models at $0.02 per million tokens, with no free tokens. Voyage published no MTEB score; its launch evaluation covered 100 datasets in eight domains by NDCG@10.

## Strengths
- Voyage reported average leads of 6.34% over OpenAI's text-embedding-3-large and 4.28% over voyage-3-lite.
- Within 0.3% of Cohere Embed v4 at one sixth of the cost, per Voyage.
- Binary rescoring improved on plain binary retrieval by up to 6.89%.

## Limitations
- Superseded by voyage-4-lite at the same price per token.
- Older-model pricing with no free tokens.
- Text only; proprietary.

## Good for
- Existing low-cost indexes built on voyage-3.5-lite.
- High-volume embedding with large per-request batches.
- Pipelines pinned to a known model version.
