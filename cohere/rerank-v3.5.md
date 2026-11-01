---
id: cohere/rerank-v3.5
name: Rerank v3.5
owned_by: cohere
type: reranker
description: Cohere's December 2024 multilingual reranker for documents and semi-structured data, with a 4,096-token query-plus-document window, available on Cohere's API, Amazon Bedrock, Azure and Oracle OCI.
aliases: [rerank-v3.5, cohere.rerank-v3-5:0, Cohere-rerank-v3.5, cohere.rerank.3-5]
context_length: 4096
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
  tokenizer: Cohere
open_weights: false
license: proprietary
release_date: "2024-12-02"
sources:
  - https://openrouter.ai/cohere/rerank-v3.5
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://docs.cohere.com/docs/models
  - https://docs.cohere.com/docs/rerank
  - https://docs.cohere.com/docs/reranking-best-practices
  - https://docs.cohere.com/docs/deprecations
  - https://cohere.com/blog/rerank-3pt5
  - https://www.mixedbread.com/blog/mxbai-rerank-v2
  - https://blog.voyageai.com/2025/08/11/rerank-2-5/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Rerank v3.5

## Overview
Rerank v3.5 (`rerank-v3.5`) was announced on 2024-12-02 with improved reasoning and multilingual ability, and Cohere deprecated the Rerank v2.0 family at the same time. It is a single multilingual model covering English and the languages of embed-multilingual-v3.0, for documents and semi-structured data (JSON sent as YAML strings). OpenRouter lists it as `cohere/rerank-v3.5` with a 4,096-token context and prices it at $0.001 per search on its model page. The model was trained with a 4,096-token context: queries over 2,048 tokens are truncated, and documents are split into 4,093-token chunks, with documents times chunks per document capped at 10,000. Cloud ids are `cohere.rerank-v3-5:0` on Amazon Bedrock, `Cohere-rerank-v3.5` on Azure AI Foundry and `cohere.rerank.3-5` on Oracle OCI.

## Strengths
- Cohere's platform table gives Bedrock and OCI ids only for v3.5 among its multilingual rerankers.
- Mixedbread's comparison gives it a 55.39 BEIR average, above Voyage rerank-2 (54.54) and bge-reranker-v2-m3 (53.94).
- The cheapest Cohere reranker on OpenRouter.

## Limitations
- 4,096-token window, an eighth of Rerank 4 and Rerank 5.
- Voyage reports rerank-2.5 7.94% ahead across 93 datasets and 12.70% ahead on MAIR instruction following; Mixedbread puts mxbai-rerank-large-v2 at 57.49 on BEIR.
- Text only and proprietary.

## Good for
- Reranking on Amazon Bedrock or Oracle OCI.
- Short passages and chunked RAG pipelines.
- Existing systems tuned to v3.5 scores.
