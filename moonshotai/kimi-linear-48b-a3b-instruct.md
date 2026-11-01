---
id: moonshotai/kimi-linear-48b-a3b-instruct
name: Kimi Linear 48B A3B Instruct
owned_by: moonshotai
type: llm
description: Kimi Linear 48B A3B Instruct is Moonshot AI's open-weight (MIT) research model for its hybrid Kimi Delta Attention architecture, a 48B-total, 3B-active mixture-of-experts model with a 1M-token context.
aliases: [moonshotai/Kimi-Linear-48B-A3B-Instruct]
context_length: 1048576
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-10-30"
benchmarks:
  gpqa_diamond: 41.2
  humanitys_last_exam: 2.5
  ifbench: 28.1
  long_context_reasoning: 28.0
  tau2_bench: 0
  terminal_bench_hard: 11.4
benchmark_variant: Kimi Linear 48B A3B Instruct
sources:
  - https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct
  - https://huggingface.co/api/models/moonshotai/Kimi-Linear-48B-A3B-Instruct
  - https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct/raw/main/config.json
  - https://artificialanalysis.ai/models/kimi-linear-48b-a3b-instruct
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Kimi Linear 48B A3B Instruct

## Overview
Kimi Linear, released on 2025-10-30 with the paper arXiv 2510.26692, is Moonshot AI's hybrid linear-attention architecture. Its core is Kimi Delta Attention (KDA), a refinement of Gated DeltaNet with finer-grained gating, interleaved with global MLA layers at a 3:1 ratio (20 KDA and 7 full-attention layers in config.json). The instruct checkpoint is a mixture-of-experts model with 48B total and 3B activated parameters (256 experts, 8 per token), trained on 5.7T tokens, with a 1,048,576-token maximum length. OpenRouter does not list it; the id follows the Hugging Face repo `moonshotai/Kimi-Linear-48B-A3B-Instruct`. Weights are MIT-licensed, and a base checkpoint is also published.

## Strengths
- Moonshot reports up to 75% less KV cache and up to 6x faster decoding at 1M tokens (6.3x faster time per output token than MLA).
- On Moonshot's comparison it scores 51.0 on MMLU-Pro at 4K context and 84.3 on RULER at 128K, with a 3.98x speed-up there.
- Only 3B active parameters, so inference is cheap for its size; vLLM serves it with `--max-model-len 1048576`.

## Limitations
- A research release, not a frontier assistant: Artificial Analysis measured 41.2% on GPQA Diamond, 28% on AA-LCR, 2.5% on Humanity's Last Exam and 0% on tau2-bench.
- Needs the `fla-core` kernels (0.4.0 or later) and `trust_remote_code`.
- Text only, with no reasoning mode; tool calling is not documented.

## Good for
- Research and benchmarking of linear-attention and hybrid architectures.
- Long-document workloads where KV-cache memory is the constraint.
