---
id: intfloat/e5-large-v2
name: E5-Large-v2
owned_by: microsoft
type: embedding
description: E5-large-v2 is Microsoft's 335M-parameter MIT-licensed English BERT-large embedding model trained with weakly supervised contrastive pre-training, returning 1,024-dimensional vectors for "query:" and "passage:" prefixed text up to 512 tokens.
aliases: [intfloat/e5-large-v2]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2023-05-19"
embedding_dimensions: 1024
mteb_score: 62.79
pricing:
  input: 0.01
  output: 0
sources:
  - https://huggingface.co/intfloat/e5-large-v2
  - https://huggingface.co/api/models/intfloat/e5-large-v2
  - https://huggingface.co/intfloat/e5-large-v2/raw/main/config.json
  - https://arxiv.org/abs/2212.03533
  - https://huggingface.co/BAAI/bge-large-en-v1.5
  - https://openrouter.ai/intfloat/e5-large-v2
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# E5-Large-v2

## Overview
E5-large-v2 is the large English model of Microsoft's E5 v2 family, from "Text Embeddings by Weakly-Supervised Contrastive Pre-training" (arXiv 2212.03533, submitted 2022-12-07). OpenRouter serves it on its embeddings endpoint as `intfloat/e5-large-v2` with a 512-token context. The release date is the Hugging Face repo creation date, 2023-05-19. It is a 24-layer BERT-large encoder (335M parameters) with 1,024-dimensional output. The paper trains E5 contrastively on CCPairs, a curated large-scale set of weakly supervised text pairs, and then fine-tunes it. Inputs need prefixes: `query: ` and `passage: ` for asymmetric retrieval, `query: ` alone for similarity, clustering and classification features. The weights are MIT licensed.

## Strengths
- BAAI's comparison table lists 62.25 on the 56-dataset English MTEB, with 86.03 on pair classification and 75.24 on classification; the MTEB leaderboard showed 62.79 on MTEB (English, v2) on 2026-11-01.
- The E5 paper reports it as the first model to beat BM25 on BEIR zero-shot without labelled data.
- Plain BERT architecture runs in any encoder stack, including Sentence Transformers.

## Limitations
- English only, and inputs are truncated at 512 tokens.
- Leaving out the prefixes degrades results, per the model card.
- Cosine similarities cluster between 0.7 and 1.0 because of the 0.01 contrastive temperature; only the ranking is meaningful.
- Newer models of the same size score higher, for example bge-large-en-v1.5 (65.89 on MTEB English v2).

## Good for
- English passage retrieval with a well-understood MIT-licensed baseline.
- Reproducing E5 results from the literature.
- Cheap hosted embeddings through OpenRouter.
