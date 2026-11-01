---
id: qwen/qwen3-vl-4b-instruct
name: Qwen3 VL 4B Instruct
owned_by: qwen
type: llm
description: Qwen3 VL 4B Instruct is Qwen's October 2025 dense 4B-class open-weight (Apache-2.0) vision-language model for images, video, documents and GUIs, with a native 256K context and no thinking mode.
aliases: [Qwen/Qwen3-VL-4B-Instruct, Qwen/Qwen3-VL-4B-Instruct-FP8, Qwen/Qwen3-VL-4B-Instruct-GGUF, "qwen3-vl:4b-instruct"]
context_length: 262144
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-15"
benchmarks:
  gpqa_diamond: 37.1
  humanitys_last_exam: 3.6
  ifbench: 31.8
  long_context_reasoning: 14.0
  mmmu_pro: 43.9
  tau2_bench: 23.4
  terminal_bench_hard: 0
benchmark_variant: Qwen3 VL 4B Instruct
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen3-VL-4B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-vl-4b-instruct
  - https://github.com/QwenLM/Qwen3-VL
  - https://arxiv.org/html/2511.21631
  - https://ollama.com/library/qwen3-vl/tags
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 VL 4B Instruct

## Overview
Qwen3-VL-4B-Instruct was released on 2025-10-15 with the 8B size and both sizes' Thinking editions, according to the Qwen3-VL GitHub README (Artificial Analysis lists 2025-10-14; the Hugging Face repo was created 2025-10-11). OpenRouter does not list it; the id follows the Hugging Face repo. The technical report says the 2B and 4B models pair a Qwen3 language model with a SigLIP2-Large (300M) vision encoder; Hugging Face counts 4.44B parameters, and config.json gives 36 layers and 262,144 positions. It shares the Qwen3-VL design: Interleaved-MRoPE, DeepStack and text-timestamp alignment, a native 256K context expandable to 1M, OCR in 32 languages, 2D and 3D grounding, GUI operation and code from screenshots. Qwen's vision settings are top_p 0.8, top_k 20, temperature 0.7, presence penalty 1.5 and 16,384 output tokens. Serving needs transformers 4.57.0 or vLLM 0.11.0. Ollama serves it as qwen3-vl:4b-instruct (3.3 GB). Artificial Analysis marks it deprecated in favour of Qwen3.5 4B.

## Strengths
- The report's text table gives MMLU-Pro 67.1, GPQA 55.9, AIME-25 46.6, LiveCodeBench v6 37.9, IFEval 82.3 and BFCL-v3 63.3, against 58.0, 41.7, 19.1, 26.4, 81.2 and 57.6 for Qwen3-4B non-thinking.
- It beats the text-only Qwen3-4B-Instruct-2507 on LiveCodeBench v6 and BFCL-v3 in that table.
- Artificial Analysis (Qwen3 VL 4B Instruct): MMMU-Pro 43.9%, IFBench 31.8%, tau2-bench 23.4%.

## Limitations
- Artificial Analysis GPQA Diamond 37.1%, long-context reasoning 14%, Terminal-Bench Hard 0% and Humanity's Last Exam 3.6%; no speed figures.
- Qwen3-4B-Instruct-2507 leads it on MMLU-Pro, GPQA, AIME-25 and IFEval.
- No thinking mode; the Thinking edition covers that.
- No published knowledge cutoff.

## Good for
- Local OCR, document parsing and screenshot understanding.
- Lightweight GUI agents on one consumer GPU.
- Video captioning and question answering at low cost.
