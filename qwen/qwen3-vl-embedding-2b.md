---
id: qwen/qwen3-vl-embedding-2b
name: Qwen3 VL Embedding 2B
owned_by: qwen
type: embedding
description: Qwen3-VL-Embedding-2B is Qwen's Apache-2.0 multimodal embedding model built on Qwen3-VL-2B-Instruct that maps text, images, screenshots and video into one space with 2,048-dimensional vectors truncatable to 64 and a 32K-token input.
aliases: [Qwen/Qwen3-VL-Embedding-2B]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2026-01-07"
embedding_dimensions: 2048
mteb_score: 63.87
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B
  - https://huggingface.co/api/models/Qwen/Qwen3-VL-Embedding-2B
  - https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B/raw/main/config.json
  - https://arxiv.org/abs/2601.04720
  - https://huggingface.co/Qwen/Qwen3-Embedding-0.6B
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# Qwen3 VL Embedding 2B

## Overview
Qwen3-VL-Embedding-2B was published on Hugging Face on 2026-01-07 with an 8B sibling and two Qwen3-VL rerankers; the technical report (arXiv 2601.04720) was submitted on 2026-01-08. OpenRouter does not list it; the id follows the Hugging Face repo `Qwen/Qwen3-VL-Embedding-2B`, and the release date is the repo creation date. It fine-tunes Qwen3-VL-2B-Instruct (28 layers, 2.1B parameters) and accepts text, images, screenshots, video and mixtures of them, returning one vector in a shared space. Output is 2,048 dimensions with user-chosen sizes from 64 to 2,048, and the sequence length is 32K tokens. Inputs are wrapped in an instruction system prompt, by default "Represent the user's input."; task-specific instructions, written in English, add 1% to 5%. Qwen states support for 30+ languages.

## Strengths
- Qwen reports 73.2 overall on MMEB-V2 (78 datasets): 75.0 on images, 61.9 on video and 79.2 on visual documents.
- 63.87 Mean (Task) on MMTEB (MTEB Multilingual) text tasks, close to Qwen3-Embedding-0.6B (64.33).
- Quantised embeddings are documented as supported, and smaller vector sizes cut storage.
- Sentence Transformers, Transformers, vLLM and SGLang usage is documented.

## Limitations
- For text-only retrieval Qwen3-Embedding-0.6B scores about the same at under a third of the size.
- 30+ languages, against 100+ for the text-only Qwen3 embedders.
- No audio input.
- Not on the MTEB leaderboard's multilingual or English v2 tables on 2026-11-01.

## Good for
- Search over screenshots, documents with figures and product images.
- Video-text retrieval and multimodal clustering.
- A first-stage retriever for Qwen3-VL-Reranker.
