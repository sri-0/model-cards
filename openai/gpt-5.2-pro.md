---
id: openai/gpt-5.2-pro
name: GPT-5.2 Pro
owned_by: openai
type: llm
description: GPT-5.2 Pro is the high-compute version of OpenAI's GPT-5.2 for professional work that needs more precise answers, served through the Responses API only and since superseded by GPT-5.5 Pro.
aliases: [gpt-5.2-pro, gpt-5.2-pro-2025-12-11, openai/gpt-5.2-pro-20251211, openai/gpt-5.2-pro:batch, azure/gpt-5.2-pro, azure/gpt-5.2-pro-2025-12-11]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [image, text, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-12-11"
knowledge_cutoff: "2025-08"
pricing:
  input: 21
  output: 168
sources:
  - https://openrouter.ai/openai/gpt-5.2-pro
  - https://openrouter.ai/api/v1/models
  - https://developers.openai.com/api/docs/models/gpt-5.2-pro
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.2 Pro

## Overview
GPT-5.2 Pro is a proprietary OpenAI model whose pinned snapshot, `gpt-5.2-pro-2025-12-11`, carries the date GPT-5.2 was released, 11 December 2025. OpenAI's docs now call it the previous pro model for professional work that produces smarter and more precise responses, and recommend GPT-5.5 Pro as the current pro model; OpenRouter says it improves agentic coding and long-context performance over GPT-5 Pro. It takes text and image input and returns text, with a 400,000-token context window, 128,000 max output tokens and a 31 August 2025 knowledge cutoff. `reasoning.effort` supports medium, high and xhigh; OpenRouter lists medium as the default. OpenAI's deprecations page lists no shutdown for it as of 1 November 2026, and Azure's retirement schedule does not list it, although LiteLLM carries `azure/gpt-5.2-pro` ids.

## Strengths
- Highest reasoning budget in the GPT-5.2 line, with xhigh effort.
- Function calling, file search, image input, image generation, MCP and web search on the Responses API.
- Knowledge to August 2025.

## Limitations
- Responses API only, not Chat Completions; OpenRouter also lists a `:batch` variant that shares this card.
- Expensive: 21 USD input and 168 USD output per million tokens on OpenRouter, with no cache-read price.
- OpenAI warns some requests take several minutes and suggests background mode to avoid timeouts.
- No none or low effort setting.
- Artificial Analysis has no page for it, so no independent benchmarks are recorded here.
- Superseded by GPT-5.5 Pro per OpenAI. Closed weights.

## Good for
- Hard, high-stakes analysis where answer quality outweighs cost and latency.
- Offline or background jobs on a still-supported GPT-5.2 snapshot.
- Reviewing work from cheaper GPT-5.2 variants.
