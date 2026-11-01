---
id: qwen/qwen3-4b
name: Qwen3 4B
owned_by: qwen
type: llm
description: Qwen3 4B is a 4.0B-parameter dense open-weight (Apache-2.0) model from the April 2025 Qwen3 series that switches between a thinking mode and a non-thinking mode in one model.
aliases: [Qwen/Qwen3-4B, Qwen/Qwen3-4B-AWQ, Qwen/Qwen3-4B-FP8, Qwen/Qwen3-4B-GGUF, Qwen/Qwen3-4B-MLX-4bit, Qwen/Qwen3-4B-MLX-6bit, Qwen/Qwen3-4B-MLX-8bit, Qwen/Qwen3-4B-MLX-bf16, qwen3-4b, "qwen3:4b-q4_K_M", "qwen3:4b-q8_0", "qwen3:4b-fp16"]
context_length: 40960
capabilities: [tool_calling, reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-04-29"
benchmarks:
  gpqa_diamond: 52.2
  humanitys_last_exam: 4.4
  ifbench: 32.5
  long_context_reasoning: 0
  tau2_bench: 19.0
benchmark_variant: Qwen3 4B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-4B
  - https://huggingface.co/api/models/Qwen/Qwen3-4B
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3-4B/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507
  - https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507
  - https://artificialanalysis.ai/models/qwen3-4b-instruct
  - https://qwenlm.github.io/blog/qwen3/
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 4B

## Overview
Qwen3-4B was released with the Qwen3 series, which the Qwen blog and GitHub README date 2025-04-29 (Artificial Analysis lists 2025-04-28; the Hugging Face repo was created 2025-04-27). OpenRouter does not list it; the id follows the Hugging Face repo Qwen/Qwen3-4B. The Hugging Face card gives 4.0B parameters (3.6B non-embedding), 36 layers, 32 query and 8 key-value heads, and 32,768 tokens natively or 131,072 with YaRN, advised only for longer prompts. config.json sets max_position_embeddings to 40,960 (32,768 for output plus 8,192 for prompts), which this card uses. Thinking is on by default, switchable with enable_thinking or the /think and /no_think tags. Serving needs transformers 4.51.0, sglang 0.4.6.post1 or vllm 0.8.5 or newer. On Ollama the bare tag qwen3:4b resolves to the Thinking-2507 build, so only the quantisation tags above are this model. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen3-4b in Singapore at $0.11 per million input tokens and $0.42 non-thinking or $1.26 thinking output. The 2507 Instruct and Thinking releases (own cards, 2025-08-06) replace its two modes.

## Strengths
- The blog says Qwen3-4B rivals Qwen2.5-72B-Instruct and Qwen3-4B-Base matches Qwen2.5-7B-Base.
- Qwen's 2507 cards report this model in thinking mode at MMLU-Pro 70.4, GPQA 55.9, AIME25 65.6, LiveCodeBench v6 48.4, IFEval 81.9 and BFCL-v3 65.9, and in non-thinking mode at 58.0, 41.7, 19.1, 26.4, 81.2 and 57.6.
- Artificial Analysis (Qwen3 4B (Reasoning)): GPQA Diamond 52.2%, IFBench 32.5%.
- Ollama's q4_K_M build is 2.6 GB.

## Limitations
- Artificial Analysis long-context reasoning 0%, tau2-bench 19% and Humanity's Last Exam 4.4%; no Intelligence Index, Terminal-Bench or speed figures.
- Qwen's tables put the 2507 releases ahead on every listed benchmark except Aider-Polyglot and TAU2-Telecom for Instruct-2507.
- No published knowledge cutoff.

## Good for
- Local chat and reasoning on one consumer GPU.
- Pipelines pinned to the original hybrid Qwen3 chat template.
- Fine-tuning a 4B base.
