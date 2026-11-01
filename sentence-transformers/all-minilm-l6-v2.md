---
id: sentence-transformers/all-minilm-l6-v2
name: all-MiniLM-L6-v2
owned_by: sentence-transformers
type: embedding
description: all-MiniLM-L6-v2 is the Sentence Transformers community's 22.7M-parameter Apache-2.0 English sentence embedding model (6 layers, 384 dimensions) trained on over one billion sentence pairs.
aliases: [sentence-transformers/all-MiniLM-L6-v2, all-minilm, "all-minilm:22m", "all-minilm:l6", "all-minilm:l6-v2"]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: Apache-2.0
release_date: "2022-03-02"
embedding_dimensions: 384
mteb_score: 59.03
pricing:
  input: 0.005
  output: 0
sources:
  - https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
  - https://huggingface.co/api/models/sentence-transformers/all-MiniLM-L6-v2
  - https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/raw/main/config.json
  - https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/raw/main/sentence_bert_config.json
  - https://huggingface.co/api/models?pipeline_tag=sentence-similarity&sort=downloads&direction=-1&limit=3
  - https://ollama.com/library/all-minilm/tags
  - https://openrouter.ai/sentence-transformers/all-minilm-l6-v2
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# all-MiniLM-L6-v2

## Overview
all-MiniLM-L6-v2 was built during the Hugging Face JAX/Flax community week, in the project "Train the Best Sentence Embedding Model Ever with 1B Training Pairs". OpenRouter serves it on its embeddings endpoint as `sentence-transformers/all-minilm-l6-v2`, listing a 512-token context (the encoder's position count). The release date is the Hugging Face repo creation date, 2022-03-02, which postdates the training event. It fine-tunes nreimers/MiniLM-L6-H384-uncased with a contrastive objective on 1,170,060,424 pairs from Reddit comments, S2ORC, WikiAnswers, PAQ, StackExchange, MS MARCO, GOOAQ, Yahoo Answers, NLI and others, for 100k steps at batch size 1,024 on a TPU v3-8 with a 128-token training length. The 6-layer, 22.7M-parameter encoder returns 384-dimensional vectors, and Sentence Transformers truncates input at 256 word pieces. Ollama's untagged `all-minilm` is this model (`22m`, `l6-v2`).

## Strengths
- Very small and fast: 384 dimensions and about 23M parameters run comfortably on CPU.
- The most-downloaded sentence-similarity model on Hugging Face, with about 186 million downloads in the month to 2026-11-01, so nearly every vector database and framework supports it.
- Apache 2.0 with the training script and data configuration in the repo.
- No prompts or prefixes are needed.

## Limitations
- Input longer than 256 word pieces is truncated by default; it is meant for sentences and short paragraphs.
- English only, and lower-cased by the tokenizer.
- The MTEB leaderboard showed 59.03 on MTEB (English, v2) on 2026-11-01, below newer small models such as granite-embedding-small-english-r2 (61.07, 47M parameters); the model card publishes no MTEB score.

## Good for
- Quick prototypes, tests and classroom examples.
- Clustering and deduplication of short English texts.
- Edge or CPU deployments where latency matters more than quality.
