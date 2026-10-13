---
id: meta-llama/llama-3.3-70b-instruct
name: Llama 3.3 70B Instruct
owned_by: meta
type: llm
description: Llama 3.3 70B Instruct is Meta's open-weight, text-only 70B instruction-tuned model for multilingual dialogue, released in December 2024.
aliases: [Llama-3.3-70B-Instruct, meta/llama-3.3-70b-instruct-maas, "llama3.3:70b", meta-llama/Llama-3.3-70B-Instruct]
context_length: 131072
max_output_tokens: 32768
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Llama3
  instruct_type: llama3
open_weights: true
license: Llama 3.3 Community License
release_date: "2024-12-06"
knowledge_cutoff: "2023-12"
pricing:
  input: 0.59
  output: 0.79
  cache_read: 0.295
benchmarks:
  intelligence_index: 7.7
  coding_index: 11.9
  omniscience_index: -54.2
  humanitys_last_exam: 3.6
  gpqa_diamond: 49.8
  terminal_bench_hard: 3
  long_context_reasoning: 15.7
  ifbench: 47.1
  tau2_bench: 26.6
  output_tokens_per_second: 92.6
  time_to_first_token_seconds: 1.73
benchmark_variant: Llama 3.3 Instruct 70B
sources:
  - https://openrouter.ai/meta-llama/llama-3.3-70b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/llama-3-3-instruct-70b
  - https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
  - https://ollama.com/library/llama3.3
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Llama 3.3 70B Instruct

## Overview
Llama 3.3 70B Instruct is a pretrained and instruction-tuned dense model with text input and text output. Meta optimised it for multilingual dialogue in English, German, French, Italian, Portuguese, Hindi, Spanish and Thai. It has a 131,072-token context window, a December 2023 knowledge cutoff, and is released under the Llama 3.3 Community License. It is widely packaged for local use (for example the Ollama tag `llama3.3:70b`).

## Strengths
- Tool calling and structured outputs are supported by providers on OpenRouter.
- Instruction following and knowledge: Artificial Analysis (Llama 3.3 Instruct 70B) reports 47.1% on IFBench and 49.8% on GPQA Diamond.
- Quick output: 92.6 tokens per second and 1.73 s to first token.
- Mature tooling and many existing deployments.

## Limitations
- Old knowledge (cutoff December 2023) and no reasoning mode or image input.
- Low current scores: Intelligence Index 7.7 (estimated), long-context reasoning 15.7%, tau2-bench 26.6%.
- Omniscience index of -54.2, so check factual answers.
- Artificial Analysis calls it particularly expensive for an open non-reasoning model of its size ($0.59 input and $0.79 output per million tokens on OpenRouter).

## Good for
- General multilingual chat in the eight listed languages.
- Summarisation, classification and extraction where a 70B dense model is already deployed.
- Simple tool-calling flows with short contexts.
