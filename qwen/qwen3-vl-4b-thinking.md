---
id: qwen/qwen3-vl-4b-thinking
name: Qwen3 VL 4B Thinking
owned_by: qwen
type: llm
description: Qwen3 VL 4B Thinking is the reasoning edition of Qwen's October 2025 dense 4B-class Qwen3-VL model, open-weight under Apache-2.0, for visual maths, documents, video and GUIs with a native 256K context.
aliases: [Qwen/Qwen3-VL-4B-Thinking, Qwen/Qwen3-VL-4B-Thinking-FP8, Qwen/Qwen3-VL-4B-Thinking-GGUF, "qwen3-vl:4b", "qwen3-vl:4b-thinking"]
context_length: 262144
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-15"
benchmarks:
  gpqa_diamond: 49.4
  humanitys_last_exam: 4.6
  ifbench: 36.6
  long_context_reasoning: 21.3
  mmmu_pro: 52.0
  tau2_bench: 15.5
  terminal_bench_hard: 1.5
benchmark_variant: Qwen3 VL 4B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-4B-Thinking
  - https://huggingface.co/api/models/Qwen/Qwen3-VL-4B-Thinking
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-VL-4B-Thinking/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-vl-4b
  - https://github.com/QwenLM/Qwen3-VL
  - https://arxiv.org/html/2511.21631
  - https://ollama.com/library/qwen3-vl/tags
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 VL 4B Thinking

## Overview
Qwen3-VL-4B-Thinking was released on 2025-10-15 with the Instruct edition and the 8B size, according to the Qwen3-VL GitHub README (Artificial Analysis lists 2025-10-14; the Hugging Face repo was created 2025-10-11). OpenRouter does not list it; the id follows the Hugging Face repo. Thinking editions are Qwen's reasoning-enhanced variants. The technical report says the 2B and 4B models pair a Qwen3 language model with a SigLIP2-Large (300M) vision encoder; Hugging Face counts 4.44B parameters, and config.json gives 36 layers and 262,144 positions. It shares the Qwen3-VL design: Interleaved-MRoPE, DeepStack and text-timestamp alignment, a native 256K context expandable to 1M, OCR in 32 languages, grounding, GUI operation and code from screenshots. Qwen's vision settings are top_p 0.95, top_k 20, temperature 1.0 and 40,960 output tokens; for text it uses 32,768, or 81,920 for AIME, LiveCodeBench and GPQA. Serving needs transformers 4.57.0 or vLLM 0.11.0. On Ollama, qwen3-vl:4b and qwen3-vl:4b-thinking are this model (3.3 GB). Artificial Analysis marks it deprecated in favour of Qwen3.5 4B.

## Strengths
- The report says the 4B size scores highest on DynaMath and VisuLogic among the small models it compares, GPT-5-Nano included.
- Its text table gives MMLU-Pro 73.6, GPQA 64.1, AIME-25 74.5, LiveCodeBench v6 51.3 and BFCL-v3 67.3, against 70.4, 55.9, 65.6, 48.4 and 65.9 for Qwen3-4B thinking.
- Artificial Analysis (Qwen3 VL 4B (Reasoning)): MMMU-Pro 52%, GPQA Diamond 49.4%, IFBench 36.6%, each above the Instruct edition.

## Limitations
- Artificial Analysis tau2-bench 15.5%, Terminal-Bench Hard 1.5%, long-context reasoning 21.3%; no speed figures.
- Qwen3-4B-Thinking-2507 leads it on all six text scores above.
- No published knowledge cutoff.

## Good for
- Visual maths and science problems on one consumer GPU.
- Chart and document questions that need worked answers.
- Small multimodal agents that reason before acting.
