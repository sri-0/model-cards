---
id: baai/bge-base-en-v1.5
name: bge-base-en-v1.5
owned_by: baai
type: embedding
description: bge-base-en-v1.5 is BAAI's 109M-parameter MIT-licensed English BERT-base embedding model with 768-dimensional vectors and a 512-token input, tuned in v1.5 for a more even similarity distribution and retrieval without instructions.
aliases: [BAAI/bge-base-en-v1.5]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2023-09-12"
embedding_dimensions: 768
mteb_score: 65.14
pricing:
  input: 0.005
  output: 0
sources:
  - https://huggingface.co/BAAI/bge-base-en-v1.5
  - https://huggingface.co/api/models/BAAI/bge-base-en-v1.5
  - https://huggingface.co/BAAI/bge-base-en-v1.5/raw/main/config.json
  - https://arxiv.org/abs/2309.07597
  - https://huggingface.co/ibm-granite/granite-embedding-english-r2
  - https://openrouter.ai/baai/bge-base-en-v1.5
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# bge-base-en-v1.5

## Overview
bge-base-en-v1.5 is the base-sized English model of BAAI's General Embedding (BGE) family; the card's news section dates the v1.5 release to 2023-09-12 (Hugging Face repo created 2023-09-11). OpenRouter serves it on its embeddings endpoint as `baai/bge-base-en-v1.5` with a 512-token context. It is a 12-layer BERT-base encoder (109M parameters) with 768-dimensional output. Version 1.5 fixes the narrow similarity distribution of v1 and improves retrieval without an instruction. For short retrieval queries BAAI suggests the prefix `Represent this sentence for searching relevant passages: `; passages never take one. The training resources are described in the C-Pack paper (arXiv 2309.07597). Weights are MIT licensed and free for commercial use.

## Strengths
- BAAI reports 63.55 on the 56-dataset English MTEB, with 53.25 on retrieval; the MTEB leaderboard showed 65.14 on MTEB (English, v2) on 2026-11-01, within a point of the large model (65.89) at a third of the size.
- IBM's comparison gives 54.8 on MTEB English v2 retrieval.
- Instruction-free queries lose only slightly against instructed ones, per BAAI.
- About 7.9 million Hugging Face downloads in the month to 2026-11-01.

## Limitations
- English only, with a 512-token limit; BAAI points to bge-m3 for more languages and longer texts.
- Absolute similarity scores are not meaningful; only their order is.
- The model card documents no Matryoshka truncation.

## Good for
- English search on CPUs or small GPUs.
- A fine-tuning base for domain retrieval, using BAAI's published scripts.
- Low-cost hosted embeddings through OpenRouter.
