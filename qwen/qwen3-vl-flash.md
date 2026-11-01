---
id: qwen/qwen3-vl-flash
name: Qwen3-VL-Flash
owned_by: qwen
type: llm
description: "Qwen3-VL-Flash is Alibaba small hosted Qwen3 vision-language model on Model Studio with thinking and non-thinking modes, 2D and 3D visual grounding and long video and document understanding; Model Studio deprecated it on 2026-10-10."
aliases: [qwen3-vl-flash-2026-01-22, qwen3-vl-flash-2025-10-15, qwen3-vl-flash-us, qwen3-vl-flash-2025-10-15-us, qwen3-vl-flash-2026-01-22-us]
capabilities: [reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-10-14"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/id/model-studio/model-depreciation
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3-VL-Flash

## Overview
Status: Model Studio lists qwen3-vl-flash and its snapshots as deprecated on 2026-10-10, with qwen3.6-flash as the replacement; its current pricing page no longer lists them. Qwen3-VL-Flash (Model Studio id `qwen3-vl-flash`) was released on 2025-10-14 in China (Beijing) and 2025-10-15 elsewhere, with `-us` ids for US deployment; no weights are published under this id and OpenRouter does not list it, so the id is the DashScope model id. The archived models page documented the stable id as equivalent to `qwen3-vl-flash-2025-10-15`, and the October 2026 pricing page as equivalent to `qwen3-vl-flash-2026-01-22`. Model Studio describes a small Qwen3 vision model that combines thinking and non-thinking modes, outperforms the open Qwen3-VL-30B-A3B while staying fast, and handles long videos and documents, spatial awareness, object recognition and 2D and 3D localisation; the 2026-01-22 snapshot improves recognition in security, retail inspection, equipment monitoring and photo problem-solving. Input is up to 260,096 tokens (258,048 in thinking mode, 16,384 per image) with an 81,920-token chain of thought. International pricing started at $0.05 input and $0.40 output per million tokens up to 32K input.

## Strengths
- Fast, cheap visual understanding with thinking.

## Limitations
- Deprecated on Model Studio.

## Good for
- Interpreting older vision integrations; qwen3.6-flash replaces it.
