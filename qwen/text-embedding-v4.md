---
id: qwen/text-embedding-v4
name: Text Embedding v4
owned_by: qwen
type: embedding
description: Alibaba Cloud Model Studio's Qwen3-Embedding-series text embedding API model, with 1024-dimensional default output (64 to 2,048), dense and sparse vectors, task instructions, 100+ languages and an 8,192-token input.
aliases: [text-embedding-v4]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
embedding_dimensions: 1024
mteb_score: 68.36
sources:
  - https://www.alibabacloud.com/help/en/model-studio/embedding
  - https://www.alibabacloud.com/help/en/model-studio/text-embedding-synchronous-api
  - https://www.alibabacloud.com/help/en/model-studio/embedding-interfaces-compatible-with-openai
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/embeddings/models
retrieved: "2026-11-01"
---

# Text Embedding v4

## Overview
text-embedding-v4 is the Model Studio (DashScope) text embedding model that Alibaba Cloud lists as part of the Qwen3-Embedding series. It is served in the Singapore, Beijing and Hong Kong regions, at $0.07 per million input tokens in Singapore and Hong Kong and $0.072 in Beijing, with a 1 million-token free quota in Singapore. OpenRouter does not list it; the id is the Model Studio API id. Each call takes up to 10 texts of up to 8,192 tokens. Output is 1024 dimensions by default, or 2,048, 1,536, 768, 512, 256, 128 or 64. Through the DashScope API it returns dense, sparse or combined vectors and accepts an English task instruction; the OpenAI-compatible endpoint returns dense vectors only, and the batch API is supported. It covers 100+ languages plus programming languages. Alibaba gives no release date. Its embedding guide now recommends qwen3.7-text-embedding first. The `mteb_score` is Alibaba's figure at the 1024-dimension default; the guide does not name the MTEB version.

## Strengths
- Alibaba's scores at 1024 dimensions: 68.36 MTEB, 59.30 MTEB retrieval, 70.14 CMTEB and 73.98 CMTEB retrieval; at 2048, 71.58 MTEB.
- The smallest output sizes of Alibaba's text embedders, down to 64 dimensions.
- The only Alibaba text embedder listed in all three regions.

## Limitations
- 8,192-token input, against 128,000 for qwen3.7-text-embedding.
- Alibaba reports qwen3.7-text-embedding 16.4% better at instruction following.
- Sparse output needs the DashScope API; the OpenAI-compatible API returns an empty result for it.

## Good for
- Chinese and multilingual semantic search in Beijing or Hong Kong.
- Hybrid dense-plus-sparse retrieval.
- Small vectors for large indexes.
