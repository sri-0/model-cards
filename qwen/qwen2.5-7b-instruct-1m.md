---
id: qwen/qwen2.5-7b-instruct-1m
name: Qwen2.5 7B Instruct 1M
owned_by: qwen
type: llm
description: Qwen2.5 7B Instruct 1M is the January 2025 long-context version of Qwen's 7.61B-parameter Qwen2.5 Instruct model, open-weight under Apache-2.0 with a context of up to 1,010,000 tokens.
aliases: [Qwen/Qwen2.5-7B-Instruct-1M, qwen2.5-7b-instruct-1m]
context_length: 1010000
capabilities: [tool_calling]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-01-27"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M
  - https://huggingface.co/api/models/Qwen/Qwen2.5-7B-Instruct-1M
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M/raw/main/tokenizer_config.json
  - https://qwenlm.github.io/blog/qwen2.5-1m/
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 7B Instruct 1M

## Overview
Qwen2.5-7B-Instruct-1M was released with its sibling in the Qwen2.5-1M blog post of 2025-01-27, the first open Qwen models with 1M-token contexts (the Hugging Face repo was created 2025-01-23). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. The Hugging Face card gives 7.61B parameters (6.53B non-embedding), 28 layers, 28 query and 4 key-value heads, a full context of 1,010,000 tokens (set in config.json) and 8,192 tokens of generation. Qwen grew the context from 4K to 256K tokens during training, raising the RoPE base from 10,000 to 10,000,000, then reaches 1M with Dual Chunk Attention. Qwen recommends its own vLLM branch with sparse attention, which it says is 3 to 7 times faster up to 1M tokens; other Qwen2.5 frameworks work but may lose accuracy beyond 262,144 tokens. Full 1M-token inputs need at least 120 GB of GPU memory across up to 4 GPUs. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-7b-instruct-1m in Singapore at $0.368 per million input and $1.47 per million output tokens.

## Strengths
- Qwen says the 1M models outperform their 128K counterparts on most long-context tasks, especially beyond 64K tokens, while keeping similar short-task scores; on 1M-token passkey retrieval the 7B model makes only minor errors.
- Apache-2.0, with an open inference framework.
- The chat template includes tool calls.

## Limitations
- The 14B 1M model, not this one, is the size Qwen says beats Qwen2.5-Turbo and GPT-4o-mini on long-context benchmarks.
- Qwen's long-context setup needs its custom vLLM branch and CUDA 12.1 or 12.3, and it recommends Ampere or Hopper GPUs.
- No reasoning mode and text input only; no published knowledge cutoff.

## Good for
- Question answering over whole books, codebases or document sets.
- Long-context retrieval and summarisation without chunking.
- A lighter alternative to Qwen2.5-14B-Instruct-1M.
