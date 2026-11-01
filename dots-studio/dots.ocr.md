---
id: dots-studio/dots.ocr
name: dots.ocr
owned_by: rednote
type: llm
description: dots.ocr is rednote's MIT-licensed multilingual document parser, a 3B VLM on a 1.7B-parameter LLM that detects layout and recognises text, tables and formulas in one pass, switching tasks by prompt.
aliases: [rednote-hilab/dots.ocr, mlx-community/dots.ocr-bf16]
context_length: 131072
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-07-30"
sources:
  - https://huggingface.co/rednote-hilab/dots.ocr
  - https://huggingface.co/api/models/rednote-hilab/dots.ocr
  - https://huggingface.co/rednote-hilab/dots.ocr/raw/main/config.json
  - https://github.com/rednote-hilab/dots.ocr
  - https://github.com/rednote-hilab/dots.mocr
  - https://github.com/opendatalab/OmniDocBench
  - https://arxiv.org/abs/2601.20552
  - https://github.com/allenai/olmocr
  - https://huggingface.co/mlx-community/dots.ocr-bf16
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# dots.ocr

## Overview
rednote's hilab released dots.ocr on 2025-07-30 under the MIT licence. The Hugging Face repo `rednote-hilab/dots.ocr` now redirects to `dots-studio/dots.ocr`, which gives the id and directory; OpenRouter does not list it. A single vision-language model built on a 1.7B LLM (3.04B parameters in the checkpoint, 131,072 positions in config.json) performs layout detection, content recognition and reading order together. The full prompt returns JSON with each element's box, category and text (tables as HTML, formulas as LaTeX), which the parser also writes as Markdown, with or without headers and footers; other prompts give layout only, plain OCR or grounded OCR of a region. rednote's dots.mocr (March 2026) is the successor.

## Strengths
- OmniDocBench v1.5 overall 88.41 (cited in arXiv 2601.20552) and v1.6 overall 90.77 on the official leaderboard; olmOCR-bench 79.1 ± 1.0.
- On rednote's 1,493-page, 100-language dots.ocr-bench, overall edit distance 0.177 against 0.251 for Gemini 2.5 Pro.
- Served by vLLM (upstream since 0.11.0; rednote's evaluations used 0.9.1), transformers with custom code, a Docker image and community MLX weights.

## Limitations
- rednote says complex tables and formulas are not yet perfect and pictures are not parsed.
- Loops on runs of ellipses or underscores and can fail when text is tiny relative to the image; rednote recommends 200 DPI and images under 11,289,600 pixels.
- Not optimised for high-throughput PDF batches; the model path must not contain a period.

## Good for
- Multilingual and low-resource-language documents.
- Layout plus content in one JSON pass.
