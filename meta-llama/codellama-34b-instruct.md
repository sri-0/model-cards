---
id: meta-llama/codellama-34b-instruct
name: Code Llama 34B Instruct
owned_by: meta
type: llm
description: Code Llama 34B Instruct is Meta's August 2023 open-weight 34B code model, tuned for instruction-following code generation and discussion with a 16k context.
aliases: [meta-llama/CodeLlama-34b-Instruct-hf, codellama/CodeLlama-34b-Instruct-hf, "codellama:34b-instruct", accounts/fireworks/models/code-llama-34b-instruct, togethercomputer/CodeLlama-34b-Instruct]
context_length: 16384
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 2 Community License
release_date: "2023-08-24"
sources:
  - https://huggingface.co/meta-llama/CodeLlama-34b-Instruct-hf
  - https://huggingface.co/api/models/meta-llama/CodeLlama-34b-Instruct-hf
  - https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf
  - https://huggingface.co/api/models/codellama/CodeLlama-34b-Instruct-hf
  - https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf/raw/main/config.json
  - https://huggingface.co/api/models?author=meta-llama
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/meta-code-llama
  - https://ollama.com/library/codellama
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Code Llama 34B Instruct

## Overview
Lifecycle: legacy. OpenRouter does not list it, Artificial Analysis has no page for it, and Meta's Hugging Face organisation has released no Code Llama model after the 70B of January 2024; LiteLLM still lists it on Fireworks (`accounts/fireworks/models/code-llama-34b-instruct`). Meta has not named a direct successor in the sources used. The weights remain on Hugging Face (`meta-llama/CodeLlama-34b-Instruct-hf`) and in Ollama (`codellama:34b-instruct`). Code Llama Instruct is the instruction-following variant of Meta's Code Llama family, trained between January and July 2023. The release date is the creation date of the `codellama/CodeLlama-34b-Instruct-hf` Hugging Face repo, 2023-08-24; Meta's own `meta-llama` copy was created on 2024-03-14. It has 33.7B parameters per Hugging Face, and its config.json sets a 16,384-token context (Ollama also lists 16K). It uses the Llama 2 `[INST]` chat format. Infilling is not supported, per both the Hugging Face card and Meta's prompt-format docs. Licence: Llama 2 Community License.

## Strengths
- Tuned for code completion and chat about code, and intended by Meta to be safer for code-assistant use than the base model.
- Many quantised local builds and an established prompt format.
- The largest of the August 2023 sizes; Ollama's base `codellama:34b` package is 19 GB.

## Limitations
- Old: trained between January and July 2023, with no tool calling and no independent current benchmarks.
- Meta lists English (plus programming languages) as the only intended language.
- Not the Python specialist; Meta ships a separate Code Llama - Python variant for that.

## Good for
- Legacy coding assistants already built on Code Llama.
- Offline code generation and explanation on modest hardware.
- Legacy code assistants that need more than the 7B or 13B can give.
