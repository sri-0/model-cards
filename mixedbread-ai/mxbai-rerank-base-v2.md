---
id: mixedbread-ai/mxbai-rerank-base-v2
name: mxbai-rerank-base-v2
owned_by: mixedbread-ai
type: reranker
description: Mixedbread's 0.5B-parameter open-weight (Apache-2.0) reranker built on Qwen-2.5 and trained with reinforcement learning, the smaller sibling of mxbai-rerank-large-v2, for 100+ languages and code.
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
open_weights: true
license: Apache-2.0
release_date: "2025-03-03"
sources:
  - https://huggingface.co/mixedbread-ai/mxbai-rerank-base-v2
  - https://huggingface.co/api/models/mixedbread-ai/mxbai-rerank-base-v2
  - https://huggingface.co/mixedbread-ai/mxbai-rerank-base-v2/raw/main/config.json
  - https://www.mixedbread.com/blog/mxbai-rerank-v2
  - https://arxiv.org/abs/2506.03487
  - https://huggingface.co/jinaai/jina-reranker-v3
  - https://huggingface.co/jinaai/jina-reranker-v3.5
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# mxbai-rerank-base-v2

## Overview
mxbai-rerank-base-v2 (also called ProRank-0.5B) is the smaller of Mixedbread's two v2 rerankers, alongside mxbai-rerank-large-v2. OpenRouter does not list it; the id follows the Hugging Face repo, and the release date is the repo creation date, 2025-03-03. It starts from Qwen-2.5 (a 24-layer Qwen2 model, about 0.5B parameters) and was trained with GRPO reinforcement learning, contrastive learning and preference learning, as described in the ProRank paper (arXiv 2506.03487). Mixedbread's blog gives long contexts of up to 8K tokens, "32k-compatible"; config.json allows 32,768 positions. It supports 100+ languages and code, and runs through Sentence Transformers' `CrossEncoder`, the `mxbai-rerank` package and the Mixedbread API.

## Strengths
- Mixedbread's NDCG@10: 55.57 BEIR average, 28.56 on Mr.TyDi, 83.70 on Chinese C-Pack and 31.73 on CoIR CosQA, with 0.67 seconds latency per query on an A100.
- 1.92 points below the large model's 57.49 BEIR at a third of the size, and ahead of mxbai-rerank-large-v1 (49.32).
- Apache 2.0 licence for commercial self-hosting.

## Limitations
- Below mxbai-rerank-large-v2 on every listed benchmark.
- In Jina's comparisons it scores 58.40 BEIR and 55.32 MIRACL against 61.94 and 66.83 for jina-reranker-v3, and 59.58 BEIR against 63.20 for jina-reranker-v3.5.
- Quality is stated for up to 8K tokens, not the full 32K window.

## Good for
- Low-latency, permissively licensed reranking.
- Chinese and English search with a 0.5B model.
- A small reranker for self-hosted RAG.
