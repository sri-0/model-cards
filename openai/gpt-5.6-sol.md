---
id: openai/gpt-5.6-sol
name: GPT-5.6 Sol
owned_by: openai
type: llm
description: GPT-5.6 Sol is the flagship tier of OpenAI's July 2026 GPT-5.6 family, above Terra and Luna, and the target of the gpt-5.6 alias; GPT-6 Sol has since succeeded it.
aliases: [gpt-5.6-sol, gpt-5.6, openai/gpt-5.6-sol-20260709, "openai/gpt-5.6-sol:batch", openai.gpt-5.6-sol, us.openai.gpt-5.6-sol, global.openai.gpt-5.6-sol, azure/gpt-5.6-sol, azure/gpt-5.6-sol-2026-07-09, gpt-daybreak-blue-latest]
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
  input: 4
  output: 20
  cache_read: 0.4
  cache_write: 5
benchmarks:
  coding_index: 78.3
  agentic_index: 47.4
  gpqa_diamond: 94.1
  humanitys_last_exam: 49.5
  ifbench: 72.7
  long_context_reasoning: 84.0
  mmmu_pro: 83.4
  output_tokens_per_second: 101.9
  scicode: 57.1
  tau2_bench: 85.1
  terminal_bench_4: 39.9
  terminal_bench_hard: 65.9
  time_to_first_token_seconds: 91.59
benchmark_variant: GPT-5.6 Sol (Max)
sources:
  - https://openrouter.ai/openai/gpt-5.6-sol
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-6-sol
  - https://developers.openai.com/api/docs/models/gpt-5.6-sol
  - https://developers.openai.com/api/docs/models/gpt-daybreak-blue-latest
  - https://developers.openai.com/api/docs/guides/latest-model/gpt-5.6
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-56-sol.html
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.6 Sol

## Overview
GPT-5.6 Sol is the flagship of OpenAI's GPT-5.6 family, released on July 9, 2026 with GPT-5.6 Terra (a balance of intelligence and cost) and GPT-5.6 Luna (efficient, high-volume). Sol roughly matches the unsuffixed tier of earlier GPT-5 families, and the `gpt-5.6` alias routes to it. OpenRouter calls it particularly strong at command-line and multi-step coding. It takes text and image input and returns text, with a 1,050,000-token context window (922,000 input), 128,000 max output tokens and a February 16, 2026 knowledge cutoff. `reasoning.effort` supports none, low, medium (default), high, xhigh and max; pro mode is a Responses API setting (see GPT-5.6 Sol Pro). OpenAI lists only the snapshot `gpt-5.6-sol`; Microsoft Foundry's version is 2026-07-09 and Bedrock's id is `openai.gpt-5.6-sol`. The deprecated Daybreak Blue alias `gpt-daybreak-blue-latest` defaults to `gpt-5.6-sol`. OpenAI gives no retirement date and names it the replacement for GPT-5 and o3, which shut down on December 11, 2026. Artificial Analysis marks it deprecated in favour of GPT-6 Sol.

## Strengths
- Artificial Analysis measured GPT-5.6 Sol (Max) at 94.1% on GPQA Diamond, 65.9% on Terminal-Bench Hard, 39.9% on Terminal-Bench 4.0 and 85.1% on tau2-bench.
- OpenRouter reports an Artificial Analysis Coding Index of 78.3 and Agentic Index of 47.4.
- About 102 output tokens per second at Max.
- Programmatic tool calling, explicit prompt caching, persisted reasoning and multi-agent (beta) in the Responses API.

## Limitations
- The 4 USD input and 20 USD output price is a promotional cut from August 21, 2026, held at least through November 21, 2026.
- Prompts over 272,000 input tokens cost 8 and 30 USD per million; cache writes cost 1.25 times input.
- Time to first token at Max was about 92 seconds. Closed weights.

## Good for
- Agentic coding and terminal work in GPT-5.6 deployments.
- Moving off GPT-5 or o3 before December 11, 2026.
- Hard problems in pro mode.
