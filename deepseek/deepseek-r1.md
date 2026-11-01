---
id: deepseek/deepseek-r1
name: DeepSeek R1
owned_by: deepseek
type: llm
description: DeepSeek R1 is DeepSeek's first open-weight reasoning model (671B MoE, 37B active, MIT), trained with large-scale reinforcement learning on the V3 base and released in January 2025.
aliases: [deepseek-ai/DeepSeek-R1, deepseek-reasoner, deepseek/deepseek-reasoner]
context_length: 64000
max_output_tokens: 16000
capabilities: [tool_calling, reasoning]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
  instruct_type: deepseek-r1
open_weights: true
license: MIT
release_date: "2025-01-20"
knowledge_cutoff: "2024-07"
pricing:
  input: 0.7
  output: 2.5
benchmarks:
  intelligence_index: 11.4
  coding_index: 24.6
  agentic_index: 1.1
  omniscience_index: -32.2
  humanitys_last_exam: 8.5
  gpqa_diamond: 70.8
  scicode: 38.3
  terminal_bench_hard: 6.1
  terminal_bench_4: 0
  long_context_reasoning: 57.7
  ifbench: 39
  tau2_bench: 11.4
  output_tokens_per_second: 148.5
  time_to_first_token_seconds: 1.09
benchmark_variant: "DeepSeek R1 (Jan '25)"
sources:
  - https://openrouter.ai/deepseek/deepseek-r1
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-r1-0120
  - https://huggingface.co/deepseek-ai/DeepSeek-R1
  - https://api-docs.deepseek.com/news/news250120
  - https://api-docs.deepseek.com/updates
  - https://ollama.com/library/deepseek-r1
  - https://docs.litellm.ai/docs/providers/deepseek
retrieved: "2026-10-16"
---

# DeepSeek R1

## Overview
DeepSeek R1 is the reasoning model DeepSeek released on 2025-01-20 under the MIT licence: 671B total parameters, 37B active, 128K context per the Hugging Face card, trained on the V3 base with large-scale reinforcement learning after a cold-start SFT stage. It returns its chain of thought in full. The vendor introduced the API id `deepseek-reasoner` for it (LiteLLM lists it as `deepseek/deepseek-reasoner`); that id was upgraded to R1 0528 on 2025-05-28, later to the V3.x and V4 Flash thinking modes, and retired on 2026-07-24, so the January weights are now available only from Hugging Face or third parties. OpenRouter lists 64,000 tokens of context and a 16,000-token output limit. Ollama's default `deepseek-r1:671b` tag now carries the 0528 revision; the January weights remain as `deepseek-r1:671b-q4_K_M`, `671b-q8_0` and `671b-fp16`. Superseded by `deepseek/deepseek-r1-0528`.

## Strengths
- DeepSeek reports AIME 2024 79.8%, MATH-500 97.3%, GPQA Diamond 71.5%, a Codeforces rating of 2029 and SWE-bench Verified 49.2%.
- Visible reasoning tokens; the licence allows distillation and commercial use.
- Artificial Analysis (variant DeepSeek R1 (Jan '25)): long-context reasoning 57.7%, 148.5 tokens per second.

## Limitations
- Weak tool use: AA tau2-bench 11.4%, Agentic Index 1.1, Terminal-Bench Hard 6.1%.
- DeepSeek advises no system prompt, temperature 0.5 to 0.7 and forcing the output to start with "<think>\n", because the model sometimes skips thinking.
- Omniscience Index -32.2.
- Same multi-node FP8 deployment as V3.

## Good for
- Maths and competitive-programming problems with visible reasoning.
- Generating reasoning traces for distillation.
- Research reproducing the R1 training recipe.
