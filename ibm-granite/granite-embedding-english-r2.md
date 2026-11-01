---
id: ibm-granite/granite-embedding-english-r2
name: Granite Embedding English R2
owned_by: ibm
type: embedding
description: Granite-Embedding-English-R2 is IBM's 149M-parameter Apache-2.0 ModernBERT English embedding model with 768-dimensional vectors and an 8,192-token input, trained only on commercially licensed and IBM-generated data.
aliases: [ibm-granite/granite-embedding-english-r2]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2025-08-15"
embedding_dimensions: 768
mteb_score: 62.8
sources:
  - https://huggingface.co/ibm-granite/granite-embedding-english-r2
  - https://huggingface.co/api/models/ibm-granite/granite-embedding-english-r2
  - https://huggingface.co/ibm-granite/granite-embedding-english-r2/raw/main/config.json
  - https://arxiv.org/abs/2508.21085
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Granite Embedding English R2

## Overview
Granite-Embedding-English-R2 was released on 2025-08-15 (Hugging Face repo created 2025-07-17) with a 47M small model; the paper "Granite Embedding R2 Models" is arXiv 2508.21085. OpenRouter does not list it; the id follows the Hugging Face repo `ibm-granite/granite-embedding-english-r2`. It replaces granite-embedding-125m-english with a ModernBERT encoder: 22 layers, alternating attention, GeGLU, rotary positions, a new 50,368-token vocabulary, 768-dimensional output and an 8,192-token input. IBM trained it with retrieval-oriented pre-training, contrastive fine-tuning, knowledge distillation and model merging. The encoder was pre-trained on GneissWeb, and fine-tuning used only permissively licensed, IBM-collected and synthetic pairs; MS MARCO was left out because of its non-commercial licence. No prompts are needed.

## Strengths
- IBM reports 62.8 on MTEB-v2 (41 tasks), 53.1 on BEIR, 55.3 on CoIR and 40.7 on MLDR; the MTEB leaderboard showed 62.84 on MTEB (English, v2) on 2026-11-01.
- 59.5 average across IBM's retrieval suite, ahead of gte-modernbert-base (57.5) and snowflake-arctic-embed-m-v2.0 (51.4).
- Leads IBM's comparison table on LongEmbed (67.8) and MTRAG multi-turn retrieval (57.6).
- About 144 documents per second on one H100, per IBM.

## Limitations
- English only; IBM's multilingual R2 models cover other languages.
- Inputs beyond 8,192 tokens are truncated.
- The card documents no Matryoshka truncation.

## Good for
- Enterprise English RAG that needs a clean licence trail.
- Long-document, table and conversational search.
- Teams replacing granite-embedding-125m-english.
