---
id: thenlper/gte-large
name: GTE-Large
owned_by: thenlper
type: embedding
description: gte-large is Alibaba DAMO Academy's 335M-parameter MIT-licensed English BERT-large General Text Embedding model with 1,024-dimensional vectors and a 512-token input, trained with multi-stage contrastive learning.
aliases: [thenlper/gte-large]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2023-07-27"
embedding_dimensions: 1024
mteb_score: 64.77
pricing:
  input: 0.01
  output: 0
sources:
  - https://huggingface.co/thenlper/gte-large
  - https://huggingface.co/api/models/thenlper/gte-large
  - https://huggingface.co/thenlper/gte-large/raw/main/config.json
  - https://arxiv.org/abs/2308.03281
  - https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct
  - https://huggingface.co/BAAI/bge-large-en-v1.5
  - https://openrouter.ai/thenlper/gte-large
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# GTE-Large

## Overview
gte-large is the largest of the original General Text Embeddings (GTE) models, which the card says Alibaba DAMO Academy trained; they are published under the `thenlper` Hugging Face account. The method is described in "Towards General Text Embeddings with Multi-stage Contrastive Learning" (arXiv 2308.03281, submitted 2023-08-07). OpenRouter serves it on its embeddings endpoint as `thenlper/gte-large` with a 512-token context. The release date is the Hugging Face repo creation date, 2023-07-27. It is a 24-layer BERT-large encoder (335M parameters) with 1,024-dimensional output, trained on a large corpus of relevance text pairs from many domains through unsupervised pre-training and supervised fine-tuning. The card's examples use no query prefix. Weights are MIT licensed; Alibaba's later GTE models, such as gte-large-en-v1.5 and gte-Qwen2, are published under the Alibaba-NLP account.

## Strengths
- The card reports 63.13 on the 56-dataset English MTEB, ahead of e5-large-v2 (62.25) and OpenAI text-embedding-ada-002 (60.99) in its table; the MTEB leaderboard showed 64.77 on MTEB (English, v2) on 2026-11-01.
- 83.35 on STS and 52.22 on retrieval in the card's table.
- Plain BERT architecture for any encoder stack, including Sentence Transformers.

## Limitations
- English only, and longer texts are truncated to 512 tokens.
- bge-large-en-v1.5, released in September 2023, scores higher on both MTEB versions (64.23 and 65.89).
- The card documents no Matryoshka truncation.

## Good for
- English semantic similarity, search and reranking features.
- A permissive, well-benchmarked 2023 baseline.
- Low-cost hosted embeddings through OpenRouter.
