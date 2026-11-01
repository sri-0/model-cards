---
id: voyageai/voyage-4
name: voyage-4
owned_by: voyageai
type: embedding
description: Voyage AI's mid-sized general-purpose and multilingual text embedding model in the Voyage 4 family, with a 32,000-token input, 1024-dimensional default output and an embedding space shared with voyage-4-large, voyage-4-lite and voyage-4-nano.
aliases: [voyage-4, voyage/voyage-4]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-01-15"
embedding_dimensions: 1024
pricing:
  input: 0.06
  output: 0
sources:
  - https://openrouter.ai/voyageai/voyage-4
  - https://openrouter.ai/api/v1/embeddings/models
  - https://docs.voyageai.com/docs/embeddings
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2026/01/15/voyage-4/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# voyage-4

## Overview
voyage-4 is the mid-sized model of the Voyage 4 family that Voyage AI (a MongoDB company) announced on 2026-01-15; it succeeds voyage-3.5, which Voyage now lists as a previous generation. OpenRouter lists it in its embeddings catalogue at $0.06 per million input tokens, the same as Voyage's own price, and Voyage gives each account its first 200 million tokens free. Input is up to 32,000 tokens per text, with up to 1,000 texts and 320K tokens per request. Output is 1024 dimensions by default, or 256, 512 or 2048 through Matryoshka learning, as float, int8, uint8, binary or ubinary. All Voyage 4 models share one embedding space, so documents embedded with voyage-4-large can be searched with voyage-4 queries. Voyage's Batch API takes 33% off with a 12-hour completion window. Voyage publishes no MTEB score; its own evaluation uses RTEB's 29 datasets and eight domains, scored by NDCG@10.

## Strengths
- Voyage says it approaches the retrieval quality of voyage-3-large; voyage-4-large leads it by an average of 1.87%.
- Shared embedding space allows asymmetric retrieval: index with voyage-4-large, query with voyage-4.
- Quantised and shortened vectors cut storage without changing models.

## Limitations
- Text only; images need voyage-multimodal-3.5.
- Voyage's charts give its scores against OpenAI, Cohere and Gemini models only as bars, not text figures.
- Proprietary; voyage-4-nano is the open-weight member of the family.

## Good for
- General-purpose and multilingual semantic search and RAG.
- Query-side embedding against a voyage-4-large document index.
- One embedding family at several price points: voyage-4-lite at $0.02 and voyage-4-large at $0.12 per million tokens.
