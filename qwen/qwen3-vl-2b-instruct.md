---
id: qwen/qwen3-vl-2b-instruct
name: Qwen3 VL 2B Instruct
owned_by: qwen
type: llm
description: Qwen3 VL 2B Instruct is the smallest model of Qwen's October 2025 Qwen3-VL series, a dense open-weight (Apache-2.0) vision-language model for images, video, documents and GUIs with a native 256K context.
aliases: [Qwen/Qwen3-VL-2B-Instruct, Qwen/Qwen3-VL-2B-Instruct-FP8, Qwen/Qwen3-VL-2B-Instruct-GGUF, "qwen3-vl:2b-instruct"]
context_length: 262144
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-21"
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen3-VL-2B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct/raw/main/config.json
  - https://github.com/QwenLM/Qwen3-VL
  - https://arxiv.org/html/2511.21631
  - https://ollama.com/library/qwen3-vl/tags
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 VL 2B Instruct

## Overview
Qwen3-VL-2B-Instruct was released on 2025-10-21 with the 32B size and both sizes' Thinking editions, according to the Qwen3-VL GitHub README (the Hugging Face repo was created 2025-10-19). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. The Qwen3-VL technical report says the 2B and 4B models pair a Qwen3 language model with a SigLIP2-Large (300M) vision encoder; Hugging Face counts 2.13B parameters, and config.json gives 28 layers and 262,144 positions. It shares the Qwen3-VL design: Interleaved-MRoPE, DeepStack fusion of multi-level ViT features and text-timestamp alignment, with a native 256K context expandable to 1M, OCR in 32 languages, 2D and 3D grounding, GUI operation and code generation from screenshots. Qwen's vision settings are top_p 0.8, top_k 20, temperature 0.7, presence penalty 1.5 and 16,384 output tokens. Serving needs transformers 4.57.0 or vLLM 0.11.0. Ollama serves it as qwen3-vl:2b-instruct (1.9 GB).

## Strengths
- The report's text table gives MMLU-Pro 49.0, GPQA 42.0, AIME-25 22.2, LiveCodeBench v6 20.3, IFEval 68.2 and BFCL-v3 55.4, against 42.3, 34.7, 10.6, 16.1, 67.1 and 52.2 for Qwen3-1.7B non-thinking.
- The full Qwen3-VL feature set at the smallest size.
- The model card describes tool use for PC and mobile GUI agents.

## Limitations
- No Artificial Analysis figures, and the card's multimodal benchmark tables are images.
- Qwen's table puts it below Qwen3-VL-4B-Instruct on every text benchmark.
- No thinking mode; the Thinking edition covers that.
- No published knowledge cutoff.

## Good for
- On-device OCR, captioning and screenshot reading.
- Lightweight GUI agents on edge hardware.
- Fine-tuning a small vision-language base.
