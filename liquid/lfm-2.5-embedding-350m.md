---
id: liquid/lfm-2.5-embedding-350m
name: LFM2.5-Embedding-350M
owned_by: liquid
type: embedding
description: LFM2.5-Embedding-350M is Liquid AI's 354M-parameter open-weight multilingual retrieval embedder, a bidirectional LFM2.5 hybrid convolution-attention model with 1,024-dimensional vectors, a 512-token input and 11 supported languages.
aliases: ["liquid/lfm-2.5-embedding-350m:free", LiquidAI/LFM2.5-Embedding-350M, LiquidAI/LFM2.5-Embedding-350M-GGUF]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: LFM Open License v1.0
release_date: "2026-06-18"
embedding_dimensions: 1024
pricing:
  input: 0
  output: 0
sources:
  - https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M
  - https://huggingface.co/api/models/LiquidAI/LFM2.5-Embedding-350M
  - https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M/raw/main/config.json
  - https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M-GGUF
  - https://www.liquid.ai/blog/lfm2-5-retrievers
  - https://openrouter.ai/liquid/lfm-2.5-embedding-350m
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# LFM2.5-Embedding-350M

## Overview
LFM2.5-Embedding-350M was released on 2026-06-18 with LFM2.5-ColBERT-350M, the first bidirectional members of Liquid AI's LFM family (Hugging Face repo created 2026-05-05). OpenRouter serves it only as the free `liquid/lfm-2.5-embedding-350m:free`, and its description says successful requests and embeddings may be retained and used for training. It is built on LFM2.5-350M-Base, with the causal attention mask replaced by a bidirectional one and the short convolutions made non-causal: 17 layers (10 convolution, 6 attention, 1 pooling), a 65,536-token vocabulary and a 1,024-dimensional CLS vector. Training ran in three stages: English contrastive pre-training, multilingual and cross-lingual distillation from a teacher, and hard-negative fine-tuning. Documents run to 512 tokens. Queries take `query: ` and passages `document: `. It supports English, Spanish, German, French, Italian, Portuguese, Arabic, Swedish, Norwegian, Japanese and Korean.

## Strengths
- Liquid reports 0.577 NDCG@10 on its multilingual NanoBEIR set, above Qwen3-Embedding-0.6B (0.556), and 0.691 Recall@20 on MKQA-11 cross-lingual retrieval.
- 7.3 ms median query embedding on an M4 Max MacBook Pro through llama.cpp, and 1.5 ms on Liquid's GPU stack.
- GGUF builds for llama.cpp; Sentence Transformers fine-tuning works directly.

## Limitations
- Short 512-token documents; Liquid targets short-context search.
- Omitting the prompts silently degrades retrieval quality, per Liquid.
- Needs `trust_remote_code=True` for the bidirectional patches.
- LFM Open License rather than a standard open licence; the card publishes no MTEB mean.

## Good for
- Multilingual product, FAQ and support search.
- On-device search over files, email and notes.
- Free hosted trials through OpenRouter, where data retention is acceptable.
