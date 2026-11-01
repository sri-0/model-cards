---
id: openai/gpt-6-astra
name: GPT-6 Astra
owned_by: openai
type: llm
description: GPT-6 Astra is the flagship of OpenAI's GPT-6 family, released in September 2026 for the most demanding reasoning, coding, computer-use, research and document work, above the Sol, Terra and Luna tiers.
aliases: [gpt-6-astra, openai/gpt-6-astra-20260903, "openai/gpt-6-astra:batch", openai.gpt-6-astra, us.openai.gpt-6-astra, global.openai.gpt-6-astra, azure/gpt-6-astra, azure/gpt-6-astra-2026-09-03]
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
release_date: "2026-09-03"
knowledge_cutoff: "2026-04"
pricing:
  input: 10
  output: 50
  cache_read: 1
  cache_write: 12.5
benchmarks:
  coding_index: 76.9
  agentic_index: 51
  gpqa_diamond: 96.1
  humanitys_last_exam: 54.7
  intelligence_index: 56.9
  long_context_reasoning: 80.7
  mmmu_pro: 86.9
  omniscience_index: 42.4
  output_tokens_per_second: 78.2
  scicode: 56.5
  terminal_bench_4: 59.1
  time_to_first_token_seconds: 270.03
benchmark_variant: GPT-6 Astra (Max)
sources:
  - https://openrouter.ai/openai/gpt-6-astra
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-6-astra
  - https://developers.openai.com/api/docs/models/gpt-6-astra
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-astra.html
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-6 Astra

## Overview
GPT-6 Astra is the flagship of OpenAI's GPT-6 family, released on September 3, 2026. OpenAI calls it its most capable model, for complex reasoning, coding, computer use, research and document creation. OpenAI's GPT-6 guide ranks the siblings below it: GPT-6.1 Sol (near-Astra performance at lower cost), GPT-6.1 Terra (fast and efficient) and GPT-6 Luna (fastest and cheapest); GPT-6 Sol preceded GPT-6.1 Sol. It takes text and image input and returns text, with a 1,050,000-token context window (922,000 input), 128,000 max output tokens and an April 30, 2026 knowledge cutoff. `reasoning.effort` supports low, medium (default), high, xhigh and max, but not none; pro mode is a Responses API setting (see GPT-6 Astra Pro). OpenAI lists only the snapshot `gpt-6-astra`; Microsoft Foundry's version is 2026-09-03 and Bedrock's id is `openai.gpt-6-astra`. OpenAI gives no retirement date.

## Strengths
- Artificial Analysis Intelligence Index (v5.0) of 56.9 for GPT-6 Astra (Max), with 96.1% on GPQA Diamond, 59.1% on Terminal-Bench 4.0, 86.9% on MMMU-Pro and an AA-Omniscience of 42.4.
- OpenRouter reports an Artificial Analysis Coding Index of 76.9 and Agentic Index of 51.
- OpenAI reports it used fewer output tokens than earlier models in several evaluations.
- Async tool calling, mid-turn steering, and Fast and Ultrafast modes.

## Limitations
- 10 USD input and 50 USD output per million tokens; 20 and 75 above 272,000 input tokens. Ultrafast costs six times standard.
- Time to first token at Max was about 270 seconds; output about 78 tokens per second.
- No custom temperature, top_p or log probabilities; tool calling requires the Responses API.
- Misalignment monitoring can raise alerts or stop a conversation for review. Closed weights.

## Good for
- The hardest end-to-end analysis, research and software engineering.
- Long-horizon agent runs with computer and browser use.
- Document creation and scientific work.
