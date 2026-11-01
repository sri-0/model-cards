---
id: qwen/qwen3.7-text-embedding
name: Qwen3.7 Text Embedding
owned_by: qwen
type: embedding
description: Alibaba Cloud Model Studio's recommended text embedding model, with 1024-dimensional default output (256 to 2,560), dense and sparse vectors, task instructions and 201 languages over a 128K-token input.
aliases: [qwen3.7-text-embedding]
context_length: 128000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
embedding_dimensions: 1024
sources:
  - https://www.alibabacloud.com/help/en/model-studio/embedding
  - https://www.alibabacloud.com/help/en/model-studio/text-embedding-synchronous-api
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/embeddings/models
retrieved: "2026-11-01"
---

# Qwen3.7 Text Embedding

## Overview
qwen3.7-text-embedding is the text embedding model that Alibaba Cloud Model Studio (DashScope) recommends for plain text and code, calling it its highest-performing embedding model. OpenRouter does not list it; the id is the Model Studio API id. The embedding guide lists it in the Singapore region only, at $0.07 per million input tokens with a free quota of 1 million tokens for 90 days; the general pricing page does not list it yet. It takes up to 20 texts per call and 128,000 tokens per text, per the API reference. Output is 1024 dimensions by default, with 2,560, 2,048, 1,536, 768, 512 and 256 also available. Through the DashScope SDK and API it returns dense, sparse or combined vectors and accepts an English task instruction (`instruct`, with `text_type` set to `query`); the OpenAI-compatible endpoint also serves it, including the batch API. Alibaba gives no release date, and no MTEB score for this model, so the card has no `mteb_score`.

## Strengths
- 201 languages and dialects, against 100+ for text-embedding-v4.
- Alibaba reports instruction following 16.4% better than text-embedding-v4, and sparse vectors 8.4% more effective, now with cross-language retrieval.
- Hybrid retrieval from one call through dense and sparse output.

## Limitations
- Singapore region only in the current guide; Beijing and Hong Kong list text-embedding-v4 instead.
- Instructions and sparse vectors are not available through the OpenAI-compatible API.
- No published benchmark figures or release date for this model.
- Proprietary and API only.

## Good for
- Multilingual semantic search and RAG over long documents.
- Hybrid dense-plus-sparse retrieval without a separate keyword index.
- Large offline embedding jobs through the batch API.
