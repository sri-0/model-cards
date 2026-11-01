---
id: snowflake/snowflake-arctic-embed-l-v2.0
name: Snowflake Arctic Embed L v2.0
owned_by: snowflake
type: embedding
description: snowflake-arctic-embed-l-v2.0 is Snowflake's 568M-parameter Apache-2.0 multilingual retrieval embedder built on bge-m3-retromae, with 1,024-dimensional vectors, an 8,192-token context and Matryoshka truncation to 256 dimensions.
aliases: [Snowflake/snowflake-arctic-embed-l-v2.0, snowflake-arctic-embed2, "snowflake-arctic-embed2:568m"]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2024-12-04"
embedding_dimensions: 1024
mteb_score: 57.03
sources:
  - https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0
  - https://huggingface.co/api/models/Snowflake/snowflake-arctic-embed-l-v2.0
  - https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0/raw/main/config.json
  - https://arxiv.org/abs/2412.04506
  - https://ollama.com/library/snowflake-arctic-embed2/tags
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Snowflake Arctic Embed L v2.0

## Overview
snowflake-arctic-embed-l-v2.0 was released on 2024-12-04 with the medium model m-v2.0, per the model card's news section (Hugging Face repo created 2024-11-08). It is described in "Arctic-Embed 2.0: Multilingual Retrieval Without Compromise" (arXiv 2412.04506). OpenRouter does not list it; the id follows the Hugging Face repo `Snowflake/snowflake-arctic-embed-l-v2.0`. It fine-tunes BAAI/bge-m3-retromae, an XLM-RoBERTa-large encoder with RoPE, so it drops into bge-m3-shaped inference stacks: 568M parameters (303M non-embedding), 1,024-dimensional CLS-pooled output and an 8,192-token context. Queries take the prefix `query: `; documents take none. The card's metadata lists 74 languages. Ollama serves it as `snowflake-arctic-embed2` (`568m`).

## Strengths
- Snowflake reports NDCG@10 of 55.6 on BEIR (15), 55.8 on MIRACL (4), 52.9 on CLEF focused and 54.3 on CLEF full, keeping English quality while adding multilingual retrieval; bge-m3 scores 48.8 on BEIR in the same table.
- Matryoshka truncation to 256 dimensions costs under 3% (BEIR 54.3), and int4 quantisation brings vectors to 128 bytes.
- The MTEB leaderboard showed 57.03 Mean (Task) on MTEB (Multilingual, v2) and 63.60 on MTEB (English, v2) on 2026-11-01.
- Apache 2.0 with free commercial use.

## Limitations
- Only 256 is a trained Matryoshka size; the 128-byte target needs 4-bit quantisation, not further truncation.
- Tuned for retrieval: Snowflake publishes retrieval benchmarks only, and its MTEB means trail general-purpose models such as multilingual-e5-large-instruct (63.22).
- Omitting the query prefix is off the documented usage.

## Good for
- Enterprise multilingual search that must not regress on English.
- Replacing bge-m3 dense retrieval without changing serving code.
- Large indexes that compress vectors aggressively.
