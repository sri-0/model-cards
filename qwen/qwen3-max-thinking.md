---
id: qwen/qwen3-max-thinking
name: Qwen3 Max Thinking
owned_by: qwen
type: llm
description: "Qwen3-Max-Thinking is the reasoning snapshot of Alibaba's hosted Qwen3-Max (Model Studio id qwen3-max-2026-01-23), with over 1 trillion parameters, adaptive use of built-in search and code tools and a 262K-token context; Model Studio deprecated it on 2026-10-10."
aliases: [qwen3-max-2026-01-23, qwen/qwen3-max-thinking-20260123, dashscope/qwen3-max-2026-01-23, deepinfra/Qwen/Qwen3-Max-Thinking]
context_length: 262144
max_output_tokens: 32768
capabilities: [tool_calling, reasoning, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
release_date: "2026-01-23"
benchmarks:
  gpqa_diamond: 86.1
  humanitys_last_exam: 28.0
  ifbench: 70.7
  long_context_reasoning: 74.3
  tau2_bench: 83.6
  terminal_bench_hard: 24.2
benchmark_variant: Qwen3 Max Thinking
sources:
  - https://openrouter.ai/qwen/qwen3-max-thinking
  - https://openrouter.ai/api/v1/models/qwen/qwen3-max-thinking/endpoints
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-max-thinking
  - https://www.alibabacloud.com/blog/qwen-glasses-debut-at-mwc-barcelona-to-begin-sales-in-china-on-march-8_602834
  - https://www.alibabacloud.com/blog/alibabas-latest-thinking-model-excels-at-adaptive-tool-use_602832
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/id/model-studio/model-depreciation
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Qwen3 Max Thinking

## Overview
Qwen3-Max-Thinking is the reasoning version of Qwen3-Max. Its API id is the dated snapshot `qwen3-max-2026-01-23`, which Model Studio labels "Thinking mode aka Qwen3-Max-Thinking"; thinking is switched with `enable_thinking`, and the snapshot also runs without it. OpenRouter keeps `qwen/qwen3-max-thinking` but it is not in OpenRouter's model list and has no endpoints. Qwen says it scales the 1-trillion-plus-parameter Qwen3-Max with large reinforcement-learning compute and adds an experience-cumulative, multi-round test-time scaling strategy; in Qwen Chat it picks search, memory and code interpreter tools on demand, and on Model Studio thinking mode includes web search, web extraction and a code interpreter. Model Studio gives a 262,144-token context (258,048 input); thinking mode allows 81,920 reasoning and 32,768 answer tokens, non-thinking 65,536. International pricing was tiered at $1.20/$6, $2.40/$12 and $3/$15 per million input/output tokens up to 32K, 128K and 252K input. Qwen documents an Anthropic-compatible endpoint for Claude Code. An earlier thinking preview ran under `qwen3-max-preview` (an alias on qwen/qwen3-max). Model Studio dates the snapshot 2026-01-23 and AA 2026-01-26; it was deprecated on 2026-10-10 in favour of qwen3.7-max.

## Strengths
- Qwen's figures: GPQA 87.4, HLE 30.2 (49.8 with tools), LiveCodeBench v6 85.9, SWE-bench Verified 75.3, IFBench 70.9, Arena-Hard v2 90.2.
- Artificial Analysis (Qwen3 Max Thinking): 86.1% GPQA Diamond, 83.6% tau2-bench, 74.3% long-context reasoning, 70.7% IFBench.

## Limitations
- Text only.
- AA measured 28% on Humanity's Last Exam and 24.2% on Terminal-Bench Hard.
- Deprecated on Model Studio.

## Good for
- Hard maths, science and search-heavy questions.
- Reproducing results reported for Qwen3-Max-Thinking in early 2026.
