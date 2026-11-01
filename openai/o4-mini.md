---
id: openai/o4-mini
name: o4 Mini
owned_by: openai
type: llm
description: o4-mini is OpenAI's small multimodal reasoning model of April 2025, succeeded by GPT-5 mini, shut down on OpenAI's API on 2026-10-23 and listed by OpenRouter only as a batch endpoint.
aliases: [o4-mini, o4-mini-2025-04-16, "openai/o4-mini:batch", azure/o4-mini, azure/o4-mini-2025-04-16]
context_length: 200000
max_output_tokens: 100000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, response_format, seed, structured_outputs, tool_choice, tools]
architecture:
  input_modalities: [image, text, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-04-16"
knowledge_cutoff: "2024-06"
pricing:
  input: 0.55
  output: 2.2
  cache_read: 0.1375
benchmarks:
  gpqa_diamond: 78.4
  humanitys_last_exam: 16.5
  ifbench: 68.7
  long_context_reasoning: 61.0
  mmmu_pro: 69.2
  output_tokens_per_second: 148.1
  tau2_bench: 55.6
  terminal_bench_hard: 15.2
  time_to_first_token_seconds: 21.91
benchmark_variant: o4-mini (High)
sources:
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/o4-mini
  - https://developers.openai.com/api/docs/models/o4-mini
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# o4 Mini

## Overview
o4-mini is OpenAI's small reasoning model of April 2025, released on 2025-04-16 (Artificial Analysis date; pinned snapshot `o4-mini-2025-04-16`). OpenAI describes it as optimised for fast, effective reasoning, particularly in coding and visual tasks; OpenRouter calls it a compact o-series model with multimodal and agentic capabilities and marks reasoning as mandatory. OpenRouter lists only the batch endpoint, `openai/o4-mini:batch`, so the frontmatter price of $0.55 input and $2.20 output per million tokens is the batch rate, the same as OpenAI's batch price; OpenAI's standard price was $1.10 and $4.40 with cached input at $0.275. It takes text and images and returns text, with a 200,000-token context window, 100,000 max output tokens and a June 2024 knowledge cutoff. OpenAI served it on Chat Completions, Responses, Batch and Fine-tuning, with streaming, function calling, structured outputs, image input and prompt caching; Azure offers reinforcement fine-tuning for it. OpenAI lists it as Shut down and succeeded by GPT-5 mini: announced 2026-04-22, it left the API on 2026-10-23 with `gpt-5.6-terra` as the recommended replacement. Azure's schedule retires fine-tuned o4-mini deployments on 2027-10-16.

## Strengths
- Artificial Analysis (High effort) measured 78.4% on GPQA Diamond, 69.2% on MMMU-Pro, 68.7% on IFBench and 61.0% on AA-LCR.
- 55.6% on tau2-bench and 16.5% on Humanity's Last Exam, both ahead of o3-mini at High effort.
- About 148 output tokens per second.

## Limitations
- Shut down on OpenAI's API; only the OpenRouter batch endpoint remained on 2026-11-01.
- 21.91-second time to first token at High effort, which includes reasoning.
- 15.2% on Terminal-Bench Hard.
- Knowledge stops at June 2024.

## Good for
- Batch reasoning over text and images at low cost.
- Reproducing results from 2025 agent systems built on it.
