---
id: qwen/qwen3.5-0.8b
name: Qwen3.5 0.8B
owned_by: qwen
type: llm
description: Qwen3.5 0.8B is one of Qwen's March 2026 small Qwen3.5 models, a dense open-weight (Apache-2.0) vision-language model with a hybrid Gated DeltaNet and gated attention design, optional thinking and a 262,144-token native context.
aliases: [Qwen/Qwen3.5-0.8B, "qwen3.5:0.8b"]
context_length: 262144
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-03-02"
benchmarks:
  gpqa_diamond: 11.1
  humanitys_last_exam: 1.1
  ifbench: 21.5
  long_context_reasoning: 9.0
  mmmu_pro: 25.8
  tau2_bench: 47.7
  terminal_bench_hard: 0
benchmark_variant: Qwen3.5 0.8B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3.5-0.8B
  - https://huggingface.co/api/models/Qwen/Qwen3.5-0.8B
  - https://huggingface.co/Qwen/Qwen3.5-0.8B/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-5-0-8b
  - https://github.com/QwenLM/Qwen3.5
  - https://ollama.com/library/qwen3.5/tags
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.5 0.8B

## Overview
Qwen3.5-0.8B was released on 2026-03-02 with the 9B, 4B, 2B and 0.8B sizes, according to the QwenLM GitHub README (Artificial Analysis agrees). OpenRouter does not list it; the id follows the Hugging Face repo, and the 9B size has its own card. It is a causal language model with a vision encoder, trained with early fusion on multimodal tokens, taking text, image and video input. The language model has a hidden size of 1,024 and 24 layers laid out as 6 × (3 × Gated DeltaNet → 1 × gated attention), each followed by a feed-forward layer; Gated DeltaNet uses 16 V and 16 QK linear-attention heads and gated attention 8 query and 2 key-value heads, with tied embeddings and multi-token prediction. The context is 262,144 tokens natively. Unlike the larger Qwen3.5 models, it runs in non-thinking mode by default; Qwen says its size suits prototyping, task-specific fine-tuning and research. Qwen states support for 201 languages and dialects. Serving uses SGLang or vLLM, with the qwen3_coder parser for tool calls; Ollama serves it as qwen3.5:0.8b (1.2 to 1.3 GB).

## Strengths
- Qwen reports OCRBench 74.5 (79.1 without thinking), MathVista 62.2 and MMMU 49 in thinking mode, and VideoMME 63.8 with subtitles.
- Artificial Analysis (Qwen3.5 0.8B (Reasoning)): tau2-bench 47.7%, MMMU-Pro 25.8%, IFBench 21.5%.
- Vision, video and tool calling in under a billion parameters (Hugging Face counts 0.87B).

## Limitations
- Weak knowledge and reasoning: Artificial Analysis GPQA Diamond 11.1% and Humanity's Last Exam 1.1%; Qwen reports thinking-mode GPQA 11.9 and TAU2-Bench 11.6.
- Artificial Analysis long-context reasoning 9% and Terminal-Bench Hard 0%; no speed figures.
- No published knowledge cutoff.

## Good for
- On-device OCR and image captioning.
- Task-specific fine-tuning of a tiny multimodal model.
- Prototyping Qwen3.5 pipelines cheaply.
