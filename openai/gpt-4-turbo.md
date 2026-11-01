---
id: openai/gpt-4-turbo
name: GPT-4 Turbo
owned_by: openai
type: llm
description: GPT-4 Turbo is OpenAI's 128K-context GPT-4 line with vision, shut down on OpenAI's API on 2026-10-23 and listed by OpenRouter only as a batch endpoint.
aliases: [gpt-4-turbo, gpt-4-turbo-2024-04-09, gpt-4-turbo-completions, "openai/gpt-4-turbo:batch", gpt-4-turbo-preview, gpt-4-0125-preview, gpt-4-1106-preview, azure/gpt-4-turbo, azure/gpt-4-turbo-2024-04-09, azure/gpt-4-1106-preview, azure/gpt-4-0125-preview]
context_length: 128000
max_output_tokens: 4096
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2023-11-06"
knowledge_cutoff: "2023-12"
pricing:
  input: 5
  output: 15
benchmarks:
  coding_index: 21.5
  humanitys_last_exam: 3.1
  output_tokens_per_second: 138.7
  time_to_first_token_seconds: 1.73
benchmark_variant: GPT-4 Turbo
sources:
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-4-turbo
  - https://developers.openai.com/api/docs/models/gpt-4-turbo
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4 Turbo

## Overview
GPT-4 Turbo is OpenAI's 128K-context GPT-4 line, which OpenAI describes as designed to be a cheaper, better version of GPT-4. It was first released as a preview on 2023-11-06 (Artificial Analysis date); the generally available snapshot `gpt-4-turbo-2024-04-09` let vision requests use JSON mode and function calling, per OpenRouter. It takes text and images and returns text, with a 128,000-token context window, 4,096 max output tokens and a December 2023 knowledge cutoff (Artificial Analysis gives April 2023). OpenRouter lists only the batch endpoint, `openai/gpt-4-turbo:batch`, so the frontmatter price of $5 input and $15 output per million tokens is the batch rate, the same as OpenAI's batch price; OpenAI's standard price was $10 and $30. OpenAI lists it as Shut down: announced 2026-04-22, it left the API on 2026-10-23 with `gpt-5.6-sol` as the recommended replacement. The preview snapshots were retired separately: `gpt-4-0125-preview` and `gpt-4-turbo-preview` on 2026-03-26 (replacement GPT-5 or GPT-4.1), and `gpt-4-1106-preview` on 2026-10-23. The vision preview, `gpt-4-vision-preview`, has its own card. Azure deployed it as model `gpt-4` version `turbo-2024-04-09`, its replacement for the `vision-preview`, `1106-Preview` and `0125-Preview` versions.

## Strengths
- Artificial Analysis measured about 139 output tokens per second with a 1.73-second time to first token.
- Function calling, JSON mode and image input on the 2024-04-09 snapshot.
- OpenRouter reports a Coding Index of 21.5.

## Limitations
- Shut down on OpenAI's API; only the OpenRouter batch endpoint remained on 2026-11-01.
- 4,096 max output tokens, and OpenAI's page does not list structured outputs.
- 3.1% on Humanity's Last Exam; Artificial Analysis publishes no other current scores for it.
- No fine-tuning and no cached-input price.

## Good for
- Reproducing results from 2024 systems that were built on it.
- Batch jobs through providers that still route to it.
