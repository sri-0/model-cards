---
id: qwen/qwen-vl-max
name: Qwen-VL-Max
owned_by: qwen
type: llm
description: "Qwen-VL-Max is the larger of Alibaba Cloud Model Studio earlier hosted Qwen-VL vision-language models, with stronger visual reasoning and instruction following than Qwen-VL-Plus; Model Studio took it offline on 2026-10-10."
aliases: [qwen-vl-max-latest, qwen-vl-max-2025-08-13, qwen-vl-max-0813, qwen-vl-max-2025-04-08, qwen-vl-max-0408, qwen-vl-max-2025-04-02, qwen-vl-max-0402, qwen-vl-max-2025-01-25, qwen-vl-max-0125, qwen-vl-max-2024-12-30, qwen-vl-max-1230, qwen-vl-max-2024-11-19, qwen-vl-max-1119, qwen-vl-max-2024-10-30, qwen-vl-max-2024-08-09]
context_length: 131072
max_output_tokens: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
sources:
  - https://www.alibabacloud.com/zh/notice/model_studionotice_on_the_decommissioning_of_certain_historical_mainline_models_731
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/id/model-studio/model-depreciation
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-VL-Max

## Overview
Status: Model Studio took qwen-vl-max offline in China (Beijing) and Singapore on 2026-10-10, per its decommissioning notice; its current pricing page no longer lists it. Qwen-VL-Max (Model Studio id `qwen-vl-max`) was the top tier of Model Studio's first commercial Qwen-VL line; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Before retirement the stable id was documented as equivalent to `qwen-vl-max-2025-08-13` (0813), with a `-latest` alias and dated snapshots back to 2024-08-09; the 2024-08-09 and 2024-10-30 snapshots were deprecated on 2026-01-30. Model Studio said that, compared with Qwen-VL-Plus, it further improves visual reasoning and instruction following for the most complex tasks. The archived models page gives a 131,072-token context with 129,024 input tokens (up to 16,384 per image) and 8,192 output tokens. It was priced at $0.80 input and $3.20 output per million tokens in Singapore.

## Strengths
- Visual reasoning and OCR over images.

## Limitations
- Offline since 2026-10-10.
- 8,192 output tokens.

## Good for
- Interpreting older vision integrations; Model Studio named the Qwen3.6 and Qwen3.7 series as replacements.
