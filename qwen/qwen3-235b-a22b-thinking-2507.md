---
id: qwen/qwen3-235b-a22b-thinking-2507
name: Qwen3 235B A22B Thinking 2507
owned_by: qwen
type: llm
description: Qwen3 235B A22B Thinking 2507 is the July 2025 thinking-only update of Qwen's 235B-parameter mixture-of-experts model (22B active), open-weight under Apache-2.0 with a native 262,144-token context.
aliases: [Qwen/Qwen3-235B-A22B-Thinking-2507, qwen3-235b-a22b-thinking-2507, "qwen3:235b-thinking", "qwen3:235b-a22b-thinking-2507-q4_K_M"]
context_length: 128000
max_output_tokens: 16384
capabilities: [tool_calling, reasoning]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, stop, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen3
  instruct_type: qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-07-25"
knowledge_cutoff: "2025-06"
pricing:
  input: 0.45
  output: 3.5
benchmarks:
  intelligence_index: 12.7
  coding_index: 22.1
  agentic_index: 1.3
  omniscience_index: -46.5
  humanitys_last_exam: 15.9
  gpqa_diamond: 79
  scicode: 41.4
  terminal_bench_hard: 13.6
  terminal_bench_4: 0
  long_context_reasoning: 72
  ifbench: 51.2
  tau2_bench: 53.2
  output_tokens_per_second: 65.4
  time_to_first_token_seconds: 0.8
benchmark_variant: Qwen3 235B A22B 2507 (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3-235b-a22b-thinking-2507
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-235b-a22b-instruct-2507-reasoning
  - https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507
  - https://github.com/QwenLM/Qwen3
  - https://ollama.com/library/qwen3
retrieved: "2026-10-16"
---

# Qwen3 235B A22B Thinking 2507

## Overview
Qwen3-235B-A22B-Thinking-2507 is the updated thinking-mode version of Qwen3-235B-A22B, released on 2025-07-25 according to the Qwen GitHub README. The Hugging Face card gives 235B total and 22B activated parameters, 94 layers, 128 experts with 8 active, and a native context of 262,144 tokens; OpenRouter lists 128,000 tokens, 16,384 output tokens and a June 2025 cutoff. It supports only thinking mode: the chat template inserts the opening think tag itself, so outputs contain only the closing tag, and Qwen says this version thinks longer than its predecessor and recommends it for hard problems, using 81,920 output tokens for its reasoning and coding benchmarks. The Hugging Face card's Qwen-Agent example uses the Model Studio id qwen3-235b-a22b-thinking-2507. On Ollama, qwen3:235b-thinking is this model, and qwen3:235b and qwen3:235b-a22b currently resolve to the same build. The Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Qwen reports AIME25 92.3, HMMT25 83.9, LiveCodeBench v6 74.1, CFEval 2134, GPQA 81.1, SuperGPQA 64.9 and MMLU-Pro 84.4.
- Qwen reports IFEval 87.8, Arena-Hard v2 79.7, WritingBench 88.3, BFCL-v3 71.9, TAU2-Retail 71.9, MultiIF 80.6 and PolyMATH 60.1.
- Artificial Analysis (Qwen3 235B A22B 2507 (Reasoning)): GPQA Diamond 79%, long-context reasoning 72%, tau2-bench 53.2%, IFBench 51.2%, Humanity's Last Exam 15.9%, 65.4 output tokens per second.

## Limitations
- Artificial Analysis Intelligence Index 12.7, Coding Index 22.1, Agentic Index 1.3, Terminal-Bench 4.0 0% and Omniscience -46.5.
- Long thinking traces raise latency and cost; OpenRouter output costs 3.50 USD per million tokens.
- No structured-output parameter on OpenRouter, and OpenRouter's 128,000-token context is below the native 262,144.
- 235B total parameters need a multi-GPU node to self-host.

## Good for
- Mathematics, science and competitive-programming problems that reward long reasoning.
- Agentic workflows that need tool calls inside a reasoning loop.
- Benchmarking open reasoning models.
