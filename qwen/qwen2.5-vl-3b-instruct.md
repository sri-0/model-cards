---
id: qwen/qwen2.5-vl-3b-instruct
name: Qwen2.5 VL 3B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 VL 3B Instruct is the smallest model of Qwen's January 2025 Qwen2.5-VL series, a 3.75B-parameter vision-language model for edge devices released under the non-commercial Qwen Research License.
aliases: [Qwen/Qwen2.5-VL-3B-Instruct, Qwen/Qwen2.5-VL-3B-Instruct-AWQ, qwen2.5-vl-3b-instruct, "qwen2.5vl:3b"]
context_length: 128000
capabilities: [vision, structured_output]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Qwen Research License Agreement
release_date: "2025-01-26"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-VL-3B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/blob/main/LICENSE
  - https://qwenlm.github.io/blog/qwen2.5-vl/
  - https://github.com/QwenLM/Qwen3-VL
  - https://ollama.com/library/qwen2.5vl/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 VL 3B Instruct

## Overview
Qwen2.5-VL-3B-Instruct is the smallest size of the Qwen2.5-VL launch (3B, 7B, 72B). The Qwen blog post is dated 2025-01-26, which this card uses; the GitHub README says 2025-01-28 and the Hugging Face repo was created 2025-01-26. OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. It shares the Qwen2.5-VL design: dynamic resolution and frame-rate sampling for video, time-aligned mRoPE and a window-attention ViT. Hugging Face counts 3.75B parameters; config.json sets max_position_embeddings to 128,000, which this card uses, although the model card says the config is set for 32,768 tokens and advises against YaRN for localisation tasks. The weights use the Qwen Research License, which allows non-commercial use only. Qwen publishes an AWQ build. Ollama serves it as qwen2.5vl:3b (3.2 GB). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-vl-3b-instruct in Singapore at $0.21 per million input and $0.63 per million output tokens.

## Strengths
- The blog calls it a solution for edge AI that outperforms the previous Qwen2-VL-7B.
- Qwen reports MMMU 53.1, DocVQA 93.9, InfoVQA 77.1, MathVista 62.3 and MathVision 21.2, each ahead of InternVL2.5-4B.
- Structured JSON output for grounding, invoices, forms and tables.

## Limitations
- Non-commercial licence.
- Qwen reports MMMU-Pro 31.6, MMStar 55.9 and MMBench-V1.1 77.6, below InternVL2.5-4B's 32.7, 58.3 and 79.3, and ScreenSpot 55.5.
- No reasoning mode or tool-call template; no published knowledge cutoff.

## Good for
- Research on on-device OCR and document reading.
- Lightweight video and chart question answering.
- Fine-tuning a small vision-language model for evaluation.
