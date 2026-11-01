---
id: alibaba-nlp/gte-multilingual-base
name: gte-multilingual-base
owned_by: qwen
type: embedding
description: gte-multilingual-base is Alibaba's 305M-parameter Apache-2.0 encoder embedding model from the mGTE work, covering 70+ languages with an 8,192-token input, 768-dimensional elastic dense vectors and optional sparse token weights.
aliases: [Alibaba-NLP/gte-multilingual-base]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2024-07-20"
embedding_dimensions: 768
sources:
  - https://huggingface.co/Alibaba-NLP/gte-multilingual-base
  - https://huggingface.co/api/models/Alibaba-NLP/gte-multilingual-base
  - https://huggingface.co/Alibaba-NLP/gte-multilingual-base/raw/main/config.json
  - https://arxiv.org/abs/2407.19669
  - https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe
  - https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# gte-multilingual-base

## Overview
gte-multilingual-base is the encoder model from Alibaba's mGTE paper, "mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval" (arXiv 2407.19669, submitted 2024-07-29). OpenRouter does not list it; the id follows the Hugging Face repo `Alibaba-NLP/gte-multilingual-base`, and the release date is the repo creation date, 2024-07-20. It is a 12-layer, 305M-parameter encoder with a 250K-token vocabulary and RoPE positions scaled to 8,192 tokens, using the CLS token as a 768-dimensional embedding. Alibaba calls the dense output elastic: it can be cut to any size from 128 to 768. The same model also emits sparse token weights for lexical or hybrid scoring. It supports over 70 languages, and the card's examples use no query prefix. Weights are Apache 2.0; gte-multilingual-reranker-base accompanies it.

## Strengths
- About ten times faster inference than Alibaba's decoder-based gte-Qwen2 models, per the card.
- Nomic's comparison lists BEIR 51.10 and MIRACL 63.40, and IBM uses it as the retrieval reference that its 97M Granite R2 model matches.
- Long 8,192-token inputs at a small-encoder cost.
- Usage is documented for Transformers, Sentence Transformers, Infinity and Text Embeddings Inference (OpenAI-compatible `/v1/embeddings`).

## Limitations
- Needs `trust_remote_code=True` for its custom architecture; Alibaba recommends xformers and unpadding for speed.
- The card's benchmark tables are images, and the MTEB leaderboard showed no overall mean for it on 2026-11-01.
- Sparse output needs Alibaba's custom code rather than Sentence Transformers.

## Good for
- Multilingual hybrid (dense plus sparse) retrieval on modest hardware.
- Long-document search in many languages.
- Pairing with gte-multilingual-reranker-base.
