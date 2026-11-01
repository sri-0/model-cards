---
id: qwen/qwen3.5-27b
name: Qwen3.5 27B
owned_by: qwen
type: llm
description: "Qwen3.5 27B is Alibaba's 27B-parameter dense open-weight (Apache-2.0) vision-language model with Gated DeltaNet linear attention, thinking mode and a 262,144-token native context."
aliases: [Qwen/Qwen3.5-27B, qwen3.5-27b, "qwen3.5:27b"]
context_length: 262144
max_output_tokens: 81920
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2026-02-24"
pricing:
  input: 0.26
  output: 2.6
benchmarks:
  intelligence_index: 22.9
  omniscience_index: -44
  humanitys_last_exam: 23.9
  gpqa_diamond: 85.8
  terminal_bench_hard: 32.6
  long_context_reasoning: 77.7
  ifbench: 75.6
  tau2_bench: 93.9
  mmmu_pro: 75
  output_tokens_per_second: 76.9
  time_to_first_token_seconds: 5.7
benchmark_variant: Qwen3.5 27B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3.5-27b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-5-27b
  - https://huggingface.co/Qwen/Qwen3.5-27B
  - https://github.com/QwenLM/Qwen3.5
  - https://ollama.com/library/qwen3.5
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
retrieved: "2026-10-16"
---

# Qwen3.5 27B

## Overview
Qwen3.5-27B was released on 2026-02-24 together with the 122B-A10B and 35B-A3B models. It is a dense 27B-parameter vision-language model: 64 layers in a repeating layout of three Gated DeltaNet blocks and one gated attention block with dense feed-forward layers, trained with early fusion on text, image and video tokens. OpenRouter describes its overall capability as comparable to Qwen3.5-122B-A10B. Native context is 262,144 tokens (1,010,000 with YaRN); OpenRouter lists 262,144 with an 81,920-token output limit. Thinking is on by default and can be disabled per request. Weights are Apache-2.0 on Hugging Face, Ollama serves `qwen3.5:27b`, and Alibaba Cloud Model Studio serves the open model as `qwen3.5-27b` (256K context, filed under legacy models at $0.3 input and $2.4 output per million tokens).

## Strengths
- Qwen reports SWE-bench Verified 72.4, Terminal Bench 2 41.6, LiveCodeBench v6 80.7, GPQA Diamond 85.5, IFEval 95.0, MMMU-Pro 75.0 and OSWorld-Verified 56.2.
- Artificial Analysis (Qwen3.5 27B, Reasoning): Intelligence Index 22.9, tau2-bench 93.9%, GPQA Diamond 85.8%, long-context reasoning 77.7%, IFBench 75.6%, MMMU-Pro 75%.
- Supports 201 languages and dialects according to Qwen.

## Limitations
- Omniscience -44, Terminal-Bench Hard 32.6% and Humanity's Last Exam 23.9% in AA's test.
- 5.7 s to first token and 76.9 tokens per second at AA's measured provider.
- Qwen's reference vLLM command uses tensor parallel across 8 GPUs for the full 262,144-token context; keep at least 128K tokens of context to preserve thinking.

## Good for
- Mid-sized agentic coding and tool use with a dense model that is simple to serve.
- Document, GUI and video understanding.
- Local deployment through Ollama.
