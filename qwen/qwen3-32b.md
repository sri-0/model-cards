---
id: qwen/qwen3-32b
name: Qwen3 32B
owned_by: qwen
type: llm
description: Qwen3 32B is a 32.8B-parameter dense open-weight (Apache-2.0) model from the April 2025 Qwen3 series that switches between a thinking mode and a non-thinking mode in one model.
aliases: [Qwen/Qwen3-32B, "qwen3:32b"]
context_length: 131072
max_output_tokens: 16384
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_a, top_k, top_logprobs, top_p]
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
  input: 0.08
  output: 0.28
benchmarks:
  intelligence_index: 7.2
  omniscience_index: -50.4
  humanitys_last_exam: 7.4
  gpqa_diamond: 66.8
  scicode: 36
  terminal_bench_hard: 3
  terminal_bench_4: 0
  long_context_reasoning: 0
  ifbench: 36.3
  tau2_bench: 29.8
  output_tokens_per_second: 27.4
  time_to_first_token_seconds: 1.61
benchmark_variant: Qwen3 32B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3-32b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-32b-instruct
  - https://huggingface.co/Qwen/Qwen3-32B
  - https://qwenlm.github.io/blog/qwen3/
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3
retrieved: "2026-10-16"
---

# Qwen3 32B

## Overview
Qwen3-32B is the largest dense model of the Qwen3 series, which the Qwen blog and GitHub README date 2025-04-29 (OpenRouter lists 2025-04-28). The Hugging Face card gives 32.8B parameters (31.2B non-embedding), 64 layers, grouped-query attention with 64 query and 8 key-value heads, and a context of 32,768 tokens natively and 131,072 tokens with YaRN; OpenRouter lists the extended 131,072 tokens with 16,384 output tokens. Qwen advises enabling YaRN only when prompts exceed 32,768 tokens. Thinking is on by default, switchable with enable_thinking or the /think and /no_think prompt tags. Serving needs transformers 4.51.0, sglang 0.4.6.post1 or vllm 0.8.5 or newer. Ollama serves it as qwen3:32b. No 2507 update exists for this size; the Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Qwen says thinking mode surpasses QwQ and non-thinking mode surpasses Qwen2.5 Instruct on mathematics, code and commonsense reasoning; the blog's figures are images, so none are quoted.
- Artificial Analysis (Qwen3 32B (Reasoning)): GPQA Diamond 66.8%, SciCode 36%, Humanity's Last Exam 7.4%, IFBench 36.3%.
- Tool calling, reasoning and structured outputs on OpenRouter at 0.08 USD per million input tokens.
- Supports more than 100 languages and dialects.

## Limitations
- Artificial Analysis Intelligence Index 7.2, Omniscience -50.4, tau2-bench 29.8%, Terminal-Bench Hard 3%, Terminal-Bench 4.0 0% and long-context reasoning 0%.
- 27.4 output tokens per second and 1.61 s to first token in Artificial Analysis' measurements.
- A dense 32B model needs a 48 GB class GPU or quantisation.

## Good for
- Self-hosted reasoning assistants where a dense model is preferred over MoE.
- Multilingual chat and translation.
- Tool-calling agents with Qwen-Agent.
