---
id: mistralai/mistral-7b-instruct-v0.3
name: Mistral 7B Instruct v0.3
owned_by: mistralai
type: llm
description: Mistral 7B Instruct v0.3 is the May 2024 update of Mistral AI's first open 7B model, under Apache 2.0, with a 32,768-token vocabulary, the v3 tokenizer and function calling.
aliases: [mistralai/Mistral-7B-Instruct-v0.3, open-mistral-7b, "mistral:7b", "mistral:v0.3"]
context_length: 32768
capabilities: [tool_calling]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2024-05-22"
sources:
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mistral-7b-0-3
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/announcing-mistral-7b
  - https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
  - https://huggingface.co/api/models/mistralai/Mistral-7B-Instruct-v0.3
  - https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3/raw/main/config.json
  - https://artificialanalysis.ai/models/mistral-7b-instruct
  - https://openrouter.ai/api/v1/models
  - https://ollama.com/library/mistral
retrieved: "2026-11-01"
---

# Mistral 7B Instruct v0.3

## Overview
Mistral 7B Instruct v0.3 was released on 2024-05-22, per Mistral's docs. OpenRouter does not list it, so the id follows the Hugging Face repo mistralai/Mistral-7B-Instruct-v0.3. It is an instruct fine-tune of Mistral-7B-v0.3, which Mistral describes as a minor update to its first open model: the vocabulary grew to 32,768 tokens, the v3 tokenizer is used, and function calling is supported. The original Mistral 7B (September 2023) has 7.3B parameters and uses grouped-query attention; config.json for v0.3 gives 32,768 positions, and Mistral's docs give a 32K context window with about 20 GB of GPU memory at bf16 and about 5 GB at fp4. On Mistral's API, mistral-tiny was renamed open-mistral-7b (alias mistral-tiny-2312) in February 2024, before v0.3 existed, so those ids are not aliases here; the changelog lists open-mistral-7b as v0.3 by July 2024. Mistral's docs list it as deprecated on 2024-11-30 and retired on 2025-03-30, with Ministral 3 8B as the replacement, so there is no current vendor price. Artificial Analysis's Mistral 7B Instruct page tests v0.1, not this checkpoint, so no benchmarks are recorded here.

## Strengths
- Apache 2.0 with no usage restrictions, per Mistral.
- Function calling through the v3 tokenizer, with mistral-inference and transformers examples on the Hugging Face card.
- About 5 GB of GPU memory at fp4, per Mistral's docs.

## Limitations
- No moderation mechanisms; the Hugging Face card calls the instruct checkpoint a quick demonstration of fine-tuning the base model.
- Limited knowledge, which Mistral attributes to its size.
- Artificial Analysis measured v0.1 at 17.7% on GPQA Diamond, 19.9% on IFBench and 0% on tau2-bench; v0.3 has no independent results.
- Text only, no reasoning mode, retired from Mistral's API.

## Good for
- Very small local deployments and teaching examples.
- Fine-tuning experiments from the Apache-2.0 base.
- Legacy integrations that still call open-mistral-7b, or Ollama's mistral:7b.
