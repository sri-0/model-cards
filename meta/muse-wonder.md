---
id: meta/muse-wonder
name: Muse Wonder
owned_by: meta
type: llm
description: Muse Wonder is Meta's proprietary reasoning model for complex, long-horizon agentic tasks, taking text, image, video, audio and PDF input and returning text.
aliases: [muse-wonder-1.0, meta/muse-wonder-1.0]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, reasoning_effort, repetition_penalty, response_format, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image, video, file, audio]
  output_modalities: [text]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-10-12"
pricing:
  input: 4
  output: 20
  cache_read: 0.2
benchmarks:
  intelligence_index: 52.4
  omniscience_index: 25.5
  humanitys_last_exam: 50.1
  scicode: 60.3
  terminal_bench_4: 52
  long_context_reasoning: 80.7
  output_tokens_per_second: 104.1
  time_to_first_token_seconds: 19.73
benchmark_variant: Muse Wonder (Max)
sources:
  - https://openrouter.ai/meta/muse-wonder
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/muse-wonder
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Muse Wonder

## Overview
Muse Wonder is a model in Meta's Muse family, released on 2026-10-12 and served through Meta's API (LiteLLM lists it as `meta/muse-wonder-1.0`). OpenRouter describes it as a reasoning model for complex personal and professional agentic tasks. It accepts text, images, video, audio and PDF documents, returns text, and has a 1,048,576-token context window. The weights are not published.

## Strengths
- Built for long-horizon agent work. Per its OpenRouter description it plans, delegates to sub-agents, calls tools in parallel and recovers from errors.
- Can operate browsers and desktop and mobile applications, and can make and verify changes across many files in an existing repository.
- Meta reports good results on complex engineering tasks, extended agentic sessions and multi-file refactors.
- Artificial Analysis (Muse Wonder, Max variant) scores it 52.4 on the Intelligence Index, with 104.1 output tokens per second and 19.73 s to first token.

## Limitations
- Proprietary and API-only. It cannot be self-hosted.
- Costly: $4 input and $20 output per million tokens on OpenRouter. Artificial Analysis calls it somewhat expensive and somewhat verbose (130M tokens to run its Intelligence Index against a median of 85M).
- Very new. OpenRouter's Artificial Analysis data had no coding or agentic index for it at retrieval.

## Good for
- Multi-step agent tasks that need tool use, sub-agents and error recovery.
- Large code changes and multi-file refactors.
- Work that mixes documents, images, audio and video in one long context.
