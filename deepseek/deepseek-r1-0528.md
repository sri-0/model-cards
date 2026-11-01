---
id: deepseek/deepseek-r1-0528
name: DeepSeek R1 0528
owned_by: deepseek
type: llm
description: DeepSeek R1 0528 is the May 2025 update of DeepSeek's R1 reasoning model (671B MoE, 37B active, MIT) with deeper reasoning, fewer hallucinations, JSON output and function calling.
aliases: [deepseek-ai/DeepSeek-R1-0528, "deepseek-r1:671b"]
context_length: 163840
max_output_tokens: 32768
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
  instruct_type: deepseek-r1
open_weights: true
license: MIT
release_date: "2025-05-28"
knowledge_cutoff: "2025-03"
pricing:
  input: 0.5
  output: 2.15
  cache_read: 0.35
benchmarks:
  intelligence_index: 13.1
  omniscience_index: -27.4
  humanitys_last_exam: 15.8
  gpqa_diamond: 81.3
  terminal_bench_hard: 15.9
  long_context_reasoning: 55.7
  ifbench: 39.6
  tau2_bench: 36.5
  output_tokens_per_second: 34.5
  time_to_first_token_seconds: 1.06
benchmark_variant: "DeepSeek R1 0528 (May '25)"
sources:
  - https://openrouter.ai/deepseek/deepseek-r1-0528
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-r1
  - https://huggingface.co/deepseek-ai/DeepSeek-R1-0528
  - https://api-docs.deepseek.com/news/news250528
  - https://api-docs.deepseek.com/updates
  - https://ollama.com/library/deepseek-r1
retrieved: "2026-10-16"
---

# DeepSeek R1 0528

## Overview
DeepSeek R1 0528 is the 2025-05-28 revision of R1 (671B MoE, 37B active, MIT licence, 128K context per the R1 card). DeepSeek credits extra post-training compute and algorithmic changes for deeper reasoning: on AIME 2025 the model now averages 23K tokens per question against 12K before. It adds a lower hallucination rate, system-prompt support, JSON output and function calling, and no longer needs a forced "<think>" prefix. The vendor id `deepseek-reasoner` served it from 2025-05-28 until DeepSeek V3.1 took over on 2025-08-21; the id was retired on 2026-07-24, so the model is now available from the weights or third parties such as OpenRouter. Ollama's `deepseek-r1:671b` tag (404 GB) is this revision; the 8B Qwen3 distillation is a separate model. Superseded by `deepseek/deepseek-chat-v3.1` in thinking mode.

## Strengths
- DeepSeek reports AIME 2025 87.5% (from 70.0%), GPQA Diamond 81.0%, LiveCodeBench 73.3%, Aider-Polyglot 71.6%, SWE-bench Verified 57.6% and Tau-bench 53.5% airline / 63.9% retail.
- Artificial Analysis (variant DeepSeek R1 0528 (May '25)): GPQA Diamond 81.3%, HLE 15.8%, long-context reasoning 55.7%, tau2-bench 36.5%.
- Improved front-end generation.

## Limitations
- Long outputs: DeepSeek's evaluations used a 64K generation limit, and OpenRouter caps output at 32,768 tokens.
- Slow in AA's measurement: 34.5 tokens per second.
- Terminal-Bench Hard 15.9%, Omniscience Index -27.4.
- Same multi-node FP8 deployment as V3; DeepSeek recommends temperature 0.6.

## Good for
- Maths, science and competition coding where accuracy matters more than token cost.
- Reasoning with function calling in OpenAI-compatible stacks.
- Front-end prototypes with visible reasoning.
