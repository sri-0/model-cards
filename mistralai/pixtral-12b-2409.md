---
id: mistralai/pixtral-12b-2409
name: Pixtral 12B
owned_by: mistralai
type: llm
description: Pixtral 12B is Mistral AI's first open-weight (Apache-2.0) multimodal model, a 12B decoder based on Mistral Nemo with a 400M vision encoder, released in September 2024 and retired from Mistral's API in December 2025.
aliases: [pixtral-12b-2409, mistralai/Pixtral-12B-2409, pixtral-12b]
context_length: 131072
capabilities: [tool_calling, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2024-09-11"
sources:
  - https://huggingface.co/mistralai/Pixtral-12B-2409
  - https://huggingface.co/api/models/mistralai/Pixtral-12B-2409
  - https://huggingface.co/mistralai/Pixtral-12B-2409/raw/main/params.json
  - https://huggingface.co/mistralai/Pixtral-12B-2409/raw/main/README.md
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/pixtral-12b-24-09
  - https://docs.mistral.ai/resources/changelogs
  - https://mistral.ai/news/pixtral-12b
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Pixtral 12B

## Overview
Pixtral 12B (version 24.09, API id pixtral-12b-2409) is dated 11 September 2024 on Mistral's model page, when the Hugging Face repo was created; the announcement and changelog entry followed on 17 September. OpenRouter does not list it; the id follows the Hugging Face repo mistralai/Pixtral-12B-2409. It is a 12B multimodal decoder based on Mistral Nemo with a 400M vision encoder trained from scratch, trained on interleaved image and text data, accepting images at their native resolution and aspect ratio, several per prompt, within 131,072 positions (params.json). A technical report is linked from Mistral's docs (arXiv 2410.07073). Mistral's models page lists it as deprecated on 2 December 2025 and retired on 31 December 2025, with Ministral 3 14B as the replacement. In November 2024 Mistral scaled the API's temperature for it by 0.43. Artificial Analysis has no page for it, so this card has no benchmarks block.

## Strengths
- Mistral reports 52.5% on MMMU, 58.0% on MathVista, 81.8% on ChartQA, 90.7% on DocVQA and 78.6% on VQAv2, ahead of Qwen2-VL 7B, LLaVA-OneVision 7B and Phi-3.5 Vision in its evaluation harness except on DocVQA, where Qwen2-VL 7B scores 94.5%.
- Text ability is kept: 69.2% on MMLU, 72.0% on HumanEval and 61.3% on text IF-Eval, as a drop-in replacement for Mistral Nemo 12B.
- Apache 2.0 weights; Mistral's API offered structured outputs, function calling, document QnA and prefix completion.

## Limitations
- Retired from Mistral's API; self-hosting only, with vLLM 0.6.2 and mistral_common 1.4.4 or later per the model card.
- No reasoning mode, and no published knowledge cutoff.
- Nine documented languages: English, French, German, Spanish, Italian, Portuguese, Russian, Chinese and Japanese.

## Good for
- Small self-hosted image and document question answering.
- Research baselines for 12B-class vision-language models.
