---
id: qwen/qwen3.6-max-preview
name: Qwen3.6 Max Preview
owned_by: qwen
type: llm
description: "Qwen3.6-Max-Preview is Alibaba's hosted preview of the largest Qwen3.6 model, a text-only reasoning model with a 256K-token context aimed at agentic coding, world knowledge and instruction following; Model Studio deprecated it on 2026-10-10."
aliases: [qwen3.6-max-preview, aihubmix/qwen3.6-max-preview]
context_length: 262144
max_output_tokens: 65536
capabilities: [tool_calling, reasoning, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
release_date: "2026-04-20"
benchmarks:
  gpqa_diamond: 88.8
  humanitys_last_exam: 30.8
  ifbench: 76.6
  long_context_reasoning: 80.7
  tau2_bench: 95.9
  terminal_bench_hard: 43.9
benchmark_variant: Qwen3.6 Max Preview
sources:
  - https://openrouter.ai/qwen/qwen3.6-max-preview
  - https://openrouter.ai/api/v1/models/qwen/qwen3.6-max-preview/endpoints
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-6-max
  - https://alibabacloud.com/blog/qwen3-6-max-preview-smarter-sharper-still-evolving_603055
  - http://web.archive.org/web/20260606115938/https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://www.alibabacloud.com/help/en/model-studio/model-depreciation
  - https://www.alibabacloud.com/help/id/model-studio/model-depreciation
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Qwen3.6 Max Preview

## Overview
Qwen3.6-Max-Preview (Model Studio id `qwen3.6-max-preview`) was an early preview of the largest Qwen3.6 model, served through Alibaba Cloud Model Studio and Qwen Studio with no published weights. OpenRouter keeps a `qwen/qwen3.6-max-preview` record (added 2026-04-27) but it is not in OpenRouter's model list and has no endpoints; its description calls the model a sparse mixture-of-experts of about 1 trillion parameters with a 262K context. Only text input was opened. Model Studio listed a 256K context, 64K maximum output and a 128K thinking budget, with thinking mode, function calling and structured output but no built-in tools or batch calls; `preserve_thinking` keeps reasoning from earlier turns. International pricing was $1.30 input and $7.80 output per million tokens up to 128K input, and $2/$12 from 128K to 256K. Model Studio's release table dates it 2026-04-20 in China (Beijing), as does AA, and 2026-04-14 in Singapore. It was deprecated on 2026-10-10 with qwen3.7-max as the replacement.

## Strengths
- Qwen reports gains over Qwen3.6-Plus: SkillsBench +9.9, SciCode +6.3, NL2Repo +5.0, Terminal-Bench 2.0 +3.8, SuperGPQA +2.3.
- Artificial Analysis (Qwen3.6 Max Preview): 95.9% tau2-bench, 88.8% GPQA Diamond, 80.7% long-context reasoning, 76.6% IFBench, 43.9% Terminal-Bench Hard.

## Limitations
- A preview: Qwen said it was still under active development, and Model Studio retires preview models on 14 days' notice.
- Text only, with no built-in tools.
- Deprecated on Model Studio.

## Good for
- Agentic coding and front-end work during its preview window.
- Comparing against the Qwen3.7 Max models that replaced it.
