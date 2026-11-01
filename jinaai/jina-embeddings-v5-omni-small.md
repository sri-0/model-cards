---
id: jinaai/jina-embeddings-v5-omni-small
name: Jina Embeddings v5 Omni Small
owned_by: jinaai
type: embedding
description: jina-embeddings-v5-omni-small is Jina AI's ~1.74B-parameter CC BY-NC 4.0 multimodal embedding model that adds frozen image, video and audio encoders to jina-embeddings-v5-text-small, sharing its 1,024-dimensional vector space and 32K-token input.
aliases: [jinaai/jina-embeddings-v5-omni-small, jina-embeddings-v5-omni-small, jinaai/jina-embeddings-v5-omni-small-retrieval, jinaai/jina-embeddings-v5-omni-small-text-matching, jinaai/jina-embeddings-v5-omni-small-classification, jinaai/jina-embeddings-v5-omni-small-clustering, jinaai/jina-embeddings-v5-omni-small-retrieval-GGUF, jinaai/jina-embeddings-v5-omni-small-text-matching-GGUF, jinaai/jina-embeddings-v5-omni-small-classification-GGUF, jinaai/jina-embeddings-v5-omni-small-clustering-GGUF, jinaai/jina-embeddings-v5-omni-small-mlx]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [embeddings]
open_weights: true
license: CC-BY-NC-4.0
release_date: "2026-05-11"
embedding_dimensions: 1024
mteb_score: 67.0
sources:
  - https://huggingface.co/jinaai/jina-embeddings-v5-omni-small
  - https://huggingface.co/api/models/jinaai/jina-embeddings-v5-omni-small
  - https://huggingface.co/jinaai/jina-embeddings-v5-omni-small/raw/main/config.json
  - https://arxiv.org/abs/2605.08384
  - https://www.elastic.co/search-labs/blog/jina-embeddings-v5-omni-all-media-one-index
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Jina Embeddings v5 Omni Small

## Overview
jina-embeddings-v5-omni-small was announced on 2026-05-11 (Hugging Face repo created 2026-04-01) with a nano sibling; the technical report is arXiv 2605.08384. OpenRouter does not list it; the id follows the Hugging Face repo `jinaai/jina-embeddings-v5-omni-small`, and Elastic Inference Service uses `jina-embeddings-v5-omni-small`. It keeps jina-embeddings-v5-text-small frozen and adds a SigLIP2 So400m vision encoder from Qwen3.5-2B and a Whisper-large-v3 audio encoder from Qwen2.5-Omni-7B, also frozen; only the connecting projectors (0.35% of the weights) were trained. Text embeddings are identical to v5-text-small, so existing text indexes can be queried with images, video, audio or PDFs. It has about 1.74B parameters, 1,024-dimensional output (Matryoshka down to 32), a 32,768-token sequence length and four task adapters; retrieval inputs take `Query: ` or `Document: ` prefixes.

## Strengths
- The MTEB leaderboard showed 67.00 on MTEB (Multilingual, v2) and 71.78 on MTEB (English, v2) on 2026-11-01.
- Elastic's launch post rates it best in its size class on image benchmarks and says only models twice its size or more beat it on audio (MAEB).
- Unused vision or audio towers can be skipped at load time to save memory.
- Trained for Elasticsearch Better Binary Quantization; binarisation costs under 3% on MTEB retrieval, per Elastic.

## Limitations
- CC BY-NC 4.0: commercial use needs a licence from Jina.
- Video embeddings use frames only; a soundtrack must be passed as separate audio.
- Needs `trust_remote_code=True`; the vLLM path is validated on vllm 0.20.1 with one task per instance.
- The card shows image, video and audio results only as a chart.

## Good for
- One index across text, images, video, audio and PDFs.
- Adding media search to an existing v5-text-small index without re-embedding.
- Elasticsearch deployments.
