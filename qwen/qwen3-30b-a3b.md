---
id: qwen/qwen3-30b-a3b
name: Qwen3 30B A3B
owned_by: qwen
type: llm
description: Qwen3 30B A3B is the April 2025 Qwen3 mixture-of-experts model with 30.5B total and 3.3B active parameters, open-weight under Apache-2.0, switching between thinking and non-thinking modes in one model.
aliases: [Qwen/Qwen3-30B-A3B]
context_length: 40960
max_output_tokens: 16384
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen3
  instruct_type: qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-04-29"
knowledge_cutoff: "2025-03"
pricing:
  input: 0.12
  output: 0.5
benchmarks:
  intelligence_index: 7.6
  omniscience_index: -51.5
  humanitys_last_exam: 6.2
  gpqa_diamond: 61.6
  terminal_bench_hard: 2.3
  long_context_reasoning: 0
  ifbench: 41.5
  tau2_bench: 26
  output_tokens_per_second: 112.9
  time_to_first_token_seconds: 0.59
benchmark_variant: Qwen3 30B A3B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3-30b-a3b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-30b-a3b-instruct
  - https://huggingface.co/Qwen/Qwen3-30B-A3B
  - https://qwenlm.github.io/blog/qwen3/
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3
retrieved: "2026-10-16"
---

# Qwen3 30B A3B

## Overview
Qwen3-30B-A3B is the smaller of the two Qwen3 mixture-of-experts models, released with the series on 2025-04-29 according to the Qwen blog and GitHub README (OpenRouter lists 2025-04-28). The Hugging Face card gives 30.5B total and 3.3B activated parameters, 48 layers, grouped-query attention with 32 query and 4 key-value heads, 128 experts with 8 active, and a context of 32,768 tokens natively and 131,072 tokens with YaRN. Its config.json sets max_position_embeddings to 40,960 (32,768 for output plus 8,192 for prompts), and OpenRouter's context_length is that same 40,960 with 16,384 output tokens; the two sources describe the native window and the YaRN extension respectively. Thinking is on by default and switchable with enable_thinking or the /no_think tag. On Ollama the tag qwen3:30b-a3b now resolves to the same build as qwen3:30b-a3b-thinking-2507-q4_K_M, so no Ollama alias is listed. Qwen3-30B-A3B-Instruct-2507 (own card) and Thinking-2507, released on 2025-07-30 and 2025-07-31, replace its two modes, and the Qwen3.5 to Qwen3.8 generations supersede it.

## Strengths
- Qwen says thinking mode surpasses QwQ and non-thinking mode surpasses Qwen2.5 Instruct on mathematics, code and commonsense reasoning; the blog's figures are images, so none are quoted.
- Artificial Analysis (Qwen3 30B A3B (Reasoning)): 112.9 output tokens per second and 0.59 s to first token, with GPQA Diamond 61.6% and IFBench 41.5%.
- 3.3B active parameters, so it runs on one GPU.
- Tool calling, reasoning and structured outputs on OpenRouter.

## Limitations
- Artificial Analysis Intelligence Index 7.6, Omniscience -51.5, Humanity's Last Exam 6.2%, tau2-bench 26%, Terminal-Bench Hard 2.3% and long-context reasoning 0%.
- Superseded by the 2507 releases, which Qwen reports as stronger on the benchmarks it lists.
- 32,768-token native context.

## Good for
- Fast local reasoning on modest hardware.
- Multilingual chat with switchable thinking.
- Pipelines pinned to the original Qwen3 chat template.
