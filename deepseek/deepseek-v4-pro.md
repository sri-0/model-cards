---
id: deepseek/deepseek-v4-pro
name: DeepSeek V4 Pro 0423
owned_by: deepseek
type: llm
description: DeepSeek V4 Pro 0423 is the April 2026 preview of DeepSeek's flagship V4 MoE model (1.6T total, 49B active, MIT) with a 1M-token context and three reasoning modes.
aliases: [deepseek-ai/DeepSeek-V4-Pro]
context_length: 1048576
max_output_tokens: 384000
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_completion_tokens, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
open_weights: true
license: MIT
release_date: "2026-04-24"
pricing:
  input: 0.430824
  output: 0.861648
  cache_read: 0.035902
benchmarks:
  intelligence_index: 30.4
  coding_index: 59.4
  agentic_index: 26.3
  omniscience_index: -10.7
  humanitys_last_exam: 37.5
  gpqa_diamond: 88.8
  scicode: 50.8
  terminal_bench_hard: 46.2
  terminal_bench_4: 14.6
  long_context_reasoning: 74.7
  ifbench: 76.5
  tau2_bench: 96.2
  output_tokens_per_second: 83.1
  time_to_first_token_seconds: 1.81
benchmark_variant: DeepSeek V4 Pro 0424 (Max)
sources:
  - https://openrouter.ai/deepseek/deepseek-v4-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v4-pro-0424
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
  - https://api-docs.deepseek.com/news/news260424
  - https://api-docs.deepseek.com/updates
  - https://docs.litellm.ai/docs/providers/deepseek
retrieved: "2026-10-16"
---

# DeepSeek V4 Pro 0423

## Overview
DeepSeek V4 Pro 0423 is the preview of DeepSeek's flagship V4 model, released 2026-04-24 under the MIT licence (Hugging Face repo `deepseek-ai/DeepSeek-V4-Pro`, created 2026-04-22): a 1.6T-parameter MoE with 49B active, a 1M-token context, FP4 experts with FP8 elsewhere, pre-trained on more than 32T tokens with the Muon optimiser. Its hybrid attention (Compressed Sparse Attention plus Heavily Compressed Attention) needs, per DeepSeek, 27% of the per-token FLOPs and 10% of the KV cache of V3.2 at 1M tokens. The vendor id `deepseek-v4-pro` served this preview from 2026-04-24 until the 0813 GA build replaced it under the same id on 2026-08-13; the vendor no longer serves the preview, which remains available as weights and on OpenRouter. LiteLLM's `deepseek/deepseek-v4-pro` is the vendor id, so it now means the 0813 build rather than this card. Artificial Analysis names this release 0424. Superseded by `deepseek/deepseek-v4-pro-0813`.

## Strengths
- DeepSeek reports for Pro Max: LiveCodeBench 93.5, Codeforces 3206, SWE-bench Verified 80.6, BrowseComp 83.4, SimpleQA-Verified 57.9, MRCR 1M 83.5.
- Artificial Analysis (variant DeepSeek V4 Pro 0424 (Max)): tau2-bench 96.2%, IFBench 76.5%, Terminal-Bench Hard 46.2%, Coding Index 59.4.
- Three reasoning modes; OpenRouter maps `xhigh` effort to max.

## Limitations
- Agentic Index 26.3 and Terminal-Bench 4.0 14.6% in AA's tests; the GA release scores far higher on DeepSeek's agent benchmarks.
- 83.1 tokens per second and 1.81 s to first token; Omniscience Index -10.7.
- Self-hosting 1.6T parameters needs a multi-GPU cluster; no Jinja template; DeepSeek recommends a 384K context for think max.
- OpenRouter's top provider offers 1,024,000 tokens of context and 384,000 of output.

## Good for
- Knowledge-heavy and maths tasks pinned to the April 2026 checkpoint.
- Full-codebase analysis within 1M tokens.
- Tool-calling workflows that need strict instruction following.
