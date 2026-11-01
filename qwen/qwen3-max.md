---
id: qwen/qwen3-max
name: Qwen3 Max
owned_by: qwen
type: llm
description: "Qwen3-Max is Alibaba's hosted Qwen3 flagship of over 1 trillion parameters, released on 2025-09-23 as a non-thinking instruct model with a 262K-token context for coding, agent and tool-calling work; Model Studio deprecated it on 2026-10-10."
aliases: [qwen3-max, qwen3-max-2025-09-23, qwen3-max-preview, dashscope/qwen3-max, dashscope/qwen3-max-preview, novita/qwen/qwen3-max, deepinfra/Qwen/Qwen3-Max]
context_length: 262144
max_output_tokens: 65536
capabilities: [tool_calling, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: false
license: proprietary
release_date: "2025-09-23"
benchmarks:
  gpqa_diamond: 76.4
  humanitys_last_exam: 11.9
  ifbench: 44.1
  long_context_reasoning: 50.0
  tau2_bench: 74.3
  terminal_bench_hard: 20.5
benchmark_variant: Qwen3 Max
sources:
  - https://openrouter.ai/qwen/qwen3-max
  - https://openrouter.ai/api/v1/models/qwen/qwen3-max/endpoints
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-max
  - https://www.alibabacloud.com/blog/qwen3-max-just-scale-it_602621
  - https://qwen.ai/blog?id=241398b9cd6353de490b0f82806c7848c5d2777d&from=research.latest-advancements-list
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-depreciation
  - https://www.alibabacloud.com/help/id/model-studio/model-depreciation
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Qwen3 Max

## Overview
Qwen3-Max is the largest model of Alibaba's Qwen3 series, served only through Alibaba Cloud Model Studio and Qwen Chat (DashScope id `qwen3-max`). OpenRouter keeps a `qwen/qwen3-max` record but it is not in OpenRouter's model list and has no endpoints. Qwen says it has over 1 trillion parameters, was pretrained on 36 trillion tokens with the Qwen3 mixture-of-experts design, and improves on the 2025-09-05 preview (`qwen3-max-preview`) in coding and agent tasks. The 2025-09-23 snapshot is non-thinking only, with a 262,144-token context (258,048 input) and 65,536 output tokens. International pricing was tiered by input length: $1.20/$6 per million input/output tokens up to 32K, $2.40/$12 to 128K and $3/$15 to 252K. The preview also had a thinking mode. By April 2026 the stable `qwen3-max` id pointed at `qwen3-max-2026-01-23` (Qwen3-Max-Thinking, see qwen/qwen3-max-thinking) in the International and China regions, while the Global region stayed on 2025-09-23. Model Studio lists qwen3-max, its snapshots and the preview as deprecated on 2026-10-10, with qwen3.7-max as the replacement.

## Strengths
- Qwen reports 69.6 on SWE-bench Verified and 74.8 on Tau2-Bench; the preview ranked in the top three of the LMArena text leaderboard.
- Artificial Analysis (Qwen3 Max): 74.3% on tau2-bench and 76.4% on GPQA Diamond.
- OpenRouter notes over 100 languages and tuning for RAG and tool calling.

## Limitations
- No thinking mode in the 2025-09-23 snapshot; AA measured 11.9% on Humanity's Last Exam and 50% on long-context reasoning.
- Price rises with prompt length.
- Deprecated on Model Studio.

## Good for
- Interpreting results and integrations that used qwen3-max in late 2025.
- Non-reasoning agent and tool-calling baselines; new work should use a current Qwen Max model.
