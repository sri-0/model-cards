---
id: qwen/qwen3.6-plus
name: Qwen3.6 Plus
owned_by: qwen
type: llm
description: "Qwen3.6 Plus is Alibaba's hosted flagship Qwen3.6 vision-language mixture-of-experts model with a 1M-token context and large gains in agentic and front-end coding over Qwen3.5 Plus, served on Model Studio as qwen3.6-plus (snapshot 2026-04-02)."
aliases: [qwen3.6-plus, qwen3.6-plus-2026-04-02]
context_length: 1000000
max_output_tokens: 65536
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: false
license: proprietary
release_date: "2026-04-02"
pricing:
  input: 0.325
  output: 1.95
  cache_write: 0.40625
benchmarks:
  intelligence_index: 27
  coding_index: 54.5
  omniscience_index: 0.9
  humanitys_last_exam: 27.8
  gpqa_diamond: 88.2
  terminal_bench_hard: 43.9
  long_context_reasoning: 78.3
  ifbench: 75.2
  tau2_bench: 97.7
  mmmu_pro: 78
  output_tokens_per_second: 56.1
  time_to_first_token_seconds: 2.05
benchmark_variant: Qwen3.6 Plus
sources:
  - https://openrouter.ai/qwen/qwen3.6-plus
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-6-plus
  - https://www.qwencloud.com/models/qwen3.6-plus
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
retrieved: "2026-10-16"
---

# Qwen3.6 Plus

## Overview
Qwen3.6 Plus is Alibaba's hosted flagship tier of the Qwen3.6 series, released on 2026-04-02 (the Model Studio snapshot id is `qwen3.6-plus-2026-04-02`, and the pricing page read on 2026-10-16 says the stable `qwen3.6-plus` is currently equivalent to it). No weights are published. OpenRouter describes a hybrid architecture of efficient linear attention and sparse mixture-of-experts routing, major gains over the 3.5 series in agentic coding, front-end development and reasoning, and strength on 3D scenes, games and repository-level problems; Qwen Cloud adds better general object recognition, OCR and object localisation. It takes text, image and video input with thinking togglable per request. OpenRouter lists a 1,000,000-token context and 65,536-token output; Qwen Cloud gives 991K max input and 65K max output. OpenRouter charges $0.325 input, $1.95 output and $0.40625 cache write per million tokens up to 256,000 prompt tokens, and $1.3, $3.9 and $1.625 from there; Model Studio's International list price is $0.5 and $3 for the first 256K tokens. Model Studio now files the Qwen3.6 models under legacy models that are no longer recommended.

## Strengths
- OpenRouter's listing cites 78.8 on SWE-bench Verified.
- Artificial Analysis (Qwen3.6 Plus): Intelligence Index 27, Coding Index 54.5, tau2-bench 97.7%, GPQA Diamond 88.2%, long-context reasoning 78.3%, MMMU-Pro 78%, IFBench 75.2%, Omniscience 0.9.
- 56.1 tokens per second and 2.05 s to first token in AA's test.

## Limitations
- Terminal-Bench Hard 43.9% and Humanity's Last Exam 27.8% in AA's test.
- Legacy on Model Studio, replaced by Qwen3.7 Plus and Qwen3.8 Max in the recommended list.
- Prompts of 256,000 tokens or more cost four times the base input price on OpenRouter.

## Good for
- Agentic and front-end coding with long context.
- Multimodal agents that read screens, documents and video.
