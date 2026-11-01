---
id: qwen/qwen3-1.7b
name: Qwen3 1.7B
owned_by: qwen
type: llm
description: Qwen3 1.7B is a 1.7B-parameter dense open-weight (Apache-2.0) model from the April 2025 Qwen3 series that switches between a thinking mode and a non-thinking mode in one model.
aliases: [Qwen/Qwen3-1.7B, Qwen/Qwen3-1.7B-FP8, Qwen/Qwen3-1.7B-GGUF, Qwen/Qwen3-1.7B-GPTQ-Int8, Qwen/Qwen3-1.7B-MLX-4bit, Qwen/Qwen3-1.7B-MLX-6bit, Qwen/Qwen3-1.7B-MLX-8bit, Qwen/Qwen3-1.7B-MLX-bf16, qwen3-1.7b, "qwen3:1.7b"]
context_length: 40960
capabilities: [tool_calling, reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-04-29"
benchmarks:
  gpqa_diamond: 35.6
  humanitys_last_exam: 4.6
  ifbench: 26.9
  long_context_reasoning: 0
  tau2_bench: 26.0
  terminal_bench_hard: 0
benchmark_variant: Qwen3 1.7B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-1.7B
  - https://huggingface.co/api/models/Qwen/Qwen3-1.7B
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-1.7B/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-1.7b-instruct
  - https://qwenlm.github.io/blog/qwen3/
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 1.7B

## Overview
Qwen3-1.7B was released with the Qwen3 series, which the Qwen blog and GitHub README date 2025-04-29 (Artificial Analysis lists 2025-04-28; the Hugging Face repo was created 2025-04-27). OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-1.7B. The Hugging Face card gives 1.7B parameters (1.4B non-embedding), 28 layers, 16 query and 8 key-value heads and a 32,768-token context with no documented YaRN extension; the blog adds tied embeddings, and config.json sets max_position_embeddings to 40,960, which this card uses. Thinking is on by default, switchable with enable_thinking or the /think and /no_think tags. Serving needs transformers 4.51.0, sglang 0.4.6.post1 or vllm 0.8.5 or newer. Ollama serves it as qwen3:1.7b. Alibaba Cloud Model Studio (models page archived 2026-06-06) lists qwen3-1.7b in Singapore at $0.11 per million input tokens and $0.42 non-thinking or $1.26 thinking output, with a 32,768-token window. Artificial Analysis marks it deprecated in favour of Qwen3.5 2B.

## Strengths
- The blog says Qwen3-1.7B-Base matches Qwen2.5-3B-Base, and that thinking mode surpasses QwQ and non-thinking mode Qwen2.5 Instruct across the series; per-size figures are images.
- Artificial Analysis (Qwen3 1.7B (Reasoning)): GPQA Diamond 35.6%, IFBench 26.9%, tau2-bench 26%, each above the 0.6B size.
- Ollama's default q4_K_M build is 1.4 GB and the fp16 build 4.1 GB.
- 119 languages and dialects, with tool calling through Qwen-Agent.

## Limitations
- Artificial Analysis long-context reasoning 0%, Terminal-Bench Hard 0% and Humanity's Last Exam 4.6%; no Intelligence Index or speed figures were published.
- Qwen recommends 32,768 output tokens for most queries, so thinking answers can be slow on small hardware.
- No published knowledge cutoff.

## Good for
- On-device chat and summarisation on laptops.
- Multilingual assistants where a 2B-class model is enough.
- Fine-tuning experiments on a small base.
