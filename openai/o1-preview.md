---
id: openai/o1-preview
name: o1 Preview
owned_by: openai
type: llm
description: o1-preview was the research preview of OpenAI's first o-series reasoning model, released in September 2024 and shut down on 28 July 2025.
aliases: [o1-preview, o1-preview-2024-09-12, azure/us/o1-preview, azure/eu/o1-preview]
context_length: 128000
max_output_tokens: 32768
capabilities: [tool_calling, reasoning, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2024-09-12"
knowledge_cutoff: "2023-10"
benchmarks:
  gpqa_diamond: 76.5
benchmark_variant: o1-preview
sources:
  - https://developers.openai.com/api/docs/models/o1-preview
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://artificialanalysis.ai/models/o1-preview
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# o1 Preview

## Overview
Shut down: OpenAI announced the deprecation on 28 April 2025 and removed `o1-preview` from the API on 28 July 2025, naming `o3` as the replacement (o3 itself is now deprecated, with shutdown on 11 December 2026). OpenRouter does not list it; the id is OpenAI's API id. OpenAI released it with o1-mini on 12 September 2024 as a research preview of the o-series: models trained with reinforcement learning that produce a long internal chain of thought before answering. Its only snapshot was `o1-preview-2024-09-12`. It was text-only, with a 128,000-token context window, 32,768 max output tokens, reasoning tokens and an October 2023 knowledge cutoff, on Chat Completions and Assistants. The model page lists streaming, structured outputs, function calling, file search and file uploads. OpenAI priced it at 15 USD input, 7.50 cached input and 60 USD output per million tokens, the same as o1.

## Strengths
- Artificial Analysis measured 76.5% on GPQA Diamond, its only published result for the model.
- The first OpenAI API model with hidden reasoning before the answer.

## Limitations
- Shut down; requests to the id fail.
- No image input.
- OpenAI's changelog says o1-preview did not support system or developer messages.
- OpenAI bills hidden reasoning tokens as output, at 60 USD per million here, so long thinking was expensive.

## Good for
- Recognising the id in 2024 reasoning experiments and evaluation logs.
- Historical comparison of the first o-series release with o1, o3 and later models.
