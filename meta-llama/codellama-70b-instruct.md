---
id: meta-llama/codellama-70b-instruct
name: Code Llama 70B Instruct
owned_by: meta
type: llm
description: Code Llama 70B Instruct is Meta's January 2024 open-weight 70B code model, the largest and last Code Llama release, tuned for instruction-following code generation.
aliases: [meta-llama/CodeLlama-70b-Instruct-hf, codellama/CodeLlama-70b-Instruct-hf, "codellama:70b-instruct", accounts/fireworks/models/code-llama-70b-instruct]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 2 Community License
release_date: "2024-01-29"
sources:
  - https://huggingface.co/meta-llama/CodeLlama-70b-Instruct-hf
  - https://huggingface.co/api/models/meta-llama/CodeLlama-70b-Instruct-hf
  - https://huggingface.co/codellama/CodeLlama-70b-Instruct-hf
  - https://huggingface.co/api/models/codellama/CodeLlama-70b-Instruct-hf
  - https://huggingface.co/codellama/CodeLlama-70b-Instruct-hf/raw/main/config.json
  - https://huggingface.co/api/models?author=meta-llama
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/meta-code-llama
  - https://ollama.com/library/codellama
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Code Llama 70B Instruct

## Overview
Lifecycle: legacy. OpenRouter does not list it, Artificial Analysis has no page for it, and Meta's Hugging Face organisation has released no Code Llama model after it; LiteLLM still lists it on Fireworks (`accounts/fireworks/models/code-llama-70b-instruct`). Meta has not named a direct successor in the sources used. The weights remain on Hugging Face (`meta-llama/CodeLlama-70b-Instruct-hf`) and in Ollama (`codellama:70b-instruct`). Code Llama 70B Instruct (69.0B parameters per Hugging Face) is the largest instruction-following Code Llama, trained between January 2023 and January 2024. The release date is the creation date of the `codellama/CodeLlama-70b-Instruct-hf` Hugging Face repo; Meta's own `meta-llama` copy was created on 2024-03-13. Unlike the smaller sizes it uses its own chat format (`Source: system`, `Source: user` turns separated by `<step>`), so use the tokenizer's chat template. Infilling is not supported. Context sources disagree: Meta says it was fine-tuned with up to 16k tokens and does not support the 100k long-context mode, while config.json in the `codellama` repo and Ollama list 4,096 tokens, so the card leaves `context_length` out. Licence: Llama 2 Community License.

## Strengths
- The most capable Code Llama, for code completion and chat about code.
- Intended by Meta to be safer for code-assistant use than the base model.

## Limitations
- Different prompt format from every other Code Llama and Llama 2 model; hand-built prompts must follow it exactly.
- Heavy to self-host: Ollama's base `codellama:70b` package is 39 GB.
- Old, with no tool calling and no independent current benchmarks; English only per Meta.

## Good for
- Legacy coding assistants already built on Code Llama 70B.
- Offline code generation where a 70B model already fits the hardware.
- Research baselines from early 2024.
