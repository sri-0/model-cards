---
id: meta-llama/llama-guard-2-8b
name: Llama Guard 2 8B
owned_by: meta
type: llm
description: Llama Guard 2 8B is Meta's April 2024 open-weight safety classifier, fine-tuned from Llama 3 8B, that labels prompts and responses safe or unsafe against 11 MLCommons hazard categories.
aliases: [meta-llama/Meta-Llama-Guard-2-8B, accounts/fireworks/models/llama-guard-2-8b]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 3 Community License
release_date: "2024-04-17"
sources:
  - https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B
  - https://huggingface.co/api/models/meta-llama/Meta-Llama-Guard-2-8B
  - https://huggingface.co/meta-llama/Llama-Guard-3-8B
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/other-models
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama Guard 2 8B

## Overview
Lifecycle: superseded by Llama Guard 3 8B, which Meta reports improves over it in English, multilingual and tool-use moderation; Meta has since also released Llama Guard 4 12B. OpenRouter does not list it, Meta's docs file it under "other models", and LiteLLM still lists it on Fireworks (`accounts/fireworks/models/llama-guard-2-8b`). The weights remain on Hugging Face as `meta-llama/Meta-Llama-Guard-2-8B` (created 2024-04-17, alongside Llama 3). Llama Guard 2 is Llama 3 8B (8.03B parameters) fine-tuned for content-safety classification. Given a user prompt or a model response, it generates "safe" or "unsafe" and, when unsafe, the violated categories. It covers 11 of the 13 MLCommons hazard categories; elections and defamation are left out because they need up-to-date facts. Meta reads the first token's probability as an "unsafe" score for thresholding.

## Strengths
- Meta's internal test: F1 0.915, AUPRC 0.974 and a 0.040 false-positive rate, against an F1 of 0.665 for Llama Guard 1, 0.796 for GPT-4 and 0.347 for the OpenAI Moderation API.
- Adapts to other policies: F1 0.884 on XSTest and 0.807 on the OpenAI moderation set.
- Low false-positive rates per category (0.009 or less in Meta's breakdown).

## Limitations
- Classification only; Meta says it is not designed for chat.
- No election or defamation categories, and false-negative rates reach 0.27 or more for some categories such as self-harm and sex crimes.
- Can be attacked by prompt injection, and Meta lists multilingual capability among its limits.
- No Artificial Analysis benchmarks.

## Good for
- Existing Llama 3 stacks that already use it.
- Reproducing 2024 safety-classifier baselines.
- Prompt and response screening where Llama Guard 3 cannot yet be deployed.
