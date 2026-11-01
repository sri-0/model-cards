---
id: baai/bge-large-en-v1.5
name: bge-large-en-v1.5
owned_by: baai
type: embedding
description: bge-large-en-v1.5 is BAAI's 335M-parameter MIT-licensed English BERT-large embedding model with 1,024-dimensional vectors and a 512-token input, tuned in v1.5 for a more even similarity distribution and retrieval without instructions.
aliases: [BAAI/bge-large-en-v1.5, bge-large, "bge-large:335m"]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2023-09-12"
embedding_dimensions: 1024
mteb_score: 65.89
pricing:
  input: 0.01
  output: 0
sources:
  - https://huggingface.co/BAAI/bge-large-en-v1.5
  - https://huggingface.co/api/models/BAAI/bge-large-en-v1.5
  - https://huggingface.co/BAAI/bge-large-en-v1.5/raw/main/config.json
  - https://arxiv.org/abs/2309.07597
  - https://ollama.com/library/bge-large/tags
  - https://openrouter.ai/baai/bge-large-en-v1.5
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# bge-large-en-v1.5

## Overview
bge-large-en-v1.5 is the large English model of BAAI's General Embedding (BGE) family; the card's news section dates the v1.5 release to 2023-09-12, the day the Hugging Face repo was created. OpenRouter serves it on its embeddings endpoint as `baai/bge-large-en-v1.5` with a 512-token context. It is a 24-layer BERT-large encoder (335M parameters) with 1,024-dimensional output. Version 1.5 fixes the narrow similarity distribution of v1 and improves retrieval without an instruction. For short retrieval queries BAAI suggests the prefix `Represent this sentence for searching relevant passages: `; passages never take one. The training resources are described in the C-Pack paper (arXiv 2309.07597). Weights are MIT licensed and free for commercial use. Ollama serves it as `bge-large` (`335m`).

## Strengths
- BAAI reports 64.23 on the 56-dataset English MTEB, the top score in its table, with 54.29 on retrieval; the MTEB leaderboard showed 65.89 on MTEB (English, v2) on 2026-11-01.
- Instruction-free queries lose only slightly against instructed ones, per BAAI.
- BAAI publishes fine-tuning code with hard-negative mining, and pairs it with its bge-reranker models.
- About 9.4 million Hugging Face downloads in the month to 2026-11-01.

## Limitations
- English only, with a 512-token limit; BAAI points to bge-m3 for more languages and longer texts.
- Absolute similarity scores are not meaningful; only their order is.
- The model card documents no Matryoshka truncation.

## Good for
- English semantic search and RAG with a permissive licence.
- A fine-tuning starting point for domain retrieval.
- Local serving through Ollama or Sentence Transformers.
