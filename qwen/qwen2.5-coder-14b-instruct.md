---
id: qwen/qwen2.5-coder-14b-instruct
name: Qwen2.5 Coder 14B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 Coder 14B Instruct is the 14B instruction-tuned code model of Qwen's Qwen2.5-Coder series, open-weight under Apache-2.0 and trained on 5.5 trillion tokens of code-related data.
aliases: [Qwen/Qwen2.5-Coder-14B-Instruct, Qwen/Qwen2.5-Coder-14B-Instruct-AWQ, Qwen/Qwen2.5-Coder-14B-Instruct-GGUF, Qwen/Qwen2.5-Coder-14B-Instruct-GPTQ-Int4, Qwen/Qwen2.5-Coder-14B-Instruct-GPTQ-Int8, qwen2.5-coder-14b-instruct, "qwen2.5-coder:14b", "qwen2.5-coder:14b-instruct"]
context_length: 32768
capabilities: [tool_calling]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2024-11-12"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-Coder-14B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct/raw/main/tokenizer_config.json
  - https://qwenlm.github.io/blog/qwen2.5-coder/
  - https://qwenlm.github.io/blog/qwen2.5-coder-family/
  - https://ollama.com/library/qwen2.5-coder/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 Coder 14B Instruct

## Overview
Qwen2.5-Coder-14B-Instruct is the instruction-tuned 14B model of Qwen2.5-Coder, the renamed CodeQwen line, released on 2024-11-12 with the 0.5B, 3B and 32B sizes in the Qwen2.5-Coder family blog post (the Hugging Face repo was created 2024-11-06). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. Built on Qwen2.5, the series is trained on 5.5 trillion tokens of source code, text-code grounding and synthetic data and covers 92 programming languages. The Hugging Face card gives 14.7B parameters (13.1B non-embedding), 48 layers and 40 query and 8 key-value heads, with a full 131,072-token context, with config.json set to 32,768 and YaRN beyond that. It needs transformers 4.37.0 or newer, and its chat template includes tool calls. Qwen publishes AWQ, GPTQ (Int4, Int8) and GGUF builds. Ollama serves it as qwen2.5-coder:14b (9.0 GB). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-coder-14b-instruct in the Beijing region only.

## Strengths
- Qwen says Qwen2.5-Coder reaches state-of-the-art open-source results at every size it released, measured on recent LiveCodeBench questions (2024.07 to 2024.11).
- The model card says the series keeps Qwen2.5's strengths in maths and general tasks while improving code generation, reasoning and fixing.
- Qwen demonstrates the series as a code assistant in Cursor and for Artifacts in Open WebUI.

## Limitations
- Qwen publishes per-size coding scores only as images.
- No reasoning mode and text input only.
- No published knowledge cutoff.

## Good for
- Local code completion, generation and repair.
- Editor assistants where latency matters.
- Fine-tuning a code model of this size.
