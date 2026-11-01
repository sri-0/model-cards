---
id: intfloat/multilingual-e5-large-instruct
name: Multilingual E5 Large Instruct
owned_by: microsoft
type: embedding
description: Multilingual-E5-large-instruct is Microsoft's 560M-parameter MIT-licensed XLM-RoBERTa-large embedding model, fine-tuned with natural-language task instructions on the query side, covering 100 languages at 1,024 dimensions.
aliases: [intfloat/multilingual-e5-large-instruct]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: MIT
release_date: "2024-02-08"
embedding_dimensions: 1024
mteb_score: 63.22
sources:
  - https://huggingface.co/intfloat/multilingual-e5-large-instruct
  - https://huggingface.co/api/models/intfloat/multilingual-e5-large-instruct
  - https://huggingface.co/intfloat/multilingual-e5-large-instruct/raw/main/config.json
  - https://arxiv.org/abs/2402.05672
  - https://huggingface.co/Qwen/Qwen3-Embedding-0.6B
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Multilingual E5 Large Instruct

## Overview
Multilingual-E5-large-instruct is the instruction-tuned member of Microsoft's multilingual E5 family, described in the technical report arXiv 2402.05672. OpenRouter does not list it; the id follows the Hugging Face repo `intfloat/multilingual-e5-large-instruct`, and the release date is the repo creation date, 2024-02-08, the day the report was submitted. The model is initialised from xlm-roberta-large (24 layers, 1,024-dimensional output), contrastively pre-trained on one billion weakly supervised text pairs and then fine-tuned on the datasets from the E5-mistral paper. It supports the 100 languages of XLM-RoBERTa. Queries carry a one-sentence instruction (`Instruct: {task}\nQuery: {text}`); documents need no prefix. The weights are MIT licensed.

## Strengths
- The MTEB leaderboard showed 63.22 Mean (Task) on MTEB (Multilingual, v2) and 65.56 on MTEB (English, v2) on 2026-11-01; Qwen's table, taken from the leaderboard on 2025-05-24, gives the same 63.22, ahead of BGE-M3 (59.56) at a similar size.
- Instructions let one model serve retrieval, clustering, classification and similarity tasks.
- Small enough for CPU serving; works with Sentence Transformers, Transformers and Infinity.

## Limitations
- Inputs are truncated at 512 tokens (config.json has 514 positions).
- Omitting the query instruction degrades results, per the model card.
- Low-resource languages may see lower quality.
- Cosine similarities cluster between 0.7 and 1.0 because of the 0.01 contrastive temperature; only the ranking is meaningful.

## Good for
- Multilingual retrieval and RAG over short passages.
- Cross-lingual search where queries and documents differ in language.
- Teams that want a permissive licence and a well-known baseline.
