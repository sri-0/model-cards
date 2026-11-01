---
id: qwen/qwen3-embedding-0.6b
name: Qwen3 Embedding 0.6B
owned_by: qwen
type: embedding
description: Qwen3-Embedding-0.6B is the smallest of Qwen's Apache-2.0 text embedding models, a 28-layer Qwen3-0.6B-Base fine-tune with a 32K-token input, 1,024-dimensional vectors truncatable to 32, and 100+ natural and programming languages.
aliases: [Qwen/Qwen3-Embedding-0.6B, Qwen/Qwen3-Embedding-0.6B-GGUF, "qwen3-embedding:0.6b"]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2025-06-05"
embedding_dimensions: 1024
mteb_score: 64.33
sources:
  - https://huggingface.co/Qwen/Qwen3-Embedding-0.6B
  - https://huggingface.co/api/models/Qwen/Qwen3-Embedding-0.6B
  - https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen3-Embedding-0.6B-GGUF
  - https://qwenlm.github.io/blog/qwen3-embedding/
  - https://arxiv.org/abs/2506.05176
  - https://ollama.com/library/qwen3-embedding/tags
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Qwen3 Embedding 0.6B

## Overview
Qwen3-Embedding-0.6B was released on 2025-06-05 with 4B and 8B embedders and three rerankers (Hugging Face repo created 2025-06-03); the technical report is arXiv 2506.05176. OpenRouter lists the 4B and 8B sizes but not this one; the id follows the Hugging Face repo `Qwen/Qwen3-Embedding-0.6B`. It is Qwen3-0.6B-Base (28 layers, 596M parameters) trained in three stages: contrastive pre-training on weakly supervised pairs that Qwen3 generated, supervised training on labelled data, then model merging. The embedding is the hidden state of the final [EOS] token. Output is 1,024 dimensions, and any size from 32 to 1,024 can be requested. Input runs to 32K tokens. Queries take a one-sentence instruction (`Instruct: {task}\nQuery:{query}`); documents take none. Qwen publishes GGUF files, and Ollama serves it as `qwen3-embedding:0.6b`.

## Strengths
- Qwen reports MTEB (Multilingual) Mean (Task) 64.33, MTEB (English, v2) 70.70 and C-MTEB 66.33, ahead of multilingual-e5-large-instruct (63.22) and BGE-M3 (59.56) in the same table. The MTEB leaderboard showed 64.34 and 70.47 on 2026-11-01.
- Query instructions add 1% to 5% on most tasks, per Qwen.
- Runs in Sentence Transformers, Transformers (4.51 or later), vLLM (0.8.5 or later) and Text Embeddings Inference.
- Apache 2.0, with about 8.7 million Hugging Face downloads in the month to 2026-11-01.

## Limitations
- The weakest of the three sizes: the 4B and 8B score 69.45 and 70.58 multilingual.
- Instructions should be written in English even for other languages, because most training instructions were English.
- Pooling takes the last token, so batched inference needs left padding or the card's `last_token_pool` code.

## Good for
- Multilingual and code retrieval on a CPU or small GPU.
- RAG over long documents up to 32K tokens.
- Indexes that want to choose their own vector size.
