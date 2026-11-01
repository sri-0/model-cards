---
id: voyageai/voyage-context-4
name: voyage-context-4
owned_by: voyageai
type: embedding
description: Voyage AI's contextualized chunk embedding model, a mixture-of-experts model that embeds each chunk with its whole document's context, with built-in auto-chunking, a 120,000-token document limit and 1024-dimensional default output.
aliases: [voyage-context-4, voyage/voyage-context-4]
context_length: 120000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
release_date: "2026-06-29"
embedding_dimensions: 1024
sources:
  - https://docs.voyageai.com/docs/contextualized-chunk-embeddings
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2026/06/29/voyage-context-4/
  - https://openrouter.ai/api/v1/embeddings/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# voyage-context-4

## Overview
voyage-context-4 was announced on 2026-06-29 as a drop-in replacement for voyage-context-3. It reads a whole document in one pass and returns one vector per chunk, each reflecting both the chunk and the surrounding document. It uses a new mixture-of-experts backbone. OpenRouter does not list it; the id is Voyage's API id under the voyageai prefix. Each chunk may hold 32,000 tokens; with `enable_auto_chunking` the model splits documents itself (`chunk_size` defaults to 512 tokens, with optional overlap) and accepts up to 120K tokens per request, otherwise 32K. Output is 1024 dimensions by default, or 256, 512 or 2048, as float, int8, uint8, binary or ubinary. Voyage charges $0.12 per million tokens, down from $0.18 for voyage-context-3, with 200 million tokens free. Voyage publishes no MTEB score; its evaluation uses 39 datasets in eight domains by NDCG@10.

## Strengths
- Voyage reports +2.08% on chunk-level and +1.4% on document-level retrieval over voyage-context-3.
- Against single-vector models: +0.45% over voyage-4-large, +10.73% over Cohere Embed v4 and +28.80% over OpenAI's text-embedding-3-large.
- Removes the separate chunking step from RAG ingestion.

## Limitations
- Within 0.4 NDCG points of voyage-4-large in tech, code and finance rather than ahead.
- Uses its own contextualized embeddings endpoint, not the standard embeddings API.
- All figures are Voyage's own; text only and proprietary.

## Good for
- RAG over long documents where chunks lose meaning in isolation.
- Ingestion pipelines that want chunking handled by the model.
- Legal, medical and conversation retrieval, where Voyage reports it leads.
