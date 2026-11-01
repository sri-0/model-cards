---
id: mistralai/mistral-embed-2312
name: Mistral Embed 2312
owned_by: mistralai
type: embedding
description: Mistral AI's general-purpose text embedding model (version 23.12), returning 1024-dimensional unit-norm vectors over an 8k-token input.
aliases: [mistral-embed-2312, mistral-embed, mistral/mistral-embed-2312, mistral/mistral-embed]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Mistral
open_weights: false
license: proprietary
release_date: "2023-12-11"
embedding_dimensions: 1024
pricing:
  input: 0.1
  output: 0
sources:
  - https://openrouter.ai/mistralai/mistral-embed-2312
  - https://openrouter.ai/api/v1/embeddings/models
  - https://docs.mistral.ai/models/mistral-embed-23-12
  - https://docs.mistral.ai/models
  - https://docs.mistral.ai/studio/knowledge-rag/embeddings/text_embeddings
  - https://docs.mistral.ai/inference/pricing
  - https://mistral.ai/pricing
  - https://mistral.ai/news/la-plateforme
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mistral Embed 2312

## Overview
Mistral Embed (version 23.12) launched with Mistral's La Plateforme on 2023-12-11. OpenRouter lists it in its embeddings catalogue as `mistralai/mistral-embed-2312` at $0.1 per million input tokens, served by Mistral. Mistral's model page gives the API id `mistral-embed-2312` with `mistral-embed` as its alias, an 8k-token context (8,192 on OpenRouter) and the `/v1/embeddings` and `/v1/batch` endpoints. Mistral describes it as a general-purpose model that turns sentences and paragraphs into vectors for retrieval, classification and similarity search. Every embedding has 1024 dimensions and norm 1, so cosine similarity, dot product and Euclidean distance rank results the same way. Mistral's pricing docs list $0.1 per million tokens ($0.01 cached), and its pricing page gives batch processing a 50% discount. The launch post reports an MTEB retrieval score of 55.26; Mistral publishes no MTEB mean score, so the card has no `mteb_score`.

## Strengths
- $0.1 per million tokens, halved through the batch API.
- Unit-norm output works with any similarity metric in a vector store.
- One vendor for embeddings and chat when a pipeline already uses Mistral models.

## Limitations
- Fixed 1024-dimension output; the text embeddings page documents no `output_dimension` or `output_dtype` options, unlike Codestral Embed.
- No published language list or knowledge cutoff.
- Proprietary and API only; no open weights.
- Version 23.12 is still Mistral's only general-purpose text embedding model.

## Good for
- Retrieval-augmented generation and semantic search on Mistral's platform.
- Clustering and classification of short to medium texts.
- Pipelines that already use Mistral's chat models.
