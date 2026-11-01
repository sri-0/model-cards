---
id: qwen/qwen3-235b-a22b
name: Qwen3 235B A22B
owned_by: qwen
type: llm
description: Qwen3 235B A22B is the April 2025 Qwen3 flagship mixture-of-experts model with 235B total and 22B active parameters, open-weight under Apache-2.0, switching between thinking and non-thinking modes in one model.
aliases: [Qwen/Qwen3-235B-A22B, Qwen/Qwen3-235B-A22B-FP8, Qwen/Qwen3-235B-A22B-GGUF, Qwen/Qwen3-235B-A22B-GPTQ-Int4, Qwen/Qwen3-235B-A22B-MLX-4bit, Qwen/Qwen3-235B-A22B-MLX-6bit, Qwen/Qwen3-235B-A22B-MLX-8bit, Qwen/Qwen3-235B-A22B-MLX-bf16, qwen3-235b-a22b, "qwen3:235b-a22b-q4_K_M", "qwen3:235b-a22b-q8_0", "qwen3:235b-a22b-fp16"]
context_length: 40960
capabilities: [tool_calling, reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-04-29"
benchmarks:
  gpqa_diamond: 70.0
  humanitys_last_exam: 11.0
  ifbench: 38.7
  long_context_reasoning: 0
  tau2_bench: 24.0
  terminal_bench_hard: 6.1
benchmark_variant: Qwen3 235B A22B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-235B-A22B
  - https://huggingface.co/api/models/Qwen/Qwen3-235B-A22B
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-235B-A22B/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507
  - https://artificialanalysis.ai/models/qwen3-235b-a22b-instruct
  - https://qwenlm.github.io/blog/qwen3/
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 235B A22B

## Overview
Qwen3-235B-A22B is the Qwen3 flagship, released on 2025-04-29 according to the Qwen blog and GitHub README (Artificial Analysis lists 2025-04-28; the Hugging Face repo was created 2025-04-27). OpenRouter no longer lists it; the id follows the Hugging Face repo Qwen/Qwen3-235B-A22B. The Hugging Face card gives 235B total and 22B activated parameters, 94 layers, 64 query and 4 key-value heads, 128 experts with 8 active, and 32,768 tokens natively or 131,072 with YaRN. config.json sets max_position_embeddings to 40,960, which this card uses; Artificial Analysis lists 32,768. Thinking is on by default, switchable with enable_thinking or the /think and /no_think tags. Qwen's SGLang example uses tensor parallelism of 8. On Ollama, qwen3:235b and qwen3:235b-a22b resolve to the Thinking-2507 build, so only the quantisation tags above are this model. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen3-235b-a22b in Singapore at $0.70 per million input tokens and $2.80 non-thinking or $8.40 thinking output, with 16,384 output tokens. The Instruct-2507 and Thinking-2507 releases (own cards) replace its two modes.

## Strengths
- The Qwen blog says it is competitive with DeepSeek-R1, o1, o3-mini, Grok-3 and Gemini-2.5-Pro on coding, maths and general tasks; its figures are images.
- Qwen's Qwen3-30B-A3B-Thinking-2507 card reports this model's thinking mode at MMLU-Pro 82.8, GPQA 71.1, AIME25 81.5, LiveCodeBench v6 55.7, Arena-Hard v2 61.5 and BFCL-v3 70.8.
- Artificial Analysis (Qwen3 235B A22B (Reasoning)): GPQA Diamond 70%, Humanity's Last Exam 11%, IFBench 38.7%.
- 22B active parameters per token; 119 languages.

## Limitations
- Artificial Analysis long-context reasoning 0%, tau2-bench 24% and Terminal-Bench Hard 6.1%; no Intelligence Index or speed figures.
- Needs a multi-GPU node; Ollama's q4_K_M build is 142 GB.
- No published knowledge cutoff.

## Good for
- Self-hosted reasoning at the top of the original Qwen3 range.
- Pipelines pinned to the hybrid thinking chat template.
- Baselines for the 2507 successors.
