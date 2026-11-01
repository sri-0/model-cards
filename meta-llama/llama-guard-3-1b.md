---
id: meta-llama/llama-guard-3-1b
name: Llama Guard 3 1B
owned_by: meta
type: llm
description: Llama Guard 3 1B is Meta's small open-weight content-safety classifier, pruned and distilled from Llama 3.2 1B and Llama Guard 3 8B, for low-cost and on-device moderation.
aliases: [meta-llama/Llama-Guard-3-1B, meta-llama/Llama-Guard-3-1B-INT4, "llama-guard3:1b", accounts/fireworks/models/llama-guard-3-1b]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 3.2 Community License
release_date: "2024-09-20"
sources:
  - https://huggingface.co/meta-llama/Llama-Guard-3-1B
  - https://huggingface.co/api/models/meta-llama/Llama-Guard-3-1B
  - https://huggingface.co/api/models?author=meta-llama
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3
  - https://ollama.com/library/llama-guard3
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama Guard 3 1B

## Overview
Llama Guard 3 1B is a Llama 3.2 1B model fine-tuned for content-safety classification. It labels a user prompt or a model response "safe" or "unsafe" and lists any violated categories from the 13 MLCommons hazards. Meta pruned it to 12 layers and a 6,400 MLP hidden dimension (1,123 million parameters), then distilled it from Llama Guard 3 8B at the logit level. A second version, `Llama-Guard-3-1B-INT4`, is also quantised and keeps only the 20 output tokens it needs, for mobile devices. It supports English, French, German, Hindi, Italian, Portuguese, Spanish and Thai. OpenRouter does not list it; the id follows the Hugging Face repo `meta-llama/Llama-Guard-3-1B`, created on 2024-09-20 for the Llama 3.2 release. Ollama lists a 128K context window.

## Strengths
- Cheap to run: Ollama's `llama-guard3:1b` package is 1.6 GB.
- Meta's English F1 of 0.899 (false-positive rate 0.090), close to the 8B's 0.939, and 0.939 in French.
- Category lists can be customised or trimmed in the prompt.

## Limitations
- Less accurate than the 8B in several languages: F1 0.680 in Hindi and 0.763 in Portuguese, with higher false-positive rates than the 8B in most of the languages Meta tested.
- Not optimised for S14 Code Interpreter Abuse; Meta points to the 8B for that.
- Categories that need current facts (defamation, intellectual property, elections) need more complex systems, per Meta.
- Classification only, and no Artificial Analysis benchmarks.

## Good for
- On-device or edge moderation alongside Llama 3.2 1B and 3B.
- High-volume, low-cost prompt and response screening.
- A first-pass filter before a larger safety model.
