---
id: qwen/qwen2.5-14b-instruct
name: Qwen2.5 14B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 14B Instruct is the 14.7B-parameter dense instruction-tuned model of Qwen's September 2024 Qwen2.5 series, open-weight under Apache-2.0, with JSON output, tool calling and up to 128K context through YaRN.
aliases: [Qwen/Qwen2.5-14B-Instruct, Qwen/Qwen2.5-14B-Instruct-AWQ, Qwen/Qwen2.5-14B-Instruct-GGUF, Qwen/Qwen2.5-14B-Instruct-GPTQ-Int4, Qwen/Qwen2.5-14B-Instruct-GPTQ-Int8, qwen2.5-14b-instruct, "qwen2.5:14b", "qwen2.5:14b-instruct"]
context_length: 32768
capabilities: [tool_calling, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2024-09-19"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-14B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-14B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-14B-Instruct/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen2.5-14B-Instruct/raw/main/tokenizer_config.json
  - https://qwenlm.github.io/blog/qwen2.5/
  - https://qwenlm.github.io/blog/qwen2.5-llm/
  - https://ollama.com/library/qwen2.5/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 14B Instruct

## Overview
Qwen2.5-14B-Instruct was announced in the Qwen blog on 2024-09-19 with the Qwen2.5 series, which brought back 14B and 32B sizes (the Hugging Face repo was created 2024-09-16). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. The Hugging Face card gives 14.7B parameters (13.1B non-embedding), 48 layers, 40 query and 8 key-value heads, and a full 131,072-token context with 8,192 tokens of generation; config.json is set to 32,768 tokens, which this card uses, and YaRN is needed beyond that. It needs transformers 4.37.0 or newer, and the blog documents tool calling through vLLM, Ollama and transformers. Qwen publishes AWQ, GPTQ (Int4, Int8) and GGUF builds; a separate 1M-token version has its own card. Ollama serves it as qwen2.5:14b (9.0 GB). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-14b-instruct in Singapore at $0.35 per million input and $1.40 per million output tokens.

## Strengths
- Qwen reports MMLU-Pro 63.7, GPQA 45.5, MATH 80.0, GSM8K 94.8, HumanEval 83.5, LiveCodeBench 42.6, IFEval 81.0 and Arena-Hard 68.3, against GPT-4o-mini's 63.1, 40.2, 70.2, 93.2, 88.4, 40.7, 80.4 and 74.9.
- The blog says Qwen2.5-14B outperforms Qwen2-57B-A14B.
- Multilingual: IFEval (multilingual) 77.08 and MGSM8K 82.27 in Qwen's table.

## Limitations
- GPT-4o-mini leads it on HumanEval and Arena-Hard in Qwen's table.
- No reasoning mode and text input only; static YaRN in vLLM can hurt short prompts.
- No published knowledge cutoff.

## Good for
- Self-hosted multilingual chat, extraction and JSON output.
- Tool-calling assistants with the Qwen2.5 template.
- Fine-tuning a mid-sized Apache-2.0 base.
