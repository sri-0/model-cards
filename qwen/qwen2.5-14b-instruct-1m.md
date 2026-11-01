---
id: qwen/qwen2.5-14b-instruct-1m
name: Qwen2.5 14B Instruct 1M
owned_by: qwen
type: llm
description: Qwen2.5 14B Instruct 1M is the January 2025 long-context version of Qwen's 14.7B-parameter Qwen2.5 Instruct model, open-weight under Apache-2.0 with a context of up to 1,010,000 tokens.
aliases: [Qwen/Qwen2.5-14B-Instruct-1M, qwen2.5-14b-instruct-1m]
context_length: 1010000
capabilities: [tool_calling]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-01-27"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M
  - https://huggingface.co/api/models/Qwen/Qwen2.5-14B-Instruct-1M
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M/raw/main/tokenizer_config.json
  - https://qwenlm.github.io/blog/qwen2.5-1m/
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 14B Instruct 1M

## Overview
Qwen2.5-14B-Instruct-1M was released with its sibling in the Qwen2.5-1M blog post of 2025-01-27, Qwen's first open models with 1M-token contexts (the Hugging Face repo was created 2025-01-23). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. The Hugging Face card gives 14.7B parameters (13.1B non-embedding), 48 layers, 40 query and 8 key-value heads, a full context of 1,010,000 tokens (set in config.json) and 8,192 tokens of generation. Qwen grew the context from 4K to 256K tokens during training, raising the RoPE base from 10,000 to 10,000,000, then reaches 1M with Dual Chunk Attention. Qwen recommends its own vLLM branch with sparse attention, which it says is 3 to 7 times faster up to 1M tokens; other Qwen2.5 frameworks work but may lose accuracy beyond 262,144 tokens. Full 1M-token inputs need at least 320 GB of GPU memory across up to 8 GPUs. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-14b-instruct-1m in Singapore at $0.805 per million input and $3.22 per million output tokens, with a 1,000,000-token input limit.

## Strengths
- Qwen says it beats Qwen2.5-Turbo and consistently outperforms GPT-4o-mini on long-context benchmarks (RULER, LV-Eval, LongBench-Chat), and matches GPT-4o-mini on short tasks.
- Apache-2.0, with an open inference framework.
- The chat template includes tool calls.

## Limitations
- Needs far more memory than the 7B 1M model for full-length inputs.
- Qwen's long-context setup needs its custom vLLM branch and CUDA 12.1 or 12.3, and it recommends Ampere or Hopper GPUs.
- No reasoning mode and text input only; no published knowledge cutoff.

## Good for
- Question answering over whole books, codebases or document sets.
- Long-context retrieval and summarisation without chunking.
- Comparisons with Qwen2.5-7B-Instruct-1M.
