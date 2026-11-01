---
id: nvidia/llama-nemotron-rerank-vl-1b-v2
name: Llama Nemotron Rerank VL 1B V2
owned_by: nvidia
type: reranker
description: NVIDIA's 1.7B open-weight multimodal cross-encoder reranker for vision RAG, scoring document page images, text or both against a text query over a 10,240-token window.
aliases: [nvidia/llama-nemotron-rerank-vl-1b-v2:free, nvidia/llama-nemotron-rerank-vl-1b-v2-fp8]
context_length: 10240
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [rerank]
  tokenizer: Other
open_weights: true
license: NVIDIA Open Model License
release_date: "2025-12-18"
sources:
  - https://openrouter.ai/nvidia/llama-nemotron-rerank-vl-1b-v2:free
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2
  - https://huggingface.co/api/models/nvidia/llama-nemotron-rerank-vl-1b-v2
  - https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/raw/main/config.json
  - https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2-fp8
  - https://arxiv.org/abs/2501.14818
retrieved: "2026-11-01"
---

# Llama Nemotron Rerank VL 1B V2

## Overview
llama-nemotron-rerank-vl-1b-v2 is NVIDIA's multimodal reranker for question-answering retrieval, released on Hugging Face on 2025-12-18. OpenRouter lists it only as the free `nvidia/llama-nemotron-rerank-vl-1b-v2:free`, with a 10,240-token context. It is a cross-encoder of about 1.7B parameters, fine-tuned from an Eagle-family vision-language model (SigLIP 2 400M vision encoder with llama-nemotron-rerank-1b-v2 as the language model), with mean pooling and a binary classification head. Documents can be page screenshots, text or both; queries are text. Output is a raw logit per pair, which a sigmoid turns into a probability. Fine-tuning used image data only, with up to four tiles and 2,048 tokens; evaluation used six tiles and 10,240 tokens, and longer inputs are truncated. It runs in Sentence Transformers or Transformers 4.56.0 or later with `trust_remote_code`, and in vLLM with the bundled score template. The weights are under the NVIDIA Open Model License and ready for commercial use; NVIDIA also notes the Llama 3.2 Community License.

## Strengths
- NVIDIA's Recall@5 over five visual document sets (ViDoRe V1 to V3 and two internal), reranking llama-nemotron-embed-vl-1b-v2 results: 76.12% for text, 76.12% for images and 77.64% for image plus text, against 71.04%, 71.20% and 73.24% for the embedder alone.
- Ahead of MonoQwen2-VL-v0.1 in all three modes and of jina-reranker-m0 on text (69.31%).
- On 92 text datasets (BEIR, MIRACL, MLQA, MLDR) it matches NVIDIA's text-only reranker, 73.98% against 73.69% average Recall@5.

## Limitations
- jina-reranker-m0 scores higher on image-only input (78.33%).
- Maximum sequence length is 10,240 tokens.
- Designed and tested for NVIDIA GPUs.

## Good for
- Vision RAG over scanned pages, slides, charts and tables.
- Mixed text-and-image corpora with one reranker.
- Commercial self-hosting under NVIDIA's open model licence.
