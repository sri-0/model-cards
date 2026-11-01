---
id: dots-studio/dots.mocr
name: dots.mocr
owned_by: rednote
type: llm
description: dots.mocr is rednote's MIT-licensed 3B multimodal OCR model, the successor to dots.ocr, that parses multilingual documents and also turns charts, UI layouts and scientific figures into SVG code.
aliases: [rednote-hilab/dots.mocr]
context_length: 131072
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2026-03-19"
sources:
  - https://huggingface.co/rednote-hilab/dots.mocr
  - https://huggingface.co/api/models/dots-studio/dots.mocr
  - https://huggingface.co/dots-studio/dots.mocr/raw/main/config.json
  - https://github.com/rednote-hilab/dots.mocr
  - https://arxiv.org/abs/2603.13032
  - https://huggingface.co/rednote-hilab/dots.mocr-svg
  - https://huggingface.co/datalab-to/chandra-ocr-2
  - https://huggingface.co/blog/lightonai/lightonocr-3
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# dots.mocr

## Overview
rednote's hilab released dots.mocr on 2026-03-19 under the MIT licence, with the paper "Multimodal OCR: Parse Anything from Documents" (arXiv 2603.13032, 2026-03-13). The repo `rednote-hilab/dots.mocr` redirects to `dots-studio/dots.mocr`, which gives the id; OpenRouter does not list it. It keeps the dots.ocr design (3.04B parameters, 131,072 positions) and its prompts and output: JSON with boxes, categories and text, plus Markdown. New is parsing of structured graphics (charts, UI layouts, scientific figures, chemical drawings) directly into SVG code; a sister model, dots.mocr-svg, specialises in that. rednote says it keeps general vision ability comparable to Qwen3-VL-4B. Datalab's tables call it dots.ocr 1.5.

## Strengths
- olmOCR-bench 83.9 ± 0.9 against 79.1 for dots.ocr; OmniDocBench v1.5 text edit distance 0.031 and reading-order edit distance 0.029, the lowest in rednote's table.
- Elo 1,124.7 across olmOCR-Bench, OmniDocBench v1.5 and XDocParse, judged by Gemini 3 Flash, behind only Gemini 3 Pro.
- UniSVG ISVGEN scores of 0.850 low-level and 0.923 high-level, ahead of Gemini 3 Pro.
- vLLM since 0.11.0, transformers (including CPU) and a Docker image.

## Limitations
- rednote omits OmniDocBench v1.5 formula and table scores as too protocol-sensitive, and the Elo scores rely on an LLM judge.
- LightOn's ParseBench run scores it 1.0 out of 100 on charts, so chart data extraction is weak in that test.
- SVG output is still limited at 3B, hence dots.mocr-svg.

## Good for
- Multilingual document parsing with figures that should become code.
- Upgrading dots.ocr deployments.
