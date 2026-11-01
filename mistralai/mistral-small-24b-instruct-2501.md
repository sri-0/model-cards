---
id: mistralai/mistral-small-24b-instruct-2501
name: Mistral Small 3
owned_by: mistralai
type: llm
description: Mistral Small 3 is a 24B Apache-2.0 open-weight instruct model from Mistral AI, tuned for low latency, with a 32K context window, released in January 2025.
aliases: [mistral-small-2501, mistralai/Mistral-Small-24B-Instruct-2501, "mistral-small:24b"]
context_length: 32768
max_output_tokens: 16384
capabilities: [structured_output]
supported_parameters: [frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Apache-2.0
release_date: "2025-01-30"
knowledge_cutoff: "2023-10"
pricing:
  input: 0.05
  output: 0.08
benchmarks:
  gpqa_diamond: 46.2
  humanitys_last_exam: 3.8
  ifbench: 26.4
  long_context_reasoning: 0
  output_tokens_per_second: 50.0
  tau2_bench: 19.6
  time_to_first_token_seconds: 1.04
benchmark_variant: Mistral Small 3
sources:
  - https://openrouter.ai/mistralai/mistral-small-24b-instruct-2501
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models/mistralai/mistral-small-24b-instruct-2501/endpoints
  - https://artificialanalysis.ai/models/mistral-small-3
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mistral-small-3-0-25-01
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/mistral-small-3
  - https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501
  - https://huggingface.co/api/models/mistralai/Mistral-Small-24B-Instruct-2501
  - https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501/raw/main/config.json
  - https://ollama.com/library/mistral-small
retrieved: "2026-11-01"
---

# Mistral Small 3

## Overview
Mistral Small 3 (API id mistral-small-2501, version 25.01) was released on 2025-01-30. It is a dense 24B instruct model with a 32K context window and the Tekken tokenizer (131K vocabulary), fine-tuned from Mistral-Small-24B-Base-2501 under Apache 2.0. Mistral says it was trained without reinforcement learning or synthetic data, reaches over 81% on MMLU, runs at 150 tokens per second and over three times faster than Llama 3.3 70B on the same hardware, and fits a single RTX 4090 or a 32 GB MacBook once quantised. The Hugging Face card reports 66.3% on MMLU Pro, 84.8% on HumanEval, 70.6% on MATH and 82.9% on IFEval. Mistral's docs list it as deprecated on 2025-11-06 and retired on 2025-11-30, replaced by Mistral Small 4; Mistral Small 3.1 (March 2025) added image input and 128K context. OpenRouter's only endpoint is DeepInfra in fp8, which does not expose tool parameters, so the capabilities above follow OpenRouter; Mistral documents native function calling and JSON output for the model itself.

## Strengths
- Cheap and fast: $0.05 input and $0.08 output per million tokens on OpenRouter; Artificial Analysis measured 50.0 output tokens per second and 1.04 s to first token.
- Artificial Analysis (Mistral Small 3): 46.2% on GPQA Diamond.
- Permissive licence, base weights for fine-tuning and strong system-prompt adherence per the Hugging Face card.

## Limitations
- 32K context, text only, and 0% on AA-LCR long-context reasoning.
- Weak instruction following and agent results: 26.4% on IFBench and 19.6% on tau2-bench.
- Knowledge base dated 2023-10-01 in Mistral's recommended system prompt. No reasoning mode.
- Retired from Mistral's API.

## Good for
- Fast conversational agents and low-latency function calling when self-hosted.
- Local inference on one consumer GPU for sensitive data.
- Fine-tuning into subject-matter specialists.
