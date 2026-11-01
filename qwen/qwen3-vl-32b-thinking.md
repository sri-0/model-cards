---
id: qwen/qwen3-vl-32b-thinking
name: Qwen3 VL 32B Thinking
owned_by: qwen
type: llm
description: Qwen3 VL 32B Thinking is the reasoning edition of Qwen's October 2025 dense 33B-parameter Qwen3-VL model, open-weight under Apache-2.0, for visual maths, documents, video and GUI agents with a native 256K context.
aliases: [Qwen/Qwen3-VL-32B-Thinking, Qwen/Qwen3-VL-32B-Thinking-FP8, Qwen/Qwen3-VL-32B-Thinking-GGUF, qwen3-vl-32b-thinking, dashscope/qwen3-vl-32b-thinking, "qwen3-vl:32b", "qwen3-vl:32b-thinking"]
context_length: 262144
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-21"
benchmarks:
  gpqa_diamond: 73.3
  humanitys_last_exam: 10.1
  ifbench: 59.4
  long_context_reasoning: 55.3
  mmmu_pro: 63.4
  tau2_bench: 45.6
  terminal_bench_hard: 7.6
benchmark_variant: Qwen3 VL 32B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-VL-32B-Thinking
  - https://huggingface.co/api/models/Qwen/Qwen3-VL-32B-Thinking
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-VL-32B-Thinking/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-vl-32b
  - https://github.com/QwenLM/Qwen3-VL
  - https://arxiv.org/html/2511.21631
  - https://ollama.com/library/qwen3-vl/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 VL 32B Thinking

## Overview
Qwen3-VL-32B-Thinking was released on 2025-10-21 with the Instruct edition and the 2B size, according to the Qwen3-VL GitHub README (Artificial Analysis agrees; the Hugging Face repo was created 2025-10-19). OpenRouter does not list it; the id follows the Hugging Face repo. Thinking editions are Qwen's reasoning-enhanced variants. Hugging Face counts 33.4B parameters, and config.json gives 64 layers, 64 query and 8 key-value heads and 262,144 positions. It shares the Qwen3-VL design: Interleaved-MRoPE, DeepStack and text-timestamp alignment, a native 256K context expandable to 1M, OCR in 32 languages, grounding, GUI operation and code from screenshots. Qwen's vision settings are top_p 0.95, top_k 20, temperature 1.0 and 40,960 output tokens. Serving needs transformers 4.57.0 or vLLM 0.11.0. On Ollama, qwen3-vl:32b and qwen3-vl:32b-thinking are this model (21 GB). Alibaba Cloud Model Studio lists it as qwen3-vl-32b-thinking. Artificial Analysis marks it deprecated in favour of Qwen3.5 27B.

## Strengths
- The report gives MMBench 89.5 and RealWorldQA 79.4, the best of the medium-sized models it compares.
- Its text table gives MMLU-Pro 82.1, GPQA 73.1, AIME-25 83.7, LiveCodeBench v6 65.6, Arena-Hard v2 60.5 and TAU2-Telecom 46.9, against 79.1, 68.4, 72.9, 60.6, 50.3 and 26.3 for Qwen3-32B thinking.
- Artificial Analysis (Qwen3 VL 32B (Reasoning)): GPQA Diamond 73.3%, IFBench 59.4%, long-context reasoning 55.3%, tau2-bench 45.6%.

## Limitations
- Artificial Analysis MMMU-Pro 63.4%, just below the Instruct edition's 64.3%; Humanity's Last Exam 10.1%, Terminal-Bench Hard 7.6%; no speed figures.
- Qwen3-32B thinking leads it on CFEval (1986 against 1842) and OJBench (24.1 against 20.0).
- No published knowledge cutoff.

## Good for
- Visual maths, science and chart reasoning.
- Tool-using multimodal agents that plan before acting.
- Long-document and video analysis with justified answers.
