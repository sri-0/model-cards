---
id: intfloat/e5-base-v2
name: E5-Base-v2
owned_by: microsoft
type: embedding
description: E5-base-v2 is Microsoft's 109M-parameter MIT-licensed English BERT-base embedding model trained with weakly supervised contrastive pre-training, returning 768-dimensional vectors for "query:" and "passage:" prefixed text up to 512 tokens.
aliases: [intfloat/e5-base-v2]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2023-05-19"
embedding_dimensions: 768
mteb_score: 62.67
pricing:
  input: 0.005
  output: 0
sources:
  - https://huggingface.co/intfloat/e5-base-v2
  - https://huggingface.co/api/models/intfloat/e5-base-v2
  - https://huggingface.co/intfloat/e5-base-v2/raw/main/config.json
  - https://arxiv.org/abs/2212.03533
  - https://huggingface.co/BAAI/bge-large-en-v1.5
  - https://huggingface.co/ibm-granite/granite-embedding-english-r2
  - https://openrouter.ai/intfloat/e5-base-v2
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# E5-Base-v2

## Overview
E5-base-v2 is the base-sized English model of Microsoft's E5 v2 family, from "Text Embeddings by Weakly-Supervised Contrastive Pre-training" (arXiv 2212.03533, submitted 2022-12-07). OpenRouter serves it on its embeddings endpoint as `intfloat/e5-base-v2` with a 512-token context. The release date is the Hugging Face repo creation date, 2023-05-19. It is a 12-layer BERT-base encoder (109M parameters) with 768-dimensional output. The paper trains E5 contrastively on CCPairs, a curated large-scale set of weakly supervised text pairs, and then fine-tunes it. Inputs need prefixes: `query: ` and `passage: ` for asymmetric retrieval, `query: ` alone for similarity, clustering and classification features. The weights are MIT licensed. About one million Hugging Face downloads in the month to 2026-11-01.

## Strengths
- BAAI's comparison table lists 61.5 on the 56-dataset English MTEB; the MTEB leaderboard showed 62.67 on MTEB (English, v2) on 2026-11-01, close to e5-large-v2 (62.79) at a third of the size.
- IBM's comparison gives 49.7 on MTEB English v2 retrieval and 50.3 on CoIR code retrieval.
- Small enough for CPU serving in any BERT stack.

## Limitations
- English only, and inputs are truncated at 512 tokens.
- Leaving out the prefixes degrades results, per the model card.
- Cosine similarities cluster between 0.7 and 1.0 because of the 0.01 contrastive temperature; only the ranking is meaningful.
- Newer base-sized models score higher, for example bge-base-en-v1.5 (65.14 on MTEB English v2).

## Good for
- Lightweight English retrieval and clustering.
- A reference baseline in embedding evaluations.
- Low-cost hosted embeddings through OpenRouter.
