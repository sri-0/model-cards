---
id: jinaai/jina-embeddings-v4
name: Jina Embeddings v4
owned_by: jinaai
type: embedding
description: jina-embeddings-v4 is Jina AI's 3.8B-parameter multimodal, multilingual embedding model built on Qwen2.5-VL-3B-Instruct, with single-vector (2,048-dimensional, Matryoshka to 128) and multi-vector output, task LoRA adapters and a 32K-token input.
aliases: [jinaai/jina-embeddings-v4, jina-embeddings-v4, jinaai/jina-embeddings-v4-vllm-retrieval, jinaai/jina-embeddings-v4-vllm-text-matching, jinaai/jina-embeddings-v4-vllm-code, jinaai/jina-embeddings-v4-text-retrieval-GGUF, jinaai/jina-embeddings-v4-text-matching-GGUF, jinaai/jina-embeddings-v4-text-code-GGUF]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [embeddings]
open_weights: true
license: Qwen Research License
release_date: "2025-06-25"
embedding_dimensions: 2048
sources:
  - https://huggingface.co/jinaai/jina-embeddings-v4
  - https://huggingface.co/api/models/jinaai/jina-embeddings-v4
  - https://huggingface.co/jinaai/jina-embeddings-v4/raw/main/config.json
  - https://jina.ai/news/jina-embeddings-v4-universal-embeddings-for-multimodal-multilingual-retrieval
  - https://arxiv.org/abs/2506.18902
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# Jina Embeddings v4

## Overview
jina-embeddings-v4 was announced on 2025-06-25 (Hugging Face repo created 2025-05-07) with the technical report arXiv 2506.18902. OpenRouter does not list it; the id follows the Hugging Face repo `jinaai/jina-embeddings-v4`, and Jina's API uses `jina-embeddings-v4`. It is built on Qwen2.5-VL-3B-Instruct (3.8B parameters) with three 60M-parameter LoRA adapters for retrieval, text matching and code, chosen at inference time. Text, images and visually rich documents (charts, tables, screenshots) pass through one decoder, giving either a mean-pooled 2,048-dimensional vector, truncatable to 1,024, 512, 256 or 128, or 128-dimensional per-token multi-vectors for late interaction. Inputs run to 32,768 tokens and the card claims 30+ languages. Separate vLLM repos merge each adapter into the weights, and GGUF builds are published.

## Strengths
- Jina reports 66.49 on MMTEB retrieval against 59.27 for OpenAI text-embedding-3-large, 67.11 on LongEmbed and 71.59 on CoIR code retrieval.
- Visual document retrieval: 90.17 on ViDoRe, per Jina's launch post, with the multi-vector mode scoring highest on the specialised sets.
- One model covers text, images and code, with dense and multi-vector modes.

## Limitations
- The licence is the Qwen Research License inherited from Qwen2.5-VL-3B (the card corrects an earlier CC BY-NC 4.0 label); check its terms before commercial use.
- Jina submitted only retrieval and STS results to MTEB, so the leaderboard showed no overall mean on 2026-11-01.
- Needs `trust_remote_code=True`, transformers 4.52 or later and peft.
- Jina's API caps inputs at 8K tokens; the full 32K needs self-hosting.
- Text-only gains over the 570M v3 are modest (55.97 against 54.33 on MTEB-EN, per Jina).

## Good for
- Retrieval over visually rich documents such as charts, tables and screenshots.
- Multilingual and code search with one model.
- Late-interaction (ColBERT-style) pipelines.
