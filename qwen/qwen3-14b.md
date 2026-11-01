---
id: qwen/qwen3-14b
name: Qwen3 14B
owned_by: qwen
type: llm
description: Qwen3 14B is a 14.8B-parameter dense open-weight (Apache-2.0) model from the April 2025 Qwen3 series that switches between a thinking mode and a non-thinking mode in one model.
aliases: [Qwen/Qwen3-14B, "qwen3:14b"]
context_length: 40960
max_output_tokens: 16384
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
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
  output: 0.24
benchmarks:
  intelligence_index: 6.4
  omniscience_index: -49
  humanitys_last_exam: 4.5
  gpqa_diamond: 60.4
  scicode: 30.7
  terminal_bench_hard: 3.8
  terminal_bench_4: 0
  long_context_reasoning: 0
  ifbench: 40.5
  tau2_bench: 34.5
  output_tokens_per_second: 27
  time_to_first_token_seconds: 0.92
benchmark_variant: Qwen3 14B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3-14b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-14b-instruct
  - https://huggingface.co/Qwen/Qwen3-14B
  - https://qwenlm.github.io/blog/qwen3/
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3
retrieved: "2026-10-16"
---

# Qwen3 14B

## Overview
Qwen3-14B was released with the Qwen3 series, which the Qwen blog and GitHub README date 2025-04-29 (OpenRouter lists 2025-04-28). The Hugging Face card gives 14.8B parameters (13.2B non-embedding), 40 layers, grouped-query attention with 40 query and 8 key-value heads, and a context of 32,768 tokens natively and 131,072 tokens with YaRN. Its config.json sets max_position_embeddings to 40,960, reserving 32,768 tokens for output and 8,192 for prompts, and OpenRouter's context_length is that same 40,960 with 16,384 output tokens, so the two sources describe the native window and the YaRN extension respectively. Thinking is on by default and can be disabled with enable_thinking or the /no_think prompt tag. Serving needs transformers 4.51.0, sglang 0.4.6.post1 or vllm 0.8.5 or newer. Ollama serves it as qwen3:14b. No 2507 update exists for this size; the Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Qwen says thinking mode surpasses QwQ and non-thinking mode surpasses Qwen2.5 Instruct on mathematics, code and commonsense reasoning; the blog's figures are images, so none are quoted.
- Artificial Analysis (Qwen3 14B (Reasoning)): GPQA Diamond 60.4%, IFBench 40.5%, tau2-bench 34.5%, SciCode 30.7%, 0.92 s to first token.
- Tool calling, reasoning and structured outputs on OpenRouter at 0.12 USD per million input tokens.
- Supports more than 100 languages and dialects.

## Limitations
- Artificial Analysis Intelligence Index 6.4, Omniscience -49, Humanity's Last Exam 4.5%, Terminal-Bench Hard 3.8%, Terminal-Bench 4.0 0% and long-context reasoning 0%.
- 27 output tokens per second in Artificial Analysis' measurements.
- 32,768-token native context.

## Good for
- Local reasoning and chat on a single GPU.
- Multilingual assistants with switchable thinking.
- Agent prototypes with Qwen-Agent and MCP tools.
