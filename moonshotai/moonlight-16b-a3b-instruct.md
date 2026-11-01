---
id: moonshotai/moonlight-16b-a3b-instruct
name: Moonlight-16B-A3B-Instruct
owned_by: moonshotai
type: llm
description: Moonlight-16B-A3B-Instruct is Moonshot AI's small open-weight (MIT) mixture-of-experts chat model (16B total, 3B active), released to show that the Muon optimiser scales to large-model training.
aliases: [moonshotai/Moonlight-16B-A3B-Instruct]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-02-22"
sources:
  - https://huggingface.co/moonshotai/Moonlight-16B-A3B-Instruct
  - https://huggingface.co/api/models/moonshotai/Moonlight-16B-A3B-Instruct
  - https://huggingface.co/moonshotai/Moonlight-16B-A3B-Instruct/raw/main/config.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Moonlight-16B-A3B-Instruct

## Overview
Moonlight is a research release from Moonshot AI, published on Hugging Face on 2025-02-22 with a technical report on scaling the Muon optimiser. Moonshot found two changes that make Muon work at scale without tuning: weight decay and a consistent update RMS across parameters. Its scaling-law runs show Muon about twice as sample-efficient as AdamW, needing roughly 52% of the training FLOPs for comparable results. Moonlight is a DeepSeek-V3-architecture mixture-of-experts model with 16B total and 3B activated parameters (64 experts, 6 per token), trained on 5.7T tokens, with an 8K context. The instruct checkpoint is the chat-tuned version; base and intermediate checkpoints are also public. It later served as the language base of Kimi-VL. OpenRouter does not list it; the id follows the Hugging Face repo. Weights are MIT-licensed.

## Strengths
- In Moonshot's comparison with Llama3.2-3B, Qwen2.5-3B and DeepSeek-V2-Lite, Moonlight scores 70.0 on MMLU, 42.4 on MMLU-Pro, 48.1 on HumanEval and 45.3 on MATH.
- Strong Chinese results in the same table: 77.2 on C-Eval and 78.2 on CMMLU.
- About 3B active parameters, so it runs on a single consumer GPU.

## Limitations
- 8K context only.
- No tool calling, reasoning mode or vision.
- An early-2025 research model, well behind later Kimi releases.
- Needs `trust_remote_code`; Moonshot recommends transformers 4.48.2.

## Good for
- Research on optimisers and mixture-of-experts training.
- Lightweight English and Chinese chat or text tasks on local hardware.
