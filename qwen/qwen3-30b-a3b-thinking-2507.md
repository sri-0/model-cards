---
id: qwen/qwen3-30b-a3b-thinking-2507
name: Qwen3 30B A3B Thinking 2507
owned_by: qwen
type: llm
description: Qwen3 30B A3B Thinking 2507 is the July 2025 thinking-only update of Qwen's 30.5B-parameter mixture-of-experts model (3.3B active), open-weight under Apache-2.0 with a native 262,144-token context.
aliases: [Qwen/Qwen3-30B-A3B-Thinking-2507, Qwen/Qwen3-30B-A3B-Thinking-2507-FP8, qwen3-30b-a3b-thinking-2507, "qwen3:30b", "qwen3:30b-a3b", "qwen3:30b-thinking", "qwen3:30b-a3b-thinking-2507-q4_K_M"]
context_length: 262144
capabilities: [tool_calling, reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-07-31"
benchmarks:
  gpqa_diamond: 70.7
  humanitys_last_exam: 10.3
  ifbench: 50.7
  long_context_reasoning: 61.3
  scicode: 33.0
  tau2_bench: 28.1
  terminal_bench_4: 0
  terminal_bench_hard: 5.3
benchmark_variant: Qwen3 30B A3B 2507 (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507
  - https://huggingface.co/api/models/Qwen/Qwen3-30B-A3B-Thinking-2507
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-30b-a3b-2507-reasoning
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 30B A3B Thinking 2507

## Overview
Qwen3-30B-A3B-Thinking-2507 updates the thinking mode of Qwen3-30B-A3B; the Qwen GitHub README dates it 2025-07-31 (Artificial Analysis lists 2025-07-30; the Hugging Face repo was created 2025-07-29). OpenRouter does not list it; the id follows the Hugging Face repo. The Hugging Face card gives 30.5B total and 3.3B activated parameters, 48 layers, 32 query and 4 key-value heads, 128 experts with 8 active, and a native 262,144-token context; config_1m.json extends it to 1 million tokens with about 240 GB of GPU memory. It runs only in thinking mode; the chat template adds the opening think tag. Alibaba Cloud Model Studio (archived 2026-06-06) serves it as qwen3-30b-a3b-thinking-2507 in Singapore at $0.20 per million input and $2.40 per million output tokens, with a 131,072-token window. On Ollama, qwen3:30b, qwen3:30b-a3b and qwen3:30b-thinking resolve to this build. Artificial Analysis marks it deprecated.

## Strengths
- Qwen reports AIME25 85.0, HMMT25 71.4, LiveCodeBench v6 66.0, GPQA 73.4, MMLU-Pro 80.9, IFEval 88.9, BFCL-v3 72.4 and TAU2-Retail 58.8, against 70.9, 49.8, 57.4, 65.8, 78.5, 86.5, 69.1 and 34.2 for the original model in thinking mode.
- Qwen's table puts it above the original Qwen3-235B-A22B thinking mode on AIME25, HMMT25, LiveCodeBench v6 and every agent benchmark.
- Artificial Analysis (Qwen3 30B A3B 2507 (Reasoning)): GPQA Diamond 70.7%, long-context reasoning 61.3%, IFBench 50.7%, SciCode 33%.
- 3.3B active parameters; Ollama's q4_K_M build is 19 GB.

## Limitations
- Artificial Analysis Terminal-Bench 4.0 0%, Terminal-Bench Hard 5.3%, tau2-bench 28.1%, Humanity's Last Exam 10.3%; no speed figures.
- Long traces: Qwen used 81,920 output tokens for reasoning and coding benchmarks.
- Gemini 2.5 Flash Thinking leads it in Qwen's table on GPQA, INCLUDE and TAU2-Telecom.
- No published knowledge cutoff.

## Good for
- Maths, science and competitive programming.
- Tool-calling agents with a reasoning loop on one GPU.
- Long-document reasoning up to 256K tokens, or 1M extended.
