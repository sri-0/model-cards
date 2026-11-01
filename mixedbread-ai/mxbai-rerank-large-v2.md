---
id: mixedbread-ai/mxbai-rerank-large-v2
name: mxbai-rerank-large-v2
owned_by: mixedbread-ai
type: reranker
description: Mixedbread's 1.5B-parameter open-weight (Apache-2.0) reranker built on Qwen-2.5 and trained with reinforcement learning, for 100+ languages, code and long contexts.
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
open_weights: true
license: Apache-2.0
release_date: "2025-03-03"
sources:
  - https://huggingface.co/mixedbread-ai/mxbai-rerank-large-v2
  - https://huggingface.co/api/models/mixedbread-ai/mxbai-rerank-large-v2
  - https://huggingface.co/mixedbread-ai/mxbai-rerank-large-v2/raw/main/config.json
  - https://www.mixedbread.com/blog/mxbai-rerank-v2
  - https://arxiv.org/abs/2506.03487
  - https://huggingface.co/jinaai/jina-reranker-v3.5
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# mxbai-rerank-large-v2

## Overview
mxbai-rerank-large-v2 (also called ProRank-1.5B) is the larger of Mixedbread's two v2 rerankers, alongside the 0.5B mxbai-rerank-base-v2. OpenRouter does not list it; the id follows the Hugging Face repo, and the release date is the repo creation date, 2025-03-03. It starts from Qwen-2.5 (a 28-layer Qwen2 model, about 1.5B parameters) and was trained in three steps: GRPO reinforcement learning, contrastive learning and preference learning, described in the ProRank paper (arXiv 2506.03487). Mixedbread's blog gives long contexts of up to 8K tokens, "32k-compatible"; config.json allows 32,768 positions. It supports 100+ languages and code. It runs through Sentence Transformers' `CrossEncoder`, Mixedbread's `mxbai-rerank` package and the Mixedbread API.

## Strengths
- Mixedbread's NDCG@10: a BEIR average of 57.49, ahead of Cohere rerank-3.5 (55.39), Voyage rerank-2 (54.54) and bge-reranker-v2-m3 (53.94).
- Top of its comparison on Chinese C-Pack (84.16) and CoIR CosQA code search (32.05); 39.2 on ToolRet tool retrieval with a BM25 first stage.
- 0.89 seconds per query on NFCorpus on an A100, against 2.24 for mxbai-rerank-large-v1.

## Limitations
- Multilingual Mr.TyDi at 29.79 trails bge-reranker-v2-m3 (30.99).
- In Jina's later comparison it scores 62.45 on BEIR but 69.65 on MIRACL, behind jina-reranker-v3.5 (74.11) and Qwen3-Reranker-4B (76.56).
- Quality is stated for up to 8K tokens, not the full 32K window.

## Good for
- Permissively licensed, self-hosted reranking for English search and RAG.
- Chinese and code retrieval.
- Tool or function selection for agents.
