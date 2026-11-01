---
id: qwen/qwen-vl-plus
name: Qwen-VL-Plus
owned_by: qwen
type: llm
description: "Qwen-VL-Plus is the enhanced tier of Alibaba Cloud Model Studio earlier hosted Qwen-VL vision-language models, with better detail and text recognition at over a million pixels; Model Studio took it offline on 2026-10-10."
aliases: [qwen-vl-plus-latest, qwen-vl-plus-2025-08-15, qwen-vl-plus-0815, qwen-vl-plus-2025-07-10, qwen-vl-plus-0710, qwen-vl-plus-2025-05-07, qwen-vl-plus-0507, qwen-vl-plus-2025-01-25, qwen-vl-plus-0125, qwen-vl-plus-2025-01-02, qwen-vl-plus-0102, qwen-vl-plus-2024-08-09]
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

# Qwen-VL-Plus

## Overview
Status: Model Studio took qwen-vl-plus offline in China (Beijing) and Singapore on 2026-10-10, per its decommissioning notice; its current pricing page no longer lists it. Qwen-VL-Plus (Model Studio id `qwen-vl-plus`) was the enhanced tier of Model Studio's first commercial Qwen-VL line; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Before retirement the stable id was documented as equivalent to `qwen-vl-plus-2025-08-15` (0815), with a `-latest` alias and dated snapshots back to 2024-08-09, which was deprecated on 2026-01-30. Model Studio said it greatly improves detail and text recognition, supports images above one million pixels at any aspect ratio, and performs well across visual tasks. The archived models page gives a 131,072-token context with 129,024 input tokens (up to 16,384 per image) and 8,192 output tokens. It was priced at $0.21 input and $0.63 output per million tokens in Singapore.

## Strengths
- Low-cost image understanding and text recognition.

## Limitations
- Offline since 2026-10-10.
- 8,192 output tokens.

## Good for
- Interpreting older vision integrations.
