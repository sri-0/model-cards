---
id: minimax/minimax-m2.1
name: MiniMax M2.1
owned_by: minimax
type: llm
description: MiniMax-M2.1 is MiniMax's December 2025 open-weight text model (230B total, 10B active parameters, reasoning always on), tuned over M2 for multilingual coding, tool use, instruction following and long-horizon planning.
aliases: [MiniMax-M2.1, MiniMax-M2.1-highspeed, minimax/MiniMax-M2.1-lightning, MiniMaxAI/MiniMax-M2.1, minimax.minimax-m2.1]
context_length: 204800
max_output_tokens: 131072
capabilities: [tool_calling, reasoning]
supported_parameters: [include_reasoning, max_tokens, reasoning, response_format, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Modified MIT
release_date: "2025-12-22"
pricing:
  input: 0.3
  output: 1.2
  cache_read: 0.03
benchmarks:
  gpqa_diamond: 83.0
  humanitys_last_exam: 23.2
  ifbench: 69.9
  long_context_reasoning: 67.7
  output_tokens_per_second: 39.4
  tau2_bench: 85.4
  terminal_bench_hard: 28.8
  time_to_first_token_seconds: 1.69
benchmark_variant: MiniMax-M2.1
sources:
  - https://openrouter.ai/minimax/minimax-m2.1
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/minimax-m2-1
  - https://huggingface.co/MiniMaxAI/MiniMax-M2.1
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-M2.1
  - https://huggingface.co/MiniMaxAI/MiniMax-M2.1/raw/main/config.json
  - https://raw.githubusercontent.com/MiniMax-AI/MiniMax-M2.1/main/LICENSE
  - https://www.minimax.io/news/minimax-m21
  - https://platform.minimax.io/docs/faq/models.md
  - https://platform.minimax.io/docs/release-notes/models.md
  - https://platform.minimax.io/docs/api-reference/text-anthropic-api.md
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# MiniMax M2.1

## Overview
MiniMax-M2.1 was released on 2025-12-22 per MiniMax's release notes (the news post and Artificial Analysis say 2025-12-23; the Hugging Face repo was created 2025-12-20). It shares M2's architecture: 230B total and 10B active parameters, 62 layers with 256 experts and 8 routed per token, FP8 weights, text only, reasoning always on. MiniMax tuned it for multilingual coding, tool use, instruction following and long-horizon planning, and published the VIBE full-stack benchmark alongside it. OpenRouter lists a 204,800-token context and 131,072 output tokens. The licence is MIT with one addition: any commercial product or service using it must display "MiniMax M2.1" in its interface. The Hugging Face card tags it Modified-MIT; AA records MIT. MiniMax's model list marks M2.1 and M2.1-highspeed retired on its own API.

## Strengths
- Artificial Analysis (MiniMax-M2.1): 83.0% on GPQA Diamond, 85.4% on tau2-bench, 67.7% on AA-LCR and 28.8% on Terminal-Bench Hard, each above M2.
- MiniMax reports 74.0% SWE-bench Verified, 72.5% SWE-bench Multilingual, 49.4% Multi-SWE-bench, 47.9% Terminal-bench 2.0 and 88.6 on VIBE.
- $0.30 input, $1.20 output and $0.03 cache read per million tokens on OpenRouter; on Bedrock as `minimax.minimax-m2.1`.
- Deployment guides for SGLang, vLLM, Transformers, KTransformers and MLX-LM.

## Limitations
- Text only, and no structured-output parameter on OpenRouter.
- 39.4 output tokens per second on AA, a third of M2's measured speed.
- Retired on MiniMax's own API; M2.5 and M2.7 score higher on most of AA's tests.
- Commercial users must show the "MiniMax M2.1" attribution.

## Good for
- Multilingual coding agents and code review on a budget.
- Self-hosted agent back ends under a near-MIT licence.
