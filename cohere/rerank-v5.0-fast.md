---
id: cohere/rerank-v5.0-fast
name: Rerank 5 Fast
owned_by: cohere
type: reranker
description: Cohere's low-latency Rerank 5 model, a roughly 500M-parameter multilingual reranker with a 32,768-token query-plus-document window, calibrated 0-1 relevance scores and Context Focus passage extraction.
aliases: [rerank-v5.0-fast, Cohere-rerank-v5-fast]
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
  - https://docs.cohere.com/docs/reranking-best-practices
  - https://docs.cohere.com/changelog/rerank-v5
  - https://cohere.com/blog/rerank-5
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Rerank 5 Fast

## Overview
Rerank 5 Fast (`rerank-v5.0-fast`) was announced on 2026-10-21 with Rerank 5 Pro, as the tier for low-latency, high-throughput work such as high-volume search and agents that run many searches per task. Cohere recommends it over `rerank-v4.0-fast` for new projects. OpenRouter does not list Rerank 5; the id is Cohere's API id. It is a proprietary model of about 500M parameters. The 32,768-token window is shared by the query and each document; documents are truncated to `max_tokens_per_doc` (default 4,096), and a request takes up to 10,000 documents. Input is text, with semi-structured data sent as YAML strings, in 100+ languages. Scores are calibrated from 0 to 1, with 0.45 as Cohere's "useful" cutoff for Fast, and Context Focus (`relevant_spans`) can return the most relevant passages. It shares Pro's endpoint and request format. Cohere's launch price is $0.02 per million tokens.

## Strengths
- Cohere says it outperforms its previous flagship, Rerank 4 Pro, and beats Voyage rerank-3-lite and Qwen3-Reranker-0.6B and 8B on its four headline benchmarks.
- About 187 standard 1,000-token documents per second on one A100, 2.9 times Pro's throughput.
- Expected calibration error of 0.058 on human labels, the same as Pro; 88.5 on Cohere's parsed-PDF suite.

## Limitations
- Below Pro on quality, for example 88.6 against 91.2 on Spanish and 86.5 against 89.7 on Arabic.
- Text only; no instructions that change how relevance is judged.
- All figures are Cohere's own.

## Good for
- Reranking inside agent loops and interactive search.
- High-volume RAG where cost per query matters.
- Setting one relevance threshold across domains.
