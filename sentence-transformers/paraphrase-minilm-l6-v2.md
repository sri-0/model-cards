---
id: sentence-transformers/paraphrase-minilm-l6-v2
name: paraphrase-MiniLM-L6-v2
owned_by: sentence-transformers
type: embedding
description: paraphrase-MiniLM-L6-v2 is the Sentence Transformers project's 22.7M-parameter Apache-2.0 sentence embedding model (6 layers, 384 dimensions, mean pooling) for paraphrase detection, similarity and clustering of short texts.
aliases: [sentence-transformers/paraphrase-MiniLM-L6-v2]
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
  - https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2
  - https://huggingface.co/api/models/sentence-transformers/paraphrase-MiniLM-L6-v2
  - https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2/raw/main/config.json
  - https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2/raw/main/sentence_bert_config.json
  - https://arxiv.org/abs/1908.10084
  - https://openrouter.ai/sentence-transformers/paraphrase-minilm-l6-v2
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# paraphrase-MiniLM-L6-v2

## Overview
paraphrase-MiniLM-L6-v2 is one of the Sentence Transformers project's paraphrase models; the card cites the Sentence-BERT paper (arXiv 1908.10084, submitted 2019-08-27) and says the model was trained by sentence-transformers. OpenRouter serves it on its embeddings endpoint as `sentence-transformers/paraphrase-minilm-l6-v2`, listing a 512-token context (the encoder's position count) and describing it as optimised for paraphrase detection, similarity scoring, clustering and lightweight retrieval. The release date is the Hugging Face repo creation date, 2022-03-02. It is a 6-layer BERT encoder with 22.7M parameters that mean-pools token embeddings into a 384-dimensional vector. The Sentence Transformers configuration truncates input at 128 tokens. No prompts are needed, and the weights are Apache 2.0.

## Strengths
- Tiny and fast: the same size as all-MiniLM-L6-v2, suited to CPU and edge use.
- Works with Sentence Transformers or plain Transformers with mean pooling.
- About 1.4 million Hugging Face downloads in the month to 2026-11-01.

## Limitations
- Input beyond 128 tokens is truncated by default, so it suits sentences rather than passages.
- The model card gives no training data, languages or benchmark scores, and the model is not on the MTEB leaderboard's English v2 table on 2026-11-01.

## Good for
- Paraphrase and near-duplicate detection on short English sentences.
- Very low-latency similarity scoring.
- Low-cost hosted embeddings through OpenRouter.
