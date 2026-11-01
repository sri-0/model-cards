---
id: qwen/qwen2.5-0.5b-instruct
name: Qwen2.5 0.5B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 0.5B Instruct is the smallest instruction-tuned model of Qwen's September 2024 Qwen2.5 series, a 0.49B-parameter dense open-weight (Apache-2.0) model for edge devices with a 32,768-token context.
aliases: [Qwen/Qwen2.5-0.5B-Instruct, Qwen/Qwen2.5-0.5B-Instruct-AWQ, Qwen/Qwen2.5-0.5B-Instruct-GGUF, Qwen/Qwen2.5-0.5B-Instruct-GPTQ-Int4, Qwen/Qwen2.5-0.5B-Instruct-GPTQ-Int8, qwen2.5-0.5b-instruct, "qwen2.5:0.5b", "qwen2.5:0.5b-instruct"]
context_length: 32768
capabilities: [tool_calling, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2024-09-19"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-0.5B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/raw/main/tokenizer_config.json
  - https://qwenlm.github.io/blog/qwen2.5/
  - https://qwenlm.github.io/blog/qwen2.5-llm/
  - https://ollama.com/library/qwen2.5/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 0.5B Instruct

## Overview
Qwen2.5-0.5B-Instruct was announced in the Qwen blog on 2024-09-19 with the rest of the Qwen2.5 series, pretrained on up to 18 trillion tokens (the Hugging Face repo was created 2024-09-16). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. The Hugging Face card gives 0.49B parameters (0.36B non-embedding), 24 layers, 14 query and 2 key-value heads, tied embeddings, a full 32,768-token context and 8,192 tokens of generation; config.json confirms 32,768. It needs transformers 4.37.0 or newer, and the chat template includes tool calls. Qwen publishes AWQ, GPTQ (Int4, Int8) and GGUF builds. Ollama serves it as qwen2.5:0.5b (398 MB). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-0.5b-instruct in the Beijing region as free for a limited time.

## Strengths
- Qwen reports MMLU-Pro 15.0, MATH 34.4, GSM8K 49.6, HumanEval 35.4, MBPP 49.6 and IFEval strict-prompt 27.9, against 14.4, 13.9, 40.1, 31.1, 39.7 and 14.6 for Qwen2-0.5B-Instruct.
- The blog positions the 0.5B and 1.5B sizes for edge use in highly resource-constrained environments.
- Apache-2.0, with official quantised builds.

## Limitations
- Weak absolute scores: LiveCodeBench 5.1 and LiveBench 12.6 in Qwen's table.
- No reasoning mode, text input only and no YaRN extension beyond 32,768 tokens.
- No published knowledge cutoff.

## Good for
- On-device classification, extraction and short replies.
- Draft models and fine-tuning experiments.
- Tests of the Qwen2.5 chat and tool-call template.
