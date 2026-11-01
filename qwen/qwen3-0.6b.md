---
id: qwen/qwen3-0.6b
name: Qwen3 0.6B
owned_by: qwen
type: llm
description: Qwen3 0.6B is the smallest dense model of the April 2025 Qwen3 series, a 0.6B-parameter open-weight (Apache-2.0) model that switches between a thinking mode and a non-thinking mode in one model.
aliases: [Qwen/Qwen3-0.6B, Qwen/Qwen3-0.6B-FP8, Qwen/Qwen3-0.6B-GGUF, Qwen/Qwen3-0.6B-GPTQ-Int8, Qwen/Qwen3-0.6B-MLX-4bit, Qwen/Qwen3-0.6B-MLX-6bit, Qwen/Qwen3-0.6B-MLX-8bit, Qwen/Qwen3-0.6B-MLX-bf16, qwen3-0.6b, "qwen3:0.6b"]
context_length: 40960
capabilities: [tool_calling, reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-04-29"
benchmarks:
  gpqa_diamond: 23.9
  humanitys_last_exam: 5.6
  ifbench: 23.3
  long_context_reasoning: 0
  tau2_bench: 21.1
  terminal_bench_hard: 0
benchmark_variant: Qwen3 0.6B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-0.6B
  - https://huggingface.co/api/models/Qwen/Qwen3-0.6B
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-0.6B/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-0.6b-instruct
  - https://qwenlm.github.io/blog/qwen3/
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 0.6B

## Overview
Qwen3-0.6B is the smallest dense model of the Qwen3 series, which the Qwen blog and GitHub README date 2025-04-29 (Artificial Analysis lists 2025-04-28; the Hugging Face repo was created 2025-04-27). OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-0.6B. The Hugging Face card gives 0.6B parameters (0.44B non-embedding), 28 layers, 16 query and 8 key-value heads and a 32,768-token context with no documented YaRN extension; the blog adds tied embeddings, and config.json sets max_position_embeddings to 40,960, which this card uses. Thinking is on by default, switchable with enable_thinking or the /think and /no_think tags. Serving needs transformers 4.51.0, sglang 0.4.6.post1 or vllm 0.8.5 or newer. Ollama serves it as qwen3:0.6b. Alibaba Cloud Model Studio (models page archived 2026-06-06) lists qwen3-0.6b in Singapore at $0.11 per million input tokens and $0.42 non-thinking or $1.26 thinking output, with a 32,768-token window. Artificial Analysis marks it deprecated in favour of Qwen3.5 0.8B.

## Strengths
- Qwen says Qwen3 thinking mode surpasses QwQ and non-thinking mode surpasses Qwen2.5 Instruct on mathematics, code and commonsense reasoning; the blog's per-size figures are images.
- Artificial Analysis (Qwen3 0.6B (Reasoning)): GPQA Diamond 23.9%, IFBench 23.3%, tau2-bench 21.1%, Humanity's Last Exam 5.6%.
- Ollama's default q4_K_M build is 523 MB and the fp16 build 1.5 GB.
- 119 languages and dialects, with tool calling through Qwen-Agent.

## Limitations
- Artificial Analysis long-context reasoning 0% and Terminal-Bench Hard 0%; no Intelligence Index or speed figures were published.
- Qwen recommends 32,768 output tokens for most queries, and presence_penalty 1.5 if output repeats endlessly.
- No published knowledge cutoff.

## Good for
- Edge and on-device assistants, short drafts and classification.
- Cheap experiments with Qwen3 chat templates and thinking switches.
- Fine-tuning on a very small base.
