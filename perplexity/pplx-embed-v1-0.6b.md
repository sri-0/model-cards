---
id: perplexity/pplx-embed-v1-0.6b
name: Embed V1 0.6B
owned_by: perplexity
type: embedding
description: pplx-embed-v1-0.6B is Perplexity's MIT-licensed open-weight multilingual text embedding model on a diffusion-pretrained Qwen3 backbone with bidirectional attention, returning unnormalised int8 1,024-dimensional vectors from up to 32K tokens without instruction prefixes.
aliases: [perplexity-ai/pplx-embed-v1-0.6b, pplx-embed-v1-0.6b]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2026-02-26"
embedding_dimensions: 1024
pricing:
  input: 0.004
  output: 0
sources:
  - https://huggingface.co/perplexity-ai/pplx-embed-v1-0.6b
  - https://huggingface.co/api/models/perplexity-ai/pplx-embed-v1-0.6b
  - https://huggingface.co/perplexity-ai/pplx-embed-v1-0.6b/raw/main/config.json
  - https://arxiv.org/abs/2602.11151
  - https://arxiv.org/html/2602.11151
  - https://docs.perplexity.ai/docs/embeddings
  - https://community.perplexity.ai/t/introducing-pplx-embed-state-of-the-art-embedding-models-for-web-scale-retrieval/4732
  - https://openrouter.ai/perplexity/pplx-embed-v1-0.6b
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# Embed V1 0.6B

## Overview
pplx-embed-v1-0.6B was released on 2026-02-26 with a 4B sibling and two contextual models (pplx-embed-context-v1); the Hugging Face repo was created on 2026-01-14 and the technical report is arXiv 2602.11151. OpenRouter serves it as `perplexity/pplx-embed-v1-0.6b` with a 32,000-token context, and Perplexity's API uses `pplx-embed-v1-0.6b`. Perplexity continued pre-training Qwen3 with a diffusion objective so it attends bidirectionally, then trained it with multi-stage contrastive learning; embeddings are mean-pooled. Output is 1,024 dimensions with Matryoshka truncation, quantised to int8 natively (binary also available) and not normalised, so Perplexity says to compare with cosine similarity (Hamming distance for binary). No instruction prefix is used.

## Strengths
- Perplexity reports 65.41 average NDCG@10 on MTEB (Multilingual, v2) retrieval and 75.85 on MTEB (Code) in int8, ahead of Qwen3-Embedding-0.6B (64.65, 75.42), and it beats that model on every MIRACL language.
- Native int8 and binary vectors store 976 and 7,812 documents per megabyte respectively.
- MIT licence; Sentence Transformers, ONNX and Text Embeddings Inference (v1.9.2 or later) are documented.

## Limitations
- Vectors are unnormalised; inner product or L2 distance gives wrong rankings.
- Text Embeddings Inference returns int8 only.
- Needs `trust_remote_code=True`.
- Perplexity reports retrieval averages only; the MTEB leaderboard showed no overall mean on 2026-11-01.

## Good for
- Low-cost web-scale retrieval with compact int8 or binary indexes.
- Multilingual and code search without prompt management.
- Self-hosted deployments under a permissive licence.
