---
id: qwen/qwen3.5-397b-a17b
name: Qwen3.5 397B A17B
owned_by: qwen
type: llm
description: "Qwen3.5 397B A17B is Alibaba's flagship open-weight (Apache-2.0) vision-language mixture-of-experts model with 397B total and 17B active parameters, Gated DeltaNet attention, thinking mode and a 262,144-token native context; the hosted Qwen3.5 Plus is its production version."
aliases: [Qwen/Qwen3.5-397B-A17B, qwen3.5-397b-a17b]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2026-02-16"
pricing:
  input: 0.5
  output: 3.6
  cache_read: 0.3
benchmarks:
  intelligence_index: 18.4
  omniscience_index: -30.8
  humanitys_last_exam: 29
  gpqa_diamond: 89.3
  scicode: 44.8
  terminal_bench_hard: 40.9
  terminal_bench_4: 0
  long_context_reasoning: 77.3
  ifbench: 78.8
  tau2_bench: 95.6
  mmmu_pro: 77.3
  output_tokens_per_second: 55.7
  time_to_first_token_seconds: 2.45
benchmark_variant: Qwen3.5 397B A17B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3.5-397b-a17b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-5-397b-a17b
  - https://huggingface.co/Qwen/Qwen3.5-397B-A17B
  - https://github.com/QwenLM/Qwen3.5
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
retrieved: "2026-10-16"
---

# Qwen3.5 397B A17B

## Overview
Qwen3.5-397B-A17B was the first Qwen3.5 release, on 2026-02-16. It is a vision-language mixture-of-experts model with 397B total and 17B activated parameters: 60 layers alternating three Gated DeltaNet blocks with one gated attention block, each followed by a 512-expert MoE layer activating 10 routed experts plus 1 shared. Qwen names the hosted Qwen3.5 Plus as its production version, with a 1M-token default context, built-in tools and adaptive tool use (see qwen/qwen3.5-plus-02-15). Native context is 262,144 tokens (1,010,000 with YaRN); OpenRouter lists 262,144 with a 235,929-token output limit and $0.3 cached-input pricing. Thinking is on by default and Qwen states 201 supported languages. Weights are Apache-2.0; Model Studio serves the open model as `qwen3.5-397b-a17b` under its legacy models at $0.6 input and $3.6 output per million tokens. It is not in the Ollama library.

## Strengths
- Qwen reports SWE-bench Verified 76.4, Terminal Bench 2 52.5, GPQA Diamond 88.4, TAU2-Bench 86.7, BrowseComp 69.0, MMMU-Pro 79.0, MathVision 88.6 and OSWorld-Verified 62.2, compared against GPT-5.2, Claude 4.5 Opus and Gemini-3 Pro.
- Artificial Analysis (Qwen3.5 397B A17B, Reasoning): tau2-bench 95.6%, GPQA Diamond 89.3%, IFBench 78.8%, MMMU-Pro 77.3%, long-context reasoning 77.3%.

## Limitations
- AA Intelligence Index 18.4, Omniscience -30.8, Humanity's Last Exam 29%, Terminal-Bench Hard 40.9% and Terminal-Bench 4.0 0%.
- 55.7 tokens per second in AA's test.
- 397B of weights need a multi-GPU node; keep at least 128K tokens of context to preserve thinking.

## Good for
- Self-hosted frontier-class coding, search and GUI agents.
- Multimodal reasoning over documents and video.
- Teams that want the open counterpart of Qwen3.5 Plus.
