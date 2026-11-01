---
id: minimax/minimax-m3.1-flash
name: MiniMax M3.1 Flash
owned_by: minimax
type: llm
description: MiniMax-M3.1-Flash is MiniMax's current open-weight multimodal mixture-of-experts model (about 428B total, 23B active parameters) for agentic coding, computer use and cybersecurity work, with a 1M-token context window and tunable reasoning effort.
aliases: [MiniMax-M3.1-Flash, MiniMax-M3.1-Flash-Preview, minimax/minimax-m3.1-flash-20261019, MiniMaxAI/MiniMax-M3.1-Flash, "minimax-m3.1-flash:cloud"]
context_length: 1048576
max_output_tokens: 524288
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MiniMax Community License
release_date: "2026-10-19"
pricing:
  input: 0.075
  output: 0.3
  cache_read: 0.0075
benchmarks:
  humanitys_last_exam: 48.0
  intelligence_index: 28.9
  long_context_reasoning: 79.7
  mmmu_pro: 79.1
  omniscience_index: -6.4
  output_tokens_per_second: 118.9
  scicode: 53.4
  terminal_bench_4: 25.8
  time_to_first_token_seconds: 1.28
benchmark_variant: MiniMax-M3.1-Flash
sources:
  - https://openrouter.ai/minimax/minimax-m3.1-flash
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/minimax-m3-1-flash
  - https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-M3.1-Flash
  - https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash/raw/main/config.json
  - https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash/raw/main/LICENSE
  - https://www.minimax.io/blog/minimax-m31f
  - https://platform.minimax.io/docs/faq/models.md
  - https://platform.minimax.io/docs/guides/text-generation.md
  - https://platform.minimax.io/docs/guides/text-m3-function-call.md
  - https://platform.minimax.io/docs/api-reference/text-anthropic-api.md
  - https://platform.minimax.io/docs/m-plan/intro.md
  - https://platform.minimax.io/docs/pricing/overview.md
  - https://platform.minimax.io/docs/release-notes/models.md
  - https://ollama.com/library/minimax-m3.1-flash
retrieved: "2026-11-01"
---

# MiniMax M3.1 Flash

## Overview
MiniMax-M3.1-Flash was released on 2026-10-19 (MiniMax release notes, blog and Artificial Analysis). The Hugging Face card describes a native multimodal mixture-of-experts model with about 428B total and 23B activated parameters and a 1M-token context. It keeps M3's architecture but swaps its first three full-attention layers for sparse attention, adds quantisation-aware training and ships a DSpark speculative-decoding draft head. The API id is `MiniMax-M3.1-Flash`; requests to the retired `MiniMax-M3.1-Flash-Preview` name are served by it. Thinking is always on and `reasoning_effort` accepts low, medium, high, xhigh and max (default max). Weights are on Hugging Face under the MiniMax Community License (repo created 2026-10-17).

## Strengths
- Artificial Analysis Intelligence Index v5 of 28.9 (MiniMax-M3.1-Flash), with 48.0% on Humanity's Last Exam, 79.1% on MMMU-Pro and 79.7% on AA-LCR.
- Fast: 118.9 output tokens per second and 1.28 s to first token on AA.
- MiniMax reports 73.7% on DeepSWE v1.1, 61.7 on OSWorld 2.0, 76.2 on BankerToolBench and 82.2 on CyberGym.
- MiniMax's API charges a flat $0.15 input, $0.60 output and $0.015 cached input per million tokens; interleaved thinking between tool calls.

## Limitations
- Thinking cannot be disabled: `thinking: disabled` or `effort: none` returns HTTP 400 on MiniMax's API.
- 25.8% on Terminal-Bench 4.0 on AA (MiniMax reports 38.1 with a Codex harness) and an Omniscience Index of -6.4.
- Commercial use requires a "Built with MiniMax M3.1-Flash" notice, a one-time notice to MiniMax, and written authorisation above US$20 million yearly revenue.
- OpenRouter charges half price from 15:00 to 01:00 UTC ($0.075 input, $0.30 output, $0.0075 cache read, as in the frontmatter) and MiniMax's list price from 01:00 to 15:00 UTC.

## Good for
- Agentic coding and terminal work on a budget.
- Computer-use and browser agents with screenshot or video input.
- Long-context work.
- Replacing MiniMax-M2.5 and M2.7, which MiniMax retires on 2026-11-18.
