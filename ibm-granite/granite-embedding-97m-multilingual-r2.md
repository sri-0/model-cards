---
id: ibm-granite/granite-embedding-97m-multilingual-r2
name: Granite Embedding 97M Multilingual R2
owned_by: ibm
type: embedding
description: Granite-Embedding-97M-Multilingual-R2 is IBM's 97M-parameter Apache-2.0 ModernBERT text embedding model, pruned from the 311M R2 model, with 384-dimensional vectors, a 32,768-token input and enhanced support for 52 languages plus code.
aliases: [ibm-granite/granite-embedding-97m-multilingual-r2]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2026-04-29"
embedding_dimensions: 384
mteb_score: 51.92
sources:
  - https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2
  - https://huggingface.co/api/models/ibm-granite/granite-embedding-97m-multilingual-r2
  - https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2/raw/main/config.json
  - https://arxiv.org/abs/2605.13521
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Granite Embedding 97M Multilingual R2

## Overview
Granite-Embedding-97M-Multilingual-R2 was released on 2026-04-29 (Hugging Face repo created 2026-04-20) with the 311M model; the paper is arXiv 2605.13521. OpenRouter does not list it; the id follows the Hugging Face repo `ibm-granite/granite-embedding-97m-multilingual-r2`. IBM built it from granite-embedding-311m-multilingual-r2 by pruning 22 layers to 12 and cutting the vocabulary from 262K to a purpose-trained 180K tokens, then recovered quality with multi-teacher distillation and contrastive fine-tuning. It is a ModernBERT encoder with SiLU activations, 384-dimensional output and a 32,768-token input, replacing granite-embedding-107m-multilingual. The encoder saw 200+ languages; 52 languages and nine programming languages get explicit retrieval training. Training data is permissively licensed or IBM-collected and generated.

## Strengths
- IBM reports 60.3 on MTEB multilingual retrieval (18 tasks), 9.4 points above multilingual-e5-small, plus 60.4 on MTEB (Code, v1) and 65.5 on LongEmbed.
- 14.6 points above granite-embedding-107m-multilingual on IBM's retrieval average, and IBM says it matches gte-multilingual-base retrieval at nearly three times the encoding speed.
- The MTEB leaderboard showed 51.92 Mean (Task) on MTEB (Multilingual, v2) on 2026-11-01.
- ONNX and OpenVINO weights; vLLM and llama.cpp (GGUF) are supported.

## Limitations
- As a pruned model it trades accuracy for speed; the 311M model scores 65.2 on the same retrieval set.
- The card lists no Matryoshka sizes for this model.
- Low-resource languages lose more quality here than in the 311M model, and the smaller vocabulary may tokenise some languages less efficiently.
- Ollama does not support ModernBERT models, per IBM.

## Good for
- Latency-sensitive multilingual search and edge deployments.
- High-throughput indexing of long documents.
- Enterprise use that needs an Apache 2.0 licence and clean data provenance.
