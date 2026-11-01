---
id: cohere/rerank-v5.0-pro
name: Rerank 5 Pro
owned_by: cohere
type: reranker
description: Cohere's highest-quality reranker (Rerank 5 generation), a roughly 2B-parameter multilingual model with a 32,768-token query-plus-document window, calibrated 0-1 relevance scores and Context Focus passage extraction.
aliases: [rerank-v5.0-pro, Cohere-rerank-v5-pro]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
open_weights: false
license: proprietary
release_date: "2026-10-21"
sources:
  - https://docs.cohere.com/docs/rerank
  - https://docs.cohere.com/docs/models
  - https://docs.cohere.com/docs/rerank-overview
  - https://docs.cohere.com/reference/rerank
  - https://docs.cohere.com/docs/reranking-best-practices
  - https://cohere.com/blog/rerank-5
  - https://cohere.com/pricing
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Rerank 5 Pro

## Overview
Rerank 5 Pro (`rerank-v5.0-pro`) was announced on 2026-10-21 with the lighter `rerank-v5.0-fast`; Cohere now recommends both over Rerank 4 for new projects. OpenRouter does not list Rerank 5 (it lists Cohere's Rerank 4 Pro, Rerank 4 Fast and Rerank v3.5); the id is Cohere's API id. It is a proprietary model of about 2B parameters (Fast is about 500M). The 32,768-token limit covers the query and one document together; longer documents are truncated to `max_tokens_per_doc` (default 4,096). A request accepts up to 10,000 documents, though the API reference recommends no more than 1,000. Input is text, with semi-structured data passed as YAML strings, in 100+ languages. Each result has a calibrated score from 0 to 1, where Cohere treats 0.50 as the "useful" cutoff. Context Focus, off by default, also returns the most relevant spans in each document (`relevant_spans` with a threshold and `max_spans`). Cohere's launch price is $0.05 per million tokens ($0.02 for Fast).

## Strengths
- Cohere reports 82.2 on BRIGHT, 5.8 points above Voyage rerank-3 and 12.4 above Rerank 4 Pro, and leads on BEIR by 1.8 points over the strongest external model.
- Parsed PDFs (47 datasets): 89.9, against 88.4 for Voyage rerank-3 and 88.3 for Rerank 4 Pro.
- Expected calibration error of 0.058 on human labels, against 0.384 for Rerank 4 Pro.
- Context Focus kept 96% of answer quality with half the context removed.

## Limitations
- Text only; no instructions that change how relevance is judged.
- All figures are Cohere's own; no absolute BEIR score is published.
- Context Focus suits targeted queries, not summarisation, and splits tables and code less cleanly.

## Good for
- Reranking keyword, vector or hybrid search results without re-indexing.
- Selecting and trimming RAG context for LLMs and agents.
- Setting one relevance threshold across queries and domains.
