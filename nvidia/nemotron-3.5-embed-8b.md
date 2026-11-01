---
id: nvidia/nemotron-3.5-embed-8b
name: Nemotron 3.5 Embed 8B
owned_by: nvidia
type: embedding
description: Nemotron 3.5 Embed 8B is NVIDIA's 8.38B-parameter open-weight multimodal retrieval embedder that adds a vision encoder to a frozen Nemotron 3 Embed 8B, embedding text, page images or both into 4,096-dimensional vectors with a 32,768-token context.
aliases: ["nvidia/nemotron-3.5-embed-8b:free", nvidia/Nemotron-3.5-Embed-8B-BF16]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: OpenMDW-1.1
release_date: "2026-10-20"
embedding_dimensions: 4096
pricing:
  input: 0
  output: 0
sources:
  - https://huggingface.co/nvidia/Nemotron-3.5-Embed-8B-BF16
  - https://huggingface.co/api/models/nvidia/Nemotron-3.5-Embed-8B-BF16
  - https://huggingface.co/nvidia/Nemotron-3.5-Embed-8B-BF16/raw/main/config.json
  - https://build.nvidia.com/nvidia/nemotron-3_5-embed-8b/modelcard
  - https://openrouter.ai/nvidia/nemotron-3.5-embed-8b
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# Nemotron 3.5 Embed 8B

## Overview
Nemotron 3.5 Embed 8B was released on Hugging Face on 2026-10-20 as `nvidia/Nemotron-3.5-Embed-8B-BF16`; the NIM API uses `nvidia/nemotron-3.5-embed-8b`. OpenRouter offers it only as the free `nvidia/nemotron-3.5-embed-8b:free`. Its vision encoder is initialised from Ministral-3-8B-Instruct-2512 and its language model from Nemotron-3-Embed-8B, which stayed frozen, so the two produce identical text embeddings; only the vision encoder and projector were trained, on image and image-text data. The language model was trained on more than 50 million text-only samples. Queries are text; documents can be page images (text, tables, charts, infographics), text or both. Output is a mean-pooled 4,096-dimensional vector that can be cut to 1,024 or 512 and re-normalised, with a 32,768-token context. Text retrieval was evaluated in 34 languages and image retrieval in 18.

## Strengths
- NVIDIA reports NDCG@10 of 60.39 (image), 60.65 (text) and 61.47 (image plus text) on ViDoRe V3, and 72.64 on MIRACL-VISION, the best in its comparison and ahead of Qwen3-VL-Embedding-8B (58.29, 53.69, 57.03, 68.33).
- It is the teacher that Nemotron 3.5 Embed 1B was distilled from.
- OpenMDW-1.1 licence for commercial or non-commercial use.

## Limitations
- Text queries only.
- 8.38B parameters and 4,096-dimensional vectors; built for NVIDIA GPUs (tested on A100 and GB200).
- Retrieval benchmarks only; NVIDIA publishes no MTEB mean.
- The 1B model is within about three points on ViDoRe V3 at a fifth of the size.

## Good for
- Highest-accuracy multimodal RAG over enterprise documents on GPU servers.
- Multilingual visual document search (MIRACL-VISION languages).
- Free hosted trials through OpenRouter.
