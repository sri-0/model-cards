---
id: cohere/rerank-4-pro
name: Rerank 4 Pro
owned_by: cohere
type: reranker
description: Cohere's previous-generation quality-tier multilingual reranker (rerank-v4.0-pro), with a 32,768-token query-plus-document window and support for semi-structured data; superseded by Rerank 5 Pro.
aliases: [rerank-v4.0-pro, cohere-rerank-v4-pro, azure_ai/cohere-rerank-v4.0-pro]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
  tokenizer: Cohere
open_weights: false
license: proprietary
release_date: "2025-12-11"
sources:
  - https://openrouter.ai/cohere/rerank-4-pro
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

# Rerank 4 Pro

## Overview
Rerank 4 Pro (Cohere API id `rerank-v4.0-pro`) was announced on Cohere's blog on 2025-12-11 with the lighter Rerank 4 Fast. Cohere's model list now marks it "previous generation" and recommends `rerank-v5.0-pro` for new projects. OpenRouter lists it as `cohere/rerank-4-pro` with a 32,768-token context and prices it at $0.0025 per search on its model page. It is a multilingual model for English and non-English documents and semi-structured data such as JSON, which Cohere asks to be sent as YAML strings. It was trained with a 32,768-token context shared by query and document, and the query may take up to half of it; longer documents are split into 32,764-token chunks. The number of documents times chunks per document must stay within 10,000. Cohere describes Pro as suited to state-of-the-art quality and complex use cases.

## Strengths
- Long context: Cohere says 32,768 tokens covers about 48 to 50 pages, so most documents are ranked whole.
- 88.3 on Cohere's 47 parsed-PDF datasets, close to Voyage rerank-3 (88.4).
- Available on Cohere's API, OpenRouter and Microsoft Foundry.

## Limitations
- Cohere reports Rerank 5 Pro 12.4 points ahead on BRIGHT and an expected calibration error of 0.384 on human labels, against 0.058 for Rerank 5.
- Voyage reports rerank-3 2.72% ahead across 95 datasets and 13.84% ahead on long documents.
- Text only and proprietary.

## Good for
- Existing pipelines tuned to Rerank 4 scores.
- Reranking long and semi-structured enterprise documents.
- Multilingual search through OpenRouter.
