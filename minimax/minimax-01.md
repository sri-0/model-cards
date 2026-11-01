---
id: minimax/minimax-01
name: MiniMax-01
owned_by: minimax
type: llm
description: MiniMax-01 is MiniMax's January 2025 open-weight generation, pairing the 456B-parameter (45.9B active) hybrid lightning-attention MiniMax-Text-01 language model with the MiniMax-VL-01 vision model, served on OpenRouter with a 1M-token context and image input.
aliases: [minimax-01, MiniMax-Text-01, MiniMaxAI/MiniMax-Text-01, MiniMaxAI/MiniMax-Text-01-hf]
context_length: 1000192
max_output_tokens: 900172
capabilities: [vision]
supported_parameters: [max_tokens, temperature, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MiniMax Model License
release_date: "2025-01-15"
knowledge_cutoff: "2024-03"
pricing:
  input: 0.2
  output: 1.1
sources:
  - https://openrouter.ai/minimax/minimax-01
  - https://openrouter.ai/api/v1/models
  - https://huggingface.co/MiniMaxAI/MiniMax-Text-01
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-Text-01
  - https://huggingface.co/MiniMaxAI/MiniMax-Text-01/raw/main/config.json
  - https://huggingface.co/MiniMaxAI/MiniMax-Text-01/raw/main/LICENSE-MODEL
  - https://huggingface.co/api/models?author=MiniMaxAI
  - https://arxiv.org/abs/2501.08313
  - https://platform.minimax.io/docs/release-notes/models.md
  - https://platform.minimax.io/docs/faq/models.md
retrieved: "2026-11-01"
---

# MiniMax-01

## Overview
MiniMax-01 is OpenRouter's name for MiniMax's first open-weight generation, released on 2025-01-15 (MiniMax release notes; the model licence carries the same date) and described in arXiv 2501.08313: MiniMax-Text-01 for text and MiniMax-VL-01 for image understanding, which has its own card (minimax/minimax-vl-01). MiniMax-Text-01 has 456B total and 45.9B activated parameters over 80 layers, a hybrid of lightning (linear) attention with one softmax-attention layer after every seven, 32 experts with top-2 routing and a 200,064-token vocabulary. It was trained at 1M tokens of context and MiniMax says it handles up to 4M at inference (config.json allows 10,240,000 positions). OpenRouter lists a 1,000,192-token context, 900,172 output tokens, text and image input and a 2024-03-31 knowledge cutoff. Weights are under the MiniMax Model License (`MiniMaxAI/MiniMax-Text-01`; `MiniMax-Text-01-hf` is the Transformers-native conversion). Artificial Analysis has no page for it.

## Strengths
- Long-context retrieval: MiniMax reports RULER 0.910 at 1M tokens and 0.947 at 128K, and 56.5 overall on LongBench v2 with chain of thought.
- MiniMax's academic table shows 88.5 on MMLU, 75.7 on MMLU-Pro, 89.1 on IFEval and 67.4 on C-SimpleQA.
- The weights support function calling with OpenAI-style definitions, and MiniMax publishes a vLLM deployment guide.
- $0.20 input and $1.10 output per million tokens on OpenRouter.

## Limitations
- No reasoning mode, tool-calling or structured-output parameters on OpenRouter; only max_tokens, temperature and top_p.
- Not benchmarked by Artificial Analysis; all numbers are MiniMax's own.
- 456B parameters; MiniMax's quickstart assumes eight GPUs with int8 quantisation.
- MiniMax's API model list no longer includes it, as available or retired. The licence is a custom one with attribution and prohibited-use terms.

## Good for
- Very long documents and code bases where a 1M-token window matters more than reasoning depth.
- Cost-sensitive workloads already built on it.
