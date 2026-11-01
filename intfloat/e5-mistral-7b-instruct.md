---
id: intfloat/e5-mistral-7b-instruct
name: E5 Mistral 7B Instruct
owned_by: microsoft
type: embedding
description: E5-mistral-7b-instruct is Microsoft's 7B-parameter MIT-licensed decoder-based embedding model fine-tuned from Mistral-7B-v0.1 on LLM-generated synthetic data, returning 4,096-dimensional vectors with instruction-prefixed queries.
aliases: [intfloat/e5-mistral-7b-instruct]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: MIT
release_date: "2023-12-20"
embedding_dimensions: 4096
mteb_score: 67.97
sources:
  - https://huggingface.co/intfloat/e5-mistral-7b-instruct
  - https://huggingface.co/api/models/intfloat/e5-mistral-7b-instruct
  - https://huggingface.co/intfloat/e5-mistral-7b-instruct/raw/main/config.json
  - https://huggingface.co/intfloat/e5-mistral-7b-instruct/raw/main/sentence_bert_config.json
  - https://arxiv.org/abs/2401.00368
  - https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# E5 Mistral 7B Instruct

## Overview
E5-mistral-7b-instruct accompanies the paper "Improving Text Embeddings with Large Language Models" (arXiv 2401.00368, submitted 2023-12-31). OpenRouter does not list it; the id follows the Hugging Face repo `intfloat/e5-mistral-7b-instruct`, and the release date is the repo creation date, 2023-12-20. It is Mistral-7B-v0.1 (32 layers, 4,096-dimensional output, 7.1B parameters in float16) fine-tuned with a contrastive loss on synthetic data that proprietary LLMs generated for hundreds of thousands of embedding tasks in 93 languages, plus labelled data. Queries take a one-sentence instruction (`Instruct: {task}\nQuery: {text}`); documents do not. The Sentence Transformers config allows 32,768 tokens. LoRA-only weights are published in the repo. The licence is MIT.

## Strengths
- The MTEB leaderboard showed 67.97 Mean (Task) on MTEB (English, v2) and 60.03 on MTEB (Multilingual, v2) on 2026-11-01; Alibaba's gte-Qwen2 card quotes 66.63 on the 56-dataset English MTEB.
- The paper reports state-of-the-art BEIR and MTEB results at release with under 1,000 training steps.
- Instruction prompts (web search, STS, summarisation and more) are preconfigured for Sentence Transformers.

## Limitations
- Microsoft does not recommend inputs over 4,096 tokens, despite the 32,768-token config.
- Recommended for English only; its multilingual quality is below multilingual-e5-large in some cases.
- A 7.1B-parameter decoder, so serving costs far more than the 560M multilingual E5 encoders.
- Omitting the query instruction degrades results, per the model card.

## Good for
- English retrieval where embedding quality outweighs serving cost.
- Research on instruction-conditioned embeddings and LoRA fine-tuning.
- GPU deployments that already run a Mistral-class model.
