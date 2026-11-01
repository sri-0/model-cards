---
id: jinaai/jina-embeddings-v5-omni-nano
name: Jina Embeddings v5 Omni Nano
owned_by: jinaai
type: embedding
description: jina-embeddings-v5-omni-nano is Jina AI's ~1.04B-parameter CC BY-NC 4.0 multimodal embedding model that adds frozen image, video and audio encoders to jina-embeddings-v5-text-nano, sharing its 768-dimensional vector space and 8,192-token input.
aliases: [jinaai/jina-embeddings-v5-omni-nano, jina-embeddings-v5-omni-nano, jinaai/jina-embeddings-v5-omni-nano-retrieval, jinaai/jina-embeddings-v5-omni-nano-text-matching, jinaai/jina-embeddings-v5-omni-nano-classification, jinaai/jina-embeddings-v5-omni-nano-clustering, jinaai/jina-embeddings-v5-omni-nano-retrieval-GGUF, jinaai/jina-embeddings-v5-omni-nano-text-matching-GGUF, jinaai/jina-embeddings-v5-omni-nano-classification-GGUF, jinaai/jina-embeddings-v5-omni-nano-clustering-GGUF, jinaai/jina-embeddings-v5-omni-nano-mlx]
context_length: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [embeddings]
open_weights: true
license: CC-BY-NC-4.0
release_date: "2026-05-11"
embedding_dimensions: 768
mteb_score: 65.52
sources:
  - https://huggingface.co/jinaai/jina-embeddings-v5-omni-nano
  - https://huggingface.co/api/models/jinaai/jina-embeddings-v5-omni-nano
  - https://huggingface.co/jinaai/jina-embeddings-v5-omni-nano/raw/main/config.json
  - https://arxiv.org/abs/2605.08384
  - https://www.elastic.co/search-labs/blog/jina-embeddings-v5-omni-all-media-one-index
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Jina Embeddings v5 Omni Nano

## Overview
jina-embeddings-v5-omni-nano was announced on 2026-05-11 (Hugging Face repo created 2026-04-01) with the larger omni-small; the technical report is arXiv 2605.08384. OpenRouter does not list it; the id follows the Hugging Face repo `jinaai/jina-embeddings-v5-omni-nano`. It keeps jina-embeddings-v5-text-nano frozen and adds a SigLIP2 Base vision encoder from Qwen3.5-0.8B and a Whisper-large-v3 audio encoder from Qwen2.5-Omni-7B, also frozen; only small projectors (under 3.5 million parameters per adapter) were trained. Text embeddings are identical to v5-text-nano, so existing text indexes can be queried with images, video, audio or PDFs. It has about 1.04B parameters, 768-dimensional output with documented truncation, an 8,192-token sequence length and four task adapters; retrieval inputs take `Query: ` or `Document: ` prefixes.

## Strengths
- The MTEB leaderboard showed 65.52 on MTEB (Multilingual, v2) and 71.11 on MTEB (English, v2) on 2026-11-01, the same text scores as v5-text-nano.
- Elastic's launch post says it beats models ten to sixty times larger on MMTEB and ranks among the top performers on MAEB audio retrieval.
- Small enough for commodity hardware, per Elastic; unused towers can be skipped at load time.

## Limitations
- CC BY-NC 4.0: commercial use needs a licence from Jina.
- Multimodal input needs transformers 5.0 or later and `trust_remote_code=True`.
- The query and document prefixes mainly affect text; image embeddings change little between the two, per the card.
- Video embeddings use frames only; a soundtrack must be passed as separate audio.
- Shorter context (8,192 tokens) than omni-small.

## Good for
- Edge or CPU-friendly search across text and media.
- Adding media search to an existing v5-text-nano index.
- Non-commercial multimodal prototypes.
