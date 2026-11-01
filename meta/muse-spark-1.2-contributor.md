---
id: meta/muse-spark-1.2-contributor
name: Muse Spark 1.2 Contributor
owned_by: meta
type: llm
description: Muse Spark 1.2 Contributor is the discounted Contributor-mode variant of Meta's Muse Spark 1.2, priced far below Standard mode in exchange for letting Meta train future models on your content.
aliases: [muse-spark-1.2-contributor]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, reasoning_effort, repetition_penalty, response_format, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image, video, file]
  output_modalities: [text]
  tokenizer: Other
open_weights: false
license: proprietary
pricing:
  input: 0.1
  output: 0.2
  cache_read: 0.002
sources:
  - https://openrouter.ai/meta/muse-spark-1.2-contributor
  - https://openrouter.ai/api/v1/models
  - https://dev.meta.ai/models/muse-spark-1-2
  - https://dev.meta.ai/docs/models
  - https://dev.meta.ai/docs/pricing-rate-limits
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Muse Spark 1.2 Contributor

## Overview
`muse-spark-1.2-contributor` is Muse Spark 1.2 in Meta's Contributor mode. Meta's pricing docs say Contributor mode "runs the same models at heavily discounted token prices, in exchange for permission to use your content to train future Meta models", where content means the prompts, code, files and context you send and the responses you get back. OpenRouter describes it as a reasoning model for developers who want to start building at an even lower cost. Inputs, the 1,048,576-token context and reasoning effort (minimal to xhigh) are as for Muse Spark 1.2, and OpenRouter's canonical slug carries the 1.2 snapshot date, 2026-08-05. Meta serves it on pay-as-you-go and in Muse Code. Meta recommends Muse Spark 1.3 for new work, and `muse-spark-1.3-contributor` is the newer Contributor variant.

## Strengths
- $0.10 input, $0.20 output and $0.002 cached input per million tokens, against $1.25, $4.25 and $0.15 for `muse-spark-1.2`.
- Tool calling, structured outputs, vision and reasoning effort control, as on Muse Spark 1.2.
- Meta recommends Muse Spark 1.2 rather than 1.3 for audio input.

## Limitations
- Meta may use everything you send and receive to train future models. Do not send confidential, personal, customer or regulated data.
- Lower rate limits: 150 requests and 3M tokens per minute, against 3,000 requests and 4M tokens for `muse-spark-1.2`.
- No separate Artificial Analysis results; see `meta/muse-spark-1.2` for the Standard-mode scores.
- Proprietary and API-only, so it cannot run in a network-isolated deployment.

## Good for
- Prototypes, integration tests and experiments with public or synthetic data.
- Learning the Muse Spark API cheaply before moving to Standard mode.
- Agent experiments that include audio, at Contributor prices.
