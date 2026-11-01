---
id: qwen/qwen3-vl-embedding-8b
name: Qwen3 VL Embedding 8B
owned_by: qwen
type: embedding
description: Qwen3-VL-Embedding-8B is Qwen's Apache-2.0 multimodal embedding model built on Qwen3-VL-8B-Instruct that maps text, images, screenshots and video into one space with 4,096-dimensional vectors truncatable to 64 and a 32K-token input.
aliases: [Qwen/Qwen3-VL-Embedding-8B]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2026-01-07"
embedding_dimensions: 4096
mteb_score: 67.88
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B
  - https://huggingface.co/api/models/Qwen/Qwen3-VL-Embedding-8B
  - https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B/raw/main/config.json
  - https://arxiv.org/abs/2601.04720
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# Qwen3 VL Embedding 8B

## Overview
Qwen3-VL-Embedding-8B was published on Hugging Face on 2026-01-07 with a 2B sibling and two Qwen3-VL rerankers; the technical report (arXiv 2601.04720) was submitted on 2026-01-08. OpenRouter does not list it; the id follows the Hugging Face repo `Qwen/Qwen3-VL-Embedding-8B`, and the release date is the repo creation date. It fine-tunes Qwen3-VL-8B-Instruct (36 layers, 8.1B parameters) and accepts text, images, screenshots, video and mixtures of them, returning one vector in a shared space. Output is 4,096 dimensions with user-chosen sizes from 64 to 4,096, and the sequence length is 32K tokens. Inputs are wrapped in an instruction system prompt, by default "Represent the user's input."; task-specific instructions, written in English, add 1% to 5%. Qwen states support for 30+ languages.

## Strengths
- Qwen reports 77.9 overall on MMEB-V2 (78 datasets), the top score in its table and ahead of Seed-1.6-embedding-1215 (76.9): 80.1 on images, 66.1 on video and 83.3 on visual documents.
- 67.88 Mean (Task) on MMTEB (MTEB Multilingual) text tasks, between Qwen3-Embedding-0.6B (64.33) and 4B (69.45).
- Quantised embeddings are documented as supported, and smaller vector sizes cut storage.
- Sentence Transformers, Transformers, vLLM and SGLang usage is documented.

## Limitations
- For text-only retrieval the text Qwen3-Embedding-4B scores higher at half the size.
- 30+ languages, against 100+ for the text-only Qwen3 embedders.
- No audio input.
- Not on the MTEB leaderboard's multilingual or English v2 tables on 2026-11-01.

## Good for
- High-quality multimodal RAG over documents, screenshots and video.
- Cross-modal search where text queries must find images or clips.
- A first-stage retriever for Qwen3-VL-Reranker.
