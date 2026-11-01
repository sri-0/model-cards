---
id: sentence-transformers/all-minilm-l12-v2
name: all-MiniLM-L12-v2
owned_by: sentence-transformers
type: embedding
description: all-MiniLM-L12-v2 is the Sentence Transformers community's 33.4M-parameter Apache-2.0 English sentence embedding model (12 layers, 384 dimensions) trained on over one billion sentence pairs.
aliases: [sentence-transformers/all-MiniLM-L12-v2, "all-minilm:33m", "all-minilm:l12", "all-minilm:l12-v2"]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: Apache-2.0
release_date: "2022-03-02"
embedding_dimensions: 384
pricing:
  input: 0.005
  output: 0
sources:
  - https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2
  - https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L12-v2
  - https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2/raw/main/config.json
  - https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2/raw/main/sentence_bert_config.json
  - https://huggingface.co/thenlper/gte-large
  - https://ollama.com/library/all-minilm/tags
  - https://openrouter.ai/sentence-transformers/all-minilm-l12-v2
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# all-MiniLM-L12-v2

## Overview
all-MiniLM-L12-v2 was built during the Hugging Face JAX/Flax community week, in the project "Train the Best Sentence Embedding Model Ever with 1B Training Pairs", alongside all-MiniLM-L6-v2. OpenRouter serves it on its embeddings endpoint as `sentence-transformers/all-minilm-l12-v2`, listing a 512-token context (the encoder's position count). The release date is the Hugging Face repo creation date, 2022-03-02, which postdates the training event. It fine-tunes microsoft/MiniLM-L12-H384-uncased with a contrastive objective on 1,170,060,424 pairs from Reddit, S2ORC, WikiAnswers, PAQ, StackExchange, MS MARCO and others, for 100k steps at batch size 1,024 on a TPU v3-8 with a 128-token training length. The 12-layer, 33.4M-parameter encoder returns 384-dimensional vectors. Ollama serves it as `all-minilm:l12` (`33m`).

## Strengths
- Alibaba's gte card lists 56.53 on the 56-dataset English MTEB, slightly above all-MiniLM-L6-v2 (56.26).
- Small and fast enough for CPU serving, with the same 384-dimensional output as the L6 model.
- Apache 2.0 with the training script and data configuration in the repo; no prompts are needed.
- About 2.4 million Hugging Face downloads in the month to 2026-11-01.

## Limitations
- The model card says input over 256 word pieces is truncated, but its sentence_bert_config.json sets 128; check the limit your library applies.
- English only, and lower-cased by the tokenizer.
- The MTEB leaderboard listed it without an overall English v2 mean on 2026-11-01.

## Good for
- Sentence similarity, clustering and deduplication on CPUs.
- Prototypes that want a little more quality than all-MiniLM-L6-v2.
- Low-cost hosted embeddings through OpenRouter.
