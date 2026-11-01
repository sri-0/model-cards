---
id: meta-llama/llamaguard-7b
name: Llama Guard 7B
owned_by: meta
type: llm
description: Llama Guard 7B is Meta's original December 2023 open-weight safety classifier, a Llama 2 7B fine-tune that labels prompts and responses safe or unsafe against six harm categories.
aliases: [meta-llama/LlamaGuard-7b, accounts/fireworks/models/llamaguard-7b]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 2 Community License
release_date: "2023-12-05"
sources:
  - https://huggingface.co/meta-llama/LlamaGuard-7b
  - https://huggingface.co/api/models/meta-llama/LlamaGuard-7b
  - https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/other-models
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama Guard 7B

## Overview
Lifecycle: superseded by Llama Guard 2 8B, which Meta reports improves on it; Meta has since released Llama Guard 3 and Llama Guard 4. OpenRouter does not list it, Meta's docs file it under "other models", and LiteLLM still lists it on Fireworks (`accounts/fireworks/models/llamaguard-7b`). The weights remain on Hugging Face as `meta-llama/LlamaGuard-7b` (created 2023-12-05), in both the original Llama format and the Transformers format. Llama Guard is a Llama 2 7B model (6.74B parameters) fine-tuned to classify LLM inputs and outputs. It generates "safe" or "unsafe" and, when unsafe, the violated categories from Meta's own six-category taxonomy: violence and hate, sexual content, guns and illegal weapons, regulated or controlled substances, suicide and self-harm, and criminal planning. Meta trained it on about 13,000 examples drawn from Anthropic's dataset and in-house red-teaming, and reads the first token's probability as an "unsafe" score.

## Strengths
- Meta's results: 0.945 on its prompt test set and 0.953 on its response test set, against 0.764 and 0.769 for the OpenAI moderation API and 0.728 and 0.699 for Perspective API.
- 0.847 on the OpenAI Moderation dataset and 0.626 on ToxicChat.
- The taxonomy and guidelines can be replaced in the prompt.

## Limitations
- Only six categories; Meta notes its score falls to an F1 of 0.665 on Llama Guard 2's 11-category test set.
- Meta says its taxonomy is a demonstration and does not reflect Meta's internal policies.
- Classification only, and no Artificial Analysis benchmarks.

## Good for
- Legacy Llama 2 stacks that already use it.
- Research on LLM-based safety classifiers and policy adaptation.
- Comparing newer Llama Guard versions against the original.
