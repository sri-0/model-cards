---
id: voyageai/voyage-4-lite
name: voyage-4-lite
owned_by: voyageai
type: embedding
description: Voyage AI's low-latency, low-cost text embedding model in the Voyage 4 family, with a 32,000-token input, 1024-dimensional default output and the family's shared embedding space.
aliases: [voyage-4-lite, voyage/voyage-4-lite]
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
  input: 0.02
  output: 0
sources:
  - https://openrouter.ai/voyageai/voyage-4-lite
  - https://openrouter.ai/api/v1/embeddings/models
  - https://docs.voyageai.com/docs/embeddings
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2026/01/15/voyage-4/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# voyage-4-lite

## Overview
voyage-4-lite is the latency- and cost-optimised model of the Voyage 4 family, announced by Voyage AI on 2026-01-15; Voyage now lists voyage-3.5-lite as the previous generation. OpenRouter lists it in its embeddings catalogue at $0.02 per million input tokens, matching Voyage's price; the first 200 million tokens are free, and the Batch API takes 33% off. Input is up to 32,000 tokens per text, with up to 1,000 texts and 1M tokens per request. Output is 1024 dimensions by default, or 256, 512 or 2048 through Matryoshka learning, as float, int8, uint8, binary or ubinary; Voyage trained the family with quantisation in mind. Its vectors share one space with voyage-4-large, voyage-4 and the open-weight voyage-4-nano, so it can query an index built with a larger model. Voyage publishes no MTEB score.

## Strengths
- Voyage says it approaches voyage-3.5's retrieval accuracy with significantly fewer parameters.
- The cheapest Voyage 4 model, with the highest per-request token limit.
- Query-side partner for a voyage-4-large document index; Voyage reports quality improves across the board in that set-up.

## Limitations
- voyage-4-large leads it by an average of 4.80% on Voyage's RTEB evaluation.
- No text figures for its own scores; Voyage gives them only in charts.
- Text only and proprietary.

## Good for
- High-volume or latency-sensitive query embedding.
- Cost-sensitive RAG and semantic search.
- Large batch indexing where price per token dominates.
