---
id: qwen/qwen-2.5-coder-32b-instruct
name: Qwen2.5 Coder 32B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 Coder 32B Instruct is Alibaba's 32.5B-parameter dense open-weight (Apache-2.0) code model, trained on 5.5 trillion code-related tokens and released in November 2024.
aliases: [Qwen/Qwen2.5-Coder-32B-Instruct, "qwen2.5-coder:32b", "qwen2.5-coder:32b-instruct"]
context_length: 32768
max_output_tokens: 29491
capabilities: []
supported_parameters: [frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, temperature, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
  instruct_type: chatml
open_weights: true
license: Apache-2.0
release_date: "2024-11-12"
knowledge_cutoff: "2024-06"
pricing:
  input: 0.66
  output: 1
benchmarks:
  intelligence_index: 6.7
  humanitys_last_exam: 3.5
  gpqa_diamond: 41.7
benchmark_variant: Qwen2.5 Coder Instruct 32B
sources:
  - https://openrouter.ai/qwen/qwen-2.5-coder-32b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen2-5-coder-32b-instruct
  - https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct
  - https://qwenlm.github.io/blog/qwen2.5-coder-family/
  - https://ollama.com/library/qwen2.5-coder
retrieved: "2026-10-16"
---

# Qwen2.5 Coder 32B Instruct

## Overview
Qwen2.5 Coder 32B Instruct is the largest of the six Qwen2.5-Coder sizes (0.5B to 32B). The Qwen blog announcing the family is dated 2024-11-12, which this card uses; OpenRouter lists 2024-11-11. The Hugging Face card gives 32.5B parameters (31.0B non-embedding), 64 layers, grouped-query attention with 40 query and 8 key-value heads, 5.5 trillion training tokens of source code, text-code grounding and synthetic data, and a full context of 131,072 tokens; config.json ships at 32,768 tokens and YaRN is needed beyond that. OpenRouter lists a 32,768-token context and 29,491 output tokens, and no tool or structured-output parameters, so capabilities are empty here. The weights are Apache 2.0 (the 3B size uses the Qwen Research licence). Ollama serves it as qwen2.5-coder:32b. Qwen3-Coder 480B, Qwen3-Coder 30B and Qwen3-Coder-Next, which have their own cards, supersede it.

## Strengths
- Qwen reports 73.7 on Aider, 65.9 on McEval and 75.2 on MdEval, and describes the model as matching GPT-4o on code generation.
- Qwen reports it kept its mathematics and general capabilities while improving code generation, reasoning and fixing.
- Code completion and fill-in-the-middle support across the Qwen2.5-Coder family.

## Limitations
- Artificial Analysis (Qwen2.5 Coder Instruct 32B): Intelligence Index 6.7, Humanity's Last Exam 3.5%, GPQA Diamond 41.7%; no speed figures were published.
- No tool calling or structured outputs through OpenRouter, and no reasoning mode.
- 32,768-token default context; a dense 32B model needs a 48 GB class GPU or quantisation.
- Knowledge ends in mid 2024.

## Good for
- Code completion, editing and repair in IDE plugins on local hardware.
- Self-hosted coding assistants where Apache 2.0 licensing matters.
- Fine-tuning on private codebases.
