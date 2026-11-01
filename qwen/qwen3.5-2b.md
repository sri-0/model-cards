---
id: qwen/qwen3.5-2b
name: Qwen3.5 2B
owned_by: qwen
type: llm
description: Qwen3.5 2B is one of Qwen's March 2026 small Qwen3.5 models, a dense open-weight (Apache-2.0) vision-language model with a hybrid Gated DeltaNet and gated attention design, optional thinking and a 262,144-token native context.
aliases: [Qwen/Qwen3.5-2B, "qwen3.5:2b"]
context_length: 262144
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-03-02"
benchmarks:
  gpqa_diamond: 45.6
  humanitys_last_exam: 2.6
  ifbench: 31.5
  long_context_reasoning: 21.0
  mmmu_pro: 43.0
  tau2_bench: 69.0
  terminal_bench_hard: 3.8
benchmark_variant: Qwen3.5 2B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3.5-2B
  - https://huggingface.co/api/models/Qwen/Qwen3.5-2B
  - https://huggingface.co/Qwen/Qwen3.5-2B/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-5-2b
  - https://github.com/QwenLM/Qwen3.5
  - https://ollama.com/library/qwen3.5/tags
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.5 2B

## Overview
Qwen3.5-2B was released on 2026-03-02 with the 9B, 4B, 2B and 0.8B sizes, according to the QwenLM GitHub README (Artificial Analysis agrees). OpenRouter does not list it; the id follows the Hugging Face repo, and the 9B size has its own card. It is a causal language model with a vision encoder, trained with early fusion on multimodal tokens, taking text, image and video input. The language model has a hidden size of 2,048 and 24 layers laid out as 6 × (3 × Gated DeltaNet → 1 × gated attention), each followed by a feed-forward layer; Gated DeltaNet uses 16 V and 16 QK linear-attention heads and gated attention 8 query and 2 key-value heads, with tied embeddings and multi-token prediction. The context is 262,144 tokens natively. Unlike the larger Qwen3.5 models, it runs in non-thinking mode by default; Qwen says its size suits prototyping, task-specific fine-tuning and research. Qwen states support for 201 languages and dialects. Serving uses SGLang or vLLM, with the qwen3_coder parser for tool calls; Ollama serves it as qwen3.5:2b (2.7 to 3.1 GB).

## Strengths
- Qwen reports thinking-mode MMLU-Pro 66.5, GPQA 51.6, IFEval 78.6, BFCL-V4 43.6 and TAU2-Bench 48.8, against 56.5, 40.1, 72.5 and no agent scores for Qwen3-1.7B.
- Vision: MMMU 64.2, MathVista 76.7, OCRBench 84.5 and VideoMME 75.6 with subtitles, above Qwen3-VL-2B on each.
- Artificial Analysis (Qwen3.5 2B (Reasoning)): tau2-bench 69%, GPQA Diamond 45.6%, MMMU-Pro 43%.

## Limitations
- Qwen3-4B-2507 leads it in Qwen's text table, for example thinking MMLU-Pro 74.0 against 66.5.
- Artificial Analysis long-context reasoning 21%, Terminal-Bench Hard 3.8% and Humanity's Last Exam 2.6%; no speed figures.
- No published knowledge cutoff.

## Good for
- Lightweight multimodal assistants and document readers.
- Fine-tuning a small vision-language model.
- Agents on edge hardware that need tool calls.
