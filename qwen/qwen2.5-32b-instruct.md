---
id: qwen/qwen2.5-32b-instruct
name: Qwen2.5 32B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 32B Instruct is the 32.5B-parameter dense instruction-tuned model of Qwen's September 2024 Qwen2.5 series, open-weight under Apache-2.0, with JSON output, tool calling and up to 128K context through YaRN.
aliases: [Qwen/Qwen2.5-32B-Instruct, Qwen/Qwen2.5-32B-Instruct-AWQ, Qwen/Qwen2.5-32B-Instruct-GGUF, Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4, Qwen/Qwen2.5-32B-Instruct-GPTQ-Int8, qwen2.5-32b-instruct, "qwen2.5:32b", "qwen2.5:32b-instruct"]
context_length: 32768
capabilities: [tool_calling, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2024-09-19"
benchmarks:
  gpqa_diamond: 46.6
  humanitys_last_exam: 4.0
benchmark_variant: Qwen2.5 Instruct 32B
sources:
  - https://huggingface.co/Qwen/Qwen2.5-32B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-32B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-32B-Instruct/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen2.5-32b-instruct
  - https://qwenlm.github.io/blog/qwen2.5/
  - https://qwenlm.github.io/blog/qwen2.5-llm/
  - https://ollama.com/library/qwen2.5/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 32B Instruct

## Overview
Qwen2.5-32B-Instruct was announced in the Qwen blog on 2024-09-19 with the Qwen2.5 series, which brought back 14B and 32B sizes and was pretrained on up to 18 trillion tokens (Artificial Analysis gives the same date; the Hugging Face repo was created 2024-09-17). OpenRouter does not list it; the id follows the Hugging Face repo. The Hugging Face card gives 32.5B parameters (31.0B non-embedding), 64 layers, 40 query and 8 key-value heads, and a full 131,072-token context with 8,192 tokens of generation; config.json is set to 32,768 tokens, which this card uses, and YaRN is needed beyond that. It needs transformers 4.37.0 or newer. The blog documents tool calling through vLLM 0.6 or newer (hermes parser), Ollama and transformers. Ollama serves it as qwen2.5:32b. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-32b-instruct in Singapore at $0.70 per million input and $2.80 per million output tokens, with a 131,072-token window. Artificial Analysis marks it deprecated in favour of Qwen3 32B.

## Strengths
- Qwen reports MMLU-Pro 69.0, GPQA 49.5, MATH 83.1, HumanEval 88.4, LiveCodeBench 51.2 and Arena-Hard 74.5, against GPT-4o-mini's 63.1, 40.2, 70.2, 88.4, 40.7 and 74.9.
- The blog says Qwen2.5-32B beats Qwen2-72B in Qwen's evaluations.
- More than 29 languages, generation beyond 8K tokens, table understanding and JSON output.
- Artificial Analysis (Qwen2.5 Instruct 32B): GPQA Diamond 46.6%.

## Limitations
- Artificial Analysis Humanity's Last Exam 4%; no other Artificial Analysis evaluations.
- No reasoning mode and text input only.
- Static YaRN in vLLM can hurt short prompts.
- Qwen reports IFEval strict-prompt 79.5, below GPT-4o-mini's 80.4; Ollama's q4_K_M build is 20 GB.
- No published knowledge cutoff.

## Good for
- Self-hosted multilingual chat, extraction and JSON output.
- Fine-tuning on a mid-sized dense base.
- Pipelines already built on the Qwen2.5 chat template.
