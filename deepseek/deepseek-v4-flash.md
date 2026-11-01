---
id: deepseek/deepseek-v4-flash
name: DeepSeek V4 Flash 0423
owned_by: deepseek
type: llm
description: DeepSeek V4 Flash 0423 is the April 2026 preview of DeepSeek's efficient V4 MoE model (284B total, 13B active, MIT) with a 1M-token context and three reasoning modes.
aliases: [deepseek-ai/DeepSeek-V4-Flash]
context_length: 1048576
max_output_tokens: 943717
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_completion_tokens, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_a, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
open_weights: true
license: MIT
release_date: "2026-04-24"
pricing:
  input: 0.091
  output: 0.182
  cache_read: 0.0182
benchmarks:
  intelligence_index: 24.2
  coding_index: 52
  agentic_index: 26.3
  omniscience_index: -23.9
  humanitys_last_exam: 34.8
  gpqa_diamond: 89.4
  scicode: 45.3
  terminal_bench_hard: 35.6
  terminal_bench_4: 2.5
  long_context_reasoning: 74.3
  ifbench: 79.2
  tau2_bench: 95
  output_tokens_per_second: 42.4
  time_to_first_token_seconds: 1.71
benchmark_variant: DeepSeek V4 Flash 0420 (Max)
sources:
  - https://openrouter.ai/deepseek/deepseek-v4-flash
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v4-flash-0420
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash
  - https://api-docs.deepseek.com/news/news260424
  - https://api-docs.deepseek.com/updates
  - https://ollama.com/library/deepseek-v4-flash
retrieved: "2026-10-16"
---

# DeepSeek V4 Flash 0423

## Overview
DeepSeek V4 Flash 0423 is the preview of the V4 Flash line, released 2026-04-24 under the MIT licence (Hugging Face repo created 2026-04-22): a 284B-parameter MoE with 13B active, pre-trained on more than 32T tokens and shipped with FP4 experts and FP8 elsewhere. V4 introduced a hybrid attention design (Compressed Sparse Attention plus Heavily Compressed Attention), manifold-constrained hyper-connections and the Muon optimiser, with a 1M-token context and three modes: non-think, think high and think max. On the vendor API the id `deepseek-v4-flash` served this preview from 2026-04-24 until the 0731 release replaced it on 2026-07-31, while `deepseek-chat` and `deepseek-reasoner` pointed at its two modes until they were retired on 2026-07-24. The vendor no longer serves it. OpenRouter keeps it as the 0423 version on a model-versions page where 0731 is current; Artificial Analysis names the same release 0420. Superseded by `deepseek/deepseek-v4-flash-0731`.

## Strengths
- DeepSeek reports for Flash Max: GPQA Diamond 88.1, LiveCodeBench 91.6, SWE-bench Verified 79.0, MRCR 1M 78.7, HLE 34.8, close to the Pro preview.
- Artificial Analysis (variant DeepSeek V4 Flash 0420 (Max)): tau2-bench 95.0%, IFBench 79.2%, GPQA Diamond 89.4%, Coding Index 52.
- Low OpenRouter price: $0.091 input, $0.182 output per million tokens.

## Limitations
- Weak as a terminal agent: AA Terminal-Bench 4.0 2.5%, Agentic Index 26.3; DeepSeek's 0731 table shows 61.8 on Terminal Bench 2.1 against 82.7 for the successor.
- 42.4 tokens per second and 1.71 s to first token in AA's test; Omniscience Index -23.9.
- Self-hosting: no Jinja template (use the `encoding` scripts); DeepSeek recommends at least a 384K context for think max. Ollama's `deepseek-v4-flash` library was retired 2026-08-27 without weights.

## Good for
- Pinned reproductions of the April 2026 preview.
- Cheap long-context reading and summarisation up to 1M tokens.
- Non-agentic reasoning and maths.
