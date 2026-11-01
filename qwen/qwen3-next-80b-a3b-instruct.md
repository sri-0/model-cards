---
id: qwen/qwen3-next-80b-a3b-instruct
name: Qwen3 Next 80B A3B Instruct
owned_by: qwen
type: llm
description: Qwen3 Next 80B A3B Instruct is Qwen's September 2025 open-weight (Apache-2.0) non-thinking model with a hybrid Gated DeltaNet and gated attention architecture, 80B total and 3B active parameters, and a native 262,144-token context extendable to 1,010,000.
aliases: [Qwen/Qwen3-Next-80B-A3B-Instruct, "qwen3-next:80b-a3b-instruct-q4_K_M"]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-09-11"
knowledge_cutoff: "2025-09"
pricing:
  input: 0.1
  output: 1.1
  cache_read: 0.07
benchmarks:
  intelligence_index: 9.6
  omniscience_index: -59.5
  humanitys_last_exam: 7.6
  gpqa_diamond: 73.8
  terminal_bench_hard: 7.6
  long_context_reasoning: 52.7
  ifbench: 39.7
  tau2_bench: 21.6
  output_tokens_per_second: 129.9
  time_to_first_token_seconds: 0.86
benchmark_variant: Qwen3 Next 80B A3B Instruct
sources:
  - https://openrouter.ai/qwen/qwen3-next-80b-a3b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-next-80b-a3b-instruct
  - https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct
  - https://github.com/QwenLM/Qwen3-Next
  - https://ollama.com/library/qwen3-next
retrieved: "2026-10-16"
---

# Qwen3 Next 80B A3B Instruct

## Overview
Qwen3-Next-80B-A3B was released on 2025-09-11 according to the Qwen3-Next GitHub README, as the first model of the Qwen3-Next series. The Hugging Face card describes hybrid attention that replaces standard attention with Gated DeltaNet and gated attention, a high-sparsity mixture of experts, zero-centred weight-decayed layernorm and multi-token prediction. It lists 80B total and 3B activated parameters (79B non-embedding), 48 layers, a hidden size of 2048, pretraining on 15 trillion tokens, and a context of 262,144 tokens natively, extendable to 1,010,000 tokens with YaRN. The Instruct model runs only in non-thinking mode. OpenRouter lists a 262,144-token context, 235,929 output tokens and a September 2025 cutoff. On Ollama the library default is the Thinking build; the Instruct build only has quantisation-specific tags such as qwen3-next:80b-a3b-instruct-q4_K_M. The Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Qwen reports MMLU-Pro 80.6, GPQA 72.9, AIME25 69.5, LiveCodeBench v6 56.6, Arena-Hard v2 82.7 and BFCL-v3 70.3, close to Qwen3-235B-A22B-Instruct-2507 in its table.
- Qwen reports a RULER average of 91.8 across 4K to 1M tokens with YaRN enabled.
- Artificial Analysis (Qwen3 Next 80B A3B Instruct): GPQA Diamond 73.8%, long-context reasoning 52.7%, 129.9 output tokens per second, 0.86 s to first token.
- Tool calling, structured outputs and prompt caching on OpenRouter.

## Limitations
- Artificial Analysis Intelligence Index 9.6, Omniscience -59.5, Terminal-Bench Hard 7.6%, tau2-bench 21.6%, IFBench 39.7%.
- No thinking mode and text input only.
- The hybrid architecture needs recent vLLM or SGLang builds.

## Good for
- Long-context retrieval and summarisation up to 256K tokens and beyond.
- High-throughput chat and tool-calling services.
- Deployments wanting 235B-class answers from 3B active parameters.
