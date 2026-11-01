---
id: openai/gpt-4o-mini
name: GPT-4o-mini
owned_by: openai
type: llm
description: GPT-4o mini is OpenAI's small multimodal model of July 2024 and its recommended replacement for GPT-3.5 Turbo, deprecated for removal from OpenAI's API on 2027-01-14.
aliases: [gpt-4o-mini, gpt-4o-mini-2024-07-18, openai/gpt-4o-mini-2024-07-18, "openai/gpt-4o-mini:batch", azure/gpt-4o-mini, azure/gpt-4o-mini-2024-07-18]
context_length: 128000
max_output_tokens: 16384
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_completion_tokens, max_tokens, prediction, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p, web_search_options]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2024-07-18"
knowledge_cutoff: "2023-10"
pricing:
  input: 0.15
  output: 0.6
  cache_read: 0.075
benchmarks:
  coding_index: 11.4
  gpqa_diamond: 42.6
  humanitys_last_exam: 4.2
  ifbench: 31.0
  mmmu_pro: 41.5
  output_tokens_per_second: 107.2
  time_to_first_token_seconds: 1.19
benchmark_variant: GPT-4o mini
sources:
  - https://openrouter.ai/openai/gpt-4o-mini
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-4o-mini
  - https://developers.openai.com/api/docs/models/gpt-4o-mini
  - https://developers.openai.com/api/docs/models/gpt-3.5-turbo
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o-mini

## Overview
GPT-4o mini is OpenAI's small multimodal model, released on 2024-07-18 (Artificial Analysis date; pinned snapshot `gpt-4o-mini-2024-07-18`). OpenAI describes it as a fast, affordable model for focused tasks, well suited to fine-tuning and to distilling outputs from a larger model such as GPT-4o; OpenRouter calls it OpenAI's most advanced small model at its release. It takes text and images and returns text, with a 128,000-token context window, 16,384 max output tokens and an October 2023 knowledge cutoff. OpenAI serves it on Chat Completions, Responses, Batch and Fine-tuning, with function calling, structured outputs, predicted outputs, web search and image input. From July 2024 OpenAI recommended it in place of GPT-3.5 Turbo. OpenAI now marks it Deprecated: announced 2026-10-14, it leaves the API on 2027-01-14 with `gpt-6-luna` as the recommended replacement; Artificial Analysis lists GPT-5 mini as its successor. Azure retires version 2024-07-18 on 2027-04-14.

## Strengths
- $0.15 input and $0.60 output per million tokens, with cache reads at $0.075 (half that on the OpenRouter batch endpoint).
- Artificial Analysis measured 42.6% on GPQA Diamond and 41.5% on MMMU-Pro; OpenRouter reports a Coding Index of 11.4.
- About 107 output tokens per second with a 1.19-second time to first token.

## Limitations
- Deprecated, with removal from OpenAI's API on 2027-01-14.
- 4.2% on Humanity's Last Exam and 31.0% on IFBench; Artificial Analysis publishes no agentic or long-context results for it.
- OpenAI now limits new fine-tuning jobs to organisations already using fine-tuning, and ends them for everyone on 2027-01-06.
- Knowledge stops at October 2023.

## Good for
- Cheap, high-volume chat, summarisation and extraction.
- Image-and-text requests where GPT-4o costs too much.
- Existing fine-tuned deployments until the January 2027 shutdown.
