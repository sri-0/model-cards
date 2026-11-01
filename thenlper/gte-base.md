---
id: thenlper/gte-base
name: GTE-Base
owned_by: thenlper
type: embedding
description: gte-base is Alibaba DAMO Academy's 109M-parameter MIT-licensed English BERT-base General Text Embedding model with 768-dimensional vectors and a 512-token input, trained with multi-stage contrastive learning.
aliases: [thenlper/gte-base]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2023-07-27"
embedding_dimensions: 768
mteb_score: 63.9
pricing:
  input: 0.005
  output: 0
sources:
  - https://huggingface.co/thenlper/gte-base
  - https://huggingface.co/api/models/thenlper/gte-base
  - https://huggingface.co/thenlper/gte-base/raw/main/config.json
  - https://arxiv.org/abs/2308.03281
  - https://huggingface.co/BAAI/bge-base-en-v1.5
  - https://openrouter.ai/thenlper/gte-base
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# GTE-Base

## Overview
gte-base is the base-sized original General Text Embeddings (GTE) model, which the card says Alibaba DAMO Academy trained; it is published under the `thenlper` Hugging Face account. The method is described in "Towards General Text Embeddings with Multi-stage Contrastive Learning" (arXiv 2308.03281, submitted 2023-08-07). OpenRouter serves it on its embeddings endpoint as `thenlper/gte-base` with a 512-token context. The release date is the Hugging Face repo creation date, 2023-07-27. It is a 12-layer BERT-base encoder (109M parameters) with 768-dimensional output, trained on a large corpus of relevance text pairs through unsupervised pre-training and supervised fine-tuning. The card's examples use no query prefix. Weights are MIT licensed.

## Strengths
- The card reports 62.39 on the 56-dataset English MTEB, ahead of e5-large-v2 (62.25) at a third of its size; the MTEB leaderboard showed 63.90 on MTEB (English, v2) on 2026-11-01.
- The GTE paper says the 110M base model outperforms OpenAI's embedding API and 10x larger models on MTEB, and handles code retrieval by treating code as text.
- Small enough for CPU serving; works in Sentence Transformers.

## Limitations
- English only, and longer texts are truncated to 512 tokens.
- bge-base-en-v1.5 scores higher on both MTEB versions (63.55 and 65.14).
- The card documents no Matryoshka truncation.

## Good for
- Lightweight English search and similarity.
- A permissive baseline for evaluations.
- Low-cost hosted embeddings through OpenRouter.
