---
id: qwen/qwen-coder-turbo
name: Qwen-Coder-Turbo
owned_by: qwen
type: llm
description: "Qwen-Coder-Turbo is an earlier fast, low-cost hosted Model Studio Qwen code generation model with a 131K-token context, offered in China (Beijing)."
aliases: [qwen-coder-turbo-latest, qwen-coder-turbo-2024-09-19, qwen-coder-turbo-0919]
context_length: 131072
max_output_tokens: 8192
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2024-09-19"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Coder-Turbo

## Overview
Status: Model Studio's current pricing page no longer lists qwen-coder-turbo; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. Qwen-Coder-Turbo (Model Studio id `qwen-coder-turbo`, documented as equivalent to `qwen-coder-turbo-2024-09-19`, also `qwen-coder-turbo-0919`, with a `-latest` alias) appears in Model Studio's release table on 2024-09-19; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes a specialised language model for programming and code generation with high inference speed and low cost. The archived models page gives a 131,072-token context with 129,024 input and 8,192 output tokens. It was priced for China (Beijing) at $0.287 input and $0.861 output per million tokens.

## Strengths
- Fast, cheap code completion.

## Limitations
- No longer listed for sale on Model Studio.
- China (Beijing) only.

## Good for
- Interpreting older coding integrations.
