---
id: jinaai/jina-embeddings-v5-text-small
name: Jina Embeddings v5 Text Small
owned_by: jinaai
type: embedding
description: jina-embeddings-v5-text-small is Jina AI's 677M-parameter multilingual text embedding model on Qwen3-0.6B-Base, distilled from Qwen3-Embedding-4B, with task LoRA adapters, a 32K-token input and 1,024-dimensional Matryoshka vectors under CC BY-NC 4.0.
aliases: [jinaai/jina-embeddings-v5-text-small, jina-embeddings-v5-text-small, jinaai/jina-embeddings-v5-text-small-retrieval, jinaai/jina-embeddings-v5-text-small-text-matching, jinaai/jina-embeddings-v5-text-small-classification, jinaai/jina-embeddings-v5-text-small-clustering, jinaai/jina-embeddings-v5-text-small-retrieval-GGUF, jinaai/jina-embeddings-v5-text-small-text-matching-GGUF, jinaai/jina-embeddings-v5-text-small-classification-GGUF, jinaai/jina-embeddings-v5-text-small-clustering-GGUF, jinaai/jina-embeddings-v5-text-small-mlx]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: CC-BY-NC-4.0
release_date: "2026-02-18"
embedding_dimensions: 1024
mteb_score: 67.7
sources:
  - https://huggingface.co/jinaai/jina-embeddings-v5-text-small
  - https://huggingface.co/api/models/jinaai/jina-embeddings-v5-text-small
  - https://huggingface.co/jinaai/jina-embeddings-v5-text-small/raw/main/config.json
  - https://arxiv.org/abs/2602.15547
  - https://huggingface.co/jinaai/jina-embeddings-v5-omni-small
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# Jina Embeddings v5 Text Small

## Overview
jina-embeddings-v5-text-small was released on 2026-02-18 (Hugging Face repo created 2026-01-22) with a nano sibling; the technical report is arXiv 2602.15547. OpenRouter does not list it; the id follows the Hugging Face repo `jinaai/jina-embeddings-v5-text-small`, and Jina's API and Elastic Inference Service use `jina-embeddings-v5-text-small`. Built on Qwen3-0.6B-Base, it was trained by distilling embeddings from Qwen3-Embedding-4B combined with task-specific contrastive losses. Four LoRA adapters (retrieval, text matching, clustering, classification) are selected per call; separate repos merge each into the weights for vLLM, Text Embeddings Inference, ONNX and GGUF. It pools the last token, returns 1,024 dimensions (Matryoshka down to 32), accepts 32,768 tokens and supports 119+ languages. Retrieval inputs use query or document prompts.

## Strengths
- Jina reports 71.7 on MTEB (English, v2) and 67.7 on MMTEB, which the card calls the highest among multilingual models under 1B parameters.
- Embeddings are robust under truncation and binary quantisation, per Jina.
- Shares a vector space with jina-embeddings-v5-omni-small, so its text indexes can be queried with images, video or audio.

## Limitations
- CC BY-NC 4.0: commercial use needs a licence from Jina.
- Needs `trust_remote_code=True`, transformers 4.57 or later, torch 2.8 or later and peft.
- The MTEB leaderboard listed it without an overall mean on 2026-11-01, so 67.7 is Jina's own figure.
- vLLM and Text Embeddings Inference need the separate per-task repos.

## Good for
- Multilingual RAG and search under 1B parameters.
- Elasticsearch deployments through Elastic Inference Service.
- Non-commercial research on distilled embedders.
