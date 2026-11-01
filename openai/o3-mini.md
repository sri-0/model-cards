---
id: openai/o3-mini
name: o3 Mini
owned_by: openai
type: llm
description: o3-mini is OpenAI's small text-only reasoning model of January 2025, shut down on OpenAI's API on 2026-10-23 and listed by OpenRouter only as a batch endpoint.
aliases: [o3-mini, o3-mini-2025-01-31, "openai/o3-mini:batch", azure/o3-mini, azure/o3-mini-2025-01-31]
context_length: 200000
max_output_tokens: 100000
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools]
architecture:
  input_modalities: [text, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-01-31"
knowledge_cutoff: "2023-10"
pricing:
  input: 0.55
  output: 2.2
  cache_read: 0.275
benchmarks:
  gpqa_diamond: 77.3
  humanitys_last_exam: 12.0
  ifbench: 67.1
  long_context_reasoning: 43.0
  output_tokens_per_second: 237.9
  scicode: 42.8
  tau2_bench: 31.3
  terminal_bench_4: 0
  terminal_bench_hard: 6.1
  time_to_first_token_seconds: 18.19
benchmark_variant: o3-mini (High)
sources:
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/o3-mini
  - https://developers.openai.com/api/docs/models/o3-mini
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# o3 Mini

## Overview
o3-mini is OpenAI's small reasoning model of January 2025, released on 2025-01-31 (Artificial Analysis date; pinned snapshot `o3-mini-2025-01-31`). OpenAI positioned it at the same cost and latency targets as o1-mini, adding structured outputs, function calling and Batch API support. OpenRouter describes it as a cost-efficient model for STEM reasoning with a `reasoning_effort` parameter. OpenRouter lists only the batch endpoint, `openai/o3-mini:batch`, so the frontmatter price of $0.55 input and $2.20 output per million tokens is the batch rate, the same as OpenAI's batch price; OpenAI's standard price was $1.10 and $4.40 with cached input at $0.55. It is text-only, with a 200,000-token context window, 100,000 max output tokens and an October 2023 knowledge cutoff. OpenAI served it on Chat Completions, Responses, Assistants and Batch, with streaming, function calling, structured outputs and reasoning tokens; no fine-tuning or image input. OpenAI lists it as Shut down: announced 2026-04-22, it left the API on 2026-10-23 with `gpt-5.6-sol` as the recommended replacement; Artificial Analysis names GPT-5 mini as its successor.

## Strengths
- Artificial Analysis (High effort) measured 77.3% on GPQA Diamond, 67.1% on IFBench and 42.8% on SciCode.
- About 238 output tokens per second at High effort.
- Function calling and structured outputs, which o1-mini lacked, at the same price.

## Limitations
- Shut down on OpenAI's API; only the OpenRouter batch endpoint remained on 2026-11-01.
- Weak agentic results: 31.3% on tau2-bench, 6.1% on Terminal-Bench Hard and 0% on Terminal-Bench 4.0.
- 43.0% on AA-LCR despite the 200K window, and an 18.19-second time to first token at High effort.
- Text only, and knowledge stops at October 2023.

## Good for
- Batch STEM reasoning and coding questions where latency does not matter.
- Reproducing results from systems built on it in 2025.
