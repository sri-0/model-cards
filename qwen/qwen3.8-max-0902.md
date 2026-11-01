---
id: qwen/qwen3.8-max-0902
name: Qwen3.8 Max 0902
owned_by: qwen
type: llm
description: "Qwen3.8 Max 0902 is the 2026-09-02 snapshot of Alibaba's hosted flagship Qwen3.8 Max, a 2.4T-parameter vision-language mixture-of-experts model with a 1M-token context, reasoning on by default and stronger engineering-scale coding and multi-tool agent work."
aliases: [qwen3.8-max-0902, qwen3.8-max-2026-09-02, qwen3.8-max]
context_length: 1000000
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, reasoning_effort, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
release_date: "2026-09-02"
pricing:
  input: 2
  output: 6
  cache_read: 0.25
benchmarks:
  intelligence_index: 45.4
  coding_index: 76.2
  agentic_index: 56
  omniscience_index: 12
  humanitys_last_exam: 43.1
  gpqa_diamond: 92.8
  scicode: 52.1
  terminal_bench_4: 38.9
  long_context_reasoning: 80.3
  mmmu_pro: 82.8
  output_tokens_per_second: 39.8
  time_to_first_token_seconds: 3.06
benchmark_variant: Qwen3.8 Max (0902)
sources:
  - https://openrouter.ai/qwen/qwen3.8-max-0902
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-8-max
  - https://www.qwencloud.com/models/qwen3.8-max-0902
  - https://www.qwencloud.com/models/qwen3.8-max
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
  - https://www.alibabacloud.com/help/en/model-studio/models
retrieved: "2026-10-16"
---

# Qwen3.8 Max 0902

## Overview
Qwen3.8 Max 0902 is the 2026-09-02 snapshot of Qwen3.8 Max, Alibaba's hosted flagship, served through Alibaba Cloud Model Studio and Qwen Cloud (alias `qwen3.8-max-2026-09-02`); OpenRouter listed it on 2026-09-03. Model Studio's vision page maps the stable `qwen3.8-max` to this snapshot and lists both ids among its current recommended models. Qwen Cloud describes Qwen3.8 Max as a 2.4-trillion-parameter MoE flagship that codes and delivers multi-day projects autonomously, handles legal, financial and design tasks end to end, and applies native visual understanding to very long documents and video; the 0902 snapshot adds engineering-scale coding, steadier multi-tool orchestration and sharper chart reasoning and document parsing. The open-weight, text-only variant is Qwen/Qwen3.8-2.4T-A95B (see qwen/qwen3.8-2.4t-a95b). It takes text, image and video input (up to 2,048 images or 64 videos of 2 hours or 2 GB per request on Model Studio), with reasoning on by default and configurable `reasoning_effort`. OpenRouter lists a 1,000,000-token context and 131,072-token output; Qwen Cloud gives 991K max input, 131K max output and 262K max reasoning tokens. Pricing is $2 input, $6 output and $0.25 cached input per million tokens on OpenRouter, Qwen Cloud and Model Studio alike, in one tier.

## Strengths
- Artificial Analysis (Qwen3.8 Max (0902)): Intelligence Index 45.4, Coding Index 76.2, Agentic Index 56, Terminal-Bench 4.0 38.9%, GPQA Diamond 92.8%, Humanity's Last Exam 43.1%, MMMU-Pro 82.8%, long-context reasoning 80.3%, Omniscience 12.
- Tool calling, structured outputs, built-in tools and explicit prompt caching.

## Limitations
- 39.8 tokens per second and 3.06 s to first token in AA's test.
- The most expensive Qwen3.8 tier apart from Max Prime.
- The stable id may move to a newer snapshot later.

## Good for
- Multi-step software projects and multi-tool agent orchestration.
- Long-document, chart and video analysis in professional domains.
