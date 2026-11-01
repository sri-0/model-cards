---
id: qwen/qwen3-vl-32b-instruct
name: Qwen3 VL 32B Instruct
owned_by: qwen
type: llm
description: Qwen3 VL 32B Instruct is Qwen's October 2025 dense 33B-parameter open-weight (Apache-2.0) vision-language model for images, video, documents and GUIs, with a native 256K context and no thinking mode.
aliases: [Qwen/Qwen3-VL-32B-Instruct, Qwen/Qwen3-VL-32B-Instruct-FP8, Qwen/Qwen3-VL-32B-Instruct-GGUF, qwen3-vl-32b-instruct, dashscope/qwen3-vl-32b-instruct, "qwen3-vl:32b-instruct"]
context_length: 262144
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-21"
benchmarks:
  gpqa_diamond: 67.1
  humanitys_last_exam: 6.8
  ifbench: 39.2
  mmmu_pro: 64.3
  tau2_bench: 29.2
  terminal_bench_hard: 8.3
benchmark_variant: Qwen3 VL 32B Instruct
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-32B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen3-VL-32B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-VL-32B-Instruct/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-vl-32b-instruct
  - https://github.com/QwenLM/Qwen3-VL
  - https://arxiv.org/html/2511.21631
  - https://ollama.com/library/qwen3-vl/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 VL 32B Instruct

## Overview
Qwen3-VL-32B-Instruct was released on 2025-10-21 with its Thinking edition and the 2B size, according to the Qwen3-VL GitHub README (Artificial Analysis agrees; the Hugging Face repo was created 2025-10-19). OpenRouter does not list it; the id follows the Hugging Face repo. Hugging Face counts 33.4B parameters, and config.json gives 64 layers, 64 query and 8 key-value heads and 262,144 positions. It shares the Qwen3-VL design: Interleaved-MRoPE, DeepStack and text-timestamp alignment, a native 256K context expandable to 1M, OCR in 32 languages, 2D and 3D grounding, GUI operation and code from screenshots. Qwen's vision settings are top_p 0.8, top_k 20, temperature 0.7, presence penalty 1.5 and 16,384 output tokens. Serving needs transformers 4.57.0 or vLLM 0.11.0. Ollama serves it as qwen3-vl:32b-instruct (21 GB). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen3-vl-32b-instruct in Singapore at $0.16 per million input and $0.64 per million output tokens, with a 131,072-token window. Artificial Analysis marks it deprecated in favour of Qwen3.5 27B.

## Strengths
- The report says the 32B size consistently beats Gemini 2.5 Flash and GPT-5 mini on multimodal reasoning and surpasses Qwen2.5-VL-72B on reasoning tasks.
- Its text table gives MMLU-Pro 78.6, GPQA 68.9, AIME-25 66.2, LiveCodeBench v6 43.8, Arena-Hard v2 64.7 and BFCL-v3 70.2, against 71.9, 54.6, 20.2, 29.1, 37.4 and 63.0 for Qwen3-32B non-thinking.
- Artificial Analysis (Qwen3 VL 32B Instruct): MMMU-Pro 64.3%, GPQA Diamond 67.1%, Terminal-Bench Hard 8.3%.

## Limitations
- Artificial Analysis tau2-bench 29.2%, IFBench 39.2% and Humanity's Last Exam 6.8%; no long-context or speed figures.
- In the same table the smaller Qwen3-VL-30B-A3B-Instruct beats it on GPQA, AIME-25 and IFEval.
- No thinking mode; the Thinking edition covers that.
- No published knowledge cutoff.

## Good for
- Self-hosted document parsing, OCR and chart extraction.
- GUI and visual-coding agents.
- Long video understanding with timestamps.
