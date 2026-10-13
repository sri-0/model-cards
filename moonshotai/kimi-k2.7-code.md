---
id: moonshotai/kimi-k2.7-code
name: Kimi K2.7 Code
owned_by: moonshotai
type: llm
description: Kimi K2.7 Code is Moonshot AI's coding-focused open-weight model in the Kimi K2 family, a 1T-parameter mixture-of-experts that always runs in thinking mode.
aliases: [kimi-k2.7-code, moonshot/kimi-k2.7-code, moonshotai/Kimi-K2.7-Code]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, parallel_tool_calls, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Modified MIT
release_date: "2026-06-12"
pricing:
  input: 0.6712
  output: 3.35
  cache_read: 0.18
benchmarks:
  intelligence_index: 25.8
  coding_index: 60.8
  agentic_index: 21
  omniscience_index: -10.2
  humanitys_last_exam: 35
  gpqa_diamond: 89.6
  scicode: 47.8
  terminal_bench_hard: 44.7
  terminal_bench_4: 1
  long_context_reasoning: 79.3
  ifbench: 63.1
  tau2_bench: 90.1
  output_tokens_per_second: 74.8
  time_to_first_token_seconds: 2.77
benchmark_variant: Kimi K2.7 Code
sources:
  - https://openrouter.ai/moonshotai/kimi-k2.7-code
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/kimi-k2-7-code
  - https://huggingface.co/moonshotai/Kimi-K2.7-Code
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Kimi K2.7 Code

## Overview
Kimi K2.7 Code was released in June 2026 and is built on Kimi K2.6. It is a mixture-of-experts model with about 1T total and 32B activated parameters, a 256K-token context window and text and image input. OpenRouter notes that it always operates in thinking mode and keeps full reasoning content across multi-turn conversations. Weights are on Hugging Face (moonshotai/Kimi-K2.7-Code) under a modified MIT licence, with the same native INT4 quantization as Kimi K2 Thinking.

## Strengths
- Moonshot reports about 30% fewer thinking tokens than Kimi K2.6, with gains on long-horizon coding tasks.
- Artificial Analysis Intelligence Index 25.8 and Coding Index 60.8 (variant: Kimi K2.7 Code).
- Tool use: tau2-bench 90.1% and Terminal-Bench Hard 44.7% on the same variant.
- Artificial Analysis rates it faster than average (74.8 output tokens per second, 2.77 s to first token) and fairly concise.

## Limitations
- No non-thinking mode, so every request pays for reasoning tokens.
- AA-Omniscience index is negative (-10.2), which points to weak factual recall. Verify facts against sources.
- Terminal-Bench 4.0 score is 1% on Artificial Analysis.
- Artificial Analysis rates it somewhat expensive compared with open-weight models of similar size.
- 1T total parameters make self-hosting demanding.

## Good for
- Coding agents that edit, test and debug across many files.
- Agentic task decomposition and multi-turn coding sessions.
- Code work that uses screenshots or UI images as input.
- Self-hosted coding assistants where a modified MIT licence is acceptable.
