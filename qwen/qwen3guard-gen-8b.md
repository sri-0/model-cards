---
id: qwen/qwen3guard-gen-8b
name: Qwen3Guard Gen 8B
owned_by: qwen
type: llm
description: Qwen3Guard Gen 8B is Qwen's September 2025 open-weight (Apache-2.0) generative safety moderation model, built on Qwen3-8B, that labels prompts and responses as safe, controversial or unsafe with a risk category.
aliases: [Qwen/Qwen3Guard-Gen-8B]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-09-23"
sources:
  - https://huggingface.co/Qwen/Qwen3Guard-Gen-8B
  - https://huggingface.co/api/models/Qwen/Qwen3Guard-Gen-8B
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen3Guard-Gen-8B/raw/main/config.json
  - https://github.com/QwenLM/Qwen3Guard
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3Guard Gen 8B

## Overview
Qwen3Guard-Gen-8B is the 8B generative model of Qwen3Guard, a safety moderation series in 0.6B, 4B and 8B sizes. Its Hugging Face repo was created on 2025-09-23, which this card uses as the release date; no release note gives a day. OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. It is built on Qwen3-8B (Hugging Face counts 8.19B parameters, and config.json sets 32,768 positions) and trained on 1.19 million prompts and responses labelled for safety. It treats classification as instruction following: given a user prompt, it returns a safety label (Safe, Unsafe or Controversial) and a category (Violent, Non-violent Illegal Acts, Sexual Content or Sexual Acts, PII, Suicide & Self-Harm, Unethical Acts, Politically Sensitive Topics, Copyright Violation or Jailbreak); given a prompt and a response, it also says whether the response is a refusal. The separate Qwen3Guard-Stream models classify tokens during streaming. Serving needs transformers 4.51.0, sglang 0.4.6.post1 or vllm 0.9.0 or newer.

## Strengths
- Three severity levels (safe, controversial, unsafe) to suit different deployment scenarios, per Qwen.
- 119 languages and dialects.
- Qwen reports state-of-the-art results on English, Chinese and multilingual safety benchmarks for both prompt and response classification.

## Limitations
- Qwen's benchmark figures are an image, so none are quoted here.
- A classifier, not a chat model; outputs follow a fixed label format.
- No published knowledge cutoff.

## Good for
- Input and output filtering for chat products.
- Refusal detection in evaluation pipelines.
- Reward signals for safety training.
