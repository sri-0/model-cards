---
id: sentence-transformers/all-mpnet-base-v2
name: all-mpnet-base-v2
owned_by: sentence-transformers
type: embedding
description: all-mpnet-base-v2 is the Sentence Transformers community's 109M-parameter Apache-2.0 English sentence embedding model on MPNet-base, with 768-dimensional vectors, trained on over one billion sentence pairs.
aliases: [sentence-transformers/all-mpnet-base-v2]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: Apache-2.0
release_date: "2022-03-02"
embedding_dimensions: 768
pricing:
  input: 0.005
  output: 0
sources:
  - https://huggingface.co/sentence-transformers/all-mpnet-base-v2
  - https://huggingface.co/api/models/sentence-transformers/all-mpnet-base-v2
  - https://huggingface.co/sentence-transformers/all-mpnet-base-v2/raw/main/config.json
  - https://huggingface.co/sentence-transformers/all-mpnet-base-v2/raw/main/sentence_bert_config.json
  - https://huggingface.co/thenlper/gte-large
  - https://huggingface.co/BAAI/bge-base-en-v1.5
  - https://openrouter.ai/sentence-transformers/all-mpnet-base-v2
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# all-mpnet-base-v2

## Overview
all-mpnet-base-v2 was built during the Hugging Face JAX/Flax community week, in the project "Train the Best Sentence Embedding Model Ever with 1B Training Pairs". OpenRouter serves it on its embeddings endpoint as `sentence-transformers/all-mpnet-base-v2` with a 512-token context; config.json has 514 positions. The release date is the Hugging Face repo creation date, 2022-03-02, which postdates the training event. It fine-tunes microsoft/mpnet-base with a contrastive objective on 1,170,060,424 pairs from Reddit, S2ORC, WikiAnswers, PAQ, StackExchange, MS MARCO and others, for 100k steps at batch size 1,024 on a TPU v3-8 with a 128-token training length. The 12-layer, 109M-parameter encoder returns 768-dimensional vectors, and Sentence Transformers truncates input at 384 word pieces. No prompts are needed.

## Strengths
- Alibaba's gte card lists 57.78 on the 56-dataset English MTEB, above both all-MiniLM models (56.53 and 56.26), with 59.36 on reranking.
- Documented for Sentence Transformers, Transformers and Text Embeddings Inference (OpenAI-compatible `/v1/embeddings`).
- Apache 2.0 with the training script and data configuration in the repo.
- About 20 million Hugging Face downloads in the month to 2026-11-01.

## Limitations
- Input longer than 384 word pieces is truncated; it is meant for sentences and short paragraphs.
- English only.
- The MTEB leaderboard listed it without an overall English v2 mean on 2026-11-01; 2023-era models such as bge-base-en-v1.5 score higher on the older MTEB (63.55).

## Good for
- General sentence similarity and clustering in English.
- A widely supported default in vector databases and frameworks.
- Low-cost hosted embeddings through OpenRouter.
