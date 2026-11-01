---
id: docling-project/docling-layout-egret
name: Docling Layout Egret
owned_by: ibm
type: llm
description: Egret is IBM's family of D-FINE document layout detectors for Docling in medium, large and xlarge sizes, trading a little accuracy against Heron for faster CPU inference.
aliases: [docling-project/docling-layout-egret-medium, docling-project/docling-layout-egret-large, docling-project/docling-layout-egret-xlarge, ds4sd/docling-layout-egret-medium, ds4sd/docling-layout-egret-large, ds4sd/docling-layout-egret-xlarge]
capabilities: [vision]
architecture:
  input_modalities: [image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-07-02"
sources:
  - https://huggingface.co/docling-project/docling-layout-egret-medium
  - https://huggingface.co/docling-project/docling-layout-egret-large
  - https://huggingface.co/docling-project/docling-layout-egret-xlarge
  - https://huggingface.co/api/models/docling-project/docling-layout-egret-large
  - https://huggingface.co/docling-project/docling-layout-egret-large/raw/main/config.json
  - https://arxiv.org/abs/2509.11720
  - https://docling-project.github.io/docling/usage/model_catalog/
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Docling Layout Egret

## Overview
The three Egret layout models were published on Hugging Face on 2025-07-02 under Apache 2.0 and are described in IBM's technical report arXiv 2509.11720 (2025-09-15). OpenRouter does not list them. The id names the family: there is no single `docling-layout-egret` repo, so the three size repos (formerly under `ds4sd`) are aliases. Each is a D-FINE object detector with an HGNet-V2 backbone: egret-m has 19.5M parameters, egret-l 31.2M and egret-x 62.7M. They predict the same 17 layout classes as Heron (text, title, section header, table, picture, formula, code, list item, caption, footnote, page header and footer, document index, checkboxes, form, key-value region) and load with `DFineForObjectDetection` in transformers. Docling lists them as alternative layout models to its default, Heron.

## Strengths
- DocLayNet COCO mAP over all predictions: 0.686 (egret-m), 0.672 (egret-l), 0.671 (egret-x), close to heron's 0.699.
- With Docling post-processing, docling-eval mAP is 0.59 to 0.60 against 0.61 for heron.
- egret-m is the fastest model in the report: 0.024 s per image on an A100 (batch 100) and 0.33 s on a 4-thread CPU (batch 32), three times faster than heron-101 on CPU.

## Limitations
- Slightly below heron on every DocLayNet measure; the larger sizes do not raise mAP.
- Transformers only in Docling (no ONNX path).
- Boxes and labels only; text, tables and formulas need other models.

## Good for
- CPU-bound Docling deployments.
- High-volume layout detection where speed matters more than the last point of mAP.
