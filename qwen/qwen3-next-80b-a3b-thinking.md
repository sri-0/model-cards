---
id: qwen/qwen3-next-80b-a3b-thinking
name: Qwen3 Next 80B A3B Thinking
owned_by: qwen
type: llm
description: Qwen3 Next 80B A3B Thinking is the thinking-only variant of Qwen's September 2025 hybrid Gated DeltaNet and MoE model, open-weight under Apache-2.0 with 80B total and 3B active parameters and a native 262,144-token context.
aliases: [Qwen/Qwen3-Next-80B-A3B-Thinking, "qwen3-next:80b-a3b-thinking"]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-09-11"
knowledge_cutoff: "2025-09"
pricing:
  input: 0.15
  output: 1.2
benchmarks:
  intelligence_index: 11.2
  coding_index: 17.4
  omniscience_index: -51.4
  humanitys_last_exam: 12.6
  gpqa_diamond: 75.9
  terminal_bench_hard: 9.8
  long_context_reasoning: 63.7
  ifbench: 60.7
  tau2_bench: 41.5
  output_tokens_per_second: 163.4
  time_to_first_token_seconds: 0.69
benchmark_variant: Qwen3 Next 80B A3B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3-next-80b-a3b-thinking
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-next-80b-a3b-reasoning
  - https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking
  - https://github.com/QwenLM/Qwen3-Next
  - https://ollama.com/library/qwen3-next
retrieved: "2026-10-16"
---

# Qwen3 Next 80B A3B Thinking

## Overview
Qwen3-Next-80B-A3B-Thinking shares the architecture of the Instruct model released on 2025-09-11: hybrid Gated DeltaNet and gated attention, a high-sparsity mixture of experts, multi-token prediction, 80B total and 3B activated parameters, 48 layers, 15 trillion pretraining tokens and a native 262,144-token context extendable to 1,010,000 tokens with YaRN. It supports only thinking mode; the chat template inserts the opening think tag, so outputs contain only the closing tag. Qwen used GSPO to stabilise reinforcement learning on the hybrid architecture, warns that it thinks longer than its predecessor, and recommends 32,768 output tokens normally and 81,920 for competition problems. OpenRouter lists a 262,144-token context, 235,929 output tokens, a September 2025 cutoff, and tool calling, reasoning and structured outputs. Ollama serves it as qwen3-next:80b-a3b-thinking, the library default. The Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Qwen reports AIME25 87.8, HMMT25 73.9, LiveCodeBench v6 68.7, CFEval 2071, GPQA 77.2 and SuperGPQA 60.8, ahead of Gemini-2.5-Flash Thinking on most of these in its table.
- Qwen reports IFEval 88.9, BFCL-v3 72.0, TAU2-Retail 67.8, MultiIF 77.8 and PolyMATH 56.3.
- Artificial Analysis (Qwen3 Next 80B A3B (Reasoning)): IFBench 60.7%, long-context reasoning 63.7%, GPQA Diamond 75.9%, 163.4 output tokens per second, 0.69 s to first token.

## Limitations
- Artificial Analysis Intelligence Index 11.2, Coding Index 17.4, Omniscience -51.4, Terminal-Bench Hard 9.8%, tau2-bench 41.5%.
- Long thinking traces add latency and tokens; OpenRouter output costs 1.20 USD per million tokens.
- Qwen reports Arena-Hard v2 62.3, well below the 235B Thinking 2507 model's 79.7.
- Needs recent vLLM or SGLang builds for the hybrid layers.

## Good for
- Mathematics, logic and coding problems that benefit from visible reasoning.
- Agent frameworks that need tool calls inside reasoning loops.
- Long-context reasoning over large documents.
