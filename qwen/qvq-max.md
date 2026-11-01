---
id: qwen/qvq-max
name: QVQ-Max
owned_by: qwen
type: llm
description: "QVQ-Max is Alibaba hosted Qwen QVQ visual reasoning model on Model Studio, taking images and producing chain-of-thought answers for maths, coding, visual analysis and creative tasks; Model Studio took it offline on 2026-10-10."
aliases: [qvq-max-latest, qvq-max-2025-05-15, qvq-max-0515, qvq-max-2025-03-25, qvq-max-0325]
context_length: 131072
max_output_tokens: 8192
capabilities: [reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-03-26"
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

# QVQ-Max

## Overview
Status: Model Studio took qvq-max offline in China (Beijing) and Singapore on 2026-10-10, per its decommissioning notice; its current pricing page no longer lists it. QVQ-Max (Model Studio id `qvq-max`, with `qvq-max-latest` and snapshots `qvq-max-2025-03-25` (0325) and `qvq-max-2025-05-15` (0515)) was released on 2025-03-26; no weights are published under this id and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes the Tongyi Qianwen QVQ visual reasoning model, which takes visual input and outputs a chain of thought, with stronger maths, programming, visual analysis, creative and general abilities; compared with QVQ-Plus it offers stronger visual reasoning and instruction following for complex tasks. The archived models page gives a 131,072-token context with 106,496 input tokens (up to 16,384 per image), a 16,384-token chain of thought and 8,192 output tokens. It was priced at $1.20 input and $4.80 output per million tokens in Singapore.

## Strengths
- Step-by-step reasoning over diagrams and photos.

## Limitations
- Offline since 2026-10-10.
- Short chain of thought and answer limits.

## Good for
- Interpreting older visual reasoning integrations.
