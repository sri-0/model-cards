---
id: openai/gpt-4.1-mini
name: GPT-4.1 Mini
owned_by: openai
type: llm
description: GPT-4.1 mini is the mid-sized model of OpenAI's April 2025 GPT-4.1 series, with a 1M-token context window and image input, deprecated for removal from OpenAI's API on 2027-01-14.
aliases: [gpt-4.1-mini, gpt-4.1-mini-2025-04-14, "openai/gpt-4.1-mini:batch", azure/gpt-4.1-mini, azure/gpt-4.1-mini-2025-04-14]
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
  input: 0.4
  output: 1.6
  cache_read: 0.1
benchmarks:
  coding_index: 20.2
  gpqa_diamond: 66.4
  humanitys_last_exam: 5.0
  ifbench: 38.3
  long_context_reasoning: 44.0
  mmmu_pro: 58.7
  output_tokens_per_second: 161.6
  tau2_bench: 52.9
  terminal_bench_hard: 7.6
  time_to_first_token_seconds: 0.85
benchmark_variant: GPT-4.1 mini
sources:
  - https://openrouter.ai/openai/gpt-4.1-mini
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-4-1-mini
  - https://developers.openai.com/api/docs/models/gpt-4.1-mini
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4.1 Mini

## Overview
GPT-4.1 mini is the mid-sized model of OpenAI's GPT-4.1 series, released on 2025-04-14 (Artificial Analysis date; pinned snapshot `gpt-4.1-mini-2025-04-14`). OpenRouter says it is competitive with GPT-4o at substantially lower latency and cost. It takes text and images and returns text, with a 1,047,576-token context window, 32,768 max output tokens and a June 2024 knowledge cutoff. OpenAI serves it on Chat Completions, Responses, Batch and Fine-tuning, with function calling, structured outputs, predicted outputs, web search and image input, and no reasoning step. OpenAI marks it Deprecated: announced 2026-10-14, it leaves the API on 2027-01-14 with `gpt-6-luna` as the recommended replacement. The model page suggests GPT-5 mini for more complex tasks, and Artificial Analysis lists GPT-5 mini as its successor. Azure retires version 2025-04-14 on 2027-04-14.

## Strengths
- Artificial Analysis measured 66.4% on GPQA Diamond, close to GPT-4.1's 66.6%, plus 58.7% on MMMU-Pro and 52.9% on tau2-bench.
- Coding Index of 20.2, as reported through OpenRouter.
- About 162 output tokens per second with a 0.85-second time to first token.
- $0.40 input and $1.60 output per million tokens, with cache reads at $0.10.

## Limitations
- 44.0% on AA-LCR, against 68.3% for GPT-4.1 with the same 1M window.
- 7.6% on Terminal-Bench Hard and 5.0% on Humanity's Last Exam.
- Deprecated, with removal from OpenAI's API on 2027-01-14.
- Knowledge stops at June 2024.

## Good for
- High-volume, low-latency tasks such as classification, extraction and short answers.
- Image-and-text requests on a budget.
- Existing fine-tuned deployments until the January 2027 shutdown.
