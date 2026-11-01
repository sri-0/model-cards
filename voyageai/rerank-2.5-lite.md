---
id: voyageai/rerank-2.5-lite
name: rerank-2.5-lite
owned_by: voyageai
type: reranker
description: Voyage AI's previous-generation latency-optimised reranker with instruction following and a 32,000-token query-plus-document window; still served but superseded by rerank-3-lite.
aliases: [rerank-2.5-lite, voyage/rerank-2.5-lite]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2025-08-11"
sources:
  - https://openrouter.ai/voyageai/rerank-2.5-lite
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://docs.voyageai.com/docs/reranker
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2025/08/11/rerank-2-5/
  - https://blog.voyageai.com/2026/09/30/rerank-3/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# rerank-2.5-lite

## Overview
rerank-2.5-lite was released on 2025-08-11 alongside rerank-2.5 as the latency-optimised member of Voyage AI's 2.5 series, with the same instruction following: natural-language instructions placed before or after the query. Voyage now lists it among earlier models still served by its API, and rerank-3-lite (2026-09-30) is its drop-in successor. OpenRouter lists `voyageai/rerank-2.5-lite` with a 32,000-token context and a token price of 0. A query may hold 8,000 tokens, the query plus any one document 32,000, and a request 1,000 documents and 600K total tokens. Voyage's pricing page lists it among older models at $0.02 per million processed tokens.

## Strengths
- Across 93 datasets in nine domains (NDCG@10), Voyage reported +7.16% over Cohere Rerank v3.5, +1.47% over Qwen3-Reranker-8B and +1.08% over rerank-2; Voyage notes it beat the 8B Qwen model at over an order of magnitude smaller.
- 3.40% ahead of rerank-2-lite at the same price.
- Instructions raised accuracy by 7.55% on average across 24 in-house datasets; on MAIR it led Cohere v3.5 by 10.36%.

## Limitations
- rerank-3-lite improves on it by 1.10% overall at the same price.
- Multilingual gains were smaller: +1.93% over Cohere v3.5 and +1.01% over Qwen3-Reranker-8B.
- All figures are Voyage's own; text only and proprietary.

## Good for
- Existing low-latency pipelines tuned to rerank-2.5-lite scores.
- Cost-sensitive reranking with instructions.
- High-throughput search over long documents.
