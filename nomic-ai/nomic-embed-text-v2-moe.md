---
id: nomic-ai/nomic-embed-text-v2-moe
name: Nomic Embed Text v2 MoE
owned_by: nomic-ai
type: embedding
description: nomic-embed-text-v2-moe is Nomic AI's Apache-2.0 mixture-of-experts multilingual text embedder (475M parameters, 305M active) with 768-dimensional Matryoshka vectors, a 512-token input and roughly 100 languages.
aliases: [nomic-ai/nomic-embed-text-v2-moe, nomic-embed-text-v2-moe, nomic-ai/nomic-embed-text-v2-moe-GGUF]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2025-02-07"
embedding_dimensions: 768
mteb_score: 57.64
sources:
  - https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe
  - https://huggingface.co/api/models/nomic-ai/nomic-embed-text-v2-moe
  - https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe/raw/main/config.json
  - https://arxiv.org/abs/2502.07972
  - https://ollama.com/library/nomic-embed-text-v2-moe/tags
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Nomic Embed Text v2 MoE

## Overview
nomic-embed-text-v2-moe is described in "Training Sparse Mixture Of Experts Text Embedding Models" (arXiv 2502.07972, submitted 2025-02-11) as the first general-purpose MoE text embedding model. OpenRouter does not list it; the id follows the Hugging Face repo `nomic-ai/nomic-embed-text-v2-moe`, and the release date is the repo creation date, 2025-02-07. It has 475M total parameters with 305M active, eight experts and top-2 routing, trained on 1.6 billion pairs with consistency filtering, then supervised fine-tuning. Output is 768 dimensions, truncatable to 256 through Matryoshka training, and the maximum input is 512 tokens. Weights, training code (contrastors) and data are all released under Apache 2.0. Ollama lists it as `nomic-embed-text-v2-moe`, and Nomic publishes GGUF files.

## Strengths
- Nomic reports BEIR 52.86 and MIRACL 65.80, above mE5 base (48.88 / 62.30) and mGTE base (51.10 / 63.40) at a similar active size.
- The MTEB leaderboard showed 57.64 Mean (Task) on MTEB (Multilingual, v2) and 63.64 on MTEB (English, v2) on 2026-11-01.
- 256-dimensional vectors cut storage threefold with small quality loss.
- Supports about 100 languages.

## Limitations
- Inputs are capped at 512 tokens.
- Prefixes are required: `search_query: ` and `search_document: `.
- Needs `trust_remote_code=True` for the custom architecture.
- Resource needs can exceed a dense model's because of the MoE design, and quality varies by language, per Nomic.

## Good for
- Multilingual RAG over short chunks at a 300M-parameter compute budget.
- Fully reproducible pipelines that want open data and code.
- Local serving through Ollama or llama.cpp.
