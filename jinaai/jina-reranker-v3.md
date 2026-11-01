---
id: jinaai/jina-reranker-v3
name: jina-reranker-v3
owned_by: jinaai
type: reranker
description: Jina AI's previous 0.6B-parameter multilingual listwise reranker built on Qwen3-0.6B, ranking up to 64 documents per pass within a 131K-token context; superseded by jina-reranker-v3.5 and CC-BY-NC-4.0 licensed.
aliases: [jina-reranker-v3, jinaai/jina-reranker-v3-GGUF, jinaai/jina-reranker-v3-mlx]
context_length: 131072
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
open_weights: true
license: CC-BY-NC-4.0
release_date: "2025-10-03"
sources:
  - https://huggingface.co/jinaai/jina-reranker-v3
  - https://huggingface.co/api/models/jinaai/jina-reranker-v3
  - https://huggingface.co/jinaai/jina-reranker-v3/raw/main/config.json
  - https://huggingface.co/jinaai/jina-reranker-v3-GGUF
  - https://huggingface.co/jinaai/jina-reranker-v3-mlx
  - https://jina.ai/news/jina-reranker-v3-0-6b-listwise-reranker-for-sota-multilingual-retrieval
  - https://arxiv.org/abs/2509.25085
  - https://huggingface.co/jinaai/jina-reranker-v3.5
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# jina-reranker-v3

## Overview
jina-reranker-v3 is superseded: its Hugging Face card tells new projects to use jina-reranker-v3.5, a drop-in upgrade with the same API. Jina AI announced v3 on 2025-10-03 (Hugging Face repo created 2025-09-18, technical report arXiv 2509.25085). OpenRouter does not list it; the id follows the Hugging Face repo, and the Jina API takes `jina-reranker-v3`. It has 0.6B parameters on Qwen3-0.6B, with 28 layers and an MLP projector (1024 to 512 to 256). Its "last but not late" design runs causal self-attention over the query and up to 64 documents in one 131,072-token window and takes each document's embedding from its last token. It loads in Transformers with `trust_remote_code`; official GGUF and MLX builds exist. Weights are CC BY-NC 4.0.

## Strengths
- Jina's nDCG@10: 61.94 on BEIR, 66.83 on MIRACL, 67.92 on MKQA and 70.64 on CoIR, ahead of mxbai-rerank-large-v2 (61.44) and Qwen3-Reranker-4B (61.16) on BEIR.
- Listwise ranking compares candidates with each other in one pass.
- Jina says it is 10 times smaller than generative listwise rerankers.

## Limitations
- jina-reranker-v3.5 scores higher in Jina's later comparison (63.20 against 62.10 BEIR) and runs 1.22 to 1.56 times faster.
- bge-reranker-v2-m3 leads it on MIRACL (69.32) and Qwen3-Reranker-4B on CoIR (73.91).
- Non-commercial licence for self-hosting.

## Good for
- Existing pipelines built on v3, until they switch the model id to v3.5.
- Research on listwise reranking.
- Local experiments through GGUF or MLX.
