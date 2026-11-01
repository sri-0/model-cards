---
id: meta-llama/llama-prompt-guard-2-86m
name: Llama Prompt Guard 2 86M
owned_by: meta
type: llm
description: Llama Prompt Guard 2 86M is Meta's open-weight multilingual classifier that labels an input string benign or malicious to catch prompt injections and jailbreaks.
aliases: [meta-llama/Llama-Prompt-Guard-2-86M, groq/meta-llama/llama-prompt-guard-2-86m]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 4 Community License
release_date: "2025-04-28"
sources:
  - https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M
  - https://huggingface.co/api/models/meta-llama/Llama-Prompt-Guard-2-86M
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama Prompt Guard 2 86M

## Overview
Llama Prompt Guard 2 86M is a BERT-style classifier, not a generative model: it takes a string and returns a "benign" or "malicious" label with a score. It flags explicit attempts to override earlier instructions, covering both prompt injections in third-party data and jailbreaks, whether or not the attack would succeed. The backbone is Microsoft's mDeBERTa-base (86M parameters; Hugging Face counts 279M in the F32 checkpoint), with a tokeniser hardened against whitespace and fragmented-token tricks. The context is 512 tokens, so longer inputs are split and scanned in parallel. OpenRouter does not list it; the id follows the Hugging Face repo `meta-llama/Llama-Prompt-Guard-2-86M`, created on 2025-04-28; Meta designed it to support the Llama 4 models. Meta presents it as a drop-in replacement for Prompt Guard 1, and LiteLLM lists it on Groq.

## Strengths
- Meta's jailbreak benchmark: AUC 0.998 in English and 0.995 multilingual, with 97.5% recall at a 1% false-positive rate (Prompt Guard 1: 21.2%).
- In AgentDojo it reached an 81.2% attack prevention rate at a 3% utility reduction, against 67.6% for Prompt Guard 1.
- Trained on English and non-English attacks; evaluated in eight languages.
- About 92 ms per 512-token classification on an A100.

## Limitations
- Detects known, explicit attack patterns; adaptive attacks can still get through.
- No separate "injection" label, and it does not judge whether content is harmful.
- Meta recommends fine-tuning on application-specific data for best results.

## Good for
- Scanning user input and retrieved documents before they reach an agent.
- A cheap first layer in front of Llama Guard content moderation.
- Logging prompt-attack attempts for review.
