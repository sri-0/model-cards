---
id: docling-project/tableformerv2
name: TableFormerV2
owned_by: ibm
type: llm
description: TableFormerV2 is IBM's preview 52M-parameter table-structure model for Docling that predicts OTSL structure tokens and one bounding box per cell from an image of a table.
aliases: [docling-project/TableFormerV2]
capabilities: [vision]
architecture:
  input_modalities: [image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-01-20"
sources:
  - https://huggingface.co/docling-project/TableFormerV2
  - https://huggingface.co/api/models/docling-project/TableFormerV2
  - https://huggingface.co/docling-project/TableFormerV2/raw/main/config.json
  - https://github.com/docling-project/docling-ibm-models
  - https://arxiv.org/abs/2305.03393
  - https://docling-project.github.io/docling/usage/model_catalog/
  - https://huggingface.co/docling-project/docling-models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# TableFormerV2

## Overview
IBM Research published TableFormerV2 on Hugging Face on 2026-01-20 under Apache 2.0 as a preview; Docling's default table-structure model is still TableFormer V1 from `docling-project/docling-models`. OpenRouter does not list it; the id follows the Hugging Face repo `docling-project/TableFormerV2`. It takes a table crop found by the layout model, resized to 448×448, and predicts the table's structure as an OTSL token sequence together with a bounding box for each cell. Docling then matches the cells to the PDF's own text cells (or uses the predicted cells) to build a `TableItem`. The model has about 52M FP32 parameters: an EfficientNetV2-S encoder with squeeze-and-excitation, a depthwise-separable spatial mixer with no encoder self-attention, a cache-aware Transformer structure decoder (four layers, 13-token vocabulary) and an attention-based box head. The code is in `docling-ibm-models`.

## Strengths
- Designed for fast CPU inference and GPU batching.
- One switch in Docling: `--table-structure-engine docling_tableformer_v2`, or the `tableformer_v2` preset in Docling Serve.
- `docling-tools models download tableformerv2` fetches the weights ahead of time for offline use.
- Cell matching keeps the PDF's native text instead of re-reading it.

## Limitations
- Preview: weights, outputs and integration may change without notice.
- The model card publishes no benchmark scores.
- Needs a layout model to find tables first; it is not prompt-driven.

## Good for
- Trying faster table-structure recognition in Docling.
- Air-gapped Docling installs that pre-download models.
