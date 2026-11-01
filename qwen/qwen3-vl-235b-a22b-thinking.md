---
id: qwen/qwen3-vl-235b-a22b-thinking
name: Qwen3 VL 235B A22B Thinking
owned_by: qwen
type: llm
description: Qwen3 VL 235B A22B Thinking is the reasoning edition of Qwen's September 2025 flagship vision-language model, a 235B-parameter mixture-of-experts (22B active) open-weight under Apache-2.0 with a native 256K context.
aliases: [Qwen/Qwen3-VL-235B-A22B-Thinking, Qwen/Qwen3-VL-235B-A22B-Thinking-FP8, Qwen/Qwen3-VL-235B-A22B-Thinking-GGUF, qwen3-vl-235b-a22b-thinking, dashscope/qwen3-vl-235b-a22b-thinking, "qwen3-vl:235b", "qwen3-vl:235b-a22b", "qwen3-vl:235b-a22b-thinking"]
context_length: 262144
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-09-23"
benchmarks:
  gpqa_diamond: 77.2
  humanitys_last_exam: 11.9
  ifbench: 56.5
  long_context_reasoning: 63.7
  mmmu_pro: 68.7
  tau2_bench: 54.1
  terminal_bench_hard: 11.4
benchmark_variant: Qwen3 VL 235B A22B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Thinking
  - https://huggingface.co/api/models/Qwen/Qwen3-VL-235B-A22B-Thinking
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Thinking/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-vl-235b-a22b
  - https://github.com/QwenLM/Qwen3-VL
  - https://arxiv.org/html/2511.21631
  - https://ollama.com/library/qwen3-vl/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 VL 235B A22B Thinking

## Overview
Qwen3-VL-235B-A22B-Thinking was released on 2025-09-23 with the Instruct edition, the first Qwen3-VL models, according to the Qwen3-VL GitHub README (Artificial Analysis agrees; the Hugging Face repo was created 2025-09-22). OpenRouter lists only the Instruct edition, which has its own card; the id follows the Hugging Face repo. Hugging Face counts 235.7B parameters, and config.json gives 94 layers, 64 query and 4 key-value heads, 128 experts with 8 active and 262,144 positions. It shares the Qwen3-VL design: Interleaved-MRoPE, DeepStack and text-timestamp alignment, a native 256K context expandable to 1M, OCR in 32 languages, 2D and 3D grounding, GUI operation and code from screenshots. Serving needs transformers 4.57.0 or vLLM 0.11.0. On Ollama, qwen3-vl:235b, qwen3-vl:235b-a22b and qwen3-vl:235b-a22b-thinking are this model (143 GB). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen3-vl-235b-a22b-thinking in Singapore at $0.40 per million input and $4.00 per million output tokens. Artificial Analysis marks it deprecated in favour of Qwen3.5 397B A17B.

## Strengths
- The report gives MMStar 78.7, the best thinking-mode score it compares, state-of-the-art MathVista, MathVision, MathVerse, ZeroBench, LogicVista and VisuLogic results, and HallusionBench 3.0, 1.0 and 6.3 points above Gemini 2.5 Pro, GPT-5 and Claude Opus 4.1.
- Artificial Analysis (Qwen3 VL 235B A22B (Reasoning)): GPQA Diamond 77.2%, MMMU-Pro 68.7%, long-context reasoning 63.7%, tau2-bench 54.1%.
- 22B active parameters per token.

## Limitations
- The text-only Qwen3-235B-A22B-Thinking-2507 leads it in the report on GPQA (81.1 against 77.1), AIME-25 (92.3 against 89.7) and LiveCodeBench v6 (74.1 against 70.1).
- Artificial Analysis Terminal-Bench Hard 11.4% and Humanity's Last Exam 11.9%; no speed figures.
- Needs a multi-GPU node.
- No published knowledge cutoff.

## Good for
- Hard visual maths and science reasoning.
- Multimodal agents for GUI and document tasks.
- Self-hosted image and video understanding at the top of the Qwen3-VL range.
