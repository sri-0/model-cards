---
id: meta-llama/codellama-7b-instruct
name: Code Llama 7B Instruct
owned_by: meta
type: llm
description: Code Llama 7B Instruct is Meta's August 2023 open-weight 7B code model, tuned for instruction-following code generation and discussion with a 16k context.
aliases: [meta-llama/CodeLlama-7b-Instruct-hf, codellama/CodeLlama-7b-Instruct-hf, "codellama:7b-instruct", accounts/fireworks/models/code-llama-7b-instruct]
context_length: 16384
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 2 Community License
release_date: "2023-08-24"
sources:
  - https://huggingface.co/meta-llama/CodeLlama-7b-Instruct-hf
  - https://huggingface.co/api/models/meta-llama/CodeLlama-7b-Instruct-hf
  - https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf
  - https://huggingface.co/api/models/codellama/CodeLlama-7b-Instruct-hf
  - https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf/raw/main/config.json
  - https://huggingface.co/api/models?author=meta-llama
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/meta-code-llama
  - https://ollama.com/library/codellama
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Code Llama 7B Instruct

## Overview
Lifecycle: legacy. OpenRouter does not list it, Artificial Analysis has no page for it, and Meta's Hugging Face organisation has released no Code Llama model after the 70B of January 2024; LiteLLM still lists it on Fireworks (`accounts/fireworks/models/code-llama-7b-instruct`). Meta has not named a direct successor in the sources used. The weights remain on Hugging Face (`meta-llama/CodeLlama-7b-Instruct-hf`) and in Ollama (`codellama:7b-instruct`). Code Llama Instruct is the instruction-following variant of Meta's Code Llama family, trained between January and July 2023. The release date is the creation date of the `codellama/CodeLlama-7b-Instruct-hf` Hugging Face repo, 2023-08-24; Meta's own `meta-llama` copy was created on 2024-03-13. It has 6.74B parameters per Hugging Face, and its config.json sets a 16,384-token context (Ollama also lists 16K). It uses the Llama 2 `[INST]` chat format. Meta's prompt-format docs say infilling works only in the 7B and 13B base models, not in Instruct, although the Hugging Face card ticks infilling for this repo. Licence: Llama 2 Community License.

## Strengths
- Tuned for code completion and chat about code, and intended by Meta to be safer for code-assistant use than the base model.
- Many quantised local builds and an established prompt format.
- The smallest Code Llama: Ollama's base `codellama:7b` package is 3.8 GB.

## Limitations
- Old: trained between January and July 2023, with no tool calling and no independent current benchmarks.
- Meta lists English (plus programming languages) as the only intended language.
- Not the Python specialist; Meta ships a separate Code Llama - Python variant for that.

## Good for
- Legacy coding assistants already built on Code Llama.
- Offline code generation and explanation on modest hardware.
- Code explanation and small snippets in English on a laptop.
