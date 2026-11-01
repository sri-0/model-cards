---
id: qwen/qwen3.8-27b
name: Qwen3.8 27B
owned_by: qwen
type: llm
description: "Qwen3.8 27B is Alibaba's 27B-parameter dense open-weight (Apache-2.0) vision-language model with Gated DeltaNet attention, thinking on by default with reasoning_effort control and preserved thinking, and a 262,144-token native context extensible to 1,000,000."
aliases: [Qwen/Qwen3.8-27B, qwen3.8-27b, "qwen3.8:27b"]
context_length: 1000000
max_output_tokens: 235929
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_a, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: true
license: Apache-2.0
release_date: "2026-08-14"
pricing:
  input: 0.24
  output: 2.2
  cache_read: 0.05
benchmarks:
  intelligence_index: 33.7
  coding_index: 68.1
  agentic_index: 45.8
  omniscience_index: -10
  humanitys_last_exam: 33.9
  gpqa_diamond: 90.5
  scicode: 46.6
  terminal_bench_4: 5.6
  long_context_reasoning: 82
  mmmu_pro: 76.3
  output_tokens_per_second: 41.3
  time_to_first_token_seconds: 3.96
benchmark_variant: Qwen3.8 27B (Xhigh)
sources:
  - https://openrouter.ai/qwen/qwen3.8-27b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-8-27b
  - https://huggingface.co/Qwen/Qwen3.8-27B
  - https://github.com/QwenLM/Qwen3.8
  - https://ollama.com/library/qwen3.8
  - https://www.qwencloud.com/models/qwen3.8-27b
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
retrieved: "2026-10-16"
---

# Qwen3.8 27B

## Overview
Qwen3.8-27B was released on 2026-08-14 (date from the QwenLM GitHub README). It is a dense 27B-parameter vision-language model on the Qwen3.5 architecture (64 layers of Gated DeltaNet and gated attention blocks) that Qwen positions for coding, professional work, research and long-horizon agent tasks, with image and video understanding up to hour-scale video. Thinking is on by default and can be disabled per request; `reasoning_effort` accepts xhigh (default), medium and low, and `preserve_thinking` is on by default. Native context is 262,144 tokens, extensible to 1,000,000 with YaRN; OpenRouter lists 1,000,000 with a 235,929-token output limit. Weights are Apache-2.0 and work with Transformers, vLLM, SGLang and TokenSpeed; Ollama serves `qwen3.8:27b` (18 GB). Qwen Cloud and Model Studio serve the hosted `qwen3.8-27b` at $0.5 input and $3 output per million tokens with a 1M context.

## Strengths
- Qwen reports Terminal Bench 2.1 (Terminus) 73.0, SWE-bench Pro 61.7, LiveCodeBench v6 90.3, GPQA Diamond 89.2, IFBench 79.5, OSWorld-Verified 84.3, AndroidWorld 81.9 and OmniDocBench 1.5 91.1, against 63.4, 53.5, 83.9, 87.8, 69.1, 63.9, 70.3 and 89.4 for Qwen3.6-27B.
- Artificial Analysis (Qwen3.8 27B, Xhigh): Intelligence Index 33.7, Coding Index 68.1, Agentic Index 45.8, GPQA Diamond 90.5%, long-context reasoning 82%, MMMU-Pro 76.3%. AA also tests Low, Medium and Non-reasoning settings, which score lower.

## Limitations
- Terminal-Bench 4.0 5.6%, Omniscience -10 and Humanity's Last Exam 33.9% in the Xhigh configuration.
- 41.3 tokens per second and 3.96 s to first token at Xhigh; Qwen warns that lower effort can cause more retries in multi-turn agent tasks.
- Contexts beyond 262,144 tokens need YaRN rope scaling in the serving engine.

## Good for
- Coding agents and computer-use or mobile-use agents on a single-node deployment.
- Long-document and long-video analysis.
- Local use through Ollama.
