---
id: openai/gpt-5.1-codex-mini
name: GPT-5.1-Codex-Mini
owned_by: openai
type: llm
description: GPT-5.1-Codex-Mini is the smaller, cheaper and less capable version of OpenAI's GPT-5.1-Codex for agentic coding, served through the Responses API only and shut down by OpenAI on 23 July 2026.
aliases: [gpt-5.1-codex-mini, openai/gpt-5.1-codex-mini-20251113, azure/gpt-5.1-codex-mini, azure/gpt-5.1-codex-mini-2025-11-13]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [image, text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-11-13"
knowledge_cutoff: "2024-09"
pricing:
  input: 0.25
  output: 2
  cache_read: 0.03
benchmarks:
  gpqa_diamond: 81.3
  humanitys_last_exam: 18.5
  ifbench: 67.9
  long_context_reasoning: 66.7
  mmmu_pro: 69.0
  output_tokens_per_second: 173.3
  tau2_bench: 62.9
  terminal_bench_hard: 33.3
  time_to_first_token_seconds: 17.3
benchmark_variant: GPT-5.1 Codex mini (High)
sources:
  - https://openrouter.ai/openai/gpt-5.1-codex-mini
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-1-codex-mini
  - https://developers.openai.com/api/docs/models/gpt-5.1-codex-mini
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.1-Codex-Mini

## Overview
GPT-5.1-Codex-Mini is a proprietary OpenAI model released to the Responses API on 13 November 2025 alongside GPT-5.1-Codex. OpenAI's docs describe it as a smaller, more cost-effective, less capable version of GPT-5.1-Codex; OpenRouter calls it smaller and faster. It takes text and image input and returns text, with a 400,000-token context window, 128,000 max output tokens and a 30 September 2024 knowledge cutoff. OpenRouter lists reasoning as mandatory with low, medium and high effort and medium as the default. OpenAI announced its shutdown on 22 April 2026 and shut it down on 23 July 2026, naming `gpt-5.6-terra` as the replacement; Artificial Analysis points to GPT-5.2 Codex. OpenRouter still listed the id on 1 November 2026. Azure runs `gpt-5.1-codex-mini` version 2025-11-13 as GA until 15 May 2027.

## Strengths
- A fifth of the price of GPT-5.1-Codex: 0.25 USD input and 2 USD output per million tokens.
- About 173 output tokens per second at High, the fastest of the GPT-5.1 line Artificial Analysis measured.
- Terminal-Bench Hard of 33.3% (High) is close to GPT-5.1-Codex (High) at 34.8%.
- Function calling, structured outputs, image input and prompt caching on the Responses API.

## Limitations
- Shut down on OpenAI's API since 23 July 2026.
- Responses API only; no Chat Completions or Batch.
- Lower scores than GPT-5.1-Codex on tau2-bench (62.9%), Humanity's Last Exam (18.5%) and GPQA Diamond (81.3%) at High.
- Knowledge stops at September 2024. Closed weights.

## Good for
- Cheap, fast coding-agent loops such as test runs, lint fixes and small patches.
- Azure or OpenRouter routes that still serve it, pending migration to GPT-5.6 Terra.
