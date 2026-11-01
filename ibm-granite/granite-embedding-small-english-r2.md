---
id: ibm-granite/granite-embedding-small-english-r2
name: Granite Embedding Small English R2
owned_by: ibm
type: embedding
description: Granite-Embedding-Small-English-R2 is IBM's 47M-parameter Apache-2.0 ModernBERT English embedding model with 384-dimensional vectors and an 8,192-token input, trained only on commercially licensed and IBM-generated data.
aliases: [ibm-granite/granite-embedding-small-english-r2]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2025-08-15"
embedding_dimensions: 384
mteb_score: 61.1
sources:
  - https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
  - https://huggingface.co/api/models/ibm-granite/granite-embedding-small-english-r2
  - https://huggingface.co/ibm-granite/granite-embedding-small-english-r2/raw/main/config.json
  - https://arxiv.org/abs/2508.21085
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Granite Embedding Small English R2

## Overview
Granite-Embedding-Small-English-R2 was released on 2025-08-15 (Hugging Face repo created 2025-07-17) with the 149M English R2 model; the paper "Granite Embedding R2 Models" is arXiv 2508.21085. OpenRouter does not list it; the id follows the Hugging Face repo `ibm-granite/granite-embedding-small-english-r2`. It replaces granite-embedding-30m-english with a ModernBERT encoder of 12 layers, GeGLU, rotary positions, a 50,368-token vocabulary, 384-dimensional output and an 8,192-token input, which IBM calls a first-of-its-kind reduced-size model. Training combined retrieval-oriented pre-training, contrastive fine-tuning, knowledge distillation and model merging on permissively licensed, IBM-collected and synthetic data, without MS MARCO. No prompts are needed. It had about 6.7 million Hugging Face downloads in the month to 2026-11-01.

## Strengths
- IBM reports 61.1 on MTEB-v2 (41 tasks), 50.9 on BEIR, 53.8 on CoIR and 39.8 on MLDR; the MTEB leaderboard showed 61.07 on MTEB (English, v2) on 2026-11-01.
- 55.6 average across IBM's retrieval suite, above e5-base-v2 (47.5) and bge-base-en-v1.5 (46.9) at under half their size.
- Nearly 200 documents per second on one H100, per IBM.
- Apache 2.0 with long 8,192-token inputs.

## Limitations
- English only.
- Lower quality than the 149M English R2 model (62.8 on MTEB-v2, 59.5 retrieval average).
- Inputs beyond 8,192 tokens are truncated, and the card documents no Matryoshka truncation.

## Good for
- High-throughput English indexing on CPUs or small GPUs.
- Long-document search where a 512-token encoder is too short.
- Enterprise deployments that need clean data provenance.
