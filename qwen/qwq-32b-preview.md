---
id: qwen/qwq-32b-preview
name: QwQ 32B Preview
owned_by: qwen
type: llm
description: QwQ 32B Preview is Qwen's November 2024 experimental open-weight (Apache-2.0) 32.5B-parameter reasoning model, fine-tuned from Qwen2.5-32B-Instruct to reason step by step before answering.
aliases: [Qwen/QwQ-32B-Preview, qwq-32b-preview, "qwq:32b-preview-q4_K_M", "qwq:32b-preview-q8_0", "qwq:32b-preview-fp16"]
context_length: 32768
capabilities: [reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2024-11-28"
benchmarks:
  gpqa_diamond: 55.7
  humanitys_last_exam: 3.9
benchmark_variant: QwQ 32B-Preview
sources:
  - https://huggingface.co/Qwen/QwQ-32B-Preview
  - https://huggingface.co/api/models/Qwen/QwQ-32B-Preview
  - https://huggingface.co/Qwen/QwQ-32B-Preview/raw/main/config.json
  - https://artificialanalysis.ai/models/QwQ-32B-Preview
  - https://qwenlm.github.io/blog/qwq-32b-preview/
  - https://ollama.com/library/qwq/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# QwQ 32B Preview

## Overview
QwQ-32B-Preview ("Qwen with Questions") is an experimental research model announced in the Qwen blog on 2024-11-28 (Artificial Analysis and the Hugging Face repo give 2024-11-27). OpenRouter does not list it; the id follows the Hugging Face repo. Its base model is Qwen2.5-32B-Instruct, and the Hugging Face card gives 32.5B parameters (31.0B non-embedding), 64 layers, 40 query and 8 key-value heads and a full 32,768-token context, which config.json confirms. Qwen's example system prompt asks it to think step by step, and it writes long reasoning before answering. Ollama serves it under qwq:32b-preview tags (20 GB at q4_K_M). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwq-32b-preview in the Beijing region only, at $0.287 per million input and $0.861 per million output tokens with 16,384 output tokens. Artificial Analysis marks it deprecated in favour of QwQ-32B, released in March 2025 with its own card.

## Strengths
- Qwen reports GPQA 65.2%, AIME 50.0%, MATH-500 90.6% and LiveCodeBench 50.0%.
- Artificial Analysis (QwQ 32B-Preview): GPQA Diamond 55.7%.
- Apache-2.0 weights.

## Limitations
- Qwen lists language mixing and code-switching, recursive reasoning loops that never conclude, the need for extra safety measures, and weaker common-sense reasoning and nuanced language understanding.
- Artificial Analysis Humanity's Last Exam 3.9%.
- 32,768-token context; no published knowledge cutoff.

## Good for
- Research on reasoning models and their failure modes.
- Maths and coding experiments where long traces are acceptable.
- Comparisons with the final QwQ-32B.
