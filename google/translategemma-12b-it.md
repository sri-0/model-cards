---
id: google/translategemma-12b-it
name: TranslateGemma 12B
owned_by: google
type: llm
description: TranslateGemma 12B is Google's open translation model fine-tuned from Gemma 3 12B for 55 languages, taking text or images and returning translated text under the Gemma Terms of Use.
aliases: [translategemma:12b]
context_length: 2048
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Gemma Terms of Use
release_date: "2026-01-15"
sources:
  - https://huggingface.co/google/translategemma-12b-it
  - https://huggingface.co/api/models/google/translategemma-12b-it
  - https://blog.google/innovation-and-ai/technology/developers-tools/translategemma/
  - https://arxiv.org/abs/2601.09012
  - https://arxiv.org/pdf/2601.09012
  - https://ollama.com/library/translategemma
retrieved: "2026-10-16"
---

# TranslateGemma 12B

## Overview
TranslateGemma 12B is the mid-sized model of Google's TranslateGemma family, announced on Google's blog on 2026-01-15. OpenRouter does not list it; the id follows the Hugging Face repo name google/translategemma-12b-it. Google fine-tuned the Gemma 3 12B checkpoint in two stages: supervised fine-tuning on 4.3 billion tokens of human-translated and Gemini-generated parallel data, then reinforcement learning on 10.2 million tokens with reward models including MetricX-QE and AutoMQM. It covers 55 languages and takes text or an image within a 2K-token total input context (model card; Ollama's GGUF builds list 128K; the gated config.json could not be read). Weights are gated on Hugging Face under the Gemma Terms of Use; Ollama offers translategemma:12b (8.1 GB).

## Strengths
- Google's technical report (Table 1): WMT24++ MetricX over 55 language pairs of 3.60 against 4.86 for Gemma 3 12B (lower is better) and Comet22 of 83.5 against 81.6; Google says it beats the Gemma 3 27B baseline (MetricX 4.04) at under half the size.
- WMT25 human evaluation (10 pairs): MQM 7.94 (Hugging Face card); competitive with Gemma 3 27B on high-resource languages, per the report.
- Vistra image translation: MetricX 2.08 against 2.33 for Gemma 3 12B.

## Limitations
- 2K-token input context, so long documents must be split.
- Vistra Comet22 fell to 72.8 from 74.9; Gemma 3 27B still wins some WMT25 pairs (English-German MQM 2.2 against 3.2, Japanese-English 11.6 against 15.7).
- Translation only; Google claims no other capabilities.
- Strict chat template (one user message, one text or image entry, source and target language codes); gated download.

## Good for
- Local translation among 55 languages on a laptop or one consumer GPU.
- Replacing Gemma 3 27B for translation at under half the size.
- Translating text in images.
