---
id: openai/gpt-5.5
name: GPT-5.5
owned_by: openai
type: llm
description: GPT-5.5 is OpenAI's April 2026 frontier model for complex professional work, succeeding GPT-5.4 and since followed by the GPT-5.6 family, with text and image input and a context window of about 1M tokens.
aliases: [gpt-5.5, gpt-5.5-2026-04-23, openai/gpt-5.5-20260423, "openai/gpt-5.5:batch", openai.gpt-5.5, us.openai.gpt-5.5, global.openai.gpt-5.5, azure/gpt-5.5, azure/gpt-5.5-2026-04-24]
context_length: 1050000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [file, image, text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-04-23"
knowledge_cutoff: "2025-12"
pricing:
  input: 5
  output: 30
  cache_read: 0.5
benchmarks:
  coding_index: 74.9
  agentic_index: 36.4
  gpqa_diamond: 93.5
  humanitys_last_exam: 45.8
  ifbench: 75.9
  long_context_reasoning: 84.3
  mmmu_pro: 79.9
  output_tokens_per_second: 77.4
  scicode: 55.8
  tau2_bench: 93.9
  terminal_bench_4: 14.6
  terminal_bench_hard: 60.6
  time_to_first_token_seconds: 47.55
benchmark_variant: GPT-5.5 (Xhigh)
sources:
  - https://openrouter.ai/openai/gpt-5.5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-5
  - https://artificialanalysis.ai/models/gpt-5-5-instant-06-26
  - https://artificialanalysis.ai/models/gpt-5-6-sol
  - https://developers.openai.com/api/docs/models/gpt-5.5
  - https://developers.openai.com/api/docs/models/chat-latest
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-55.html
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.5

## Overview
GPT-5.5 is a proprietary OpenAI model that, per OpenRouter, builds on GPT-5.4 with stronger reasoning, higher reliability and better token efficiency on hard tasks. It takes text and image input and returns text. OpenAI lists a 1,050,000-token context window, 128,000 max output tokens and a December 1, 2025 knowledge cutoff; OpenRouter and Microsoft cap input at 922,000 tokens. `reasoning.effort` supports none, low, medium (default), high and xhigh. The pinned snapshot is `gpt-5.5-2026-04-23`; OpenAI's changelog dates the API release April 24, 2026. Bedrock serves it as `openai.gpt-5.5` and Microsoft Foundry as version 2026-04-24. GPT-5.5 Pro is the higher-compute sibling. OpenAI gives no retirement date; the GPT-5.6 family (Sol, Terra, Luna) followed in July 2026, and Artificial Analysis marks GPT-5.5 deprecated in favour of GPT-5.6 Sol. Artificial Analysis also tests GPT-5.5 Instant (May and June 2026), a ChatGPT model with no API id; the API reaches ChatGPT's Instant model only through the rolling `chat-latest` alias.

## Strengths
- Artificial Analysis measured GPT-5.5 (Xhigh) at 93.5% on GPQA Diamond, 93.9% on tau2-bench, 84.3% on AA-LCR and 75.9% on IFBench.
- OpenRouter reports an Artificial Analysis Coding Index of 74.9 and Agentic Index of 36.4.
- Time to first token at Xhigh was about 48 seconds.
- Chat Completions, Responses and Batch; function calling, structured outputs, web search, computer use and prompt caching.

## Limitations
- 5 USD input and 30 USD output per million tokens; prompts over 272,000 input tokens cost 10 and 45. Regional processing adds 10%.
- Terminal-Bench 4.0 was 14.6% at Xhigh, against 39.9% for GPT-5.6 Sol (Max).
- Caching works only with extended prompt caching, not in-memory.
- Closed weights.

## Good for
- Existing GPT-5.5 integrations not yet moved to GPT-5.6 or GPT-6.
- Tool-heavy agent workflows, where its tau2-bench result is strong.
- Long-document work under the 272,000-token price threshold.
