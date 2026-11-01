---
id: meta-llama/llama-guard-3-8b
name: Llama Guard 3 8B
owned_by: meta
type: llm
description: Llama Guard 3 8B is Meta's open-weight content-safety classifier, fine-tuned from Llama 3.1 8B, that labels prompts and responses safe or unsafe against 14 hazard categories in eight languages.
aliases: [meta-llama/Llama-Guard-3-8B, meta-llama/Llama-Guard-3-8B-INT8, "llama-guard3:8b", accounts/fireworks/models/llama-guard-3-8b, "@cf/meta/llama-guard-3-8b"]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 3.1 Community License
release_date: "2024-07-22"
sources:
  - https://huggingface.co/meta-llama/Llama-Guard-3-8B
  - https://huggingface.co/api/models/meta-llama/Llama-Guard-3-8B
  - https://huggingface.co/api/models?author=meta-llama
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3
  - https://ollama.com/library/llama-guard3
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama Guard 3 8B

## Overview
Llama Guard 3 8B is Llama 3.1 8B fine-tuned for content-safety classification. It is not a chat model: given a user prompt or a model response, it generates "safe" or "unsafe" and, when unsafe, the violated categories. The categories are the 13 MLCommons hazards (S1 to S13) plus S14 Code Interpreter Abuse, and they can be replaced or excluded in the prompt. It moderates English, French, German, Hindi, Italian, Portuguese, Spanish and Thai, and was also trained on search and code-interpreter tool calls. OpenRouter does not list it; the id follows the Hugging Face repo `meta-llama/Llama-Guard-3-8B`, created on 2024-07-22 (Meta says it shipped with Llama 3.1). Ollama lists a 128K context window. Meta also publishes an INT8 version about 40% smaller with very little quality loss.

## Strengths
- Meta's English response-classification test: F1 0.939 and AUPRC 0.985, against 0.877 and 0.927 for Llama Guard 2 and an F1 of 0.805 for GPT-4.
- Tool-call moderation: F1 0.856 on search tool calls and 0.885 on code-interpreter abuse.
- Meta reads the first token's probability as an "unsafe" score, so thresholds can be tuned.
- Open weights that run next to a self-hosted model (Ollama `llama-guard3:8b`, 4.9 GB).

## Limitations
- Classification only; no general generation or tool use.
- Meta notes that defamation, intellectual property and elections need up-to-date facts and more complex systems.
- Can raise refusals of benign prompts, and is itself open to prompt injection.
- No Artificial Analysis benchmarks.

## Good for
- Input and output moderation for Llama 3.1 chat and agent stacks.
- Screening code-interpreter and search tool calls.
- Moderation in the eight supported languages.
