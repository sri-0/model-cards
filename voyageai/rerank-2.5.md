---
id: voyageai/rerank-2.5
name: rerank-2.5
owned_by: voyageai
type: reranker
description: Voyage AI's previous-generation quality-tier reranker, the first Voyage reranker with instruction following, with a 32,000-token query-plus-document window; still served but superseded by rerank-3.
aliases: [rerank-2.5, voyage/rerank-2.5]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2025-08-11"
sources:
  - https://openrouter.ai/voyageai/rerank-2.5
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://docs.voyageai.com/docs/reranker
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2025/08/11/rerank-2-5/
  - https://blog.voyageai.com/2026/09/30/rerank-3/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# rerank-2.5

## Overview
rerank-2.5 was released on 2025-08-11 with rerank-2.5-lite, adding instruction following to Voyage's rerankers: natural-language instructions placed before or after the query, such as "This is an e-commerce application about cars". Voyage now lists it among earlier models still served by its API, and rerank-3 (2026-09-30) is its drop-in successor. OpenRouter lists `voyageai/rerank-2.5` with a 32,000-token context and a token price of 0. A query may hold 8,000 tokens, the query plus any one document 32,000 (eight times Cohere Rerank v3.5 at launch), and a request 1,000 documents and 600K total tokens. Voyage's pricing page lists it among older models at $0.05 per million processed tokens.

## Strengths
- Across 93 datasets in nine domains (NDCG@10), Voyage reported +7.94% over Cohere Rerank v3.5, +2.25% over Qwen3-Reranker-8B and +1.85% over rerank-2.
- Multilingual (51 datasets, 31 languages): +3.26% over Cohere v3.5 and +2.34% over Qwen3-Reranker-8B.
- Instructions raised accuracy by 8.13% on average across 24 in-house datasets; on MAIR it led Cohere v3.5 by 12.70%.

## Limitations
- rerank-3 improves on it by 0.96% overall and 3.35% on long documents at the same price.
- All figures are Voyage's own relative gains.
- Text only and proprietary.

## Good for
- Existing pipelines tuned to rerank-2.5 scores; rerank-3 keeps its score distribution.
- Instruction-guided reranking for domain-specific relevance.
- Long-document reranking.
