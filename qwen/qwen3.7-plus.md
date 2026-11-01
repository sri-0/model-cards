---
id: qwen/qwen3.7-plus
name: Qwen3.7 Plus
owned_by: qwen
type: llm
description: "Qwen3.7 Plus is Alibaba's cost-effective hosted Qwen3.7 model with text and image input, a 1M-token context and multimodal agent abilities such as screen reading, GUI and mobile-app navigation and code from visual references, served on Model Studio as qwen3.7-plus (snapshot 2026-05-26)."
aliases: [qwen3.7-plus, qwen3.7-plus-2026-05-26]
context_length: 1000000
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
release_date: "2026-06-01"
pricing:
  input: 0.32
  output: 1.28
  cache_read: 0.064
  cache_write: 0.4
benchmarks:
  intelligence_index: 25.2
  coding_index: 55.9
  agentic_index: 17.5
  omniscience_index: 1.1
  humanitys_last_exam: 35.6
  gpqa_diamond: 90
  scicode: 46.1
  terminal_bench_hard: 47
  terminal_bench_4: 1
  long_context_reasoning: 73
  ifbench: 78
  tau2_bench: 93
  mmmu_pro: 80.5
  output_tokens_per_second: 56
  time_to_first_token_seconds: 2.28
benchmark_variant: Qwen3.7 Plus
sources:
  - https://openrouter.ai/qwen/qwen3.7-plus
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-7-plus
  - https://www.qwencloud.com/models/qwen3.7-plus
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
retrieved: "2026-10-16"
---

# Qwen3.7 Plus

## Overview
Qwen3.7 Plus is the cost-effective hosted tier of Alibaba's Qwen3.7 series, released on 2026-06-01 according to Artificial Analysis (OpenRouter listed it on 2026-06-03), with no published weights. Alibaba Cloud Model Studio's pricing page (read 2026-10-16) says the stable `qwen3.7-plus` is currently equivalent to `qwen3.7-plus-2026-05-26`, and the text-generation page recommends it for general use. Qwen Cloud and OpenRouter describe a comprehensive upgrade of the series' vision-language abilities on top of its text capability, keeping full-stack agent intelligence for coding, tool use and productivity; its distinguishing trait is multimodal interactive hybrid agent capability: perceiving real-world scenes, reading screens and interacting with GUIs, generating code from visual references and navigating mobile apps end to end. OpenRouter lists text and image input (Qwen Cloud and Model Studio also list video), a 1,000,000-token context and 131,072-token output. OpenRouter charges $0.32 input, $1.28 output, $0.064 cache read and $0.4 cache write per million tokens up to 256,000 prompt tokens, and $0.96, $3.84, $0.192 and $1.2 from there; Model Studio's International list price is $0.4 and $1.6 for the first 256K tokens with a limited-time 20% discount.

## Strengths
- Artificial Analysis (Qwen3.7 Plus): Intelligence Index 25.2, Coding Index 55.9, MMMU-Pro 80.5%, GPQA Diamond 90%, IFBench 78%, tau2-bench 93%, Terminal-Bench Hard 47%, Humanity's Last Exam 35.6%.
- Screen reading, GUI and mobile-app navigation, code from visual references.
- 56 tokens per second and 2.28 s to first token in AA's test.

## Limitations
- Agentic Index 17.5, Terminal-Bench 4.0 1% and Omniscience 1.1 in AA's test.
- Long-context reasoning 73%, the weakest of its AA scores.
- Prompts of 256,000 tokens or more cost three times the base price on OpenRouter.

## Good for
- Multimodal agents that operate GUIs and mobile apps.
- General coding and productivity work at Plus-tier cost.
