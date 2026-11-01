---
id: jinaai/jina-embeddings-v5-text-nano
name: Jina Embeddings v5 Text Nano
owned_by: jinaai
type: embedding
description: jina-embeddings-v5-text-nano is Jina AI's 239M-parameter multilingual text embedding model on EuroBERT-210M, distilled from Qwen3-Embedding-4B, with task LoRA adapters, an 8,192-token input and 768-dimensional Matryoshka vectors under CC BY-NC 4.0.
aliases: [jinaai/jina-embeddings-v5-text-nano, jina-embeddings-v5-text-nano, jinaai/jina-embeddings-v5-text-nano-retrieval, jinaai/jina-embeddings-v5-text-nano-text-matching, jinaai/jina-embeddings-v5-text-nano-classification, jinaai/jina-embeddings-v5-text-nano-clustering, jinaai/jina-embeddings-v5-text-nano-retrieval-GGUF, jinaai/jina-embeddings-v5-text-nano-text-matching-GGUF, jinaai/jina-embeddings-v5-text-nano-classification-GGUF, jinaai/jina-embeddings-v5-text-nano-clustering-GGUF, jinaai/jina-embeddings-v5-text-nano-mlx]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: CC-BY-NC-4.0
release_date: "2026-02-18"
embedding_dimensions: 768
mteb_score: 65.5
sources:
  - https://huggingface.co/jinaai/jina-embeddings-v5-text-nano
  - https://huggingface.co/api/models/jinaai/jina-embeddings-v5-text-nano
  - https://huggingface.co/jinaai/jina-embeddings-v5-text-nano/raw/main/config.json
  - https://arxiv.org/abs/2602.15547
  - https://www.elastic.co/search-labs/blog/jina-embeddings-v5-omni-all-media-one-index
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Jina Embeddings v5 Text Nano

## Overview
jina-embeddings-v5-text-nano was released on 2026-02-18 (Hugging Face repo created 2026-01-22) with the larger v5-text-small; the technical report is arXiv 2602.15547. OpenRouter does not list it; the id follows the Hugging Face repo `jinaai/jina-embeddings-v5-text-nano`, and Jina's API uses `jina-embeddings-v5-text-nano`. Built on EuroBERT-210M, it was trained by distilling embeddings from Qwen3-Embedding-4B combined with task-specific contrastive losses. Four LoRA adapters (retrieval, text matching, clustering, classification) are selected per call; separate repos merge each into the weights for vLLM, ONNX and GGUF (llama.cpp). It pools the last token and returns 768 dimensions (Matryoshka down to 32). The card's feature table and config.json give an 8,192-token sequence length, although its summary says 32K. Elastic says its pretraining covered 15 major languages.

## Strengths
- Jina reports 71.0 on MTEB (English, v2) and 65.5 on MMTEB with 239M parameters, matching or beating sub-500M models such as EmbeddingGemma 300M. The MTEB leaderboard showed 65.52 and 71.11 on 2026-11-01.
- Embeddings are robust under truncation and binary quantisation, per Jina.
- Shares a vector space with jina-embeddings-v5-omni-nano for later media search.

## Limitations
- CC BY-NC 4.0: commercial use needs a licence from Jina.
- Narrower language coverage than v5-text-small (119+ languages).
- Needs `trust_remote_code=True`, transformers 4.57 or later and peft.
- Conflicting context figures on the card; plan for 8,192 tokens.

## Good for
- Multilingual retrieval on CPUs and small GPUs.
- Local llama.cpp deployments using the GGUF builds.
- Non-commercial projects that need strong quality per parameter.
