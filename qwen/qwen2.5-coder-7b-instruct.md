---
id: qwen/qwen2.5-coder-7b-instruct
name: Qwen2.5 Coder 7B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 Coder 7B Instruct is the 7.61B-parameter instruction-tuned code model of Qwen's September 2024 Qwen2.5-Coder series, open-weight under Apache-2.0 and covering 92 programming languages.
aliases: [Qwen/Qwen2.5-Coder-7B-Instruct, Qwen/Qwen2.5-Coder-7B-Instruct-AWQ, Qwen/Qwen2.5-Coder-7B-Instruct-GGUF, Qwen/Qwen2.5-Coder-7B-Instruct-GPTQ-Int4, Qwen/Qwen2.5-Coder-7B-Instruct-GPTQ-Int8, qwen2.5-coder-7b-instruct, "qwen2.5-coder:7b", "qwen2.5-coder:7b-instruct"]
context_length: 32768
capabilities: [tool_calling]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2024-09-19"
benchmarks:
  gpqa_diamond: 33.9
  humanitys_last_exam: 4.9
benchmark_variant: Qwen2.5 Coder Instruct 7B
sources:
  - https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-Coder-7B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct/raw/main/tokenizer_config.json
  - https://artificialanalysis.ai/models/qwen2-5-coder-7b-instruct
  - https://qwenlm.github.io/blog/qwen2.5-coder/
  - https://qwenlm.github.io/blog/qwen2.5-coder-family/
  - https://ollama.com/library/qwen2.5-coder/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 Coder 7B Instruct

## Overview
Qwen2.5-Coder-7B-Instruct is the instruction-tuned 7B model of Qwen2.5-Coder, the renamed CodeQwen line, announced on 2024-09-19 with 1.5B and 7B sizes (Artificial Analysis gives the same date; the Hugging Face repo was created 2024-09-17); 0.5B, 3B, 14B and 32B sizes followed on 2024-11-12. OpenRouter does not list it; the id follows the Hugging Face repo. Built on Qwen2.5 and trained on 5.5 trillion tokens of source code, text-code grounding and synthetic data, it covers 92 programming languages. The Hugging Face card gives 7.61B parameters (6.53B non-embedding), 28 layers, 28 query and 4 key-value heads, and a full 131,072-token context; config.json is set to 32,768 tokens, which this card uses, with YaRN beyond that. It needs transformers 4.37.0 or newer, and its chat template includes tool calls. Ollama serves it as qwen2.5-coder:7b, also qwen2.5-coder:latest. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-coder-7b-instruct only in the Beijing region, at $0.144 per million input and $0.287 per million output tokens. Artificial Analysis marks it deprecated in favour of Qwen3 8B.

## Strengths
- Qwen says the 7B base model outperforms the larger DeepSeek-Coder-V2-Lite and Codestral-22B on code tasks.
- Qwen reports MATH 66.8, MMLU-Pro 45.6, MMLU 68.7, IFEval 58.6 and GPQA 35.6, each above DeepSeek-Coder-V2-Lite-Instruct.
- Ollama's q4_K_M build is 4.7 GB.
- Artificial Analysis (Qwen2.5 Coder Instruct 7B): GPQA Diamond 33.9%.

## Limitations
- Artificial Analysis Humanity's Last Exam 4.9%; no Artificial Analysis coding, agent or speed figures.
- No reasoning mode and text input only.
- Qwen reports GSM8K 86.7, below DeepSeek-Coder-V2-Lite-Instruct's 87.6, and AIME24 10.0.
- No published knowledge cutoff.

## Good for
- Local code generation, completion and repair on one consumer GPU.
- Editor assistants where latency matters.
- Fine-tuning a small code model.
