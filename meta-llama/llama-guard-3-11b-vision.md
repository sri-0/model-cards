---
id: meta-llama/llama-guard-3-11b-vision
name: Llama Guard 3 11B Vision
owned_by: meta
type: llm
description: Llama Guard 3 11B Vision is Meta's open-weight multimodal safety classifier, fine-tuned from Llama 3.2 11B Vision, that labels image-and-text prompts and their responses safe or unsafe.
aliases: [meta-llama/Llama-Guard-3-11B-Vision]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Llama 3.2 Community License
release_date: "2024-09-20"
sources:
  - https://huggingface.co/meta-llama/Llama-Guard-3-11B-Vision
  - https://huggingface.co/api/models/meta-llama/Llama-Guard-3-11B-Vision
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-3
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama Guard 3 11B Vision

## Overview
Llama Guard 3 11B Vision is Llama 3.2 11B Vision fine-tuned for content-safety classification of conversations that include an image. It classifies a text-and-image prompt, or that prompt with the model's text response, and generates "safe" or "unsafe" plus any violated categories from the 13 MLCommons hazards. Meta trained it to treat attempts to identify real people in images as unsafe. It has 10.67B parameters per Hugging Face. OpenRouter does not list it; the id follows the Hugging Face repo `meta-llama/Llama-Guard-3-11B-Vision`, created on 2024-09-20 for the Llama 3.2 release. Meta's model card calls it the first safety classifier for LLM image-understanding tasks.

## Strengths
- Meta's response-classification results: precision 0.961, recall 0.916 and F1 0.938, against an F1 of 0.667 for GPT-4o and 0.641 for GPT-4o mini.
- Prompt classification is more precise than GPT-4o (0.891 against 0.544), though with lower recall.
- Uses the same prompt format as the other Llama Guard 3 models, with an added image token.

## Limitations
- Prompt classification is harder: recall 0.623 and F1 0.733.
- Optimised for English and evaluates one image per prompt; images are rescaled into four 560x560 chunks.
- Not meant for image-only or text-only classification (Meta points to Llama Guard 3 8B or 1B for text), and does not support images that were themselves made with generative AI.
- Classification only, and no Artificial Analysis benchmarks.

## Good for
- Screening image-and-text prompts sent to Llama 3.2 Vision models.
- Checking text answers to questions about uploaded images.
- Flagging requests to identify people in photos.
