---
id: ibm-granite/granite-embedding-311m-multilingual-r2
name: Granite Embedding 311M Multilingual R2
owned_by: ibm
type: embedding
description: Granite-Embedding-311M-Multilingual-R2 is IBM's Apache-2.0 ModernBERT text embedding model with 768-dimensional Matryoshka vectors, a 32,768-token input and enhanced support for 52 languages plus code, trained only on data cleared for enterprise use.
aliases: [ibm-granite/granite-embedding-311m-multilingual-r2]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2026-04-29"
embedding_dimensions: 768
mteb_score: 55.96
sources:
  - https://huggingface.co/ibm-granite/granite-embedding-311m-multilingual-r2
  - https://huggingface.co/api/models/ibm-granite/granite-embedding-311m-multilingual-r2
  - https://huggingface.co/ibm-granite/granite-embedding-311m-multilingual-r2/raw/main/config.json
  - https://arxiv.org/abs/2605.13521
  - https://huggingface.co/ibm-granite/granite-embedding-english-r2
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# Granite Embedding 311M Multilingual R2

## Overview
Granite-Embedding-311M-Multilingual-R2 was released on 2026-04-29 (Hugging Face repo created 2026-04-20) with a 97M sibling; the paper is arXiv 2605.13521. OpenRouter does not list it; the id follows the Hugging Face repo `ibm-granite/granite-embedding-311m-multilingual-r2`. It replaces granite-embedding-278m-multilingual and swaps XLM-RoBERTa for ModernBERT: 22 layers, alternating attention, GeGLU, rotary positions and a 262K-token vocabulary derived from the Gemma 3 tokenizer. Output is 768 dimensions with Matryoshka sizes 512, 384, 256 and 128, and inputs run to 32,768 tokens (512 in R1). Training combined multi-teacher distillation, contrastive fine-tuning and model merging on permissively licensed, IBM-collected and IBM-generated data. The encoder saw 200+ languages; 52 languages and nine programming languages get explicit retrieval training. No query or document prompt is configured.

## Strengths
- IBM reports 65.2 on MTEB multilingual retrieval (18 tasks), 13 points above R1, plus 63.8 on MTEB (Code, v1) and 71.7 on LongEmbed.
- The MTEB leaderboard showed 55.96 Mean (Task) on MTEB (Multilingual, v2) on 2026-11-01.
- Truncating to 128 dimensions keeps multilingual retrieval at 62.5, against 63.9 at full size.
- ONNX and OpenVINO weights ship with the model; vLLM and llama.cpp (GGUF) are supported.
- Apache 2.0, with training data cleared for commercial use.

## Limitations
- Ollama does not support ModernBERT models, per IBM.
- Languages outside the 52-language set rely on cross-lingual transfer and score lower.
- For mainly English data IBM recommends granite-embedding-english-r2, which scores 56.4 on MTEB English v2 retrieval against 52.6 here.
- The tokenizer is derived from Gemma 3, and IBM notes its use is subject to the Gemma Terms of Use.

## Good for
- Enterprise multilingual RAG that needs clean data provenance.
- Long-document and code retrieval.
- CPU or Intel deployments through ONNX or OpenVINO.
