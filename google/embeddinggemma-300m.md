---
id: google/embeddinggemma-300m
name: EmbeddingGemma 300M
owned_by: google
type: embedding
description: EmbeddingGemma is Google DeepMind's 308M-parameter open-weight text embedding model built from Gemma 3 for on-device retrieval, with 768-dimensional Matryoshka vectors, a 2,048-token input and 100+ languages.
aliases: [google/embeddinggemma-300m, embeddinggemma, "embeddinggemma:300m", "embeddinggemma:300m-qat-q8_0", "embeddinggemma:300m-qat-q4_0", google/embeddinggemma-300m-qat-q8_0-unquantized, google/embeddinggemma-300m-qat-q4_0-unquantized]
context_length: 2048
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Gemma Terms of Use
release_date: "2025-09-04"
embedding_dimensions: 768
mteb_score: 61.15
sources:
  - https://huggingface.co/google/embeddinggemma-300m
  - https://huggingface.co/api/models/google/embeddinggemma-300m
  - https://ai.google.dev/gemma/docs/embeddinggemma/model_card
  - https://developers.googleblog.com/en/introducing-embeddinggemma/
  - https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/
  - https://arxiv.org/abs/2509.20354
  - https://ollama.com/library/embeddinggemma/tags
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# EmbeddingGemma 300M

## Overview
EmbeddingGemma was announced on 2025-09-04 (Hugging Face repo created 2025-07-17) and is described in arXiv 2509.20354. OpenRouter does not list it; the id follows the Hugging Face repo `google/embeddinggemma-300m`. Google counts 308M parameters, roughly 100M in the transformer and 200M in the embedding table, on a Gemma 3 backbone with T5Gemma initialisation and the Gemma 3n tokenizer. It takes up to 2,048 tokens and returns a 768-dimensional vector that Matryoshka training lets you truncate to 512, 256 or 128 and re-normalise. Training used about 320 billion tokens in 100+ languages. The weights are gated behind the Gemma Terms of Use; QAT checkpoints (Q8_0, Q4_0, mixed precision) are published alongside. Ollama serves it as `embeddinggemma`.

## Strengths
- Google's model card reports MTEB (Multilingual, v2) Mean (Task) 61.15, MTEB (English, v2) 69.67 and MTEB (Code, v1) 68.76 at 768 dimensions; 128 dimensions still scores 58.23 multilingual. The MTEB leaderboard showed 61.14 and 69.67 on 2026-11-01.
- QAT checkpoints lose little: Q8_0 scores 60.93 and Q4_0 60.62 multilingual, and Google quotes under 200 MB of RAM when quantised.
- Under 15 ms to embed 256 tokens on EdgeTPU, per the launch post.
- Task prompts cover search, question answering, fact checking, classification, clustering and code retrieval.

## Limitations
- Input is capped at 2,048 tokens; use the query prompt `task: search result | query: {content}` and the document prompt `title: {title | "none"} | text: {content}`.
- Activations do not support float16; run it in float32 or bfloat16.
- Gated: accept Google's terms before downloading.
- For large server-side applications Google points to its Gemini Embedding API instead.
- EmbeddingGemma 2 (2026-10) adds 8,192-token input and media.

## Good for
- On-device or laptop RAG and semantic search in many languages.
- Text and code in one small embedder.
- Storage-constrained indexes that truncate to 256 or 128 dimensions.
