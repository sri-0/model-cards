---
id: sentence-transformers/multi-qa-mpnet-base-dot-v1
name: multi-qa-mpnet-base-dot-v1
owned_by: sentence-transformers
type: embedding
description: multi-qa-mpnet-base-dot-v1 is the Sentence Transformers community's 109M-parameter English semantic-search model on MPNet-base, trained on 215M question-answer pairs, returning unnormalised 768-dimensional vectors for dot-product scoring.
aliases: [sentence-transformers/multi-qa-mpnet-base-dot-v1]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
release_date: "2022-03-02"
embedding_dimensions: 768
pricing:
  input: 0.005
  output: 0
sources:
  - https://huggingface.co/sentence-transformers/multi-qa-mpnet-base-dot-v1
  - https://huggingface.co/api/models/sentence-transformers/multi-qa-mpnet-base-dot-v1
  - https://huggingface.co/sentence-transformers/multi-qa-mpnet-base-dot-v1/raw/main/config.json
  - https://huggingface.co/sentence-transformers/multi-qa-mpnet-base-dot-v1/raw/main/sentence_bert_config.json
  - https://openrouter.ai/sentence-transformers/multi-qa-mpnet-base-dot-v1
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# multi-qa-mpnet-base-dot-v1

## Overview
multi-qa-mpnet-base-dot-v1 was built during the Hugging Face JAX/Flax community week for semantic search. OpenRouter serves it on its embeddings endpoint as `sentence-transformers/multi-qa-mpnet-base-dot-v1` with a 512-token context. The release date is the Hugging Face repo creation date, 2022-03-02. It fine-tunes microsoft/mpnet-base (12 layers, 109M parameters) on 214,988,242 question-answer pairs from WikiAnswers, PAQ, StackExchange, MS MARCO, GOOAQ, Amazon QA, Yahoo Answers, SearchQA, ELI5, Quora, Natural Questions, SQuAD 2.0 and TriviaQA, using MultipleNegativesRankingLoss. Unlike the all-* models it uses CLS pooling and dot-product similarity, and its 768-dimensional embeddings are not normalised. Input is truncated at 512 word pieces, but training used up to 250. No prompts are needed. The model card states no licence.

## Strengths
- Trained specifically for matching questions and queries to answer passages.
- Documented for Sentence Transformers, Transformers and Text Embeddings Inference; ONNX and OpenVINO exports are in the repo.
- About 1.5 million Hugging Face downloads in the month to 2026-11-01.

## Limitations
- Scores must use dot product; cosine similarity on its unnormalised vectors is off the documented usage.
- Quality may drop on inputs longer than the 250 word pieces seen in training, per the card.
- English only, and no licence is given on the model card or in its metadata.
- Not on the MTEB leaderboard's English v2 table on 2026-11-01, and the card publishes no benchmark scores.

## Good for
- English FAQ, help-centre and question-answering search.
- Retrieval pipelines that already score with dot product.
- Low-cost hosted embeddings through OpenRouter.
