---
id: openai/gpt-6.1-terra
name: GPT-6.1 Terra
owned_by: openai
type: llm
description: GPT-6.1 Terra is the mid-tier model of OpenAI's GPT-6.1 series, released in October 2026 below GPT-6.1 Sol and built for visual reasoning, precise computer use and clear writing.
aliases: [gpt-6.1-terra, openai/gpt-6.1-terra-20261026, "openai/gpt-6.1-terra:batch", openai.gpt-6.1-terra, us.openai.gpt-6.1-terra, global.openai.gpt-6.1-terra, azure/gpt-6.1-terra]
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
release_date: "2026-10-26"
knowledge_cutoff: "2026-06"
pricing:
  input: 1
  output: 5
  cache_read: 0.05
  cache_write: 1.25
benchmarks:
  humanitys_last_exam: 46.2
  intelligence_index: 51.0
  long_context_reasoning: 82.7
  mmmu_pro: 84.7
  omniscience_index: 29.6
  output_tokens_per_second: 97.2
  scicode: 55.1
  terminal_bench_4: 55.6
  time_to_first_token_seconds: 274.62
benchmark_variant: GPT-6.1 Terra (Max)
sources:
  - https://openrouter.ai/openai/gpt-6.1-terra
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-6-1-terra
  - https://artificialanalysis.ai/models/gpt-5-6-terra
  - https://artificialanalysis.ai/models/gpt-6-1-sol
  - https://developers.openai.com/api/docs/models/gpt-6.1-terra
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-1-terra.html
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-6.1 Terra

## Overview
GPT-6.1 Terra is the mid-tier model of OpenAI's GPT-6.1 series, released on October 26, 2026 and priced below GPT-6.1 Sol; GPT-6 Astra (flagship) sits above both and GPT-6 Luna (cheapest) below. OpenAI calls it a fast, efficient model for visual reasoning, precise computer use and clear, natural writing, such as matching product photos to catalogue entries, interpreting technical drawings or acting on application screens. OpenRouter notes particular strength at understanding screenshots and on-screen content. It takes text and image input and returns text, with a 1,050,000-token context window (922,000 input), 128,000 max output tokens and a June 1, 2026 knowledge cutoff. `reasoning.effort` supports none, low, medium (default), high, xhigh and max; pro mode is a Responses API setting (see GPT-6.1 Terra Pro). OpenAI lists only the snapshot `gpt-6.1-terra`; Microsoft Foundry's version is 2026-10-26 and Bedrock's id is `openai.gpt-6.1-terra`. OpenAI gives no retirement date. Artificial Analysis marks GPT-5.6 Terra as superseded by it.

## Strengths
- Artificial Analysis Intelligence Index (v5.0) of 51.0 for GPT-6.1 Terra (Max), with 55.6% on Terminal-Bench 4.0, 84.7% on MMMU-Pro and 82.7% on AA-LCR.
- 1 USD input, 0.05 USD cached input and 5 USD output per million tokens, half GPT-6.1 Sol's rates.
- About 97 output tokens per second at Max.
- Cache writes cost 1.25 USD (30-minute retention) or 2.50 USD (12-hour) per million tokens.

## Limitations
- Time to first token at Max was about 275 seconds.
- AA-Omniscience was 29.6 at Max, against 42.0 for GPT-6.1 Sol (Max).
- Tool calling requires the Responses API.
- Prompts over 272,000 input tokens cost double on input and 1.5 times on output. Closed weights.

## Good for
- Screenshot and image understanding, and computer-use agents.
- Everyday coding, agent and writing work at mid-tier prices.
- Replacing GPT-5.6 Terra.
