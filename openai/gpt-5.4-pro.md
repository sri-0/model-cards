---
id: openai/gpt-5.4-pro
name: GPT-5.4 Pro
owned_by: openai
type: llm
description: GPT-5.4 Pro is a higher-compute version of OpenAI's GPT-5.4 that spends more reasoning on each request, available only through the Responses API.
aliases: [gpt-5.4-pro, gpt-5.4-pro-2026-03-05]
context_length: 1050000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-03-05"
knowledge_cutoff: "2025-08"
pricing:
  input: 30
  output: 180
sources:
  - https://openrouter.ai/openai/gpt-5.4-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-5-4-pro
  - https://developers.openai.com/api/docs/models/gpt-5.4-pro
retrieved: "2026-10-14"
---

# GPT-5.4 Pro

## Overview
GPT-5.4 Pro is a proprietary OpenAI model released in March 2026. OpenAI says it uses more compute to think harder and give more consistent answers. It accepts text and image input and returns text, with a 1,050,000-token context window, 128,000 max output tokens and an August 31, 2025 knowledge cutoff. `reasoning.effort` supports medium (default), high and xhigh. The pinned snapshot is `gpt-5.4-pro-2026-03-05`.

## Strengths
- OpenRouter positions it for agentic coding, long-context workflows and multi-step problem solving where accuracy matters.
- Large context window shared with GPT-5.4.
- Tool calling, structured outputs and image input.

## Limitations
- Available in OpenAI's Responses API only, not Chat Completions.
- OpenAI warns that some requests take several minutes and suggests background mode to avoid timeouts. OpenAI rates its speed as the slowest in the lineup.
- Expensive: 30 USD input and 180 USD output per million tokens on OpenRouter, rising to 60 and 270 for prompts over 272,000 tokens.
- Artificial Analysis lists the model but publishes no Intelligence Index or speed figures for it.
- No low or none reasoning setting. Closed weights.

## Good for
- Hard, high-stakes problems where answer quality outweighs cost and latency.
- Offline or batch analysis that can wait for long responses.
- Checking or reviewing work produced by cheaper models.
