---
id: openai/gpt-4.1
name: GPT-4.1
owned_by: openai
type: llm
description: GPT-4.1 is OpenAI's non-reasoning flagship of April 2025 with a 1M-token context window and text and image input, deprecated for removal from OpenAI's API on 2027-01-14.
aliases: [gpt-4.1, gpt-4.1-2025-04-14, "openai/gpt-4.1:batch", azure/gpt-4.1, azure/gpt-4.1-2025-04-14]
context_length: 1047576
max_output_tokens: 32768
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [max_completion_tokens, max_tokens, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [image, text, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-04-14"
knowledge_cutoff: "2024-06"
pricing:
  input: 2
  output: 8
  cache_read: 0.5
benchmarks:
  gpqa_diamond: 66.6
  humanitys_last_exam: 4.2
  ifbench: 43.0
  long_context_reasoning: 68.3
  mmmu_pro: 61.2
  output_tokens_per_second: 165.1
  tau2_bench: 47.1
  terminal_bench_hard: 13.6
  time_to_first_token_seconds: 0.97
benchmark_variant: GPT-4.1
sources:
  - https://openrouter.ai/openai/gpt-4.1
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-4-1
  - https://developers.openai.com/api/docs/models/gpt-4.1
  - https://developers.openai.com/api/docs/deprecations
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4.1

## Overview
GPT-4.1 is the flagship of OpenAI's GPT-4.1 series, released on 2025-04-14 (Artificial Analysis date; pinned snapshot `gpt-4.1-2025-04-14`). OpenAI calls it its smartest non-reasoning model: low latency, no reasoning step. It takes text and images and returns text, with a 1,047,576-token context window, 32,768 max output tokens and a June 2024 knowledge cutoff (OpenRouter gives 2024-06-30, Artificial Analysis 2024-05-31). OpenAI serves it on Chat Completions, Responses, Batch and Fine-tuning, with function calling, structured outputs, predicted outputs, prompt caching and image input. OpenAI marks it Deprecated: announced 2026-10-14, it leaves the API on 2027-01-14 with `gpt-6-luna` as the recommended replacement, and fine-tuned versions follow the same date. Its model page suggests GPT-5 for complex tasks, and Artificial Analysis lists GPT-5 as its successor.

## Strengths
- OpenRouter describes it as built for instruction following, real-world software engineering and long-context reasoning.
- Artificial Analysis measured 66.6% on GPQA Diamond, 68.3% on AA-LCR, 61.2% on MMMU-Pro and 47.1% on tau2-bench.
- About 165 output tokens per second with a 0.97-second time to first token.
- Cache reads cost $0.50 per million tokens, a quarter of the $2 input price.

## Limitations
- No reasoning step: 4.2% on Humanity's Last Exam and 13.6% on Terminal-Bench Hard.
- Deprecated, with removal from OpenAI's API on 2027-01-14.
- Knowledge stops at June 2024.
- Closed weights, API access only.

## Good for
- Latency-sensitive tasks that do not need reasoning, the use OpenAI's deprecation notes name for GPT-4.1.
- Answering over very long documents within the 1M-token window.
- Existing fine-tuned deployments until the January 2027 shutdown.
