---
id: qwen/qwen3-vl-2b-thinking
name: Qwen3 VL 2B Thinking
owned_by: qwen
type: llm
description: Qwen3 VL 2B Thinking is the reasoning edition of the smallest Qwen3-VL model, a dense open-weight (Apache-2.0) vision-language model from October 2025 with a native 256K context.
aliases: [Qwen/Qwen3-VL-2B-Thinking, Qwen/Qwen3-VL-2B-Thinking-FP8, Qwen/Qwen3-VL-2B-Thinking-GGUF, "qwen3-vl:2b", "qwen3-vl:2b-thinking"]
context_length: 262144
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-21"
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-2B-Thinking
  - https://huggingface.co/api/models/Qwen/Qwen3-VL-2B-Thinking
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-VL-2B-Thinking/raw/main/config.json
  - https://github.com/QwenLM/Qwen3-VL
  - https://arxiv.org/html/2511.21631
  - https://ollama.com/library/qwen3-vl/tags
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 VL 2B Thinking

## Overview
Qwen3-VL-2B-Thinking was released on 2025-10-21 with the Instruct edition and the 32B size, according to the Qwen3-VL GitHub README (the Hugging Face repo was created 2025-10-19). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. The Thinking editions are Qwen's reasoning-enhanced variants. The technical report says the 2B and 4B models pair a Qwen3 language model with a SigLIP2-Large (300M) vision encoder; Hugging Face counts 2.13B parameters, and config.json gives 28 layers and 262,144 positions. It shares the Qwen3-VL design: Interleaved-MRoPE, DeepStack and text-timestamp alignment, a native 256K context expandable to 1M, OCR in 32 languages, grounding, GUI operation and code from screenshots. Qwen's vision settings are top_p 0.95, top_k 20, temperature 1.0 and 40,960 output tokens; for text it uses 32,768, or 81,920 for AIME, LiveCodeBench and GPQA. Serving needs transformers 4.57.0 or vLLM 0.11.0. On Ollama, qwen3-vl:2b and qwen3-vl:2b-thinking are this model (1.9 GB).

## Strengths
- The report's text table gives MMLU-Pro 62.3, GPQA 49.5, AIME-25 39.0, LiveCodeBench v6 29.3, IFEval 75.1 and BFCL-v3 57.2, against 58.1, 27.9, 36.8, 31.3, 72.5 and 56.6 for Qwen3-1.7B in thinking mode.
- The report gives MMBench-EN 79.9 and MMStar 68.1 in thinking mode, and says even the 2B model shows strong reasoning.
- Above the 2B Instruct edition on every text benchmark in the report.

## Limitations
- No Artificial Analysis figures; most multimodal tables are images.
- Qwen3-1.7B thinking beats it on LiveCodeBench v6 (31.3 against 29.3), HMMT-25 and LiveBench.
- Qwen's settings allow 40,960 output tokens for vision tasks, so answers can be long.
- No published knowledge cutoff.

## Good for
- Visual maths and diagram questions on edge devices.
- Step-by-step document and chart reasoning at low cost.
- Research on small multimodal reasoners.
