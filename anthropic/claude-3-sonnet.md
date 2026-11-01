---
id: anthropic/claude-3-sonnet
name: Claude 3 Sonnet
owned_by: anthropic
type: llm
description: The middle model of Anthropic's March 2024 Claude 3 family, retired from the Claude API on July 21, 2025 and left on Amazon Bedrock in three regions until November 13, 2026.
aliases: [claude-3-sonnet-20240229, "anthropic.claude-3-sonnet-20240229-v1:0", "claude-3-sonnet@20240229", claude-3-sonnet]
context_length: 200000
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2024-03-04"
knowledge_cutoff: "2023-08"
benchmarks:
  gpqa_diamond: 40.0
  humanitys_last_exam: 3.6
benchmark_variant: Claude 3 Sonnet
sources:
  - https://artificialanalysis.ai/models/claude-3-sonnet
  - https://www.anthropic.com/news/claude-3-family
  - https://claude.com/resources/articles/tool-use-ga
  - https://www.anthropic.com/news/claude-3-7-sonnet
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Claude 3 Sonnet

## Overview
Claude 3 Sonnet (Claude Sonnet 3 in Anthropic's current docs) is retired on the Claude API: Anthropic announced its deprecation on January 21, 2025 and retired it on July 21, 2025, and its deprecations page now names `claude-sonnet-5-5` as the replacement. Amazon Bedrock still serves `anthropic.claude-3-sonnet-20240229-v1:0` in ap-south-1, ap-southeast-1 and eu-west-2, where AWS moved it to Legacy on October 10, 2026 and lists end-of-life on November 13, 2026. It is the middle model of the Claude 3 family, released on March 4, 2024 on the Claude API and Amazon Bedrock, with Vertex AI in private preview. OpenRouter no longer lists it, so the id follows OpenRouter's naming style; the Claude API id is `claude-3-sonnet-20240229`. Anthropic's launch price was $3 input and $15 output per million tokens, with a 200K-token context window. Artificial Analysis gives an August 2023 knowledge cutoff; Anthropic's current docs state none.

## Strengths
- Anthropic pitched it as the balance of intelligence and speed for enterprise workloads, about twice as fast as Claude 2 and Claude 2.1 for most tasks.
- Image input covering photos, charts, graphs and technical diagrams, and tool use, generally available since May 30, 2024.
- Anthropic said Claude 3 models refuse harmless borderline prompts much less often than earlier generations.

## Limitations
- Retired on the Claude API; the last Bedrock regions end on November 13, 2026, and AWS says prices can rise during the public extended access period that began on October 10, 2026.
- No extended thinking, which arrived with Claude 3.7 Sonnet, and no parallel tool calls when tool use launched.
- Artificial Analysis measured only 40.0% on GPQA Diamond and 3.6% on Humanity's Last Exam.
- 200K context window.

## Good for
- Bedrock workloads in those three regions until November 13, 2026.
- Reproducing early-2024 results; Anthropic recommends Claude Sonnet 5.5 instead.
