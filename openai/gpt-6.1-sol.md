---
id: openai/gpt-6.1-sol
name: GPT-6.1 Sol
owned_by: openai
type: llm
description: GPT-6.1 Sol is OpenAI's September 2026 upgrade to GPT-6 Sol, offering near-Astra performance for complex coding, computer use and professional work at a fifth of GPT-6 Astra's per-token price.
aliases: [gpt-6.1-sol, openai/gpt-6.1-sol-20260929, "openai/gpt-6.1-sol:batch", openai.gpt-6.1-sol, us.openai.gpt-6.1-sol, global.openai.gpt-6.1-sol, azure/gpt-6.1-sol, azure/gpt-6.1-sol-2026-09-29]
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
release_date: "2026-09-29"
knowledge_cutoff: "2026-04"
pricing:
  input: 2
  output: 10
  cache_read: 0.1
  cache_write: 2.5
benchmarks:
  humanitys_last_exam: 52.9
  intelligence_index: 54.5
  long_context_reasoning: 83.0
  mmmu_pro: 86.0
  omniscience_index: 42.0
  output_tokens_per_second: 79.3
  scicode: 54.2
  terminal_bench_4: 56.1
  time_to_first_token_seconds: 315.06
benchmark_variant: GPT-6.1 Sol (Max)
sources:
  - https://openrouter.ai/openai/gpt-6.1-sol
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-6-1-sol
  - https://artificialanalysis.ai/models/gpt-6-astra
  - https://developers.openai.com/api/docs/models/gpt-6.1-sol
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-sol.html
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-6.1 Sol

## Overview
GPT-6.1 Sol is OpenAI's upgrade to GPT-6 Sol, released on September 29, 2026. OpenAI's GPT-6 guide places it below the flagship GPT-6 Astra as near-Astra performance for complex coding, computer use and professional work at lower cost, with GPT-6.1 Terra (fast and efficient) and GPT-6 Luna (cheapest) below it. OpenRouter says it makes fewer factual errors than GPT-6 Sol and better respects explicit restrictions and user intent in agent tasks. It takes text and image input and returns text, with a 1,050,000-token context window (922,000 input), 128,000 max output tokens and an April 30, 2026 knowledge cutoff. `reasoning.effort` supports low, medium (default), high, xhigh and max, but not none; pro mode is a Responses API setting (see GPT-6.1 Sol Pro). Multi-agent delegation is in beta, and Ultrafast mode arrived on October 8, 2026. OpenAI lists only the snapshot `gpt-6.1-sol`; Microsoft Foundry's version is 2026-09-29 and Bedrock's id is `openai.gpt-6.1-sol` (Bedrock lists a 1M context and 131,072 output tokens). OpenAI gives no retirement date.

## Strengths
- Artificial Analysis Intelligence Index (v5.0) of 54.5 for GPT-6.1 Sol (Max), against 56.9 for GPT-6 Astra (Max); 56.1% on Terminal-Bench 4.0, 86.0% on MMMU-Pro and an AA-Omniscience of 42.0.
- 2 USD input and 10 USD output per million tokens; cached input costs 5% of the input rate.
- Function calling, structured outputs, web search, computer use and prompt caching.

## Limitations
- Time to first token at Max was about 315 seconds; output about 79 tokens per second.
- Tool calling requires the Responses API; no custom temperature, top_p or log probabilities.
- Prompts over 272,000 input tokens cost 4 and 15 USD per million; Ultrafast costs six times standard. Closed weights.

## Good for
- Agentic coding, computer use and document-heavy professional work.
- Near-Astra results without Astra's price.
- Upgrading GPT-6 Sol deployments.
