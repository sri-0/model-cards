---
id: qwen/qwen3-coder-plus
name: Qwen3-Coder-Plus
owned_by: qwen
type: llm
description: "Qwen3-Coder-Plus is Alibaba hosted Qwen3 coding-agent model on Model Studio with strong tool calling and environment interaction and a 1M-token context; Model Studio deprecated it on 2026-10-10."
aliases: [qwen3-coder-plus-2025-09-23, qwen3-coder-plus-2025-07-22]
context_length: 1000000
max_output_tokens: 65536
capabilities: [tool_calling]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-07-22"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/id/model-studio/model-depreciation
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-Coder-Plus

## Overview
Status: Model Studio lists qwen3-coder-plus and its snapshots as deprecated on 2026-10-10, with qwen3.7-plus as the replacement; its current pricing page no longer lists them. Qwen3-Coder-Plus (Model Studio id `qwen3-coder-plus`, documented as equivalent to `qwen3-coder-plus-2025-09-23`, with an earlier `qwen3-coder-plus-2025-07-22` snapshot) was released on 2025-07-22 in China (Beijing) and 2025-07-23 internationally; no weights are published under this id and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes a Qwen3-based code generation model with strong coding-agent ability that excels at tool calling and environment interaction and can program autonomously while keeping general ability. The archived models page gives a 1,000,000-token context with 997,952 input and 65,536 output tokens. International pricing was tiered by input length: $1/$5 per million input/output tokens up to 32K, $1.80/$9 to 128K, $3/$15 to 256K and $6/$60 to 1M.

## Strengths
- Agentic coding with tools over a 1M context.

## Limitations
- Deprecated on Model Studio.
- Output price rises steeply above 256K input.

## Good for
- Interpreting older coding-agent integrations; qwen3.7-plus replaces it.
