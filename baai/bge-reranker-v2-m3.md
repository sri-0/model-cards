---
id: baai/bge-reranker-v2-m3
name: bge-reranker-v2-m3
owned_by: baai
type: reranker
description: BAAI's lightweight open-weight (Apache-2.0) multilingual cross-encoder reranker, a 568M-parameter XLM-RoBERTa model initialised from bge-m3 that outputs a query-passage relevance score.
aliases: [BAAI/bge-reranker-v2-m3, novita/baai/bge-reranker-v2-m3]
context_length: 8194
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
open_weights: true
license: Apache-2.0
release_date: "2024-03-15"
sources:
  - https://huggingface.co/BAAI/bge-reranker-v2-m3
  - https://huggingface.co/api/models/BAAI/bge-reranker-v2-m3
  - https://huggingface.co/BAAI/bge-reranker-v2-m3/raw/main/config.json
  - https://github.com/FlagOpen/FlagEmbedding
  - https://arxiv.org/abs/2402.03216
  - https://huggingface.co/Qwen/Qwen3-Reranker-8B
  - https://www.mixedbread.com/blog/mxbai-rerank-v2
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# bge-reranker-v2-m3

## Overview
bge-reranker-v2-m3 is the multilingual member of BAAI's BGE reranker v2 family. OpenRouter does not list it (it lists BAAI's bge-m3 embedding model); the id follows the Hugging Face repo, and the release date is the repo creation date, 2024-03-15. It is a cross-encoder built on bge-m3: an XLM-RoBERTa sequence classifier with 24 layers and about 568M parameters. Given a query and a passage it returns a raw relevance score, which a sigmoid maps to the 0-1 range (`normalize=True` in FlagEmbedding). config.json allows 8,194 positions, though the model card's Transformers example truncates pairs at 512 tokens. It runs through FlagEmbedding's `FlagReranker` (fp16 optional), Sentence Transformers, Transformers and Text Embeddings Inference. BAAI's own BEIR, CMTEB-retrieval and MIRACL results are published only as images.

## Strengths
- BAAI recommends it for multilingual use, for Chinese and English, and where efficiency matters.
- Mixedbread's comparison puts it top on multilingual Mr.TyDi at 30.99, ahead of mxbai-rerank-large-v2 (29.79).
- Qwen's table scores it 72.16 on CMTEB-R, above jina-reranker-v2-base-multilingual (63.37).

## Limitations
- Older than the LLM-based rerankers: Qwen reports 57.03 on MTEB-R and 41.38 on MTEB-Code, against 65.80 and 73.42 for Qwen3-Reranker-0.6B.
- Mixedbread reports a BEIR average of 53.94, against 57.49 for mxbai-rerank-large-v2.
- No instruction input and no published text figures from BAAI.

## Good for
- Fast self-hosted reranking in many languages on modest hardware.
- Chinese and English retrieval pipelines built on bge-m3.
- A permissively licensed baseline reranker.
