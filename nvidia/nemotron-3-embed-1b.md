---
id: nvidia/nemotron-3-embed-1b
name: Nemotron 3 Embed 1B
owned_by: nvidia
type: embedding
description: Nemotron 3 Embed 1B is NVIDIA's 1.14B-parameter open-weight multilingual text embedding model, pruned and distilled from Ministral 3 3B, with 2,048-dimensional vectors truncatable to 512 and a 32,768-token input.
aliases: ["nvidia/nemotron-3-embed-1b:free", nvidia/Nemotron-3-Embed-1B-BF16, nvidia/Nemotron-3-Embed-1B-NVFP4]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: OpenMDW-1.1
release_date: "2026-07-16"
embedding_dimensions: 2048
pricing:
  input: 0
  output: 0
sources:
  - https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16
  - https://huggingface.co/api/models/nvidia/Nemotron-3-Embed-1B-BF16
  - https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16/raw/main/config.json
  - https://huggingface.co/nvidia/Nemotron-3-Embed-1B-NVFP4
  - https://build.nvidia.com/nvidia/nemotron-3-embed-1b/modelcard
  - https://openrouter.ai/nvidia/nemotron-3-embed-1b
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# Nemotron 3 Embed 1B

## Overview
Nemotron 3 Embed 1B was released on Hugging Face on 2026-07-16 as `nvidia/Nemotron-3-Embed-1B-BF16`, with an NVFP4 quantised build that shares its embedding space; the NIM API uses `nvidia/nemotron-3-embed-1b`. OpenRouter offers it only as the free `nvidia/nemotron-3-embed-1b:free`. NVIDIA trained Ministral-3-3B-Instruct-2512 as an embedder, pruned it to 2B with ModelOpt neural architecture search, distilled it from Nemotron-3-Embed-8B, then repeated the cycle to reach 1.14B parameters. It uses bidirectional attention and mean pooling to give a 2,048-dimensional vector that can be sliced to 1,024 or 512 and re-normalised. Inputs run to 32,768 tokens; queries take `query: ` and documents `passage: `. Training used over 8.5 million commercially permissible and synthetic samples, and NVIDIA evaluated 34 languages. It is ready for commercial use.

## Strengths
- NVIDIA reports NDCG@10 of 72.38 on RTEB, 71.04 on MMTEB retrieval and 57.74 on ViDoRe V3 text, against 61.98, 59.71 and 52.54 for llama-nemotron-embed-vl-1b-v2 (at a 4,096-token setting).
- OpenMDW-1.1 licence (with an Apache-2.0 note) and commercial use allowed.
- vLLM serving with FP8 on Hopper and Ada GPUs, plus Sentence Transformers and Transformers 5.2 or later.

## Limitations
- Built and tested for NVIDIA GPUs (Ampere, Hopper, Blackwell) on Linux.
- NVIDIA publishes retrieval scores only; the MTEB leaderboard showed no overall mean on 2026-11-01.
- Prefixes must be added by hand on vLLM's OpenAI-compatible `/v1/embeddings` route.

## Good for
- Multilingual enterprise search and RAG at about 1B parameters.
- Code and agentic retrieval on GPU servers.
- Free hosted trials through OpenRouter.
