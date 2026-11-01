---
id: deepseek/deepseek-chat-v3.1
name: DeepSeek V3.1
owned_by: deepseek
type: llm
description: DeepSeek V3.1 is DeepSeek's first hybrid thinking/non-thinking model (671B MoE, 37B active, MIT, 128K context), released in August 2025 with stronger tool use.
aliases: [deepseek-ai/DeepSeek-V3.1]
context_length: 163840
max_output_tokens: 32768
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
  instruct_type: deepseek-v3.1
open_weights: true
license: MIT
release_date: "2025-08-21"
knowledge_cutoff: "2025-03"
pricing:
  input: 0.25
  output: 0.95
  cache_read: 0.13
benchmarks:
  intelligence_index: 13.5
  omniscience_index: -29.6
  humanitys_last_exam: 14.3
  gpqa_diamond: 77.9
  terminal_bench_hard: 25
  long_context_reasoning: 56.7
  ifbench: 41.5
  tau2_bench: 37.4
  output_tokens_per_second: 119.7
  time_to_first_token_seconds: 3.45
benchmark_variant: DeepSeek V3.1 (Reasoning)
sources:
  - https://openrouter.ai/deepseek/deepseek-chat-v3.1
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v3-1
  - https://huggingface.co/deepseek-ai/DeepSeek-V3.1
  - https://api-docs.deepseek.com/news/news250821
  - https://api-docs.deepseek.com/updates
  - https://ollama.com/library/deepseek-v3.1
retrieved: "2026-10-16"
---

# DeepSeek V3.1

## Overview
DeepSeek V3.1, released on 2025-08-21 under the MIT licence, is the first DeepSeek model with a thinking mode and a non-thinking mode in one checkpoint, switched by the chat template (`<think>` versus `</think>` prefix). It is a 671B-parameter MoE with 37B active and a 128K context, post-trained on V3.1-Base, which extended V3 with 840B tokens of long-context training; weights and activations use the UE8M0 FP8 scale format. On the vendor API `deepseek-chat` was its non-thinking mode and `deepseek-reasoner` its thinking mode until V3.1 Terminus replaced it on 2025-09-22; both ids were retired on 2026-07-24, so the model is now served only by third parties such as OpenRouter or from the weights. Ollama's `deepseek-v3.1` default tag carries Terminus; the original checkpoint is only in the `671b-q8_0` and `671b-fp16` tags. Superseded by `deepseek/deepseek-v3.1-terminus`.

## Strengths
- Thinking mode: DeepSeek reports MMLU-Pro 84.8, GPQA Diamond 80.1, LiveCodeBench 74.8 and AIME 2025 88.4, with faster answers than R1 0528.
- Non-thinking agent mode: SWE-bench Verified 66.0, SWE-bench Multilingual 54.5, Terminal-bench 31.3.
- Artificial Analysis (variant DeepSeek V3.1 (Reasoning)): GPQA Diamond 77.9%, long-context reasoning 56.7%, 119.7 tokens per second.

## Limitations
- Tool calls only in non-thinking mode; search agents use a separate thinking-mode format.
- Users reported Chinese-English mixing and stray characters, fixed in Terminus.
- AA Intelligence Index 13.5, tau2-bench 37.4%, 3.45 s to first token, Omniscience Index -29.6.
- Self-hosting: load `mlp.gate.e_score_correction_bias` in FP32 and keep UE8M0 FP8 scales; OpenRouter output limit 32,768 tokens.

## Good for
- One deployment covering fast chat and deliberate reasoning.
- Code and search agents built on the V3.1 tool format.
- Anthropic-format clients, which the vendor API began supporting with this release.
