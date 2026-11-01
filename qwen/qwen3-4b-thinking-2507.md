---
id: qwen/qwen3-4b-thinking-2507
name: Qwen3 4B Thinking 2507
owned_by: qwen
type: llm
description: Qwen3 4B Thinking 2507 is the August 2025 thinking-only update of Qwen's 4.0B-parameter dense model, open-weight under Apache-2.0 with a native 262,144-token context.
aliases: [Qwen/Qwen3-4B-Thinking-2507, Qwen/Qwen3-4B-Thinking-2507-FP8, "qwen3:4b", "qwen3:4b-thinking", "qwen3:4b-thinking-2507-q4_K_M"]
context_length: 262144
capabilities: [tool_calling, reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-08-06"
benchmarks:
  gpqa_diamond: 66.7
  humanitys_last_exam: 6.2
  ifbench: 49.8
  long_context_reasoning: 37.3
  tau2_bench: 25.4
  terminal_bench_hard: 1.5
benchmark_variant: Qwen3 4B 2507 (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507
  - https://huggingface.co/api/models/Qwen/Qwen3-4B-Thinking-2507
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-4b-2507-instruct-reasoning
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3/tags
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 4B Thinking 2507

## Overview
Qwen3-4B-Thinking-2507 is the updated thinking-mode version of Qwen3-4B, released on 2025-08-06 per the Qwen GitHub README (Artificial Analysis agrees; the Hugging Face repo was created 2025-08-05). OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-4B-Thinking-2507. The Hugging Face card gives 4.0B parameters (3.6B non-embedding), 36 layers, 32 query and 8 key-value heads, and a native 262,144-token context, which config.json confirms. It runs only in thinking mode: the chat template inserts the opening think tag, so output shows only the closing tag. Qwen says it thinks longer than before and recommends it for highly complex reasoning; it suggests temperature 0.6, top_p 0.95, top_k 20 and a context above 131,072 tokens. On Ollama, qwen3:4b, qwen3:4b-thinking and qwen3:4b-thinking-2507-q4_K_M share one build of this model. Artificial Analysis marks it deprecated in favour of Qwen3.5 4B.

## Strengths
- Qwen reports AIME25 81.3, HMMT25 55.5, LiveCodeBench v6 55.2, GPQA 65.8, MMLU-Pro 74.0, IFEval 87.4, BFCL-v3 71.2 and TAU2-Retail 53.5, against 65.6, 42.1, 48.4, 55.9, 70.4, 81.9, 65.9 and 38.6 for the original Qwen3-4B in thinking mode.
- Qwen's table puts it above Qwen3-30B-A3B thinking mode on AIME25, HMMT25, IFEval, WritingBench and every agent benchmark listed.
- Artificial Analysis (Qwen3 4B 2507 (Reasoning)): GPQA Diamond 66.7%, IFBench 49.8%, long-context reasoning 37.3%.
- 256K context; Ollama's q4_K_M build is 2.5 GB.

## Limitations
- Artificial Analysis Terminal-Bench Hard 1.5%, tau2-bench 25.4% and Humanity's Last Exam 6.2%; no Intelligence Index or speed figures.
- Long traces: Qwen recommends 32,768 output tokens for most queries and 81,920 for competition problems.
- Qwen reports MMLU-ProX 64.2 and INCLUDE 64.4, below Qwen3-30B-A3B thinking mode.
- No published knowledge cutoff.

## Good for
- Maths, science and competitive programming on small hardware.
- Agent loops with visible reasoning and tool calls at 4B scale.
- Long-context reasoning over documents up to 256K tokens.
