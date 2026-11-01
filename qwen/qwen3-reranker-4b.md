---
id: qwen/qwen3-reranker-4b
name: Qwen3 Reranker 4B
owned_by: qwen
type: reranker
description: Qwen's mid-sized open-weight (Apache-2.0) Qwen3 reranker, a 4B instruction-aware cross-encoder built on Qwen3-4B-Base that scores highest of the series on English retrieval and instruction following.
aliases: [Qwen/Qwen3-Reranker-4B, fireworks_ai/accounts/fireworks/models/qwen3-reranker-4b]
context_length: 40960
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
open_weights: true
license: Apache-2.0
release_date: "2025-06-05"
sources:
  - https://huggingface.co/Qwen/Qwen3-Reranker-4B
  - https://huggingface.co/api/models/Qwen/Qwen3-Reranker-4B
  - https://huggingface.co/Qwen/Qwen3-Reranker-4B/raw/main/config.json
  - https://qwenlm.github.io/blog/qwen3-embedding/
  - https://github.com/QwenLM/Qwen3-Embedding
  - https://arxiv.org/abs/2506.05176
  - https://huggingface.co/jinaai/jina-reranker-v3.5
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Qwen3 Reranker 4B

## Overview
Qwen3-Reranker-4B is the middle size of the Qwen3 Embedding series rerankers, announced on Qwen's blog on 2025-06-05 under Apache 2.0 (Hugging Face repo created 2025-06-03). OpenRouter does not list it; the id follows the Hugging Face repo. It is a cross-encoder fine-tuned from Qwen3-4B-Base (36 layers, about 4.0B parameters) that scores a query-document pair from the "yes" and "no" logits. The model card gives a 32K context; config.json gives 40,960 positions. It is instruction-aware, and Qwen reports that a task instruction, ideally in English, improves results by 1% to 5%. It runs in Sentence Transformers' `CrossEncoder` or Transformers 4.51.0 or later; LiteLLM lists a Fireworks deployment.

## Strengths
- Qwen's scores, reranking the top 100 candidates from Qwen3-Embedding-0.6B: 69.76 on MTEB-R (English v2 retrieval), the best of the series, 75.94 on CMTEB-R, 72.74 on MMTEB-R, 69.97 on MLDR, 81.20 on MTEB-Code and 14.84 on FollowIR, also the best.
- Within 0.25 points of the 8B model on MMTEB-R, MLDR and MTEB-Code at half the size.
- In Jina's comparison (top 100 from jina-embeddings-v5-text-small) it leads on MIRACL (76.56), RTEB (77.68) and Struct-IR (55.6).

## Limitations
- Jina reports jina-reranker-v3.5 (0.6B) slightly ahead on BEIR, 63.20 against 62.28.
- Behind the 8B model on CMTEB-R (75.94 against 77.45).
- Cross-encoder cost grows with the number of candidates.

## Good for
- The best quality-to-size balance in the Qwen3 reranker family.
- Instruction-guided reranking, such as domain-specific relevance rules.
- Self-hosted multilingual and code retrieval.
