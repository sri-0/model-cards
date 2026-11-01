---
id: qwen/qwen3-vl-plus
name: Qwen3-VL-Plus
owned_by: qwen
type: llm
description: "Qwen3-VL-Plus is Alibaba hosted Qwen3 vision-language model on Model Studio with thinking and non-thinking modes, strong visual agent results, visual coding, spatial perception and very long video understanding; Model Studio lists it as legacy."
aliases: [qwen3-vl-plus-2025-09-23, qwen3-vl-plus-2025-12-19]
context_length: 262144
max_output_tokens: 32768
capabilities: [tool_calling, reasoning, vision, structured_output]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-09-23"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-vl-plus
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/id/model-studio/model-depreciation
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-VL-Plus

## Overview
Status: Model Studio's visual understanding page lists qwen3-vl-plus and its snapshots among legacy models that are no longer recommended; it is still priced. Qwen3-VL-Plus (Model Studio id `qwen3-vl-plus`, with snapshots 2025-09-23 and 2025-12-19) was released on 2025-09-23; no weights are published under this id and OpenRouter does not list it, so the id is the DashScope model id. Model Studio says it combines thinking and non-thinking modes, leads public visual-agent benchmarks such as OS World, and upgrades visual coding, spatial perception, multimodal reasoning and recognition, including very long videos. It has a 262,144-token context with 260,096 input tokens (258,048 in thinking mode), 32,768 output tokens and an 81,920-token chain of thought. Structured output, prefix completion and caching are supported; function calling only in China (Beijing). Singapore pricing is tiered by input length: $0.20/$1.60 per million input/output tokens up to 32K, $0.30/$2.40 to 128K and $0.60/$4.80 to 256K.

## Strengths
- Visual agent and GUI tasks.
- Long-video understanding.

## Limitations
- Legacy; Model Studio recommends the Qwen3.6 or Qwen3.5 series for new projects.
- Function calling only in China (Beijing).

## Good for
- Existing vision integrations pinned to qwen3-vl-plus.
