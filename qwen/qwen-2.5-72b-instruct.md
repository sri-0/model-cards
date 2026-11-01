---
id: qwen/qwen-2.5-72b-instruct
name: Qwen2.5 72B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 72B Instruct is the 72.7B-parameter dense open-weight chat model of Alibaba's September 2024 Qwen2.5 series, released under the Qwen licence rather than Apache 2.0.
aliases: [Qwen/Qwen2.5-72B-Instruct, "qwen2.5:72b", "qwen2.5:72b-instruct"]
context_length: 32768
max_output_tokens: 16384
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
  instruct_type: chatml
open_weights: true
license: Qwen License Agreement
release_date: "2024-09-19"
knowledge_cutoff: "2024-06"
pricing:
  input: 0.36
  output: 0.4
benchmarks:
  intelligence_index: 7.7
  omniscience_index: -53.1
  humanitys_last_exam: 3.6
  gpqa_diamond: 49.1
  terminal_bench_hard: 4.5
  ifbench: 36.9
  tau2_bench: 34.5
  output_tokens_per_second: 30.9
  time_to_first_token_seconds: 3.9
benchmark_variant: Qwen2.5 Instruct 72B
sources:
  - https://openrouter.ai/qwen/qwen-2.5-72b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen2-5-72b-instruct
  - https://huggingface.co/Qwen/Qwen2.5-72B-Instruct
  - https://qwenlm.github.io/blog/qwen2.5/
  - https://ollama.com/library/qwen2.5
retrieved: "2026-10-16"
---

# Qwen2.5 72B Instruct

## Overview
Qwen2.5 72B Instruct was announced in the Qwen blog on 2024-09-19 as the largest model of the Qwen2.5 series, pretrained on up to 18 trillion tokens. The Hugging Face card lists 72.7B parameters (70.0B non-embedding), 80 layers, grouped-query attention with 64 query and 8 key-value heads, and a full context of 131,072 tokens with 8,192 tokens of generation. The shipped config.json is set to 32,768 tokens; longer inputs need YaRN rope scaling, which vLLM applies statically. OpenRouter lists a 32,768-token context, 16,384 output tokens and a June 2024 knowledge cutoff. Unlike the other sizes except 3B, the 72B weights use the Qwen licence, not Apache 2.0. Ollama serves it as qwen2.5:72b. Qwen3 and the Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Qwen reports more knowledge and better coding and mathematics than Qwen2, plus improved instruction following, long text generation over 8K tokens, table understanding and JSON output.
- Supports more than 29 languages, including Chinese, English, French, Spanish, German, Japanese, Korean, Arabic and Vietnamese.
- Tool calling and structured outputs on OpenRouter.
- Artificial Analysis (Qwen2.5 Instruct 72B): GPQA Diamond 49.1%, IFBench 36.9%, tau2-bench 34.5%.

## Limitations
- Artificial Analysis Intelligence Index 7.7, Omniscience -53.1, Humanity's Last Exam 3.6% and Terminal-Bench Hard 4.5%.
- 30.9 output tokens per second and 3.9 s to first token in Artificial Analysis' measurements.
- No reasoning mode, text input only, and the Qwen licence carries conditions Apache 2.0 does not.
- A dense 72B model needs several GPUs or heavy quantisation to self-host.

## Good for
- Existing deployments built on the Qwen2.5 series.
- Multilingual chat and structured JSON extraction from text.
- Fine-tuning where the Qwen licence is acceptable.
