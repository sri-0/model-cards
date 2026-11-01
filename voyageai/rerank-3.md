---
id: voyageai/rerank-3
name: rerank-3
owned_by: voyageai
type: reranker
description: Voyage AI's quality-tier reranker, a drop-in successor to rerank-2.5 with a 32,000-token query-plus-document window, instruction following and the largest gains on long documents and code.
aliases: [rerank-3, voyage/rerank-3]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-09-30"
sources:
  - https://openrouter.ai/voyageai/rerank-3
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://docs.voyageai.com/docs/reranker
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2026/09/30/rerank-3/
  - https://cohere.com/blog/rerank-5
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# rerank-3

## Overview
rerank-3 and rerank-3-lite were released on 2026-09-30 as successors to rerank-2.5 and rerank-2.5-lite, with an updated backbone and training data mix but the same API, context and pricing, so the upgrade needs only the model name. OpenRouter lists `voyageai/rerank-3` with a 32,000-token context and a token price of 0. A query may hold up to 8,000 tokens, the query plus any one document up to 32,000, and a request up to 1,000 documents and 600K total tokens (query tokens times documents plus all document tokens). Voyage charges $0.05 per million of those tokens, about $0.0025 per 100-document request, with 200 million tokens free. Scores are calibrated to rerank-2.5's distribution, so existing thresholds still apply.

## Strengths
- Across 95 datasets in nine domains (NDCG@10, top-100 candidates from four first-stage retrievers), Voyage reports +0.96% over rerank-2.5, +2.72% over Cohere Rerank v4.0 Pro and +3.02% over Qwen3-Reranker-8B.
- Long documents (LongEmbed): +3.35% over rerank-2.5 and +13.84% over Cohere v4.0 Pro.
- Code: +2.17% and +2.11% over rerank-2.5 on voyage-3-large and voyage-4-large candidates; multilingual (51 datasets, 31 languages): +0.52%.

## Limitations
- All figures are Voyage's own relative gains; instruction following on MAIR is only on par with rerank-2.5.
- Cohere's Rerank 5 post measures an expected calibration error of 0.234 for rerank-3 on human labels, against 0.058 for Rerank 5 Pro.
- Text only and proprietary.

## Good for
- Second-stage ranking over BM25 or vector search results.
- Long-document and code retrieval.
- Drop-in upgrades from rerank-2.5.
