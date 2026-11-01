---
id: cohere/rerank-4-fast
name: Rerank 4 Fast
owned_by: cohere
type: reranker
description: Cohere's previous-generation low-latency multilingual reranker (rerank-v4.0-fast), a lighter version of Rerank 4 Pro with the same 32,768-token query-plus-document window; superseded by Rerank 5 Fast.
aliases: [rerank-v4.0-fast, cohere-rerank-v4-fast, azure_ai/cohere-rerank-v4.0-fast]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
  tokenizer: Cohere
open_weights: false
license: proprietary
release_date: "2025-12-11"
sources:
  - https://openrouter.ai/cohere/rerank-4-fast
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://docs.cohere.com/docs/models
  - https://docs.cohere.com/docs/rerank
  - https://docs.cohere.com/docs/reranking-best-practices
  - https://cohere.com/blog/rerank-4
  - https://cohere.com/blog/rerank-5
  - https://blog.voyageai.com/2026/09/30/rerank-3/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Rerank 4 Fast

## Overview
Rerank 4 Fast (Cohere API id `rerank-v4.0-fast`) was announced on Cohere's blog on 2025-12-11 with Rerank 4 Pro. Cohere describes it as a lighter version of `rerank-v4.0-pro` for low-latency, high-throughput use, and now recommends `rerank-v5.0-fast` for new projects. OpenRouter lists it as `cohere/rerank-4-fast` with a 32,768-token context and prices it at $0.002 per search on its model page. Like Pro, it is multilingual, handles semi-structured data sent as YAML strings, and was trained with a 32,768-token context shared by query and document, with the query allowed up to half. Longer documents are split into 32,764-token chunks, and documents times chunks per document must stay within 10,000.

## Strengths
- Same 32,768-token window as Pro, enough for most documents to be ranked whole.
- Lower price per search than Rerank 4 Pro on OpenRouter ($0.002 against $0.0025).
- Multilingual, with the same semi-structured data support as Pro.

## Limitations
- Voyage reports rerank-3 5.74% and rerank-3-lite 5.25% ahead of it across 95 datasets.
- Cohere's own Rerank 5 Fast beats Rerank 4 Pro on its four headline benchmarks.
- Text only and proprietary.

## Good for
- Existing high-throughput pipelines tuned to Rerank 4 Fast.
- Reranking in agent loops and interactive search where latency matters.
- Multilingual reranking through OpenRouter.
