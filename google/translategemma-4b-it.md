---
id: google/translategemma-4b-it
name: TranslateGemma 4B
owned_by: google
type: llm
description: TranslateGemma 4B is Google's open translation model fine-tuned from Gemma 3 4B for 55 languages, taking text or images and returning translated text under the Gemma Terms of Use.
aliases: [translategemma:4b, translategemma:latest]
context_length: 2048
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Gemma Terms of Use
release_date: "2026-01-15"
sources:
  - https://huggingface.co/google/translategemma-4b-it
  - https://huggingface.co/api/models/google/translategemma-4b-it
  - https://blog.google/innovation-and-ai/technology/developers-tools/translategemma/
  - https://arxiv.org/abs/2601.09012
  - https://arxiv.org/pdf/2601.09012
  - https://ollama.com/library/translategemma
retrieved: "2026-10-16"
---

# TranslateGemma 4B

## Overview
TranslateGemma 4B is the smallest of Google's three TranslateGemma models (4B, 12B and 27B), announced on Google's blog on 2026-01-15. OpenRouter does not list it; the id follows the Hugging Face repo name google/translategemma-4b-it. Google fine-tuned the Gemma 3 4B checkpoint in two stages: supervised fine-tuning on 4.3 billion tokens of human-translated and Gemini-generated parallel data, then reinforcement learning on 10.2 million tokens with reward models including MetricX-QE and AutoMQM. It covers 55 languages and takes text or an image within a 2K-token total input context (model card; Ollama's GGUF builds list 128K; the gated config.json could not be read). Weights are gated on Hugging Face under the Gemma Terms of Use and on Ollama as translategemma:4b (3.3 GB, also the latest tag).

## Strengths
- Google's technical report (Table 1): WMT24++ MetricX over 55 language pairs of 5.32 against 6.97 for Gemma 3 4B (lower is better) and Comet22 of 80.1 against 77.2 (the Hugging Face card lists 81.6); Google says it rivals the Gemma 3 12B baseline (MetricX 4.86).
- Vistra image translation (English into German, Spanish, Russian and Chinese): MetricX 2.58 against 2.60 for Gemma 3 4B.
- Sized for mobile and edge deployment (Google blog).

## Limitations
- 2K-token input context, so long documents must be split.
- No WMT25 human evaluation for the 4B, and only small image-translation gains at this size.
- Translation only; Google claims no other capabilities.
- Strict chat template (one user message, one text or image entry, source and target language codes); gated download.

## Good for
- On-device or edge translation among the 55 languages.
- Translating text in photographs and screenshots.
- Fine-tuning for further language pairs (Google trained on nearly 500 extra, unevaluated).
