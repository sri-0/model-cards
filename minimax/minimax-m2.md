---
id: minimax/minimax-m2
name: MiniMax M2
owned_by: minimax
type: llm
description: MiniMax-M2 is MiniMax's October 2025 open-weight mixture-of-experts text model (230B total, 10B active parameters) with interleaved thinking, built for fast, cheap coding and agentic tool-use loops.
aliases: [MiniMax-M2, MiniMaxAI/MiniMax-M2, minimax.minimax-m2, minimaxai/minimax-m2-maas]
context_length: 204800
max_output_tokens: 131072
capabilities: [tool_calling, reasoning]
supported_parameters: [include_reasoning, max_tokens, reasoning, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Modified MIT
release_date: "2025-10-27"
pricing:
  input: 0.255
  output: 1.02
benchmarks:
  gpqa_diamond: 77.7
  humanitys_last_exam: 13.7
  ifbench: 72.3
  long_context_reasoning: 64.3
  output_tokens_per_second: 122.9
  tau2_bench: 86.8
  terminal_bench_hard: 25.8
  time_to_first_token_seconds: 1.34
benchmark_variant: MiniMax-M2
sources:
  - https://openrouter.ai/minimax/minimax-m2
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/minimax-m2
  - https://huggingface.co/MiniMaxAI/MiniMax-M2
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-M2
  - https://huggingface.co/MiniMaxAI/MiniMax-M2/raw/main/config.json
  - https://raw.githubusercontent.com/MiniMax-AI/MiniMax-M2/main/LICENSE
  - https://www.minimax.io/news/minimax-m2
  - https://platform.minimax.io/docs/faq/models.md
  - https://platform.minimax.io/docs/release-notes/models.md
  - https://platform.minimax.io/docs/api-reference/text-anthropic-api.md
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# MiniMax M2

## Overview
MiniMax-M2 was released on 2025-10-27 per MiniMax's release notes and news post (Artificial Analysis says 2025-10-26; the Hugging Face repo dates from 2025-10-22), with free API access until 2025-11-07. It is a 230B-total, 10B-active mixture-of-experts model: 62 layers, 256 experts with 8 routed per token, softmax attention in every layer (unlike the lightning-attention M1), FP8 weights and 196,608 positions in config.json; OpenRouter lists a 204,800-token context and 131,072 output tokens. It takes text only and is an interleaved thinking model: MiniMax says the thinking content of earlier assistant turns must be passed back in the history, in its original `<think>` tags, or quality drops. The licence is MIT with one addition: products with more than 100 million monthly active users or US$30 million in annual recurring revenue must display "MiniMax M2" in their interface. MiniMax's model list marks M2 retired on its own API.

## Strengths
- Fast: 122.9 output tokens per second and 1.34 s to first token on Artificial Analysis (MiniMax-M2).
- AA: 86.8% on tau2-bench, 72.3% on IFBench and 77.7% on GPQA Diamond.
- MiniMax reports 69.4% SWE-bench Verified, 46.3% Terminal-Bench and 44% BrowseComp.
- $0.255 input and $1.02 output per million tokens on OpenRouter; on Bedrock (`minimax.minimax-m2`) and Vertex (`minimaxai/minimax-m2-maas`).

## Limitations
- Text only; no structured-output parameter on OpenRouter.
- 13.7% on Humanity's Last Exam and 25.8% on Terminal-Bench Hard on AA. Later M2.x releases score higher on GPQA Diamond, HLE, AA-LCR and Terminal-Bench Hard, though AA measured them as slower.
- Retired from MiniMax's API; LiteLLM's catalogue gives the Vertex endpoint a 2026-10-21 deprecation date.
- Thinking cannot be disabled and must be round-tripped in the conversation history.

## Good for
- High-throughput agent loops where speed matters more than peak accuracy.
- Local serving with SGLang, vLLM, MLX-LM or Transformers under a permissive licence.
