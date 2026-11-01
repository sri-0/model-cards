---
id: openai/gpt-5.1-codex-max
name: GPT-5.1-Codex-Max
owned_by: openai
type: llm
description: GPT-5.1-Codex-Max is OpenAI's December 2025 agentic coding model for long-running, high-context software work with an xhigh reasoning effort, served through the Responses API only and shut down by OpenAI on 23 July 2026.
aliases: [gpt-5.1-codex-max, openai/gpt-5.1-codex-max-20251204, azure/gpt-5.1-codex-max]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-12-04"
knowledge_cutoff: "2024-09"
pricing:
  input: 1.25
  output: 10
  cache_read: 0.125
sources:
  - https://openrouter.ai/openai/gpt-5.1-codex-max
  - https://openrouter.ai/api/v1/models
  - https://developers.openai.com/api/docs/models/gpt-5.1-codex-max
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.1-Codex-Max

## Overview
GPT-5.1-Codex-Max is a proprietary OpenAI model released to the Responses API on 4 December 2025. OpenAI's docs call it a version of GPT-5.1-Codex optimised for long-running tasks and purpose-built for agentic coding; OpenRouter says it is based on an updated version of the 5.1 reasoning stack and trained on agentic software work. It takes text and image input and returns text, with a 400,000-token context window, 128,000 max output tokens and a 30 September 2024 knowledge cutoff. OpenRouter lists reasoning as mandatory with low, medium, high and xhigh effort and medium as the default; Azure's docs confirm xhigh support and that `none` is not accepted. OpenAI announced its shutdown on 22 April 2026 and shut it down on 23 July 2026, naming `gpt-5.6-sol` as the replacement. OpenRouter still listed the id on 1 November 2026. Azure runs `gpt-5.1-codex-max` version 2025-12-04 as GA until 18 May 2027.

## Strengths
- The first GPT-5.1-family model with an xhigh reasoning effort for the hardest coding tasks.
- Built for long, high-context agentic sessions, per OpenAI and OpenRouter.
- Function calling, structured outputs, web search and prompt caching on the Responses API.
- Same price as GPT-5.1-Codex: 1.25 USD input and 10 USD output per million tokens, cache reads at 0.125.

## Limitations
- Shut down on OpenAI's API since 23 July 2026.
- Responses API only; no Chat Completions or Batch.
- Artificial Analysis has no page for it, so no independent benchmarks are recorded here.
- Reasoning cannot be turned off; xhigh runs are slow and token-heavy by design.
- Knowledge stops at September 2024. Closed weights.

## Good for
- Multi-hour agentic coding runs on an Azure deployment or an OpenRouter route that still serves it.
- A reference point when moving long-running Codex workloads to GPT-5.3-Codex or GPT-5.6 Sol.
