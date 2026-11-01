---
id: openai/gpt-oss-120b
name: gpt-oss-120b
owned_by: openai
type: llm
description: gpt-oss-120b is OpenAI's open-weight (Apache-2.0) 117B-parameter mixture-of-experts reasoning model with 5.1B active parameters, quantised in MXFP4 to fit one 80 GB GPU.
aliases: [openai/gpt-oss-120b, "gpt-oss:120b", "openai.gpt-oss-120b-1:0", groq/openai/gpt-oss-120b, together_ai/openai/gpt-oss-120b, fireworks_ai/accounts/fireworks/models/gpt-oss-120b, cerebras/gpt-oss-120b, azure_ai/gpt-oss-120b, vertex_ai/openai/gpt-oss-120b-maas, databricks/databricks-gpt-oss-120b]
context_length: 131072
max_output_tokens: 65536
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_a, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: true
license: Apache-2.0
release_date: "2025-08-05"
knowledge_cutoff: "2024-06"
pricing:
  input: 0.15
  output: 0.6
  cache_read: 0.075
benchmarks:
  intelligence_index: 11.6
  coding_index: 30.4
  agentic_index: 3.7
  omniscience_index: -49.2
  humanitys_last_exam: 19.6
  gpqa_diamond: 78.2
  scicode: 34
  terminal_bench_hard: 23.5
  terminal_bench_4: 0
  long_context_reasoning: 52
  ifbench: 69
  tau2_bench: 65.8
  output_tokens_per_second: 215.4
  time_to_first_token_seconds: 0.85
benchmark_variant: gpt-oss-120b (High)
sources:
  - https://openrouter.ai/openai/gpt-oss-120b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-oss-120b
  - https://huggingface.co/openai/gpt-oss-120b
  - https://huggingface.co/api/models/openai/gpt-oss-120b
  - https://openai.com/index/introducing-gpt-oss/
  - https://arxiv.org/abs/2508.10925
  - https://github.com/openai/gpt-oss
  - https://ollama.com/library/gpt-oss
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-10-16"
---

# gpt-oss-120b

## Overview
gpt-oss-120b was released on 2025-08-05 under Apache 2.0, with gpt-oss-20b, as OpenAI's first open-weight language models since GPT-2. It is a 36-layer mixture-of-experts transformer with 128 experts per block and 4 active per token, 117B total and 5.1B active parameters, and a 131,072-token context. MXFP4-quantised expert weights let it fit one 80 GB GPU. Training used a mostly English, text-only STEM-heavy corpus with a June 2024 knowledge cutoff and the o200k_harmony tokenizer. Prompts must use the harmony response format; the chain of thought is exposed and unsupervised, and reasoning effort is set to low, medium or high in the system message. OpenAI does not serve it on its own API; OpenRouter, Ollama (gpt-oss:120b), Bedrock, Azure, Groq and Cerebras do.

## Strengths
- OpenAI reports, at high reasoning, 92.5% on AIME 2025, 80.1% on GPQA Diamond, 90.0% on MMLU, 62.4% on SWE-bench Verified and 67.8% on Tau-Bench Retail, near o4-mini.
- Artificial Analysis (gpt-oss-120b (High)): Intelligence Index 11.6, GPQA Diamond 78.2%, IFBench 69.0%, tau2-bench 65.8%, AA-LCR 52.0%.
- 215.4 tokens per second and 0.85 s to first token in AA's measurement.
- Function calling, browsing and Python tool use, Structured Outputs; fine-tunable on one H100 node.

## Limitations
- Text only.
- AA Omniscience Index -49.2 and Humanity's Last Exam 19.6%: it guesses on factual recall.
- Terminal-Bench Hard 23.5%, Terminal-Bench 4.0 at 0% and AA Agentic Index 3.7: long terminal agent tasks are unreliable.
- Non-harmony prompts produce wrong output; raw chain of thought is not for end users. AA's Low effort variant scores lower.

## Good for
- Self-hosted reasoning and agent workloads on one data-centre GPU.
- Cost-sensitive API use at OpenRouter's $0.15 input and $0.60 output per million tokens.
- Fine-tuning for domain tasks under a permissive licence.
