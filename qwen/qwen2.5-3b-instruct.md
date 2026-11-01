---
id: qwen/qwen2.5-3b-instruct
name: Qwen2.5 3B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 3B Instruct is the 3.09B-parameter dense instruction-tuned model of Qwen's September 2024 Qwen2.5 series, aimed at mobile devices and released under the non-commercial Qwen Research License.
aliases: [Qwen/Qwen2.5-3B-Instruct, Qwen/Qwen2.5-3B-Instruct-AWQ, Qwen/Qwen2.5-3B-Instruct-GGUF, Qwen/Qwen2.5-3B-Instruct-GPTQ-Int4, Qwen/Qwen2.5-3B-Instruct-GPTQ-Int8, qwen2.5-3b-instruct, "qwen2.5:3b", "qwen2.5:3b-instruct"]
context_length: 32768
capabilities: [tool_calling, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Qwen Research License Agreement
release_date: "2024-09-19"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-3B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-3B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/raw/main/tokenizer_config.json
  - https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/blob/main/LICENSE
  - https://qwenlm.github.io/blog/qwen2.5/
  - https://qwenlm.github.io/blog/qwen2.5-llm/
  - https://ollama.com/library/qwen2.5/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 3B Instruct

## Overview
Qwen2.5-3B-Instruct was announced in the Qwen blog on 2024-09-19 as one of three sizes new to the Qwen2.5 series, which Qwen added for mobile applications (the Hugging Face repo was created 2024-09-17). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. The Hugging Face card gives 3.09B parameters (2.77B non-embedding), 36 layers, 16 query and 2 key-value heads, tied embeddings, a full 32,768-token context and 8,192 tokens of generation. Unlike the other Qwen2.5 sizes it uses the Qwen Research License, which allows non-commercial (research or evaluation) use only; commercial users must request a licence. It needs transformers 4.37.0 or newer, and the chat template includes tool calls. Qwen publishes AWQ, GPTQ (Int4, Int8) and GGUF builds. Ollama serves it as qwen2.5:3b (1.9 GB). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-3b-instruct in the Beijing region at $0.044 per million input and $0.130 per million output tokens.

## Strengths
- Qwen reports MATH 65.9, GSM8K 86.7, HumanEval 74.4, MultiPL-E 60.2 and MMLU-Pro 43.7, and says it beats Phi-3.5-mini-Instruct and MiniCPM3-4B on maths and coding with fewer parameters.
- Qwen pitches the 3B size for mobile applications.

## Limitations
- Non-commercial licence.
- Qwen reports IFEval strict-prompt 58.2, below MiniCPM3-4B's 68.4, and LiveCodeBench 19.9, below its 23.8.
- No reasoning mode, text input only and no published knowledge cutoff.

## Good for
- Research and evaluation on mobile-class hardware.
- Maths and coding helpers where a 3B model is enough.
- Fine-tuning studies on a small base.
