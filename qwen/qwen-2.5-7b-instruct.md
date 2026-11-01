---
id: qwen/qwen-2.5-7b-instruct
name: Qwen2.5 7B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 7B Instruct is the 7.61B-parameter dense open-weight (Apache-2.0) chat model of Alibaba's September 2024 Qwen2.5 series, sized for a single GPU.
aliases: [Qwen/Qwen2.5-7B-Instruct, "qwen2.5:7b", "qwen2.5:7b-instruct"]
context_length: 32768
max_output_tokens: 29491
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
  instruct_type: chatml
open_weights: true
license: Apache-2.0
release_date: "2024-09-19"
knowledge_cutoff: "2024-06"
pricing:
  input: 0.1
  output: 0.2
sources:
  - https://openrouter.ai/qwen/qwen-2.5-7b-instruct
  - https://openrouter.ai/api/v1/models
  - https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
  - https://qwenlm.github.io/blog/qwen2.5/
  - https://ollama.com/library/qwen2.5
retrieved: "2026-10-16"
---

# Qwen2.5 7B Instruct

## Overview
Qwen2.5 7B Instruct was announced in the Qwen blog on 2024-09-19 alongside the rest of the Qwen2.5 series, which was pretrained on up to 18 trillion tokens. The Hugging Face card lists 7.61B parameters (6.53B non-embedding), 28 layers, grouped-query attention with 28 query and 4 key-value heads, and a full context of 131,072 tokens with 8,192 tokens of generation; the shipped config.json is set to 32,768 tokens and YaRN rope scaling is needed beyond that. OpenRouter lists a 32,768-token context, 29,491 output tokens and a June 2024 knowledge cutoff, and the OpenRouter page was created on 2024-10-16. The weights are Apache 2.0 and need transformers 4.37.0 or newer. Ollama serves it as qwen2.5:7b. The card carries no Artificial Analysis figures. Qwen3 and the Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Qwen reports gains over Qwen2 in knowledge, coding and mathematics, instruction following, long text generation over 8K tokens, table understanding and JSON output.
- Supports more than 29 languages, including Chinese, English, French, Spanish, German, Japanese, Korean, Arabic and Vietnamese.
- Tool calling and structured outputs on OpenRouter, at 0.10 USD per million input tokens.
- Small enough to run on one consumer GPU.

## Limitations
- No reasoning mode and text input only.
- Default context is 32,768 tokens unless YaRN is enabled, which vLLM applies statically and can hurt short prompts.
- No independent benchmark figures are recorded on this card.
- Knowledge ends in mid 2024.

## Good for
- Low-cost multilingual chat and extraction on modest hardware.
- Fine-tuning experiments on a 7B base.
- Pipelines already built on the Qwen2.5 chat template.
