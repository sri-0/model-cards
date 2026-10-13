---
id: z-ai/glm-4.7-flash
name: GLM 4.7 Flash
owned_by: z-ai
type: llm
description: GLM-4.7-Flash is Z.ai's small open-weight mixture-of-experts model (about 31B total, 3B active parameters) for lightweight agentic coding, with a 200K-token context window.
aliases: [glm-4.7-flash, zai/glm-4.7-flash, zai-org/GLM-4.7-Flash]
context_length: 200000
max_output_tokens: 117964
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2026-01-19"
pricing:
  input: 0.0605
  output: 0.4
benchmarks:
  intelligence_index: 14.9
  omniscience_index: -62.6
  humanitys_last_exam: 7.6
  gpqa_diamond: 58.1
  terminal_bench_hard: 22
  long_context_reasoning: 41.7
  ifbench: 60.8
  tau2_bench: 98.8
  output_tokens_per_second: 71.1
  time_to_first_token_seconds: 1.67
benchmark_variant: GLM-4.7-Flash (Reasoning)
sources:
  - https://openrouter.ai/z-ai/glm-4.7-flash
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-4-7-flash
  - https://huggingface.co/zai-org/GLM-4.7-Flash
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 4.7 Flash

## Overview
GLM-4.7-Flash was released in January 2026. The model README calls it a 30B-A3B MoE model aimed at lightweight deployment. It takes text input and returns text, with a 200K-token context window. Weights are on Hugging Face as `zai-org/GLM-4.7-Flash` under the MIT licence, with vLLM, SGLang and Transformers listed for local serving. Z.ai recommends turning on Preserved Thinking mode for multi-turn agentic tasks.

## Strengths
- Artificial Analysis places GLM-4.7-Flash (Reasoning) among the leading open-weight models of its size (Intelligence Index 15, marked as estimated, against a median of 8).
- Only about 3B parameters are active per token, so it is cheap to serve.
- Low API price on OpenRouter (0.0605 USD input and 0.4 USD output per million tokens).
- Tool calling and structured output. Optimised for agentic coding, long-horizon planning and tool use, per OpenRouter.
- Short time to first token (about 1.7 seconds).

## Limitations
- Text only.
- Much lower knowledge scores than larger GLM models: Artificial Analysis Omniscience Index is -62.6 and Humanity's Last Exam is 7.6%.
- Slightly slower than average output (about 71 tokens per second) per Artificial Analysis.
- vLLM and SGLang support required their main branches at the time the README was written.

## Good for
- Local or single-node deployment where GPU memory is limited.
- Coding agents and tool-calling workflows on a budget.
- High-volume tasks where a small active parameter count matters.
