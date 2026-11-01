---
id: openai/o1-mini
name: o1-mini
owned_by: openai
type: llm
description: o1-mini is the small text-only model of OpenAI's first o-series, shut down on OpenAI's API on 2025-10-27 in favour of o4-mini.
aliases: [o1-mini, o1-mini-2024-09-12, azure/o1-mini, azure/o1-mini-2024-09-12]
context_length: 128000
max_output_tokens: 65536
capabilities: [reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2024-09-12"
knowledge_cutoff: "2023-10"
benchmarks:
  gpqa_diamond: 60.3
  humanitys_last_exam: 3.6
benchmark_variant: o1-mini
sources:
  - https://artificialanalysis.ai/models/o1-mini
  - https://developers.openai.com/api/docs/models/o1-mini
  - https://developers.openai.com/api/docs/deprecations
  - https://openrouter.ai/api/v1/models
  - https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# o1-mini

## Overview
o1-mini is the small member of OpenAI's first o-series, released on 2024-09-12 (Artificial Analysis date; pinned snapshot `o1-mini-2024-09-12`). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix and the frontmatter carries no OpenRouter price or parameters; the limits come from OpenAI's page. OpenAI described it as a faster and more affordable alternative to o1. It is text-only, with a 128,000-token context window, 65,536 max output tokens, reasoning tokens and an October 2023 knowledge cutoff. OpenAI served it on Chat Completions and Assistants, with streaming and file search; its page lists neither function calling nor structured outputs, and it did not support the Responses or Batch endpoints. OpenAI's price was $1.10 input, $0.55 cached input and $4.40 output per million tokens. OpenAI lists it as Shut down: announced 2025-04-28, it left the API on 2025-10-27 with o4-mini as the recommended replacement. Its model page points to o3-mini, which OpenAI says offers higher intelligence at the same latency and price. Azure's model list still describes version 2024-09-12 as available for Global Standard deployment.

## Strengths
- Artificial Analysis measured 60.3% on GPQA Diamond, against 42.6% for GPT-4o mini.
- Reasoning at $4.40 per million output tokens, against $60 for o1.

## Limitations
- Shut down on OpenAI's API since 2025-10-27 and not listed on OpenRouter.
- No function calling, structured outputs, image input, Responses API or Batch.
- 3.6% on Humanity's Last Exam; Artificial Analysis publishes no other current scores for it.
- Knowledge stops at October 2023.

## Good for
- Reproducing results from 2024 and 2025 systems that were built on it.
- A reference point for the o-series small models that followed (o3-mini, o4-mini).
