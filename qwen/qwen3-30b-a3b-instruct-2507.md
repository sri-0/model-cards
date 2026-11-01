---
id: qwen/qwen3-30b-a3b-instruct-2507
name: Qwen3 30B A3B Instruct 2507
owned_by: qwen
type: llm
description: Qwen3 30B A3B Instruct 2507 is the July 2025 non-thinking update of Qwen's 30.5B-parameter mixture-of-experts model (3.3B active), open-weight under Apache-2.0 with a native 262,144-token context.
aliases: [Qwen/Qwen3-30B-A3B-Instruct-2507, "qwen3:30b-instruct", "qwen3:30b-a3b-instruct-2507-q4_K_M"]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-07-30"
knowledge_cutoff: "2025-06"
pricing:
  input: 0.1
  output: 0.3
benchmarks:
  intelligence_index: 7.5
  omniscience_index: -66.2
  humanitys_last_exam: 6.9
  gpqa_diamond: 65.9
  terminal_bench_hard: 6.1
  long_context_reasoning: 26.3
  ifbench: 33.1
  tau2_bench: 10.2
  output_tokens_per_second: 41.8
  time_to_first_token_seconds: 1.13
benchmark_variant: Qwen3 30B A3B 2507 Instruct
sources:
  - https://openrouter.ai/qwen/qwen3-30b-a3b-instruct-2507
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-30b-a3b-2507
  - https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3
retrieved: "2026-10-16"
---

# Qwen3 30B A3B Instruct 2507

## Overview
Qwen3-30B-A3B-Instruct-2507 is the updated non-thinking version of Qwen3-30B-A3B. The Qwen GitHub README dates the release 2025-07-30 (OpenRouter lists 2025-07-29). The Hugging Face card gives 30.5B total and 3.3B activated parameters (29.9B non-embedding), 48 layers, grouped-query attention with 32 query and 4 key-value heads, 128 experts with 8 active, and a native context of 262,144 tokens; a GitHub note of 2025-08-08 says the 2507 models now handle 1 million token inputs. It only runs in non-thinking mode and never emits think blocks, so enable_thinking is not needed. OpenRouter lists a 262,144-token context, 235,929 output tokens and a June 2025 knowledge cutoff. On Ollama the tags qwen3:30b-instruct and qwen3:30b-a3b-instruct-2507-q4_K_M share one build of this model. The Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Qwen reports MMLU-Pro 78.4, GPQA 70.4, AIME25 61.3, ZebraLogic 90.0, LiveCodeBench v6 43.2, MultiPL-E 83.8, IFEval 84.7 and Arena-Hard v2 69.0, against 69.1, 54.8, 21.6, 33.2, 29.0, 74.6, 83.7 and 24.8 for the original Qwen3-30B-A3B in non-thinking mode.
- Only 3.3B parameters active per token, so it runs on modest hardware.
- Tool calling and structured outputs on OpenRouter at 0.10 USD per million input tokens.

## Limitations
- Artificial Analysis (Qwen3 30B A3B 2507 Instruct): Intelligence Index 7.5, Omniscience -66.2, tau2-bench 10.2%, Terminal-Bench Hard 6.1%, long-context reasoning 26.3%.
- 41.8 output tokens per second and 1.13 s to first token in Artificial Analysis' measurements.
- No thinking mode; the separate Thinking-2507 release covers that.
- Qwen reports Aider-Polyglot 35.6 and TAU2-Telecom 12.3, both below the 235B 2507 model.

## Good for
- Fast general chat, writing and instruction following on a single GPU.
- Long-document reading up to 256K tokens.
- Lightweight tool-calling agents where a thinking model is too slow.
