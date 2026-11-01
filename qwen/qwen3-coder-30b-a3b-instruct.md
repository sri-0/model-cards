---
id: qwen/qwen3-coder-30b-a3b-instruct
name: Qwen3 Coder 30B A3B Instruct
owned_by: qwen
type: llm
description: Qwen3 Coder 30B A3B Instruct is Qwen's July 2025 open-weight (Apache-2.0) mixture-of-experts coding model with 30.5B total and 3.3B active parameters, a native 262,144-token context and non-thinking output.
aliases: [Qwen/Qwen3-Coder-30B-A3B-Instruct, "qwen3-coder:30b"]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, max_tokens, response_format, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-07-31"
knowledge_cutoff: "2025-06"
pricing:
  input: 0.07
  output: 0.28
benchmarks:
  intelligence_index: 9.6
  omniscience_index: -50.7
  humanitys_last_exam: 3.8
  gpqa_diamond: 51.6
  terminal_bench_hard: 15.2
  long_context_reasoning: 32.7
  ifbench: 32.7
  tau2_bench: 34.5
  output_tokens_per_second: 155.9
  time_to_first_token_seconds: 1.02
benchmark_variant: Qwen3 Coder 30B A3B Instruct
sources:
  - https://openrouter.ai/qwen/qwen3-coder-30b-a3b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-coder-30b-a3b-instruct
  - https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct
  - https://qwenlm.github.io/blog/qwen3-coder/
  - https://ollama.com/library/qwen3-coder
retrieved: "2026-10-16"
---

# Qwen3 Coder 30B A3B Instruct

## Overview
Qwen3-Coder-30B-A3B-Instruct is the smaller Qwen3-Coder release; its Hugging Face repository was created on 2025-07-31, the date OpenRouter also lists. The Hugging Face card gives 30.5B total and 3.3B activated parameters, 48 layers, grouped-query attention with 32 query and 4 key-value heads, 128 experts with 8 active, and a native context of 262,144 tokens, extendable to 1M tokens with YaRN. It runs only in non-thinking mode and uses the Qwen3-Coder function-call format supported by Qwen Code and Cline. Qwen recommends temperature 0.7, top_p 0.8, top_k 20, repetition penalty 1.05 and 65,536 output tokens. OpenRouter lists a 262,144-token context, 235,929 output tokens and a June 2025 cutoff. Ollama serves it as qwen3-coder:30b, the library default. Qwen3-Coder-Next and the Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Artificial Analysis (Qwen3 Coder 30B A3B Instruct): Terminal-Bench Hard 15.2%, tau2-bench 34.5%, long-context reasoning 32.7%, GPQA Diamond 51.6%.
- 155.9 output tokens per second in Artificial Analysis' measurements, the fastest of the Qwen3 coder cards.
- 3.3B active parameters, so it runs locally on one GPU, and costs 0.07 USD input and 0.28 USD output per million tokens on OpenRouter.
- Tool calling and structured outputs on OpenRouter.

## Limitations
- Artificial Analysis Intelligence Index 9.6, Omniscience -50.7, Humanity's Last Exam 3.8% and IFBench 32.7%.
- No thinking mode and text input only.
- Neither the Hugging Face card nor the blog publishes benchmark figures in text for this size.
- OpenRouter exposes a reduced parameter set (no seed, logit_bias or presence_penalty).

## Good for
- Local coding agents and IDE assistants on consumer hardware.
- Repository-scale understanding with 256K context.
- Function-calling pipelines that need fast, cheap completions.
