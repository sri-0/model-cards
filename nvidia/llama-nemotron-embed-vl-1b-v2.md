---
id: nvidia/llama-nemotron-embed-vl-1b-v2
name: Llama Nemotron Embed VL 1B V2
owned_by: nvidia
type: embedding
description: llama-nemotron-embed-vl-1b-v2 is NVIDIA's 1.7B-parameter open-weight multimodal retrieval embedder (Llama 3.2 1B plus a SigLIP2 image encoder) that embeds text, document page images or both into 2,048-dimensional vectors for text queries.
aliases: ["nvidia/llama-nemotron-embed-vl-1b-v2:free", nvidia/llama-nemotron-embed-vl-1b-v2-fp8]
context_length: 131072
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: true
license: NVIDIA Open Model License
release_date: "2025-12-18"
embedding_dimensions: 2048
pricing:
  input: 0
  output: 0
sources:
  - https://huggingface.co/nvidia/llama-nemotron-embed-vl-1b-v2
  - https://huggingface.co/api/models/nvidia/llama-nemotron-embed-vl-1b-v2
  - https://huggingface.co/nvidia/llama-nemotron-embed-vl-1b-v2/raw/main/config.json
  - https://huggingface.co/nvidia/llama-nemotron-embed-vl-1b-v2-fp8
  - https://build.nvidia.com/nvidia/llama-nemotron-embed-vl-1b-v2/modelcard
  - https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16
  - https://openrouter.ai/nvidia/llama-nemotron-embed-vl-1b-v2
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# Llama Nemotron Embed VL 1B V2

## Overview
llama-nemotron-embed-vl-1b-v2 was released on Hugging Face on 2025-12-18 (repo created 2025-12-03) as part of NVIDIA's Nemotron RAG collection, and is also served as a NeMo Retriever NIM under the same id. OpenRouter offers it only as the free `nvidia/llama-nemotron-embed-vl-1b-v2:free` and lists a 131,072-token context; NVIDIA evaluated up to 10,240 tokens (the NIM card says 8,192). It is an Eagle-style VLM: a Llama 3.2 1B language model (16 layers, 2,048 hidden size) and a 428M SigLIP2 image encoder, mean-pooled to a 2,048-dimensional vector. Images are tiled at 256 tokens per tile (up to six tiles plus a thumbnail). Queries are text; documents can be page images, text or both, with `query:` and `passage:` prefixes.

## Strengths
- NVIDIA reports 73.24% average Recall@5 on DC10k, Earnings V2 and ViDoRe V1 to V3 with image plus text input, above its closed predecessor (71.71%).
- Also slightly better on text retrieval than NVIDIA's text-only llama-nemotron-embed-1b-v2 (67.42% against 67.19% Recall@5).
- Handles tables, charts and infographics in page images; an FP8 checkpoint is published.

## Limitations
- NVIDIA Open Model License with Llama 3.2 Community Licence terms ("Built with Llama").
- Needs `trust_remote_code=True` and transformers 4.56 or later; vLLM requires the bundled chat template for the prefixes.
- Text queries only; image tokens count against the context limit.
- For text-only retrieval NVIDIA's Nemotron 3 Embed 1B scores much higher (71.04 against 59.71 on MMTEB retrieval).

## Good for
- Retrieval over page images of PDFs, slides and reports.
- One embedder for mixed text and page-image corpora.
- Free hosted trials through OpenRouter.
