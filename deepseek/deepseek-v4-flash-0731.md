---
id: deepseek/deepseek-v4-flash-0731
name: DeepSeek V4 Flash 0731
owned_by: deepseek
type: llm
description: DeepSeek V4 Flash 0731 is the July 2026 official release of DeepSeek V4 Flash (284B MoE, 13B active, MIT, 1M context), re-post-trained for agentic coding with DSpark speculative decoding.
aliases: [deepseek-ai/DeepSeek-V4-Flash-0731, deepseek-v4-flash, "~deepseek/deepseek-v4-flash-latest"]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, parallel_tool_calls, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_a, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
open_weights: true
license: MIT
release_date: "2026-07-31"
pricing:
  input: 0.016
  output: 0.64
  cache_read: 0.016
benchmarks:
  intelligence_index: 34.3
  coding_index: 69.1
  agentic_index: 41
  omniscience_index: -14.3
  humanitys_last_exam: 38.6
  gpqa_diamond: 90.8
  scicode: 50.3
  terminal_bench_4: 12.1
  long_context_reasoning: 79.7
  output_tokens_per_second: 173.7
  time_to_first_token_seconds: 1.16
benchmark_variant: DeepSeek V4 Flash 0731 (Max)
sources:
  - https://openrouter.ai/deepseek/deepseek-v4-flash-0731
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v4-flash
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731
  - https://api-docs.deepseek.com/updates
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://openrouter.ai/~deepseek/deepseek-v4-flash-latest
retrieved: "2026-10-16"
---

# DeepSeek V4 Flash 0731

## Overview
DeepSeek V4 Flash 0731, released 2026-07-31 under the MIT licence, is the official release of V4 Flash: the same 284B-parameter MoE (13B active, 1M context) as the April preview, re-post-trained only, with a DSpark speculative-decoding module attached to the checkpoint. The `reasoning_effort` parameter gained low, high and max levels. On the vendor API the id `deepseek-v4-flash` served it from 2026-07-31 (public beta, with native Responses API support) until 2026-09-10, when DeepSeek retired V4 Flash and began routing that legacy id to V4.1 Flash. The model remains available from the weights and on OpenRouter, whose versions page lists 0731 as current and whose router id `~deepseek/deepseek-v4-flash-latest` ("always redirects to the latest model in the DeepSeek V4 Flash family") currently resolves to it. An experimental vision variant, `deepseek/deepseek-v4-flash-vision-exp`, builds on it. Superseded by `deepseek/deepseek-v4.1-flash`.

## Strengths
- DeepSeek reports large agent gains over the preview: Terminal Bench 2.1 82.7 (from 61.8), NL2Repo 54.2, DeepSWE 54.4, Toolathlon-Verified 70.3, Cybergym 76.7, ahead of the V4 Pro preview.
- Artificial Analysis (variant DeepSeek V4 Flash 0731 (Max)): Coding Index 69.1, Agentic Index 41, GPQA Diamond 90.8%, long-context reasoning 79.7%, 173.7 tokens per second.
- OpenRouter price $0.016 input and $0.64 output per million tokens.

## Limitations
- Terminal-Bench 4.0 12.1% and HLE 38.6% in AA's tests; Omniscience Index -14.3.
- Retired from the vendor API; `deepseek-v4-flash` now returns V4.1 Flash.
- Self-hosting: DeepSeek's recipes target a single 4x GB300 node with vLLM (`--speculative-config` method `dspark`) or SGLang (`--speculative-algorithm DSPARK`); recommended maximum output 384K tokens for high and max effort, temperature 1.0 and top_p 0.95 for agents; no Jinja template.

## Good for
- Coding, terminal and tool-use agents at low cost.
- 1M-token context analysis.
- Claude Code, OpenCode and Codex-style harnesses.
