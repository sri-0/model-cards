---
id: openai/gpt-4o
name: GPT-4o
owned_by: openai
type: llm
description: GPT-4o is OpenAI's multimodal flagship of 2024 in three API snapshots, the first shut down in October 2026 and the other two deprecated for removal from OpenAI's API on 2027-01-14.
aliases: [gpt-4o, gpt-4o-2024-05-13, gpt-4o-2024-08-06, gpt-4o-2024-11-20, openai/gpt-4o-2024-05-13, openai/gpt-4o-2024-08-06, openai/gpt-4o-2024-11-20, "openai/gpt-4o:batch", azure/gpt-4o, azure/gpt-4o-2024-05-13, azure/gpt-4o-2024-08-06, azure/gpt-4o-2024-11-20]
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
release_date: "2024-05-13"
knowledge_cutoff: "2023-10"
pricing:
  input: 2.5
  output: 10
  cache_read: 1.25
benchmarks:
  gpqa_diamond: 54.3
  humanitys_last_exam: 2.4
  ifbench: 34.3
  long_context_reasoning: 49.3
  output_tokens_per_second: 165.0
  tau2_bench: 25.1
  terminal_bench_hard: 8.3
  time_to_first_token_seconds: 1.04
benchmark_variant: "GPT-4o (Nov '24)"
sources:
  - https://openrouter.ai/openai/gpt-4o
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-4o
  - https://artificialanalysis.ai/models/gpt-4o-2024-05-13
  - https://developers.openai.com/api/docs/models/gpt-4o
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirements
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o

## Overview
GPT-4o ("o" for "omni") is the model OpenAI's page calls its versatile, high-intelligence flagship, first released on 2024-05-13 (Artificial Analysis date for the first snapshot). It takes text and images and returns text, with a 128,000-token context window, 16,384 max output tokens and an October 2023 knowledge cutoff. Three snapshots share this card. `gpt-4o-2024-05-13`, the launch version, had 4,096 max output tokens and costs $5 input and $15 output per million tokens on OpenRouter; OpenAI shut it down on 2026-10-23 (substitute `gpt-5.6-sol`). `gpt-4o-2024-08-06`, the default snapshot and the one OpenAI prices for fine-tuning, added structured outputs with a JSON schema in `response_format` and costs $2.50 and $10, with cache reads at $1.25. `gpt-4o-2024-11-20` improved creative writing and work with uploaded files, per OpenRouter. OpenAI's page lists Chat Completions, Responses, Batch and Fine-tuning, with function calling, predicted outputs and image input. The 2024-08-06 and 2024-11-20 snapshots were deprecated on 2026-10-14 and leave the API on 2027-01-14 (replacement `gpt-6-luna`). Azure retires version 2024-05-13 on 2027-01-14 and the later two on 2027-04-14.

## Strengths
- Artificial Analysis measured the Nov '24 snapshot at 54.3% on GPQA Diamond and 49.3% on AA-LCR, with about 165 output tokens per second and a 1.04-second time to first token.
- OpenRouter says it keeps GPT-4 Turbo's intelligence level.
- Function calling, structured outputs and prompt caching on the current snapshots.

## Limitations
- Deprecated, with removal from OpenAI's API on 2027-01-14.
- Weak agentic results for the Nov '24 snapshot: 25.1% on tau2-bench and 8.3% on Terminal-Bench Hard; 2.4% on Humanity's Last Exam.
- Knowledge stops at October 2023, and the window is 128K tokens.

## Good for
- Existing GPT-4o integrations and fine-tunes that must keep running until January 2027.
- General chat and image understanding where a newer model is not yet approved.
