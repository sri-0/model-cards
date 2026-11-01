---
id: nvidia/nemotron-3.5-embed-1b
name: Nemotron 3.5 Embed 1B
owned_by: nvidia
type: embedding
description: Nemotron 3.5 Embed 1B is NVIDIA's 1.55B-parameter open-weight multimodal retrieval embedder that adds a Pixtral vision encoder to a frozen Nemotron 3 Embed 1B, embedding text, page images or both into 2,048-dimensional vectors with a 32,768-token context.
aliases: ["nvidia/nemotron-3.5-embed-1b:free", nvidia/Nemotron-3.5-Embed-1B-BF16, nvidia/Nemotron-3.5-Embed-1B-NVFP4]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: OpenMDW-1.1
release_date: "2026-10-20"
embedding_dimensions: 2048
pricing:
  input: 0
  output: 0
sources:
  - https://huggingface.co/nvidia/Nemotron-3.5-Embed-1B-BF16
  - https://huggingface.co/api/models/nvidia/Nemotron-3.5-Embed-1B-BF16
  - https://huggingface.co/nvidia/Nemotron-3.5-Embed-1B-BF16/raw/main/config.json
  - https://huggingface.co/nvidia/Nemotron-3.5-Embed-1B-NVFP4
  - https://build.nvidia.com/nvidia/nemotron-3_5-embed-1b/modelcard
  - https://openrouter.ai/nvidia/nemotron-3.5-embed-1b
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# Nemotron 3.5 Embed 1B

## Overview
Nemotron 3.5 Embed 1B was released on Hugging Face on 2026-10-20 as `nvidia/Nemotron-3.5-Embed-1B-BF16`, with an NVFP4 quantised build that shares its embedding space; the NIM API uses `nvidia/nemotron-3.5-embed-1b`. OpenRouter offers it only as the free `nvidia/nemotron-3.5-embed-1b:free`. It pairs a Pixtral vision encoder initialised from Ministral-3-3B-Instruct-2512 with the language model of Nemotron-3-Embed-1B, which stayed frozen, so its text embeddings share Nemotron 3 Embed 1B's space. Only the vision encoder and projector were trained, by distillation from Nemotron-3.5-Embed-8B. Queries are text; documents can be page images (text, tables, charts, infographics), text or both. Output is a mean-pooled 2,048-dimensional vector that can be cut to 1,024 or 512 and re-normalised, with a 32,768-token context. Text retrieval was evaluated in 34 languages.

## Strengths
- NVIDIA reports NDCG@10 of 58.02 (image), 57.80 (text) and 58.82 (image plus text) on ViDoRe V3, and 68.93 on MIRACL-VISION, ahead of Qwen3-VL-Embedding-2B (52.89, 48.31, 51.97, 58.42).
- Drop-in image support for existing Nemotron 3 Embed 1B text indexes.
- OpenMDW-1.1 licence for commercial or non-commercial use.

## Limitations
- Text queries only.
- Built for NVIDIA GPUs (tested on A100 and GB200); examples assume FlashAttention 2 and transformers 5.20.
- Retrieval benchmarks only; NVIDIA publishes no MTEB mean.
- Image resolution (default longest edge 1,120 pixels, up to 1,540) trades accuracy against tokens.

## Good for
- Multimodal RAG over PDFs and slide decks.
- Adding page-image search to a Nemotron 3 Embed 1B deployment.
- Free hosted trials through OpenRouter.
