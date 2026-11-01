---
id: google/embeddinggemma-2
name: EmbeddingGemma 2
owned_by: google
type: embedding
description: EmbeddingGemma 2 is Google DeepMind's 740M-parameter Apache-2.0 multimodal embedding model on the Gemma 4 architecture that maps text, code, images, video and audio into one 768-dimensional space with an 8,192-token context.
aliases: [google/embeddinggemma-2, embeddinggemma-2, "embeddinggemma-2:740m", "embeddinggemma-2:570m", "embeddinggemma-2:440m", "embeddinggemma-2:270m"]
context_length: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [embeddings]
open_weights: true
license: Apache-2.0
release_date: "2026-10-06"
knowledge_cutoff: "2025-01"
embedding_dimensions: 768
mteb_score: 61.36
sources:
  - https://huggingface.co/google/embeddinggemma-2
  - https://huggingface.co/api/models/google/embeddinggemma-2
  - https://huggingface.co/google/embeddinggemma-2/raw/main/config.json
  - https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/
  - https://arxiv.org/abs/2610.37364
  - https://ollama.com/library/embeddinggemma-2/tags
  - https://huggingface.co/spaces/mteb/leaderboard
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28Multilingual%2C%20v2%29/scores
  - https://mteb-leaderboard-backend.hf.space/v1/benchmarks/MTEB%28eng%2C%20v2%29/scores
retrieved: "2026-11-01"
---

# EmbeddingGemma 2

## Overview
EmbeddingGemma 2 was announced on 2026-10-06 (Hugging Face repo created 2026-09-14); the technical report is arXiv 2610.37364. OpenRouter does not list it; the id follows the Hugging Face repo `google/embeddinggemma-2`. Its 740M parameters split into a 270M text model (130M transformer, 140M embedder), a 170M vision encoder and a 300M audio encoder; unused encoders can be left unloaded. It is a 24-layer Gemma 4 design with mean pooling. All modalities share one 8,192-token context: an image costs 280 tokens, a video frame 140 and a second of audio 25. Output is 768 dimensions with Matryoshka truncation to 512, 256 or 128. Google claims 100+ languages; pre-training data has a January 2025 cutoff. The weights are ungated, and Ollama ships `embeddinggemma-2` in 270m to 740m tags.

## Strengths
- Google reports MTEB (Multilingual, v2) Mean (Task) 61.36, MTEB (English, v2) 68.46 and MTEB (Code, v1) 78.68, up from 68.76. The MTEB leaderboard showed 60.52 and 67.53 on 2026-11-01.
- Multimodal results: MIEB (lite) 65.67, MMEB v2 image 57.28, visual documents 67.84, video 50.67, MSEB retrieval 69.54 and MAEB 49.87.
- Near-lossless at 256 dimensions (60.41 multilingual).
- About 191 MB of active RAM for quantised text-only weights and 567 MB for the full model on a Pixel 11 Pro, per Google.

## Limitations
- 128 dimensions degrades multimodal quality substantially (MMEB overall 45.65 against 59.01).
- Run in bfloat16 or float32; float16 returns NaN or silently degraded vectors.
- Text inputs should carry a task prefix (for example `task: search result | query: {query}`).
- No safety tuning; the Gemma Prohibited Use Policy applies.
- config.json allows 262,144 positions; the documented context is 8,192.

## Good for
- On-device search and RAG over mixed text, images, video and audio.
- Code and multilingual text retrieval in one small model.
- Loading only the encoders needed.
