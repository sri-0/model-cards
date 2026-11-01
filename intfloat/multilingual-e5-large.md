---
id: intfloat/multilingual-e5-large
name: Multilingual-E5-Large
owned_by: microsoft
type: embedding
description: Multilingual-E5-large is Microsoft's 560M-parameter MIT-licensed XLM-RoBERTa-large embedding model trained with "query:" and "passage:" prefixes, producing 1,024-dimensional vectors for 100 languages.
aliases: [intfloat/multilingual-e5-large]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2023-06-30"
embedding_dimensions: 1024
pricing:
  input: 0.01
  output: 0
sources:
  - https://huggingface.co/intfloat/multilingual-e5-large
  - https://huggingface.co/api/models/intfloat/multilingual-e5-large
  - https://huggingface.co/intfloat/multilingual-e5-large/raw/main/config.json
  - https://arxiv.org/abs/2402.05672
  - https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct
  - https://openrouter.ai/intfloat/multilingual-e5-large
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# Multilingual-E5-Large

## Overview
Multilingual-E5-large is the largest of Microsoft's three multilingual E5 models (small, base, large), released in mid-2023 according to the technical report arXiv 2402.05672. OpenRouter serves it on its embeddings endpoint as `intfloat/multilingual-e5-large`, with a 512-token context. The release date is the Hugging Face repo creation date, 2023-06-30. It is initialised from xlm-roberta-large (24 layers, 1,024-dimensional output, 560M parameters) and trained in two stages: weakly supervised contrastive pre-training on pairs from mC4 (1B), NLLB translations (2.4B), Reddit (800M), CC News, Wikipedia, S2ORC, StackExchange and xP3, then supervised fine-tuning on MS MARCO, NQ, TriviaQA, NLI, ELI5, DuReader, FEVER, HotpotQA, SQuAD, Quora, Mr. TyDi and MIRACL. The weights are MIT licensed.

## Strengths
- Average MRR@10 of 70.5 on Mr. TyDi across 11 languages, against 64.4 for the small and 65.9 for the base model.
- Alibaba's gte-Qwen2 card lists 61.50 on the 56-dataset English MTEB and 58.81 on C-MTEB.
- Supports the 100 languages of XLM-RoBERTa; Sentence Transformers usage is documented.
- A widely deployed baseline: about 6.7 million Hugging Face downloads in the month to 2026-11-01.

## Limitations
- Inputs are truncated at 512 tokens.
- Prefixes are mandatory: `query:` and `passage:` for retrieval, `query:` alone for symmetric tasks and features; leaving them off degrades results.
- Low-resource languages may see lower quality.
- Cosine similarities cluster between 0.7 and 1.0; only the ranking matters.
- The MTEB leaderboard showed no overall MTEB (Multilingual, v2) mean for it on 2026-11-01; Microsoft also publishes an instruction-tuned variant, `intfloat/multilingual-e5-large-instruct`.

## Good for
- Multilingual passage retrieval where a fixed prefix scheme is acceptable.
- Bitext mining and cross-lingual similarity.
- Reproducing published results that used the E5 baseline.
