---
id: baai/bge-m3
name: bge-m3
owned_by: baai
type: embedding
description: BGE-M3 is BAAI's MIT-licensed XLM-RoBERTa-large embedding model that returns dense 1,024-dimensional, sparse lexical and multi-vector representations in one pass, for 100+ languages and inputs up to 8,192 tokens.
aliases: [BAAI/bge-m3, bge-m3, "bge-m3:567m"]
context_length: 8194
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2024-01-27"
embedding_dimensions: 1024
mteb_score: 59.56
pricing:
  input: 0.01
  output: 0
sources:
  - https://huggingface.co/BAAI/bge-m3
  - https://huggingface.co/api/models/BAAI/bge-m3
  - https://huggingface.co/BAAI/bge-m3/raw/main/config.json
  - https://arxiv.org/abs/2402.03216
  - https://huggingface.co/Qwen/Qwen3-Embedding-0.6B
  - https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0
  - https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe
  - https://ollama.com/library/bge-m3/tags
  - https://openrouter.ai/baai/bge-m3
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# bge-m3

## Overview
BGE-M3 is the Beijing Academy of Artificial Intelligence's multi-function embedding model, described in arXiv 2402.03216 (submitted 2024-02-05). OpenRouter serves it on its embeddings endpoint as `baai/bge-m3`, listing 8,194 tokens, the config.json position count; BAAI documents 8,192. The release date is the Hugging Face repo creation date, 2024-01-27. It is an XLM-RoBERTa-large encoder (24 layers, 1,024 dimensions) whose positions were extended to 8,192 and further pre-trained with RetroMAE, then contrastively trained and fine-tuned with self-knowledge distillation across its retrieval modes. One forward pass yields a dense 1,024-dimensional vector, sparse lexical token weights and ColBERT-style multi-vectors. It supports more than 100 languages, and queries need no instruction. Weights are MIT licensed; Ollama serves it as `bge-m3` (`567m`).

## Strengths
- Dense, sparse and multi-vector retrieval from one model; Vespa and Milvus support hybrid search with it.
- Qwen's table, from the MTEB leaderboard on 2025-05-24, gives 59.56 Mean (Task) on MTEB (Multilingual), with 79.11 on bitext mining and 74.12 on STS.
- Strong multilingual retrieval: Nomic's comparison lists MIRACL 69.20, the highest in its table.
- About 30 million Hugging Face downloads in the month to 2026-11-01.

## Limitations
- English retrieval trails newer models: BEIR 48.8 in Snowflake's and Nomic's tables, against 55.6 for snowflake-arctic-embed-l-v2.0.
- The model card documents no Matryoshka truncation.
- Sparse and multi-vector outputs come from BAAI's FlagEmbedding library; the card points to Sentence Transformers and Transformers for dense vectors only.
- The MTEB leaderboard showed no overall mean for it on 2026-11-01.

## Good for
- Hybrid dense plus sparse retrieval in Milvus or Vespa.
- Multilingual RAG over long documents.
- A base for fine-tuning; BAAI publishes unified fine-tuning code and data.
