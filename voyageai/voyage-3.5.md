---
id: voyageai/voyage-3.5
name: voyage-3.5
owned_by: voyageai
type: embedding
description: Voyage AI's previous-generation general-purpose and multilingual text embedding model, distilled from voyage-3-large, with a 32,000-token input and 1024-dimensional default output; still served but superseded by voyage-4.
aliases: [voyage-3.5, voyage/voyage-3.5]
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

# voyage-3.5

## Overview
voyage-3.5 was announced on 2025-05-20 with voyage-3.5-lite and distilled from voyage-3-large. Voyage now lists it among earlier models that remain available through its API, and recommends the Voyage 4 family for new work. OpenRouter does not list it; the id is Voyage's API id under the voyageai prefix. Input is up to 32,000 tokens per text, with up to 1,000 texts and 320K tokens per request. Output is 1024 dimensions by default, or 256, 512 or 2048 through Matryoshka learning, as float, int8, uint8, binary or ubinary. Voyage's pricing page lists it among older models at $0.06 per million tokens, with no free tokens. Voyage published no MTEB score; its launch evaluation covered 100 datasets in eight domains, including 62 multilingual datasets in 26 languages, scored by NDCG@10.

## Strengths
- Voyage reported average leads of 8.26% over OpenAI's text-embedding-3-large, 1.63% over Cohere Embed v4 and 2.66% over voyage-3.
- In int8 at 2048 dimensions it cut vector database costs by 83% against text-embedding-3-large at 3072 floats; binary at 1024 dimensions cut them by 99% and still scored 3.63% higher.
- Same price per token as voyage-4.

## Limitations
- Superseded: Voyage says its latest models are strictly better in quality, context, latency and throughput.
- Its launch comparisons predate Voyage 4, Gemini Embedding 2 and Cohere's Embed 5.
- No free tokens on older models.

## Good for
- Existing voyage-3.5 indexes that are not yet worth re-embedding.
- Multilingual retrieval with compact quantised vectors.
- Pipelines pinned to a known model version.
