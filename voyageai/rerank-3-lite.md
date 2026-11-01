---
id: voyageai/rerank-3-lite
name: rerank-3-lite
owned_by: voyageai
type: reranker
description: Voyage AI's latency-optimised reranker, a drop-in successor to rerank-2.5-lite with a 32,000-token query-plus-document window and instruction following, which Voyage says matches rerank-2.5 quality at 40% of its price.
aliases: [rerank-3-lite, voyage/rerank-3-lite]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-09-30"
sources:
  - https://openrouter.ai/voyageai/rerank-3-lite
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://docs.voyageai.com/docs/reranker
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2026/09/30/rerank-3/
  - https://cohere.com/blog/rerank-5
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# rerank-3-lite

## Overview
rerank-3-lite was released on 2026-09-30 with rerank-3, replacing rerank-2.5-lite with an updated backbone and training mix but the same API, context, instruction following and price, so switching needs only the model name. OpenRouter lists `voyageai/rerank-3-lite` with a 32,000-token context and a token price of 0. A query may hold up to 8,000 tokens, the query plus any one document up to 32,000, and a request up to 1,000 documents and 600K total tokens (query tokens times documents plus all document tokens). Voyage charges $0.02 per million of those tokens, about $0.001 per 100-document request, with 200 million tokens free. Scores are calibrated to rerank-2.5-lite's distribution, so existing thresholds still apply.

## Strengths
- Across 95 datasets in nine domains (NDCG@10), Voyage reports +1.10% over rerank-2.5-lite, +2.23% over Cohere Rerank v4.0 Pro, +5.25% over v4.0 Fast and +2.53% over Qwen3-Reranker-8B.
- Code: +3.72% and +3.58% over rerank-2.5-lite on two first-stage retrievers; long documents +1.86%.
- Instruction following on MAIR: +0.91% over rerank-2.5-lite and +2.34% over Cohere v4.0 Pro.

## Limitations
- All figures are Voyage's own relative gains.
- Cohere's Rerank 5 post measures an expected calibration error of 0.226 on human labels, against 0.058 for Rerank 5 Pro and Fast.
- Text only and proprietary.

## Good for
- Latency-sensitive reranking in search and agent loops.
- High-volume RAG where reranking cost matters.
- Drop-in upgrades from rerank-2.5-lite.
