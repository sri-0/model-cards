---
id: qwen/qwen2.5-vl-7b-instruct
name: Qwen2.5 VL 7B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 VL 7B Instruct is the mid-sized open-weight (Apache-2.0) vision-language model of Qwen's January 2025 Qwen2.5-VL series, for document parsing, charts, video understanding, object grounding and GUI agents.
aliases: [Qwen/Qwen2.5-VL-7B-Instruct, Qwen/Qwen2.5-VL-7B-Instruct-AWQ, qwen2.5-vl-7b-instruct, "qwen2.5vl:7b"]
context_length: 128000
capabilities: [vision, structured_output]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-01-26"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-VL-7B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/raw/main/config.json
  - https://qwenlm.github.io/blog/qwen2.5-vl/
  - https://github.com/QwenLM/Qwen3-VL
  - https://ollama.com/library/qwen2.5vl/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 VL 7B Instruct

## Overview
Qwen2.5-VL-7B-Instruct is the middle size of the Qwen2.5-VL launch (3B, 7B, 72B). The Qwen blog post is dated 2025-01-26, which this card uses; the GitHub README (now the Qwen3-VL repository) says 2025-01-28, and the Hugging Face repo was created 2025-01-26. OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. Qwen describes dynamic resolution and frame-rate sampling for video, mRoPE aligned to absolute time, and a window-attention ViT with SwiGLU and RMSNorm. config.json sets max_position_embeddings to 128,000, which this card uses, although the model card says the config is set for 32,768 tokens and advises against YaRN because it harms temporal and spatial localisation. Images can be files, base64 or URLs; videos must be local files. Inference needs transformers built from source and qwen-vl-utils. Ollama serves it as qwen2.5vl:7b (also qwen2.5vl:latest, 6.0 GB). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-vl-7b-instruct in Singapore at $0.35 per million input and $1.05 per million output tokens, with a 131,072-token window.

## Strengths
- Qwen reports MMMU 58.6, MMMU-Pro 41.0, DocVQA 95.7, InfoVQA 82.6, ChartQA 87.3, OCRBench 864 and MathVista 68.2; it beats GPT-4o-mini on MMMU-Pro, OCRBench and MathVista.
- Video-MME 65.1 without and 71.6 with subtitles; Qwen says it understands videos over an hour long.
- ScreenSpot 84.7 and Android Control Low 93.7, with bounding boxes or points returned as JSON.

## Limitations
- GPT-4o-mini leads it on MMMU (60 against 58.6).
- ScreenSpot Pro 29.0 and AndroidWorld 25.5 are weak for harder GUI tasks.
- No reasoning mode, and the chat template has no tool-call support.
- No published knowledge cutoff.

## Good for
- Document OCR, chart reading and form extraction on one GPU.
- Video question answering with event localisation.
- Lightweight GUI grounding.
