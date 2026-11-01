---
id: mixedbread-ai/mxbai-embed-large-v1
name: mxbai-embed-large-v1
owned_by: mixedbread-ai
type: embedding
description: mxbai-embed-large-v1 is Mixedbread's 335M-parameter Apache-2.0 BERT-large English embedding model with 1,024-dimensional output, a 512-token input and support for Matryoshka truncation and binary quantisation.
aliases: [mixedbread-ai/mxbai-embed-large-v1, mxbai-embed-large, "mxbai-embed-large:335m", "mxbai-embed-large:v1"]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2024-03-07"
embedding_dimensions: 1024
mteb_score: 66.26
sources:
  - https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
  - https://huggingface.co/api/models/mixedbread-ai/mxbai-embed-large-v1
  - https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/raw/main/config.json
  - https://www.mixedbread.com/blog/mxbai-embed-large-v1
  - https://ollama.com/library/mxbai-embed-large/tags
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# mxbai-embed-large-v1

## Overview
mxbai-embed-large-v1 is Mixedbread's English sentence embedding model, announced on 2024-03-08. OpenRouter does not list it; the id follows the Hugging Face repo `mixedbread-ai/mxbai-embed-large-v1`, and the release date is the repo creation date, 2024-03-07. It is a 24-layer BERT-large (335M parameters) trained contrastively on over 700 million pairs and then tuned on over 30 million triplets with the AnglE loss, with no MTEB training data except MS MARCO. Output is 1,024 dimensions from a 512-token input. The model card says it supports Matryoshka truncation and binary quantisation; Mixedbread's API adds native int8 and binary output. No custom code is needed. Ollama serves it as `mxbai-embed-large`.

## Strengths
- Mixedbread reports a 64.68 average on the 56-dataset English MTEB, with 85.00 on STS and 75.64 on classification, ahead of OpenAI text-embedding-3-large (64.58) and bge-large-en-v1.5 (64.23) on that benchmark. The MTEB leaderboard showed 66.26 on MTEB (English, v2) on 2026-11-01.
- Only one prompt to manage: `Represent this sentence for searching relevant passages: ` on retrieval queries, nothing otherwise.
- Runs in Sentence Transformers, Transformers, Transformers.js and Infinity.

## Limitations
- English only.
- Inputs are truncated at 512 tokens; Mixedbread chose not to support long context.
- A single prompt; Mixedbread notes domain-specific prompts could help but are not supported.
- The card's Matryoshka and binary claims come without published per-dimension scores.

## Good for
- English semantic search and RAG with a permissive licence.
- Memory-constrained vector stores using binary or truncated vectors.
- Drop-in use through Ollama or Transformers.js.
