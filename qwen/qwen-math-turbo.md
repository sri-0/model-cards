---
id: qwen/qwen-math-turbo
name: Qwen-Math-Turbo
owned_by: qwen
type: llm
description: "Qwen-Math-Turbo is an earlier fast, low-cost hosted Model Studio Qwen maths problem-solving model, offered in China (Beijing)."
aliases: [qwen-math-turbo-latest, qwen-math-turbo-2024-09-19, qwen-math-turbo-0919]
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

# Qwen-Math-Turbo

## Overview
Status: Model Studio's current pricing page no longer lists qwen-math-turbo; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. Qwen-Math-Turbo (Model Studio id `qwen-math-turbo`, documented as equivalent to `qwen-math-turbo-2024-09-19`, also `qwen-math-turbo-0919`, with a `-latest` alias) appears in Model Studio's release table on 2024-09-19; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes a specialised language model for maths problem-solving with high inference speed and low cost, the cheaper sibling of Qwen-Math-Plus (qwen/qwen-math-plus). It was priced for China (Beijing) at $0.287 input and $0.861 output per million tokens. The archived pages that list it give no separate context limits.

## Strengths
- Cheaper maths solving than Qwen-Math-Plus.

## Limitations
- No longer listed for sale on Model Studio.
- Context limits are not documented.

## Good for
- Interpreting older maths integrations.
