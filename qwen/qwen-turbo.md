---
id: qwen/qwen-turbo
name: Qwen-Turbo
owned_by: qwen
type: llm
description: "Qwen-Turbo is the low-cost tier of Alibaba Cloud Model Studio's hosted Qwen models, a 1M-token-context text model first released as Qwen2.5-Turbo and later moved to Qwen3 snapshots with a thinking mode; Model Studio took it offline on 2026-10-10."
aliases: [qwen-turbo, qwen-turbo-latest, qwen-turbo-2025-07-15, qwen-turbo-0715, qwen-turbo-2025-04-28, qwen-turbo-0428, qwen-turbo-2024-11-01, qwen-turbo-1101, qwen-turbo-2024-09-19, dashscope/qwen-turbo, dashscope/qwen-turbo-latest]
context_length: 1000000
max_output_tokens: 16384
capabilities: [tool_calling, reasoning, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
release_date: "2024-11-15"
benchmarks:
  gpqa_diamond: 41.0
  humanitys_last_exam: 4.1
benchmark_variant: Qwen2.5 Turbo
sources:
  - https://openrouter.ai/api/v1/models/qwen/qwen-turbo/endpoints
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen-turbo
  - https://qwenlm.github.io/blog/qwen2.5-turbo/
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20260606115938/https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/zh/notice/model_studionotice_on_the_decommissioning_of_certain_historical_mainline_models_731
  - https://www.alibabacloud.com/help/id/model-studio/model-depreciation
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Qwen-Turbo

## Overview
Qwen-Turbo (DashScope id `qwen-turbo`) is the cheapest tier of Alibaba Cloud Model Studio's first commercial Qwen line; no weights are published. OpenRouter keeps a `qwen/qwen-turbo` record, describing a Qwen2.5-based 1M-context model, but it is not in OpenRouter's model list and has no endpoints. The Qwen team released Qwen2.5-Turbo on 2024-11-15, extending the context from 128K to 1M tokens with sparse attention; that is the version Artificial Analysis tested. Model Studio later pointed the stable id at the Qwen3-based `qwen-turbo-2025-04-28`, which adds a thinking mode: 1,000,000 tokens of context without thinking, 131,072 with it, 16,384 output tokens and up to 38,912 reasoning tokens. `qwen-turbo-2024-11-01` kept the 1M context with 8,192 output tokens. International pricing was $0.05 input and $0.20 output per million tokens ($0.50 output with thinking). Model Studio marked Qwen-Turbo as no longer updated, recommended Qwen-Flash, and took qwen-turbo offline in Beijing and Singapore on 2026-10-10.

## Strengths
- Qwen reports 100% on 1M-token passkey retrieval and 93.1 on RULER for Qwen2.5-Turbo.
- Function calling, structured output and built-in tools on Model Studio.
- Very low price per token.

## Limitations
- Retired: Model Studio says calls fail once a model is offline.
- Artificial Analysis (Qwen2.5 Turbo): 41% on GPQA Diamond and 4.1% on Humanity's Last Exam.
- Qwen notes its long-sequence performance can be unstable.
- The stable id changed model generation over time, so old results may not match.

## Good for
- Interpreting old integrations and logs that name qwen-turbo.
- Picking a replacement: Model Studio points to Qwen-Flash and the Qwen3.6 and Qwen3.7 series.
