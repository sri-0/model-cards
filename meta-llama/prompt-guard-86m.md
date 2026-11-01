---
id: meta-llama/prompt-guard-86m
name: Prompt Guard 86M
owned_by: meta
type: llm
description: Prompt Guard 86M is Meta's July 2024 open-weight mDeBERTa classifier that labels input text benign, injection or jailbreak, since replaced by Llama Prompt Guard 2.
aliases: [meta-llama/Prompt-Guard-86M]
context_length: 512
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 3.1 Community License
release_date: "2024-07-21"
sources:
  - https://huggingface.co/meta-llama/Prompt-Guard-86M
  - https://huggingface.co/api/models/meta-llama/Prompt-Guard-86M
  - https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Prompt Guard 86M

## Overview
Lifecycle: replaced. Meta says developers should migrate to Llama Prompt Guard 2 (`meta-llama/llama-prompt-guard-2-86m` or `-22m`), which it presents as a drop-in replacement. OpenRouter does not list it. The weights remain on Hugging Face as `meta-llama/Prompt-Guard-86M` (created 2024-07-21, with Llama 3.1). Prompt Guard is a classifier, not a generative model, built on Microsoft's mDeBERTa-v3-base (86M backbone and 192M word-embedding parameters). It labels a string benign, injection (out-of-place instructions, suited to filtering third-party data) or jailbreak (explicit attempts to override the system prompt, suited to filtering user input). The context is 512 tokens, so longer text is split and scanned in parallel. It was trained on English and non-English attacks and evaluated in eight languages.

## Strengths
- Meta's results: 99.9% true-positive rate at a 0.4% false-positive rate on its jailbreak set, and 97.5% at 3.9% on out-of-distribution jailbreaks.
- 91.5% detection on multilingual jailbreaks and 71.4% on CyberSecEval indirect injections.
- Small enough to deploy or fine-tune without GPUs, per Meta.

## Limitations
- Superseded: Prompt Guard 2 86M reaches 97.5% recall at a 1% false-positive rate against 21.2% for this model, and 81.2% attack prevention in AgentDojo against 67.6%.
- Meta later dropped the "injection" label, finding it too broad to be useful.
- Open to adaptive attacks, and Meta recommends fine-tuning on application data.

## Good for
- Existing pipelines that rely on the separate injection label.
- Research comparisons with Prompt Guard 2.
- CPU-only prompt-attack screening where the newer models are not yet deployed.
