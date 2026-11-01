---
id: qwen/qwen3-8b
name: Qwen3 8B
owned_by: qwen
type: llm
description: Qwen3 8B is an 8.2B-parameter dense open-weight (Apache-2.0) model from the April 2025 Qwen3 series that switches between a thinking mode and a non-thinking mode in one model.
aliases: [Qwen/Qwen3-8B, Qwen/Qwen3-8B-AWQ, Qwen/Qwen3-8B-FP8, Qwen/Qwen3-8B-GGUF, Qwen/Qwen3-8B-MLX-4bit, Qwen/Qwen3-8B-MLX-6bit, Qwen/Qwen3-8B-MLX-8bit, Qwen/Qwen3-8B-MLX-bf16, qwen3-8b, "qwen3:8b"]
context_length: 40960
capabilities: [tool_calling, reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-04-29"
benchmarks:
  gpqa_diamond: 58.9
  humanitys_last_exam: 3.9
  ifbench: 33.5
  long_context_reasoning: 0
  scicode: 27.9
  tau2_bench: 27.8
  terminal_bench_4: 0
  terminal_bench_hard: 2.3
benchmark_variant: Qwen3 8B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-8B
  - https://huggingface.co/api/models/Qwen/Qwen3-8B
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-8B/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-8b-instruct
  - https://qwenlm.github.io/blog/qwen3/
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 8B

## Overview
Qwen3-8B was released with the Qwen3 series, which the Qwen blog and GitHub README date 2025-04-29 (Artificial Analysis lists 2025-04-28; the Hugging Face repo was created 2025-04-27). OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-8B. The Hugging Face card gives 8.2B parameters (6.95B non-embedding), 36 layers, 32 query and 8 key-value heads, and 32,768 tokens natively or 131,072 with YaRN, the figure Artificial Analysis lists. config.json sets max_position_embeddings to 40,960 (32,768 for output plus 8,192 for prompts), which this card uses. Thinking is on by default, switchable with enable_thinking or the /think and /no_think tags. Serving needs transformers 4.51.0, sglang 0.4.6.post1 or vllm 0.8.5 or newer. Ollama serves it as qwen3:8b, which is also qwen3:latest. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen3-8b in Singapore at $0.18 per million input tokens and $0.70 non-thinking or $2.10 thinking output, with 8,192 output tokens. No 2507 update exists for this size; Artificial Analysis marks it deprecated.

## Strengths
- The blog says Qwen3-8B-Base matches Qwen2.5-14B-Base, and that thinking mode surpasses QwQ and non-thinking mode Qwen2.5 Instruct; its figures are images.
- Artificial Analysis (Qwen3 8B (Reasoning)): GPQA Diamond 58.9%, IFBench 33.5%, tau2-bench 27.8%, SciCode 27.9%.
- Ollama's q4_K_M build is 5.2 GB and the fp16 build 16 GB.
- 119 languages and dialects, with tool calling through Qwen-Agent and MCP.

## Limitations
- Artificial Analysis long-context reasoning 0%, Terminal-Bench 4.0 0%, Terminal-Bench Hard 2.3% and Humanity's Last Exam 3.9%; no Intelligence Index or speed figures.
- YaRN is static in common frameworks and can hurt short prompts.
- No published knowledge cutoff.

## Good for
- Single-GPU reasoning assistants and local coding help.
- Multilingual chat with switchable thinking.
- Agent prototypes with Qwen-Agent and MCP tools.
