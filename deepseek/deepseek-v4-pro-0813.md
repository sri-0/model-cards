---
id: deepseek/deepseek-v4-pro-0813
name: DeepSeek V4 Pro 0813
owned_by: deepseek
type: llm
description: DeepSeek V4 Pro 0813 is the August 2026 GA release of DeepSeek V4 Pro (1.6T MoE, 49B active, MIT, 1M context) with much stronger agent performance and DSpark speculative decoding.
aliases: [deepseek-ai/DeepSeek-V4-Pro-0813, deepseek-v4-pro, "~deepseek/deepseek-pro-latest", "deepseek-v4-pro:cloud", "deepseek-v4-pro:0813-cloud"]
context_length: 1048576
max_output_tokens: 393216
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
open_weights: true
license: MIT
release_date: "2026-08-13"
pricing:
  input: 0.66
  output: 1.98
  cache_read: 0.022
benchmarks:
  intelligence_index: 36
  coding_index: 68.8
  agentic_index: 41.3
  omniscience_index: 0.8
  humanitys_last_exam: 41
  gpqa_diamond: 92.8
  scicode: 51
  terminal_bench_4: 14.1
  long_context_reasoning: 80.3
  output_tokens_per_second: 92
  time_to_first_token_seconds: 1.62
benchmark_variant: DeepSeek V4 Pro 0813 (Max)
sources:
  - https://openrouter.ai/deepseek/deepseek-v4-pro-0813
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v4-pro
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813
  - https://api-docs.deepseek.com/news/news260813
  - https://api-docs.deepseek.com/news/news260910
  - https://api-docs.deepseek.com/updates
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://api-docs.deepseek.com/guides/thinking_mode
  - https://openrouter.ai/~deepseek/deepseek-pro-latest
  - https://ollama.com/library/deepseek-v4-pro
  - https://docs.litellm.ai/docs/providers/deepseek
retrieved: "2026-10-16"
---

# DeepSeek V4 Pro 0813

## Overview
DeepSeek V4 Pro 0813 is the official (GA) release of DeepSeek V4 Pro, published 2026-08-13 under the MIT licence: the same 1.6T-parameter MoE (49B active, 1M context) as the April preview with a DSpark speculative-decoding module attached and much stronger agent post-training. The vendor API serves it today as `deepseek-v4-pro` (thinking on by default with low, high and max effort; 384K maximum output; OpenAI, Anthropic and Responses formats; 500 concurrent requests). DeepSeek said on 2026-09-10 that it was phasing V4 Pro out in favour of V4.1 Flash, then kept the API running "until V4.1-Pro launches" at unchanged billing. OpenRouter's router id `~deepseek/deepseek-pro-latest` ("always redirects to the latest model in the DeepSeek Pro family") currently resolves here, and Ollama offers it as the cloud-only tags `deepseek-v4-pro:cloud` and `deepseek-v4-pro:0813-cloud`. LiteLLM's `deepseek/deepseek-v4-pro` reaches this build although that string is the OpenRouter id of the 0423 preview card. Supersedes `deepseek/deepseek-v4-pro`.

## Strengths
- DeepSeek reports Terminal Bench 2.1 87.9, NL2Repo 61.5, Cybergym 83.3, DeepSWE 62.7, Toolathlon-Verified 74.1 and HLE 42.7 (60.0 with tools).
- Artificial Analysis (variant DeepSeek V4 Pro 0813 (Max)): Intelligence Index 36.0, Omniscience Index 0.8, GPQA Diamond 92.8%, HLE 41.0%, Coding Index 68.8.

## Limitations
- Vendor and OpenRouter prices double in peak hours (01:00 to 04:00 and 06:00 to 10:00 UTC on weekdays): $0.66/$1.98 off-peak against $1.32/$3.96 per million tokens; cache hits $0.022/$0.044.
- Terminal-Bench 4.0 14.1% and 92 tokens per second in AA's tests, behind V4.1 Flash.
- Self-hosting needs a cluster (DeepSeek's recipes use 4x GB300 nodes with vLLM or SGLang and DSpark); no Jinja template.

## Good for
- Knowledge-intensive research and long-horizon agents where recall matters.
- Full-codebase analysis within 1M tokens.
- Codex and Claude Code style harnesses through the Responses or Anthropic APIs.
