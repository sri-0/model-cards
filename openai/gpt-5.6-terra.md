---
id: openai/gpt-5.6-terra
name: GPT-5.6 Terra
owned_by: openai
type: llm
description: GPT-5.6 Terra is the middle tier of OpenAI's July 2026 GPT-5.6 family, between Sol and Luna and roughly the mini tier of earlier GPT-5 families; GPT-6.1 Terra has since succeeded it.
aliases: [gpt-5.6-terra, openai/gpt-5.6-terra-20260709, "openai/gpt-5.6-terra:batch", openai.gpt-5.6-terra, us.openai.gpt-5.6-terra, global.openai.gpt-5.6-terra, in.openai.gpt-5.6-terra, azure/gpt-5.6-terra, azure/gpt-5.6-terra-2026-07-09]
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
  input: 2
  output: 12
  cache_read: 0.2
  cache_write: 2.5
benchmarks:
  coding_index: 76.7
  agentic_index: 43.2
  gpqa_diamond: 92.5
  humanitys_last_exam: 42.9
  ifbench: 71.2
  long_context_reasoning: 83.0
  mmmu_pro: 80.7
  omniscience_index: -9.3
  output_tokens_per_second: 111.1
  scicode: 55.0
  tau2_bench: 86.3
  terminal_bench_4: 35.4
  terminal_bench_hard: 57.6
  time_to_first_token_seconds: 139.39
benchmark_variant: GPT-5.6 Terra (Max)
sources:
  - https://openrouter.ai/openai/gpt-5.6-terra
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-6-terra
  - https://developers.openai.com/api/docs/models/gpt-5.6-terra
  - https://developers.openai.com/api/docs/guides/latest-model/gpt-5.6
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-56-terra.html
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.6 Terra

## Overview
GPT-5.6 Terra is the middle tier of OpenAI's GPT-5.6 family, released on July 9, 2026 between GPT-5.6 Sol (flagship) and GPT-5.6 Luna (efficient, high-volume). OpenAI built it for workloads that balance intelligence and cost and says it roughly matches the mini tier of earlier GPT-5 families; OpenRouter puts it at about half Sol's cost, for everyday coding, reasoning and agentic tasks. It takes text and image input and returns text, with a 1,050,000-token context window (922,000 input), 128,000 max output tokens and a February 16, 2026 knowledge cutoff. `reasoning.effort` supports none, low, medium (default), high, xhigh and max; pro mode is a Responses API setting (see GPT-5.6 Terra Pro). OpenAI lists only the snapshot `gpt-5.6-terra`; Microsoft Foundry's version is 2026-07-09 and Bedrock's id is `openai.gpt-5.6-terra`. OpenAI gives no retirement date and names it the replacement for GPT-5 mini (shutting down December 11, 2026) and o4-mini. Artificial Analysis marks it deprecated in favour of GPT-6.1 Terra.

## Strengths
- Artificial Analysis measured GPT-5.6 Terra (Max) at 92.5% on GPQA Diamond, 86.3% on tau2-bench, 35.4% on Terminal-Bench 4.0 and about 111 output tokens per second.
- OpenRouter reports an Artificial Analysis Coding Index of 76.7 and Agentic Index of 43.2.
- OpenAI cut the price 20% on July 30, 2026, to 2 USD input and 12 USD output per million tokens.
- Chat Completions, Responses and Batch; function calling, structured outputs, web search and prompt caching.

## Limitations
- AA-Omniscience was -9.3 at Max: wrong answers outweighed correct ones.
- Time to first token at Max was about 139 seconds.
- Prompts over 272,000 input tokens cost 4 and 18 USD per million. Closed weights.

## Good for
- Everyday coding and agent steps where Sol's price is not justified.
- GPT-5.6 deployments not yet moved to GPT-6.1 Terra.
- Moving off GPT-5 mini before December 11, 2026.
