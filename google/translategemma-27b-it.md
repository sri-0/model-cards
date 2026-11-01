---
id: google/translategemma-27b-it
name: TranslateGemma 27B
owned_by: google
type: llm
description: TranslateGemma 27B is Google's largest open translation model, fine-tuned from Gemma 3 27B for 55 languages, taking text or images and returning translated text under the Gemma Terms of Use.
aliases: [translategemma:27b]
context_length: 2048
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Gemma Terms of Use
release_date: "2026-01-15"
sources:
  - https://huggingface.co/google/translategemma-27b-it
  - https://huggingface.co/api/models/google/translategemma-27b-it
  - https://blog.google/innovation-and-ai/technology/developers-tools/translategemma/
  - https://arxiv.org/abs/2601.09012
  - https://arxiv.org/pdf/2601.09012
  - https://ollama.com/library/translategemma
retrieved: "2026-10-16"
---

# TranslateGemma 27B

## Overview
TranslateGemma 27B is the largest of Google's TranslateGemma models, announced on Google's blog on 2026-01-15. OpenRouter does not list it; the id follows the Hugging Face repo name google/translategemma-27b-it. Google fine-tuned the Gemma 3 27B checkpoint in two stages: supervised fine-tuning on 4.3 billion tokens of human-translated and Gemini-generated parallel data, then reinforcement learning on 10.2 million tokens with reward models including MetricX-QE and AutoMQM. It covers 55 languages and takes text or an image within a 2K-token total input context (model card; Ollama's GGUF builds list 128K; the gated config.json could not be read). Weights are gated on Hugging Face under the Gemma Terms of Use; Ollama offers translategemma:27b (17 GB). Google says it runs on one H100 GPU or TPU.

## Strengths
- Google's technical report (Table 1): WMT24++ MetricX over 55 language pairs of 3.09 against 4.04 for Gemma 3 27B (lower is better) and Comet22 of 84.4 against 83.1.
- WMT25 human evaluation (10 pairs): MQM 5.86 (Hugging Face card); ahead of Gemma 3 27B on most pairs in the report (English-Italian 1.8 against 2.5, English-Marathi 3.1 against 4.7, English-Serbian 8.7 against 10.4).
- Vistra image translation: MetricX 1.58 against 2.03 and Comet22 77.7 against 76.1 for Gemma 3 27B.

## Limitations
- 2K-token input context, so long documents must be split.
- Level with Gemma 3 27B into German (MQM 2.3 against 2.2) and worse on Japanese-English (13.4 against 11.6) from named-entity errors.
- Translation only; Google claims no other capabilities.
- Strict chat template (one user message, one text or image entry, source and target language codes); gated download.

## Good for
- The family's highest translation quality on one data-centre GPU.
- Low-resource target languages, where Google reports the largest gains.
- Translating text in images.
