---
id: qwen/qwen3-reranker-0.6b
name: Qwen3 Reranker 0.6B
owned_by: qwen
type: reranker
description: The smallest of Qwen's open-weight (Apache-2.0) Qwen3 rerankers, a 0.6B instruction-aware cross-encoder built on Qwen3-0.6B-Base for fast multilingual and code reranking.
aliases: [Qwen/Qwen3-Reranker-0.6B, fireworks_ai/accounts/fireworks/models/qwen3-reranker-0p6b]
context_length: 40960
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
open_weights: true
license: Apache-2.0
release_date: "2025-06-05"
sources:
  - https://huggingface.co/Qwen/Qwen3-Reranker-0.6B
  - https://huggingface.co/api/models/Qwen/Qwen3-Reranker-0.6B
  - https://huggingface.co/Qwen/Qwen3-Reranker-0.6B/raw/main/config.json
  - https://qwenlm.github.io/blog/qwen3-embedding/
  - https://github.com/QwenLM/Qwen3-Embedding
  - https://arxiv.org/abs/2506.05176
  - https://huggingface.co/jinaai/jina-reranker-v3.5
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Qwen3 Reranker 0.6B

## Overview
Qwen3-Reranker-0.6B is the smallest reranker in the Qwen3 Embedding series, announced on Qwen's blog on 2025-06-05 under Apache 2.0 (Hugging Face repo created 2025-05-29). OpenRouter does not list it; the id follows the Hugging Face repo. It is a cross-encoder fine-tuned from Qwen3-0.6B-Base (28 layers, about 0.6B parameters) that scores a query-document pair from the "yes" and "no" logits. The model card gives a 32K context; config.json gives 40,960 positions. It supports 100+ languages, including programming languages, and is instruction-aware: Qwen reports that a task instruction, ideally in English, improves results by 1% to 5%. It runs in Sentence Transformers' `CrossEncoder` or Transformers 4.51.0 or later.

## Strengths
- Qwen's scores, reranking the top 100 candidates from Qwen3-Embedding-0.6B: 65.80 on MTEB-R (English v2 retrieval), 71.31 on CMTEB-R, 66.36 on MMTEB-R, 67.28 on MLDR, 73.42 on MTEB-Code and 5.41 on FollowIR.
- Ahead of bge-reranker-v2-m3 (57.03 MTEB-R, 41.38 MTEB-Code) at a similar size in the same table.
- The smallest model in the series, at about 0.6B parameters.

## Limitations
- 3 to 4 points behind the 4B and 8B models on MTEB-R and about 8 on MTEB-Code.
- In Jina's comparison (top 100 from jina-embeddings-v5-text-small) it scores 56.94 on BEIR, against 63.20 for the same-sized jina-reranker-v3.5.
- FollowIR (instruction following) is 5.41, against 14.84 for the 4B model.

## Good for
- Low-latency reranking in self-hosted RAG.
- Multilingual and code retrieval on limited hardware.
- A first reranking stage before a larger model.
