---
id: jinaai/jina-reranker-v3.5
name: jina-reranker-v3.5
owned_by: jinaai
type: reranker
description: Jina AI's 0.6B-parameter multilingual listwise reranker built on Qwen3-0.6B, ranking a query against many documents in one forward pass over a 131K-token context; weights are CC-BY-NC-4.0.
aliases: [jina-reranker-v3.5, jinaai/jina-reranker-v3.5-GGUF, jinaai/jina-reranker-v3.5-mlx]
context_length: 131072
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
open_weights: true
license: CC-BY-NC-4.0
release_date: "2026-07-27"
sources:
  - https://huggingface.co/jinaai/jina-reranker-v3.5
  - https://huggingface.co/api/models/jinaai/jina-reranker-v3.5
  - https://huggingface.co/jinaai/jina-reranker-v3.5/raw/main/config.json
  - https://huggingface.co/jinaai/jina-reranker-v3.5-GGUF
  - https://huggingface.co/jinaai/jina-reranker-v3.5-mlx
  - https://arxiv.org/abs/2607.18152
  - https://www.elastic.co/search-labs/blog/jina-reranker-35-legal-medical-structured-data
  - https://jina.ai/reranker
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# jina-reranker-v3.5

## Overview
jina-reranker-v3.5 is Jina AI's current reranker, announced on Elastic's Search Labs blog on 2026-07-27 (Hugging Face repo created 2026-07-14, technical report arXiv 2607.18152) as a drop-in upgrade to jina-reranker-v3. OpenRouter does not list it; the id follows the Hugging Face repo, and the Jina API takes `jina-reranker-v3.5`. It has 597M parameters on Qwen3-0.6B: 28 layers with hybrid attention (sliding-window layers of 1,024 tokens interleaved with global layers) and a small MLP projector. Its "last but not late" listwise design puts the query and all candidates in one 131,072-token pass and scores each by cosine similarity, so there is no fixed document limit. It was trained on 52 languages. It loads in Transformers with `trust_remote_code`, and official GGUF and MLX builds exist. Weights are CC BY-NC 4.0; commercial use goes through Elastic sales, the Jina API, Elastic Inference Service or an on-premises container.

## Strengths
- Jina's nDCG@10 (top 100 from jina-embeddings-v5-text-small): 63.20 on BEIR, above Qwen3-Reranker-4B (62.28) and mxbai-rerank-large-v2 (62.45); 74.11 on MIRACL; 70.95 on RTEB.
- Gains over v3 on Struct-IR (48.3 against 38.7) and legal tasks such as AILA-Case (32.55 against 20.82).
- 1.22 to 1.56 times faster than v3 on listwise inference.

## Limitations
- Non-commercial licence for self-hosting.
- Qwen3-Reranker-4B still leads on MIRACL (76.56), RTEB (77.68) and Struct-IR (55.6).
- All candidates must fit in one context window.

## Good for
- Reranking long candidate lists in a single call.
- Legal, medical and structured-data retrieval.
- Research and prototypes on local hardware through GGUF or MLX.
