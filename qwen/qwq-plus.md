---
id: qwen/qwq-plus
name: QwQ-Plus
owned_by: qwen
type: llm
description: "QwQ-Plus is the enhanced hosted version of Alibaba Qwen QwQ reasoning model on Model Studio, trained on Qwen2.5 with reinforcement learning; Model Studio took it offline on 2026-10-10."
aliases: [qwq-plus-latest, qwq-plus-2025-03-05, qwq-plus-0305]
context_length: 131072
max_output_tokens: 8192
capabilities: [reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-03-05"
sources:
  - https://www.alibabacloud.com/zh/notice/model_studionotice_on_the_decommissioning_of_certain_historical_mainline_models_731
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# QwQ-Plus

## Overview
Status: Model Studio took qwq-plus offline in China (Beijing) and Singapore on 2026-10-10, per its decommissioning notice; its current pricing page no longer lists it. QwQ-Plus (Model Studio id `qwq-plus`, with `qwq-plus-latest` and the `qwq-plus-2025-03-05` snapshot, also `qwq-plus-0305`) was released on 2025-03-05; no weights are published under this id and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes the enhanced version of the QwQ reasoning model, trained on Qwen2.5, whose reasoning improved greatly through reinforcement learning, reaching the level of the full DeepSeek-R1 on maths and coding metrics such as AIME 24/25 and LiveCodeBench and on general metrics such as IFEval and LiveBench. The archived models page gives a 131,072-token context with 98,304 input tokens, a 32,768-token chain of thought and 8,192 output tokens. It was priced at $0.80 input and $2.40 output per million tokens in Singapore and $0.23 and $0.574 in China (Beijing).

## Strengths
- Maths and coding results at the level of the full DeepSeek-R1, per Model Studio.

## Limitations
- Offline since 2026-10-10.
- Reasoning only; 8,192 answer tokens.

## Good for
- Interpreting older reasoning integrations.
