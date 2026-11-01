---
id: qwen/qwen3-reranker-8b
name: Qwen3 Reranker 8B
owned_by: qwen
type: reranker
description: The largest of Qwen's open-weight (Apache-2.0) Qwen3 rerankers, an 8B instruction-aware cross-encoder built on Qwen3-8B-Base for text retrieval in 100+ languages and code.
aliases: [Qwen/Qwen3-Reranker-8B, fireworks_ai/accounts/fireworks/models/qwen3-reranker-8b, novita/qwen/qwen3-reranker-8b]
context_length: 40960
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-06-05"
sources:
  - https://openrouter.ai/qwen/qwen3-reranker-8b
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/Qwen/Qwen3-Reranker-8B
  - https://huggingface.co/api/models/Qwen/Qwen3-Reranker-8B
  - https://huggingface.co/Qwen/Qwen3-Reranker-8B/raw/main/config.json
  - https://qwenlm.github.io/blog/qwen3-embedding/
  - https://github.com/QwenLM/Qwen3-Embedding
  - https://arxiv.org/abs/2506.05176
  - https://blog.voyageai.com/2026/09/30/rerank-3/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Qwen3 Reranker 8B

## Overview
Qwen3-Reranker-8B is the largest reranker in the Qwen3 Embedding series, announced on Qwen's blog on 2025-06-05 under Apache 2.0 (Hugging Face repo created 2025-05-29). It is a cross-encoder fine-tuned from Qwen3-8B-Base (36 layers, about 8.2B parameters) that reads a query and a document and scores relevance from the model's "yes" and "no" logits. The model card gives a 32K context; config.json and OpenRouter give 40,960 positions. OpenRouter lists it as `qwen/qwen3-reranker-8b`, served by Fireworks; its API gives a token price of 0, and its model page prices it at $0.20 per million tokens. It is instruction-aware: Qwen reports that a task instruction, ideally in English, improves results by 1% to 5%. It runs in Sentence Transformers' `CrossEncoder` or Transformers 4.51.0 or later.

## Strengths
- Qwen's scores, reranking the top 100 candidates from Qwen3-Embedding-0.6B: 69.02 on MTEB-R (English v2 retrieval), 77.45 on CMTEB-R, 72.94 on MMTEB-R, 70.19 on MLDR, 81.22 on MTEB-Code and 8.05 on FollowIR.
- Best of the three Qwen3 rerankers on CMTEB-R, MMTEB-R, MLDR and MTEB-Code; bge-reranker-v2-m3 scores 57.03 on MTEB-R in the same table.
- Open weights for self-hosting.

## Limitations
- Qwen3-Reranker-4B scores higher on MTEB-R (69.76) and FollowIR (14.84).
- Voyage reports rerank-3 3.02% ahead of it across 95 datasets.
- An 8B cross-encoder runs one forward pass per query-document pair, so latency grows with candidate count.

## Good for
- Highest-quality open-weight reranking in Chinese, multilingual and code retrieval.
- Long-document reranking.
- Self-hosted RAG stacks already using Qwen3 embeddings.
