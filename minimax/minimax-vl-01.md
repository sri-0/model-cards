---
id: minimax/minimax-vl-01
name: MiniMax-VL-01
owned_by: minimax
type: llm
description: MiniMax-VL-01 is MiniMax's January 2025 open-weight vision-language model, a 303M-parameter vision transformer and MLP projector on the 456B-parameter (45.9B active) MiniMax-Text-01 backbone, with dynamic image resolution up to 2016x2016.
aliases: [MiniMaxAI/MiniMax-VL-01, MiniMax-VL-01]
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: MiniMax Model License
release_date: "2025-01-15"
sources:
  - https://huggingface.co/MiniMaxAI/MiniMax-VL-01
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-VL-01
  - https://huggingface.co/MiniMaxAI/MiniMax-VL-01/raw/main/config.json
  - https://huggingface.co/MiniMaxAI/MiniMax-VL-01/raw/main/LICENSE-MODEL
  - https://huggingface.co/MiniMaxAI/MiniMax-Text-01/raw/main/config.json
  - https://huggingface.co/api/models?author=MiniMaxAI
  - https://arxiv.org/abs/2501.08313
  - https://platform.minimax.io/docs/release-notes/models.md
  - https://platform.minimax.io/docs/faq/models.md
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# MiniMax-VL-01

## Overview
MiniMax-VL-01 was released on 2025-01-15 together with MiniMax-Text-01 (MiniMax release notes; the Hugging Face repo was created 2025-01-12; paper arXiv 2501.08313). OpenRouter does not list it on its own: its minimax/minimax-01 endpoint takes images but names MiniMax-Text-01 as the repo, so this id follows the Hugging Face repo `MiniMaxAI/MiniMax-VL-01`. The model uses the ViT-MLP-LLM design: a 303M-parameter vision transformer trained from scratch on 694M image-caption pairs, a randomly initialised two-layer MLP projector and the MiniMax-Text-01 language model (456B total, 45.9B active, hybrid lightning and softmax attention). Images are resized on a preset grid from 336x336 to 2016x2016, split into patches and encoded alongside a 336x336 thumbnail; 512B tokens were processed over four training stages. No context length is stated: config.json carries 8,192 positions in `text_config` while the Text-01 backbone's own config allows 10,240,000, so the card leaves the field out. Weights are under the MiniMax Model License.

## Strengths
- MiniMax reports 91.7 on ChartQA, 96.4 on DocVQA, 865 on OCRBench and 68.5 on MMMU, against GPT-4o (11-20), Claude 3.5 Sonnet and Gemini models in its own table.
- Dynamic resolution suits documents, charts and screenshots.
- Function calling with OpenAI-style definitions; vLLM deployment guide.

## Limitations
- Not benchmarked by Artificial Analysis; all numbers are MiniMax's own.
- The quickstart covers single images and documents no video input; MiniMax's example assumes eight GPUs with int8 quantisation.
- Weaker on maths and science images per MiniMax: 24.2 on OlympiadBench and 68.6 on MathVista.
- MiniMax's API now lists only MiniMax-M3 and M3.1-Flash for image input. The licence is a custom one with attribution and prohibited-use terms.

## Good for
- Document, chart and OCR-style question answering on self-hosted hardware.
- Research on hybrid-attention vision-language models.
