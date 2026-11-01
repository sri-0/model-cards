---
id: docling-project/granite-docling-2stage-258m
name: Granite-Docling-2stage-258M
owned_by: ibm
type: llm
description: Granite-Docling-2stage-258M is IBM's fine-tune of Granite-Docling-258M that adds docling-layout-heron detections to the prompt as DocTags, making page conversion more robust on unfamiliar layouts.
context_length: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-03-11"
sources:
  - https://huggingface.co/docling-project/granite-docling-2stage-258m
  - https://huggingface.co/api/models/docling-project/granite-docling-2stage-258m
  - https://huggingface.co/docling-project/granite-docling-2stage-258m/raw/main/config.json
  - https://arxiv.org/abs/2605.19866
  - https://huggingface.co/ibm-granite/granite-docling-258M
  - https://huggingface.co/docling-project/docling-layout-heron
  - https://docling-project.github.io/docling/
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Granite-Docling-2stage-258M

## Overview
The Hugging Face repo `docling-project/granite-docling-2stage-258m` was created on 2026-03-11 under Apache 2.0 (its card repeats the base model's 2025-09-17 release date); IBM Research and ETH Zurich describe the method in arXiv 2605.19866 (2026-05-19). OpenRouter does not list it; the id is the Hugging Face repo name. Stage one runs the RT-DETR detector docling-layout-heron; its boxes and labels are serialised as DocTags and placed in the prompt next to the full page image. Stage two is granite-docling-258M fine-tuned to use that prior (257.8M parameters, Idefics3 architecture, 8,192 positions). Output is DocTags, as for the base model, and Docling runs it through the experimental `ThreadedLayoutVlmPipeline`.

## Strengths
- IBM reports markdown F1 rising from 0.37 to 0.92 on its proprietary 10k-page NoveltySet of unseen layouts.
- OmniDocBench English subset edit distances of 0.17 text, 0.34 table and 0.19 reading order against 0.78, 0.44 and 0.69 for the base; Chinese table TEDS 0.36 against 0.01.
- Model card: layout mAP 0.31 and F1 0.90 (base 0.27, 0.86); full-page OCR edit distance 0.27 (0.45).
- Fewer infinite-loop failures across the 26k pages of ViDoRe V3.

## Limitations
- About 15% slower: 2.6 s per page against 2.26 s on an A100, plus a median 74 extra prompt tokens.
- Needs the detector in the loop; the Docling pipeline for it is experimental.
- English first: about 1% of training data is Chinese.

## Good for
- Docling users whose documents look unlike the training data, such as forms and unusual layouts.
- Batch conversion where looping decoder failures are costly.
