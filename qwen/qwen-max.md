---
id: qwen/qwen-max
name: Qwen-Max
owned_by: qwen
type: llm
description: "Qwen-Max is Alibaba Cloud Model Studio's hosted large mixture-of-experts Qwen model; its stable international version is Qwen2.5-Max (qwen-max-2025-01-25), pretrained on over 20 trillion tokens, with a 32K-token context, and Model Studio now lists it as legacy."
aliases: [qwen-max, qwen-max-latest, qwen-max-2025-01-25, qwen-max-0125, qwen-max-2024-09-19, qwen-max-0919, dashscope/qwen-max]
context_length: 32768
max_output_tokens: 8192
capabilities: [tool_calling, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
release_date: "2025-01-28"
benchmarks:
  gpqa_diamond: 58.7
  humanitys_last_exam: 3.8
benchmark_variant: Qwen2.5 Max
sources:
  - https://openrouter.ai/api/v1/models/qwen/qwen-max/endpoints
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen-2-5-max
  - https://qwenlm.github.io/blog/qwen2.5-max/
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Qwen-Max

## Overview
Qwen-Max (DashScope id `qwen-max`) is the top tier of Model Studio's first commercial Qwen line. Its international stable version is `qwen-max-2025-01-25` (also `qwen-max-0125`), which the Qwen team announced on 2025-01-28 as Qwen2.5-Max: a large mixture-of-experts model pretrained on over 20 trillion tokens and post-trained with supervised fine-tuning and RLHF. Weights and parameter count are not published. OpenRouter keeps a `qwen/qwen-max` record but it is not in OpenRouter's model list and has no endpoints. Model Studio gives a 32,768-token context (30,720 input, 8,192 output) at $1.60 input and $6.40 output per million tokens internationally, with batch calls at half price. In China (Beijing) the stable id pointed at the older `qwen-max-2024-09-19`, and `qwen-max-latest` had a 131,072-token context there. Model Studio's October 2026 text generation page lists "qwen-max and its snapshots" under legacy models: no thinking mode, but function calling, built-in tools and structured output.

## Strengths
- Qwen reports Qwen2.5-Max ahead of DeepSeek V3 on Arena-Hard, LiveBench, LiveCodeBench and GPQA-Diamond, and competitive on MMLU-Pro.
- OpenAI-compatible API with function calling and structured output.

## Limitations
- The 32K context and 8K output are small next to later Qwen models.
- No reasoning mode.
- Artificial Analysis (Qwen2.5 Max): 58.7% on GPQA Diamond and 3.8% on Humanity's Last Exam; AA marks it deprecated.
- Model Studio no longer recommends it; its current flagship is qwen3.8-max.

## Good for
- Existing integrations pinned to qwen-max or qwen-max-2025-01-25.
- Short-context chat and tool calling where a non-reasoning model is wanted.
