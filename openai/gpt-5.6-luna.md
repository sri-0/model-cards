---
id: openai/gpt-5.6-luna
name: GPT-5.6 Luna
owned_by: openai
type: llm
description: GPT-5.6 Luna is the fast, low-cost tier of OpenAI's July 2026 GPT-5.6 family, below Sol and Terra and roughly the nano tier of earlier GPT-5 families; GPT-6 Luna has since succeeded it.
aliases: [gpt-5.6-luna, openai/gpt-5.6-luna-20260709, "openai/gpt-5.6-luna:batch", openai.gpt-5.6-luna, us.openai.gpt-5.6-luna, global.openai.gpt-5.6-luna, in.openai.gpt-5.6-luna, azure/gpt-5.6-luna, azure/gpt-5.6-luna-2026-07-09]
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
release_date: "2026-07-09"
knowledge_cutoff: "2026-02"
pricing:
  input: 0.2
  output: 1.2
  cache_read: 0.02
  cache_write: 0.25
benchmarks:
  coding_index: 71.4
  agentic_index: 42.1
  gpqa_diamond: 91.1
  humanitys_last_exam: 39.5
  long_context_reasoning: 83.7
  mmmu_pro: 78.6
  output_tokens_per_second: 118.9
  scicode: 53.6
  terminal_bench_4: 11.6
  time_to_first_token_seconds: 103.45
benchmark_variant: GPT-5.6 Luna (Max)
sources:
  - https://openrouter.ai/openai/gpt-5.6-luna
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-6-luna
  - https://artificialanalysis.ai/models/gpt-5-6-sol
  - https://developers.openai.com/api/docs/models/gpt-5.6-luna
  - https://developers.openai.com/api/docs/guides/latest-model/gpt-5.6
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-56-luna.html
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.6 Luna

## Overview
GPT-5.6 Luna is the cheapest tier of OpenAI's GPT-5.6 family, released on July 9, 2026 with GPT-5.6 Sol (flagship) and GPT-5.6 Terra (balanced). OpenAI designed it for cost-sensitive, high-volume workloads and says it roughly matches the nano tier of earlier GPT-5 families; OpenRouter suits it to chat, classification and lightweight agent work. It takes text and image input and returns text, with a 1,050,000-token context window (922,000 input), 128,000 max output tokens and a February 16, 2026 knowledge cutoff. `reasoning.effort` supports none, low, medium (default), high, xhigh and max; pro mode is a Responses API setting (see GPT-5.6 Luna Pro). OpenAI lists only the snapshot `gpt-5.6-luna`; Microsoft Foundry's version is 2026-07-09 and Bedrock's id is `openai.gpt-5.6-luna`. OpenAI gives no retirement date and names it the replacement for GPT-5 nano (shutting down December 11, 2026) and GPT-4.1 nano. Artificial Analysis marks it deprecated in favour of GPT-6 Luna, released September 22, 2026.

## Strengths
- 0.20 USD input and 1.20 USD output per million tokens after an 80% price cut on July 30, 2026.
- Artificial Analysis measured GPT-5.6 Luna (Max) at 91.1% on GPQA Diamond, 83.7% on AA-LCR and about 119 output tokens per second.
- OpenRouter reports an Artificial Analysis Coding Index of 71.4 and Agentic Index of 42.1.
- Chat Completions, Responses and Batch; function calling, structured outputs, web search and prompt caching.

## Limitations
- Terminal-Bench 4.0 was 11.6% at Max, against 39.9% for GPT-5.6 Sol (Max).
- Time to first token at Max was about 103 seconds, as it includes reasoning.
- Prompts over 272,000 input tokens cost double on input and 1.5 times on output. Closed weights.

## Good for
- High-volume chat, classification and routing where cost per token matters most.
- Lightweight agent steps and summarisation.
- GPT-5.6 deployments not yet moved to GPT-6 Luna.
