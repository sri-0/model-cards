---
id: qwen/qwen3-4b-instruct-2507
name: Qwen3 4B Instruct 2507
owned_by: qwen
type: llm
description: Qwen3 4B Instruct 2507 is the August 2025 non-thinking update of Qwen's 4.0B-parameter dense model, open-weight under Apache-2.0 with a native 262,144-token context.
aliases: [Qwen/Qwen3-4B-Instruct-2507, Qwen/Qwen3-4B-Instruct-2507-FP8, "qwen3:4b-instruct", "qwen3:4b-instruct-2507-q4_K_M"]
context_length: 262144
capabilities: [tool_calling]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-08-06"
benchmarks:
  gpqa_diamond: 51.7
  humanitys_last_exam: 4.5
  ifbench: 33.5
  long_context_reasoning: 11.3
  tau2_bench: 26.6
  terminal_bench_hard: 4.5
benchmark_variant: Qwen3 4B 2507 Instruct
sources:
  - https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507
  - https://huggingface.co/api/models/Qwen/Qwen3-4B-Instruct-2507
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-4b-2507-instruct
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3/tags
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 4B Instruct 2507

## Overview
Qwen3-4B-Instruct-2507 is the updated non-thinking version of Qwen3-4B, released on 2025-08-06 as the last open Qwen3-2507 model, per the Qwen GitHub README (Artificial Analysis agrees; the Hugging Face repo was created 2025-08-05). OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-4B-Instruct-2507. The Hugging Face card gives 4.0B parameters (3.6B non-embedding), 36 layers, 32 query and 8 key-value heads, and a native context of 262,144 tokens, which config.json confirms. It runs only in non-thinking mode and never emits think blocks. Qwen suggests temperature 0.7, top_p 0.8, top_k 20, min_p 0 and 16,384 output tokens, and says to cut the context to 32,768 if memory runs out. Serving needs sglang 0.4.6.post1 or vllm 0.8.5 or newer. On Ollama, qwen3:4b-instruct and qwen3:4b-instruct-2507-q4_K_M share one build of this model. Artificial Analysis marks it deprecated in favour of Qwen3.5 4B.

## Strengths
- Qwen reports MMLU-Pro 69.6, GPQA 62.0, AIME25 47.4, ZebraLogic 80.2, LiveCodeBench v6 35.1, Arena-Hard v2 43.4, Creative Writing v3 83.5 and BFCL-v3 61.9, against 58.0, 41.7, 19.1, 35.2, 26.4, 9.5, 53.6 and 57.6 for the original Qwen3-4B in non-thinking mode.
- In Qwen's table it scores above GPT-4.1-nano on every benchmark where a GPT-4.1-nano figure is given.
- Artificial Analysis (Qwen3 4B 2507 Instruct): GPQA Diamond 51.7%, IFBench 33.5%, tau2-bench 26.6%.
- 256K context; Ollama's q4_K_M build is 2.5 GB.

## Limitations
- Artificial Analysis long-context reasoning 11.3%, Terminal-Bench Hard 4.5% and Humanity's Last Exam 4.5%; no Intelligence Index or speed figures.
- No thinking mode; the separate Thinking-2507 release covers that.
- Qwen reports Aider-Polyglot 12.9 and TAU2-Telecom 13.2, below the original Qwen3-4B non-thinking (13.8, 17.5).
- No published knowledge cutoff.

## Good for
- Fast chat, writing and instruction following on small hardware.
- Long-document reading up to 256K tokens at 4B scale.
- Lightweight tool-calling agents that need fast replies.
