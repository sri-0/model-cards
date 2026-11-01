---
id: nomic-ai/nomic-embed-text-v1.5
name: Nomic Embed Text v1.5
owned_by: nomic-ai
type: embedding
description: nomic-embed-text-v1.5 is Nomic AI's 137M-parameter Apache-2.0 English embedding model with an 8,192-token context and Matryoshka vectors that scale from 768 down to 64 dimensions.
aliases: [nomic-ai/nomic-embed-text-v1.5, nomic-embed-text, "nomic-embed-text:v1.5", nomic-ai/nomic-embed-text-v1.5-GGUF]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2024-02-10"
embedding_dimensions: 768
mteb_score: 62.2
sources:
  - https://huggingface.co/nomic-ai/nomic-embed-text-v1.5
  - https://huggingface.co/api/models/nomic-ai/nomic-embed-text-v1.5
  - https://huggingface.co/nomic-ai/nomic-embed-text-v1.5/raw/main/config.json
  - https://arxiv.org/abs/2402.01613
  - https://ollama.com/library/nomic-embed-text/tags
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Nomic Embed Text v1.5

## Overview
nomic-embed-text-v1.5 adds Matryoshka Representation Learning to Nomic Embed v1 (technical report arXiv 2402.01613). OpenRouter does not list it; the id follows the Hugging Face repo `nomic-ai/nomic-embed-text-v1.5`, and the release date is the repo creation date, 2024-02-10. It starts from nomic-bert-2048, a long-context BERT, with unsupervised contrastive training on weakly related pairs (StackExchange, Quora, Amazon reviews, news summaries) and then fine-tuning on labelled search data; the full training data is released. The model has 137M parameters and 768-dimensional output. It was trained on 2,048 positions, and config.json and Sentence Transformers set 8,192, which the card says the model scales to natively. nomic-embed-vision-v1.5 shares its vector space. Ollama's `nomic-embed-text` is this model, served with a 2K context.

## Strengths
- Nomic reports MTEB 62.28 at 768 dimensions, 61.96 at 512, 61.04 at 256, 59.34 at 128 and 56.10 at 64; the MTEB leaderboard showed 62.20 on MTEB (English, v2) on 2026-11-01.
- Long 8,192-token inputs at a 137M-parameter cost.
- Apache 2.0 weights plus open training data and code (contrastors).
- About 12 million Hugging Face downloads in the month to 2026-11-01.

## Limitations
- Task prefixes are mandatory: `search_document: `, `search_query: `, `clustering: ` or `classification: `.
- English-focused; the multilingual successor is nomic-embed-text-v2-moe.
- Older Transformers versions need `trust_remote_code=True` (not from transformers 5.5.0 and sentence-transformers 5.3.0).
- Ollama's default 2K context is a quarter of what the model supports.

## Good for
- English RAG with long chunks on modest hardware.
- Indexes that trade dimensions for storage.
- Local Ollama deployments.
