---
id: lightonai/lightonocr-2-1b
name: LightOnOCR-2-1B
owned_by: lightonai
type: llm
description: LightOnOCR-2-1B is LightOn's second-generation Apache-2.0 1B end-to-end OCR model, trained with RLVR, that scored 83.2 on olmOCR-bench (headers and footers excluded) while being about nine times smaller than Chandra.
aliases: [lightonai/LightOnOCR-2-1B, mlx-community/LightOnOCR-2-1B-bf16]
context_length: 16384
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-01-19"
sources:
  - https://huggingface.co/lightonai/LightOnOCR-2-1B
  - https://huggingface.co/api/models/lightonai/LightOnOCR-2-1B
  - https://huggingface.co/lightonai/LightOnOCR-2-1B/raw/main/config.json
  - https://huggingface.co/blog/lightonai/lightonocr-2
  - https://arxiv.org/abs/2601.14251
  - https://huggingface.co/lightonai/LightOnOCR-2-1B-bbox
  - https://huggingface.co/datasets/lightonai/LightOnOCR-mix-0126
  - https://huggingface.co/blog/lightonai/lightonocr-3
  - https://huggingface.co/mlx-community/LightOnOCR-2-1B-bf16
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# LightOnOCR-2-1B

## Overview
LightOn released LightOnOCR-2-1B on 2026-01-19 under Apache 2.0, with the paper arXiv 2601.14251 (2026-01-20). OpenRouter does not list it; the id follows the Hugging Face repo `lightonai/LightOnOCR-2-1B`. It keeps the first version's Pixtral-initialised encoder and Qwen3-architecture decoder (1.01B parameters, 16,384 positions) and is trained on a larger, cleaner distillation mix with more French, arXiv and scanned pages, better LaTeX handling and steps against looping, then refined with RLVR. The default checkpoint is OCR only: one page image in, naturally ordered Markdown out. Sibling checkpoints add bounding boxes for embedded images (`-bbox`, `-bbox-soup`) or serve as fine-tuning bases (`-base`, `-bbox-base`); the training mix is released as LightOnOCR-mix-0126.

## Strengths
- olmOCR-bench 83.2 ± 0.9 with headers and footers excluded, more than 1.5 points above Chandra (9B), with gains on arXiv, old scans with maths and tables.
- LightOn reports it 3.3× faster than Chandra, 1.7× faster than olmOCR and 5× faster than dots.ocr.
- In transformers from v5 and in vLLM; community MLX weights.

## Limitations
- The 83.2 leaves out olmOCR-bench's headers-and-footers category, on which LightOn's later run scores it 19.7.
- LightOn's ParseBench run gives 13.5 on charts and 0 on visual grounding.
- Superseded by the LightOnOCR-3 family; LightOnOCR-3-1B is a drop-in upgrade.

## Good for
- Fast transcription of scientific, French and scanned documents.
- Fine-tuning from the published base checkpoints.
