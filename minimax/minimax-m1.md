---
id: minimax/minimax-m1
name: MiniMax M1
owned_by: minimax
type: llm
description: MiniMax-M1 is MiniMax's June 2025 open-weight (Apache 2.0) hybrid lightning-attention reasoning model, 456B total and 45.9B active parameters with a native 1M-token context, released in 40K and 80K thinking-budget variants.
aliases: [MiniMax-M1, MiniMaxAI/MiniMax-M1-80k, MiniMaxAI/MiniMax-M1-40k, MiniMaxAI/MiniMax-M1-80k-hf, MiniMaxAI/MiniMax-M1-40k-hf]
context_length: 1000000
max_output_tokens: 40000
capabilities: [tool_calling, reasoning]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, seed, stop, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Apache-2.0
release_date: "2025-06-17"
knowledge_cutoff: "2024-06"
pricing:
  input: 0.55
  output: 2.2
benchmarks:
  gpqa_diamond: 69.7
  humanitys_last_exam: 8.9
  ifbench: 41.8
  long_context_reasoning: 57.7
  output_tokens_per_second: 114.9
  tau2_bench: 34.2
  terminal_bench_hard: 3.0
  time_to_first_token_seconds: 1.57
benchmark_variant: MiniMax M1 80k
sources:
  - https://openrouter.ai/minimax/minimax-m1
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/minimax-m1-80k
  - https://artificialanalysis.ai/models/minimax-m1-40k
  - https://huggingface.co/MiniMaxAI/MiniMax-M1-80k
  - https://huggingface.co/MiniMaxAI/MiniMax-M1-40k
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-M1-80k
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-M1-40k
  - https://huggingface.co/MiniMaxAI/MiniMax-M1-80k/raw/main/config.json
  - https://huggingface.co/MiniMaxAI/MiniMax-M1-80k/raw/main/LICENSE
  - https://huggingface.co/api/models?author=MiniMaxAI
  - https://arxiv.org/abs/2506.13585
retrieved: "2026-11-01"
---

# MiniMax M1

## Overview
MiniMax-M1 is MiniMax's first open-weight reasoning model, released on 2025-06-17 per Artificial Analysis (the 40k weights reached Hugging Face on 2025-06-05 and the 80k on 2025-06-13; the paper is arXiv 2506.13585). It is built on MiniMax-Text-01: 456B total and 45.9B active parameters, 80 layers of hybrid attention with one softmax layer after every seven lightning-attention layers, 32 experts with top-2 routing, and a native 1M-token context. The two variants, `MiniMax-M1-40k` and `MiniMax-M1-80k`, differ in thinking budget and were trained with reinforcement learning (MiniMax's CISPO algorithm) on maths, logic and sandboxed software-engineering tasks. OpenRouter lists a 1,000,000-token context, 40,000 output tokens and a 2024-06-30 knowledge cutoff; the weights are Apache 2.0 (`-hf` repos hold the Transformers-native conversion). Artificial Analysis marks both variants deprecated in favour of MiniMax-M2. The benchmarks above are the 80k variant.

## Strengths
- Long context: 1M tokens natively, and MiniMax reports 73.4% on OpenAI-MRCR at 128K and 56.2% at 1M for the 80k variant.
- Efficient test-time scaling: MiniMax says M1 uses 25% of DeepSeek R1's FLOPs at a 100K-token generation.
- MiniMax reports 56.0% on SWE-bench Verified for the 80k variant.
- Fast on AA: 114.9 output tokens per second and 1.57 s to first token (MiniMax M1 80k).
- Permissive Apache 2.0 licence; function calling documented; vLLM (0.9.2 or later) and Transformers deployment guides.

## Limitations
- Weak agentic and knowledge results on AA for the 80k variant: 3.0% on Terminal-Bench Hard, 34.2% on tau2-bench, 8.9% on Humanity's Last Exam and 41.8% on IFBench. The 40k variant scores lower still (68.2% GPQA Diamond, 2.3% Terminal-Bench Hard, 31.6% tau2-bench).
- Text only, and 456B parameters to host.
- Superseded by MiniMax-M2 in October 2025.

## Good for
- Research on hybrid lightning attention and long-context reinforcement learning.
- Very long single-document tasks under a permissive licence.
