---
id: perplexity/pplx-embed-v1-4b
name: Embed V1 4B
owned_by: perplexity
type: embedding
description: pplx-embed-v1-4B is Perplexity's MIT-licensed open-weight multilingual text embedding model on a diffusion-pretrained Qwen3 backbone with bidirectional attention, returning unnormalised int8 2,560-dimensional vectors from up to 32K tokens without instruction prefixes.
aliases: [perplexity-ai/pplx-embed-v1-4b, pplx-embed-v1-4b]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2026-02-26"
embedding_dimensions: 2560
pricing:
  input: 0.03
  output: 0
sources:
  - https://huggingface.co/perplexity-ai/pplx-embed-v1-4b
  - https://huggingface.co/api/models/perplexity-ai/pplx-embed-v1-4b
  - https://huggingface.co/perplexity-ai/pplx-embed-v1-4b/raw/main/config.json
  - https://arxiv.org/abs/2602.11151
  - https://arxiv.org/html/2602.11151
  - https://docs.perplexity.ai/docs/embeddings
  - https://community.perplexity.ai/t/introducing-pplx-embed-state-of-the-art-embedding-models-for-web-scale-retrieval/4732
  - https://openrouter.ai/perplexity/pplx-embed-v1-4b
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# Embed V1 4B

## Overview
pplx-embed-v1-4B was released on 2026-02-26 with a 0.6B sibling and two contextual models (pplx-embed-context-v1); the Hugging Face repo was created on 2026-01-20 and the technical report is arXiv 2602.11151. OpenRouter serves it as `perplexity/pplx-embed-v1-4b` with a 32,000-token context, and Perplexity's API uses `pplx-embed-v1-4b`. Perplexity continued pre-training Qwen3 (36 layers, 4.0B parameters) with a diffusion objective so it attends bidirectionally, then trained it with multi-stage contrastive learning; embeddings are mean-pooled. Output is 2,560 dimensions with Matryoshka truncation, quantised to int8 natively (binary also available) and not normalised, so Perplexity says to compare with cosine similarity (Hamming distance for binary). No instruction prefix is used.

## Strengths
- Perplexity reports 69.66 average NDCG@10 on MTEB (Multilingual, v2) retrieval in int8, matching Qwen3-Embedding-4B (69.60) and above gemini-embedding-001 (67.71), plus 78.73 on MTEB (Code).
- Binary vectors keep 68.22 on the same retrieval set while storing 3,125 documents per megabyte.
- MIT licence; Sentence Transformers, ONNX and Text Embeddings Inference (v1.9.2 or later) are documented.

## Limitations
- Vectors are unnormalised; inner product or L2 distance gives wrong rankings.
- Trails Qwen3-Embedding-4B on MTEB (Code) (80.07), and the 0.6B model scores higher on MIRACL, per the paper.
- Needs `trust_remote_code=True`; Text Embeddings Inference returns int8 only.
- Retrieval averages only; the MTEB leaderboard showed no overall mean on 2026-11-01.

## Good for
- High-accuracy web-scale retrieval with compact indexes.
- Multilingual search where prompt management is unwanted.
- Self-hosted deployments under a permissive licence.
