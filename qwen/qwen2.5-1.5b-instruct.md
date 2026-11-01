---
id: qwen/qwen2.5-1.5b-instruct
name: Qwen2.5 1.5B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 1.5B Instruct is a 1.54B-parameter dense open-weight (Apache-2.0) instruction-tuned model from Qwen's September 2024 Qwen2.5 series, built for edge devices with a 32,768-token context.
aliases: [Qwen/Qwen2.5-1.5B-Instruct, Qwen/Qwen2.5-1.5B-Instruct-AWQ, Qwen/Qwen2.5-1.5B-Instruct-GGUF, Qwen/Qwen2.5-1.5B-Instruct-GPTQ-Int4, Qwen/Qwen2.5-1.5B-Instruct-GPTQ-Int8, qwen2.5-1.5b-instruct, "qwen2.5:1.5b", "qwen2.5:1.5b-instruct"]
context_length: 32768
capabilities: [tool_calling, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2024-09-19"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-1.5B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct/raw/main/tokenizer_config.json
  - https://qwenlm.github.io/blog/qwen2.5/
  - https://qwenlm.github.io/blog/qwen2.5-llm/
  - https://ollama.com/library/qwen2.5/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 1.5B Instruct

## Overview
Qwen2.5-1.5B-Instruct was announced in the Qwen blog on 2024-09-19 with the rest of the Qwen2.5 series, pretrained on up to 18 trillion tokens (the Hugging Face repo was created 2024-09-17). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. The Hugging Face card gives 1.54B parameters (1.31B non-embedding), 28 layers, 12 query and 2 key-value heads, tied embeddings, a full 32,768-token context and 8,192 tokens of generation; config.json confirms 32,768. It needs transformers 4.37.0 or newer, and the chat template includes tool calls. Qwen publishes AWQ, GPTQ (Int4, Int8) and GGUF builds. Ollama serves it as qwen2.5:1.5b (986 MB). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-1.5b-instruct in the Beijing region as free for a limited time.

## Strengths
- Qwen reports MMLU-Pro 32.4, MATH 55.2, GSM8K 73.2, HumanEval 61.6, MBPP 63.2 and IFEval strict-prompt 42.5, against 22.9, 25.3, 61.6, 42.1, 44.2 and 29.0 for Qwen2-1.5B-Instruct.
- The blog positions the 0.5B and 1.5B sizes for edge use in highly resource-constrained environments.
- Apache-2.0, with official quantised builds.

## Limitations
- Qwen reports LiveCodeBench 14.8 and LiveBench 18.8.
- No reasoning mode, text input only and no YaRN extension beyond 32,768 tokens.
- No published knowledge cutoff.

## Good for
- On-device chat, summarisation and extraction.
- Low-latency helpers inside larger pipelines.
- Fine-tuning a small Apache-2.0 base.
