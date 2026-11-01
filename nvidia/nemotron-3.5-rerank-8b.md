---
id: nvidia/nemotron-3.5-rerank-8b
name: Nemotron 3.5 Rerank 8B
owned_by: nvidia
type: reranker
description: NVIDIA's 8.38B open-weight (OpenMDW-1.1) multilingual and multimodal cross-encoder reranker built on Ministral 3 8B, scoring text, page images or both against a text query over a 32,768-token window.
aliases: [nvidia/nemotron-3.5-rerank-8b:free, nvidia/Nemotron-3.5-Rerank-8B-BF16]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [rerank]
  tokenizer: Other
open_weights: true
license: OpenMDW-1.1
release_date: "2026-10-20"
sources:
  - https://openrouter.ai/nvidia/nemotron-3.5-rerank-8b:free
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/nvidia/Nemotron-3.5-Rerank-8B-BF16
  - https://huggingface.co/api/models/nvidia/Nemotron-3.5-Rerank-8B-BF16
  - https://huggingface.co/nvidia/Nemotron-3.5-Rerank-8B-BF16/raw/main/config.json
  - https://huggingface.co/blog/nvidia/nemotron-retriever-world-class-agentic-retrieval
  - https://openmdw.ai/license/1-1/
retrieved: "2026-11-01"
---

# Nemotron 3.5 Rerank 8B

## Overview
Nemotron-3.5-Rerank-8B is NVIDIA's multilingual, multimodal reranker for question-answering retrieval, released on Hugging Face on 2026-10-20 as `nvidia/Nemotron-3.5-Rerank-8B-BF16`. OpenRouter lists it only as the free `nvidia/nemotron-3.5-rerank-8b:free`, with a 32,768-token context. The 8.38B-parameter model pairs a Pixtral-based vision encoder with a bidirectional Ministral 3 language tower derived from Ministral-3-8B-Instruct-2512; it was trained first on text-only data, then on image and image-text data. Each input is one text query and one document (text, a page image or both, including charts, tables and infographics), and the output is a raw relevance logit. Images default to a 1,120-pixel longest edge, adjustable to 1,540. It runs in Transformers, Sentence Transformers and vLLM on NVIDIA Ampere, Hopper or Blackwell GPUs under Linux. The weights are under OpenMDW-1.1 for commercial or non-commercial use; the base model is Apache 2.0.

## Strengths
- NVIDIA reports state-of-the-art results on the ViDoRe v3.1 reranking leaderboard as of 2026-10-20.
- NDCG@10 reranking the top 50 from Nemotron-3.5-Embed-1B: 67.22 (image), 66.89 (text) and 67.56 (image plus text) on ViDoRe V3, and 78.69 on MIRACL-VISION, against 66.02, 64.88, 66.03 and 75.06 for Qwen3-VL-Reranker-8B.
- Evaluated on text retrieval in 34 languages and image retrieval in 18.

## Limitations
- One query-document pair per forward pass at 8B scale, so reranking cost grows with candidates.
- Published figures are NVIDIA's own and cover visual document retrieval only.
- Linux and NVIDIA GPUs only per the model card.

## Good for
- Multilingual vision RAG and agentic retrieval over document images.
- Reranking mixed text and page-image results in one model.
- Self-hosted deployments needing a permissive licence.
