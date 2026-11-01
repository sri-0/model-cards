---
id: openai/gpt-oss-20b
name: gpt-oss-20b
owned_by: openai
type: llm
description: gpt-oss-20b is OpenAI's open-weight (Apache-2.0) 21B-parameter mixture-of-experts reasoning model with 3.6B active parameters that runs within 16 GB of memory.
aliases: [openai/gpt-oss-20b, "gpt-oss:20b", "openai.gpt-oss-20b-1:0", groq/openai/gpt-oss-20b, together_ai/openai/gpt-oss-20b, fireworks_ai/accounts/fireworks/models/gpt-oss-20b, vertex_ai/openai/gpt-oss-20b-maas, databricks/databricks-gpt-oss-20b, cloudflare/@cf/openai/gpt-oss-20b]
context_length: 131072
max_output_tokens: 32768
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: true
license: Apache-2.0
release_date: "2025-08-05"
knowledge_cutoff: "2024-06"
pricing:
  input: 0.018
  output: 0.09
  cache_read: 0.009
benchmarks:
  intelligence_index: 9
  omniscience_index: -63
  humanitys_last_exam: 11
  gpqa_diamond: 68.8
  scicode: 38.9
  terminal_bench_hard: 10.6
  terminal_bench_4: 0
  long_context_reasoning: 34.7
  ifbench: 65.1
  tau2_bench: 60.2
  output_tokens_per_second: 225.7
  time_to_first_token_seconds: 0.73
benchmark_variant: gpt-oss-20b (High)
sources:
  - https://openrouter.ai/openai/gpt-oss-20b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-oss-20b
  - https://huggingface.co/openai/gpt-oss-20b
  - https://huggingface.co/api/models/openai/gpt-oss-20b
  - https://openai.com/index/introducing-gpt-oss/
  - https://arxiv.org/abs/2508.10925
  - https://github.com/openai/gpt-oss
  - https://ollama.com/library/gpt-oss
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-10-16"
---

# gpt-oss-20b

## Overview
gpt-oss-20b was released on 2025-08-05 with gpt-oss-120b under Apache 2.0. It is a 24-layer mixture-of-experts transformer with 32 experts per block and 4 active per token, 21B total and 3.6B active parameters, and the same 131,072-token context as its sibling. With MXFP4-quantised expert weights it runs within 16 GB of memory, aimed at edge devices and local inference. Training data was mostly English STEM-heavy text with a June 2024 knowledge cutoff. The model only works with the harmony response format (chat templates apply it), exposes an unsupervised chain of thought and takes a low, medium or high reasoning effort from the system message. OpenAI does not serve it through its own API; OpenRouter, Ollama (gpt-oss:20b), Bedrock, Groq, Cloudflare and Fireworks do.

## Strengths
- OpenAI reports, at high reasoning, 91.7% on AIME 2025, 71.5% on GPQA Diamond, 85.3% on MMLU and 60.7% on SWE-bench Verified, matching or beating o3-mini.
- Artificial Analysis (gpt-oss-20b (High)): Intelligence Index 9.0, SciCode 38.9%, IFBench 65.1%, tau2-bench 60.2%.
- 225.7 tokens per second and 0.73 s to first token in AA's measurement.
- OpenRouter charges $0.018 per million input and $0.09 per million output tokens; fine-tunable on consumer hardware.

## Limitations
- Text only.
- AA Omniscience Index -63.0, Humanity's Last Exam 11.0% and AA-LCR 34.7%: weak factual recall and long-context reasoning.
- Terminal-Bench Hard 10.6% and Terminal-Bench 4.0 at 0%.
- Harmony format is mandatory; the raw chain of thought may contain content that should not reach users. AA's Low effort variant scores lower.

## Good for
- Local assistants and coding helpers on a 16 GB GPU or laptop.
- High-volume, low-cost reasoning calls where o3-mini-level quality is enough.
- Fine-tuning experiments and chain-of-thought monitoring research.
