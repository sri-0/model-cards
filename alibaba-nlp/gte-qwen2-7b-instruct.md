---
id: alibaba-nlp/gte-qwen2-7b-instruct
name: gte-Qwen2-7B-instruct
owned_by: qwen
type: embedding
description: gte-Qwen2-7B-instruct is Alibaba's 7.6B-parameter Apache-2.0 decoder embedding model built on Qwen2-7B with bidirectional attention and query-side instructions, returning 3,584-dimensional vectors from up to 32K tokens.
aliases: [Alibaba-NLP/gte-Qwen2-7B-instruct]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2024-06-15"
embedding_dimensions: 3584
mteb_score: 62.51
sources:
  - https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct
  - https://huggingface.co/api/models/Alibaba-NLP/gte-Qwen2-7B-instruct
  - https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct/raw/main/config.json
  - https://arxiv.org/abs/2308.03281
  - https://huggingface.co/Qwen/Qwen3-Embedding-0.6B
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# gte-Qwen2-7B-instruct

## Overview
gte-Qwen2-7B-instruct is the largest model in Alibaba's GTE (General Text Embedding) family. The Hugging Face repo was created on 2024-06-15, used here as the release date, and the card says it ranked first in MTEB English and Chinese evaluations on 2024-06-16. OpenRouter does not list it; the id follows the Hugging Face repo `Alibaba-NLP/gte-Qwen2-7B-instruct`. It starts from Qwen2-7B (28 layers) and uses the same fine-tuning data and recipe as gte-Qwen1.5-7B-instruct, adding bidirectional attention and instruction tuning on the query side only. Training mixes weakly supervised and supervised multilingual data. Output is 3,584 dimensions and input runs to 32K tokens. Queries take `Instruct: {task}\nQuery: `; documents take none. The GTE training method is described in arXiv 2308.03281.

## Strengths
- Alibaba reports 70.24 on the 56-dataset English MTEB, 72.05 on C-MTEB, 68.25 on MTEB-fr and 67.86 on MTEB-pl.
- The MTEB leaderboard showed 62.51 Mean (Task) on MTEB (Multilingual, v2) and 70.72 on MTEB (English, v2) on 2026-11-01, the same figures Qwen quotes.
- Ahead of multilingual-e5-large-instruct on English v2 (70.72 against 65.53) in Qwen's table.
- Usage is documented for Sentence Transformers, Transformers and Infinity.

## Limitations
- Qwen3-Embedding-8B, from the same Alibaba group, scores higher (70.58 multilingual, 75.22 English v2).
- 7.6B parameters stored in float32, about 26 GB in Alibaba's size table.
- Needs `trust_remote_code=True`; transformers 4.39.2 and flash_attn 2.5.6 or later are listed requirements.
- The card documents no Matryoshka truncation.

## Good for
- Chinese and English retrieval where a well-benchmarked 2024 model is acceptable.
- Reproducing 2024 MTEB results.
- GPU deployments with memory to spare.
