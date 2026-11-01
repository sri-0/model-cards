---
id: deepseek/deepseek-v3.2-exp
name: DeepSeek V3.2 Exp
owned_by: deepseek
type: llm
description: DeepSeek V3.2 Exp is an experimental September 2025 build of V3.1 Terminus (671B MoE, 37B active, MIT) that introduces DeepSeek Sparse Attention for cheaper long-context inference.
aliases: [deepseek-ai/DeepSeek-V3.2-Exp]
context_length: 163840
max_output_tokens: 147456
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, reasoning, response_format, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
  instruct_type: deepseek-v3.1
open_weights: true
license: MIT
release_date: "2025-09-29"
knowledge_cutoff: "2025-07"
pricing:
  input: 0.27
  output: 0.41
benchmarks:
  intelligence_index: 16.6
  omniscience_index: -31
  humanitys_last_exam: 14.9
  gpqa_diamond: 79.7
  terminal_bench_hard: 31.1
  long_context_reasoning: 72.3
  ifbench: 54.1
  tau2_bench: 33.9
benchmark_variant: DeepSeek V3.2 Exp (Reasoning)
sources:
  - https://openrouter.ai/deepseek/deepseek-v3.2-exp
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v3-2-0925
  - https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp
  - https://api-docs.deepseek.com/news/news250929
  - https://api-docs.deepseek.com/updates
retrieved: "2026-10-16"
---

# DeepSeek V3.2 Exp

## Overview
DeepSeek V3.2 Exp, released 2025-09-29 under the MIT licence, is an experimental intermediate step between V3.1 and DeepSeek's next architecture. It continues V3.1 Terminus (671B MoE, 37B active, 128K context) with DeepSeek Sparse Attention (DSA), a fine-grained sparse attention mechanism meant to cut long-context training and inference cost; DeepSeek aligned the training configuration with Terminus so the effect of DSA could be measured. Vendor API prices were cut by more than 50% with this release. The vendor ids `deepseek-chat` (non-thinking) and `deepseek-reasoner` (thinking) served it until DeepSeek V3.2 replaced it on 2025-12-01; the vendor API no longer serves it and it is available from the weights or through OpenRouter. Superseded by `deepseek/deepseek-v3.2`.

## Strengths
- DeepSeek reports parity with Terminus: MMLU-Pro 85.0, AIME 2025 89.3, Codeforces 2121, SWE-bench Verified 67.8, Terminal-bench 37.7, BrowseComp 40.1.
- Artificial Analysis (variant DeepSeek V3.2 Exp (Reasoning)): long-context reasoning 72.3%, GPQA Diamond 79.7%, Terminal-Bench Hard 31.1%.
- Day-0 vLLM support, SGLang Docker images (`lmsysorg/sglang:dsv32`) and open TileLang, DeepGEMM and FlashMLA kernels.

## Limitations
- Experimental: built to validate DSA rather than raise accuracy; HLE 19.8 against 21.7 for Terminus in DeepSeek's table.
- AA Intelligence Index 16.6, tau2-bench 33.9%, Omniscience Index -31.0; no AA speed figures.
- Early demo code had a RoPE layout bug in the indexer, fixed 2025-11-17; use the updated inference code.
- No cached-input price on OpenRouter.

## Good for
- Long-context workloads where DSA's lower cost matters.
- Research on sparse attention with open kernels.
- Reasoning and agent tasks at Terminus-level quality for less.
