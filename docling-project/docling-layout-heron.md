---
id: docling-project/docling-layout-heron
name: Docling Layout Heron
owned_by: ibm
type: llm
description: Heron is IBM's RT-DETRv2 document layout detector and the default layout model of Docling, returning boxes for 17 element classes on a page image; heron-101 is its larger ResNet-101 sibling.
aliases: [ds4sd/docling-layout-heron, docling-project/docling-layout-heron-onnx, docling-project/docling-layout-heron-101, ds4sd/docling-layout-heron-101]
capabilities: [vision]
architecture:
  input_modalities: [image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-04-15"
sources:
  - https://huggingface.co/docling-project/docling-layout-heron
  - https://huggingface.co/api/models/docling-project/docling-layout-heron
  - https://huggingface.co/docling-project/docling-layout-heron/raw/main/config.json
  - https://huggingface.co/docling-project/docling-layout-heron-101
  - https://huggingface.co/docling-project/docling-layout-heron-onnx
  - https://arxiv.org/abs/2509.11720
  - https://arxiv.org/abs/2605.19866
  - https://docling-project.github.io/docling/usage/model_catalog/
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Docling Layout Heron

## Overview
Heron is Docling's default layout analysis model. Its Hugging Face repo was created on 2025-04-15 under Apache 2.0, and IBM describes it with its siblings in the technical report arXiv 2509.11720 (2025-09-15), which notes Docling v2.50.0 made it the default. OpenRouter does not list it; the id follows `docling-project/docling-layout-heron` (formerly `ds4sd`). It is an object detector, not a language model: given a page image it returns boxes with scores and one of 17 labels (caption, footnote, formula, list item, page header and footer, picture, section header, table, text, title, document index, code, two checkbox states, form, key-value region). Docling post-processes the boxes and sends regions to OCR, TableFormer and CodeFormulaV2. heron uses an RT-DETRv2 ResNet-50 backbone (42.9M parameters), heron-101 a ResNet-101 (76.7M); both load with `RTDetrV2ForObjectDetection`, and heron also has an ONNX export.

## Strengths
- DocLayNet COCO mAP over all predictions: heron 0.699, heron-101 0.696, against 0.505 for Docling's previous layout model; heron-101 reaches 0.780 on IBM's canonical DocLayNet.
- 28 ms per image for heron-101 on an A100; heron adds a median 28 ms per page in IBM's two-stage Granite-Docling pipeline.
- Runs on CPU, CUDA, MPS and XPU through transformers; only heron also runs on ONNX Runtime in Docling.

## Limitations
- Boxes and labels only; text needs a separate OCR engine.
- Docling's post-processing lowers COCO mAP to 0.564 (heron), though IBM finds the output closer to the ground truth.
- On CPU (batch 32) heron takes 0.64 s and heron-101 0.99 s per image, against 0.33 s for egret-m.

## Good for
- Docling's standard PDF pipeline.
- A layout front end for other OCR engines or for Granite-Docling-2stage.
