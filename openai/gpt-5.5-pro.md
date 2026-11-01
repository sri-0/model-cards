---
id: openai/gpt-5.5-pro
name: GPT-5.5 Pro
owned_by: openai
type: llm
description: GPT-5.5 Pro is the higher-compute version of OpenAI's GPT-5.5 for hard, high-stakes problems, served through the Responses and Batch APIs only, and the newest OpenAI model with a separate Pro id.
aliases: [gpt-5.5-pro, gpt-5.5-pro-2026-04-23, openai/gpt-5.5-pro-20260423, "openai/gpt-5.5-pro:batch"]
context_length: 1050000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [file, image, text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-04-23"
knowledge_cutoff: "2025-12"
pricing:
  input: 30
  output: 180
sources:
  - https://openrouter.ai/openai/gpt-5.5-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-5-pro
  - https://developers.openai.com/api/docs/models/gpt-5.5-pro
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/guides/latest-model/gpt-5.6
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
retrieved: "2026-11-01"
---

# GPT-5.5 Pro

## Overview
GPT-5.5 Pro is a proprietary OpenAI model released with GPT-5.5. OpenAI says it uses more compute to think harder and give consistently better answers; OpenRouter positions it for deep reasoning, agentic coding and long-horizon problem solving where accuracy matters. It takes text and image input and returns text, with a 1,050,000-token context window (922,000 input per OpenRouter), 128,000 max output tokens and a December 1, 2025 knowledge cutoff. OpenAI lists `reasoning.effort` as medium, high (default) and xhigh; OpenRouter gives medium as its default. The pinned snapshot is `gpt-5.5-pro-2026-04-23`; the changelog dates the release April 24, 2026. OpenAI's catalogue has no Pro id after it: from GPT-5.6 on, pro is `reasoning.mode: pro` on the base model (see GPT-5.6 Sol Pro), and OpenAI says existing Pro ids keep their behaviour and pricing. The deprecations page gives no retirement date. Artificial Analysis lists GPT-5.5 Pro (Xhigh) but publishes no results for it.

## Strengths
- More compute per request than GPT-5.5, for harder problems.
- Responses API tools: function calling, web search, file search, image generation, code interpreter, hosted shell and MCP.
- Same 1M-token window as GPT-5.5.

## Limitations
- Responses and Batch endpoints only; no Chat Completions.
- Some requests take several minutes; OpenAI suggests background mode to avoid timeouts.
- 30 USD input and 180 USD output per million tokens, rising to 60 and 270 above 272,000 input tokens, with no cached-input discount. GPT-5.6 pro mode has no such premium.
- No low or none reasoning setting. Closed weights.

## Good for
- Hard, high-stakes analysis where answer quality outweighs cost and latency.
- Batch or background jobs that can wait minutes per response.
- Reviewing work produced by cheaper models.
