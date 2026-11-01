---
id: qwen/qwen-deep-research
name: Qwen-Deep-Research
owned_by: qwen
type: llm
description: "Qwen-Deep-Research is Alibaba hosted research agent model on Model Studio that plans multi-step research, searches the web and writes traceable reports, using a clarify-then-research workflow."
context_length: 1000000
max_output_tokens: 32768
capabilities: [reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-08-22"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen-deep-research
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-Deep-Research

## Overview
Qwen-Deep-Research (Model Studio id `qwen-deep-research`) was released on 2025-08-22 and is documented for the China (Beijing) region only; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes an agent system for complex research tasks with multi-step reasoning and global planning that uses tools such as internet search to break down a task, reason, analyse and produce traceable, logically rigorous research reports. Calls follow two steps: a follow-up question step in which the model clarifies the research scope, then the deep research step that searches, analyses and writes the report. It supports streaming output only, through the DashScope Python SDK or HTTP; the Java SDK and the OpenAI-compatible API are not supported. The archived models page gives a 1,000,000-token context with 997,952 input and 32,768 output tokens. The price is $7.742 input and $23.367 output per million tokens.

## Strengths
- End-to-end research reports with sources.
- Clarifying questions before long runs.

## Limitations
- China (Beijing) only; no OpenAI-compatible API.
- High per-token price.

## Good for
- Market and literature research reports.
