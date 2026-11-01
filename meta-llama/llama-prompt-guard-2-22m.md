---
id: meta-llama/llama-prompt-guard-2-22m
name: Llama Prompt Guard 2 22M
owned_by: meta
type: llm
description: Llama Prompt Guard 2 22M is Meta's small open-weight classifier, based on DeBERTa-xsmall, that labels an input string benign or malicious to catch prompt injections and jailbreaks at low latency.
aliases: [meta-llama/Llama-Prompt-Guard-2-22M, groq/meta-llama/llama-prompt-guard-2-22m]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 4 Community License
release_date: "2025-04-28"
sources:
  - https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M
  - https://huggingface.co/api/models/meta-llama/Llama-Prompt-Guard-2-22M
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama Prompt Guard 2 22M

## Overview
Llama Prompt Guard 2 22M is the smaller of Meta's two Prompt Guard 2 classifiers. It is not a generative model: it takes a string and returns a "benign" or "malicious" label with a score, flagging explicit attempts to override earlier instructions (prompt injections and jailbreaks). The backbone is Microsoft's DeBERTa-xsmall (22M parameters; Hugging Face counts 70.8M in the F32 checkpoint), with the same attack-resistant tokeniser and energy-based training loss as the 86M. The context is 512 tokens, so longer inputs are split and scanned in parallel. OpenRouter does not list it; the id follows the Hugging Face repo `meta-llama/Llama-Prompt-Guard-2-22M`, created on 2025-04-28; Meta designed it to support the Llama 4 models. LiteLLM lists it on Groq.

## Strengths
- About 75% less latency and compute than the 86M: 19.3 ms per 512-token classification on an A100, against 92.4 ms.
- Meta's jailbreak benchmark: AUC 0.995 in English with 88.7% recall at a 1% false-positive rate.
- In AgentDojo it reached a 78.4% attack prevention rate at a 3% utility reduction, close to the 86M's 81.2%.

## Limitations
- Weaker outside English: multilingual AUC 0.942 against 0.995 for the 86M, because no multilingual DeBERTa-xsmall exists. Meta suggests it mainly for English-only, resource-constrained use.
- Detects known, explicit attack patterns; adaptive attacks can still get through.
- No separate "injection" label, and it does not judge whether content is harmful.

## Good for
- Low-latency screening of English user input and tool results.
- Resource-constrained deployments where the 86M costs too much.
- High-volume pre-filtering ahead of a content-safety model.
