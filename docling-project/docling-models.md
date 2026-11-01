---
id: docling-project/docling-models
name: Docling Models (TableFormer V1)
owned_by: ibm
type: llm
description: docling-models is IBM's original Docling model bundle, holding the TableFormer V1 table-structure model that is still Docling's default (accurate and fast modes) and the legacy RT-DETR layout model.
aliases: [ds4sd/docling-models]
capabilities: [vision]
architecture:
  input_modalities: [image]
  output_modalities: [text]
open_weights: true
license: CDLA-Permissive-2.0 and Apache-2.0
release_date: "2024-07-02"
sources:
  - https://huggingface.co/docling-project/docling-models
  - https://huggingface.co/api/models/docling-project/docling-models
  - https://arxiv.org/abs/2408.09869
  - https://arxiv.org/abs/2509.11720
  - https://docling-project.github.io/docling/usage/model_catalog/
  - https://github.com/docling-project/docling-ibm-models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Docling Models (TableFormer V1)

## Overview
The repo `docling-project/docling-models` (formerly `ds4sd`) was created on 2024-07-02 and carries both CDLA-Permissive-2.0 and Apache-2.0 licence tags; IBM's Docling Technical Report (arXiv 2408.09869) describes it. OpenRouter does not list it; the id is the Hugging Face repo name. It bundles two models that powered the first Docling releases. TableFormer (Nassar et al., CVPR 2022) reads an image of a table region found by the layout model and recovers rows, columns and cells; Docling's model catalog lists its accurate mode as the default table-structure model, with a fast mode as the alternative, both run by `docling-ibm-models` on CPU, CUDA or XPU. The second is the original RT-DETR layout model with 11 labels; Docling now defaults to the Heron layout model instead. TableFormerV2 is a separate preview repo.

## Strengths
- The card's TableFormer TEDS: 95.4 on simple tables, 90.1 on complex and 93.6 overall, against 88.3 for EDD and 73.0 for Camelot.
- Default table extraction in Docling's standard PDF pipeline, with no VLM needed.
- Small specialised models that run on CPU.

## Limitations
- The TEDS comparison dates from the 2022 paper and the card does not name the dataset.
- IBM's report (arXiv 2509.11720) scores Docling's previous layout model at 0.505 DocLayNet mAP against 0.699 for Heron.
- MPS is disabled for TableFormer because of performance problems.

## Good for
- Default Docling table extraction from PDFs.
- Reproducing earlier Docling results.
