---
id: qwen/qwen3-vl-8b-thinking
name: Qwen3 VL 8B Thinking
owned_by: qwen
type: llm
description: Qwen3 VL 8B Thinking is the reasoning edition of Qwen's October 2025 dense 8B Qwen3-VL model, open-weight under Apache-2.0, for visual maths, documents, video and GUIs with a native 256K context.
aliases: [Qwen/Qwen3-VL-8B-Thinking, Qwen/Qwen3-VL-8B-Thinking-FP8, Qwen/Qwen3-VL-8B-Thinking-GGUF, qwen3-vl-8b-thinking, "qwen3-vl:8b", "qwen3-vl:8b-thinking"]
context_length: 262144
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-15"
benchmarks:
  gpqa_diamond: 57.9
  humanitys_last_exam: 3.8
  ifbench: 39.9
  long_context_reasoning: 33.3
  mmmu_pro: 56.6
  tau2_bench: 22.5
  terminal_bench_hard: 3.8
benchmark_variant: Qwen3 VL 8B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-8B-Thinking
  - https://huggingface.co/api/models/Qwen/Qwen3-VL-8B-Thinking
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-VL-8B-Thinking/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-vl-8b
  - https://github.com/QwenLM/Qwen3-VL
  - https://arxiv.org/html/2511.21631
  - https://ollama.com/library/qwen3-vl/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 VL 8B Thinking

## Overview
Qwen3-VL-8B-Thinking was released on 2025-10-15 with the Instruct edition and the 4B size, according to the Qwen3-VL GitHub README (Artificial Analysis lists 2025-10-14; the Hugging Face repo was created 2025-10-11). OpenRouter lists only the Instruct edition, which has its own card; the id follows the Hugging Face repo. Thinking editions are Qwen's reasoning-enhanced variants. Hugging Face counts 8.77B parameters, and config.json gives 36 layers and 262,144 positions. It shares the Qwen3-VL design: Interleaved-MRoPE, DeepStack and text-timestamp alignment, a native 256K context expandable to 1M, OCR in 32 languages, grounding, GUI operation and code from screenshots. Qwen's vision settings are top_p 0.95, top_k 20, temperature 1.0 and 40,960 output tokens. Serving needs transformers 4.57.0 or vLLM 0.11.0. On Ollama, qwen3-vl:8b and qwen3-vl:8b-thinking are this model (6.2 GB), as is qwen3-vl:latest. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen3-vl-8b-thinking in Singapore at $0.18 per million input and $2.10 per million output tokens. Artificial Analysis marks it deprecated in favour of Qwen3.5 9B.

## Strengths
- The report says the 8B model leads the small Qwen3-VL sizes overall, with MMBench-EN 85.3 and MMStar 75.3 in thinking mode.
- Its text table gives MMLU-Pro 77.3, GPQA 69.9, AIME-25 80.3, HMMT-25 60.6 and LiveCodeBench v6 58.6, against 74.6, 62.0, 67.3, 43.2 and 51.0 for Qwen3-8B thinking.
- Artificial Analysis (Qwen3 VL 8B (Reasoning)): MMMU-Pro 56.6%, GPQA Diamond 57.9%, IFBench 39.9%.

## Limitations
- Artificial Analysis tau2-bench 22.5%, Terminal-Bench Hard 3.8% and Humanity's Last Exam 3.8%; no speed figures.
- Qwen3-8B thinking leads it on IFEval (85.0 against 83.2) and BFCL-v3 (68.1 against 63.0).
- No published knowledge cutoff.

## Good for
- Visual maths, science and chart reasoning on one GPU.
- Document analysis that needs justified answers.
- Multimodal agents that reason before acting.
