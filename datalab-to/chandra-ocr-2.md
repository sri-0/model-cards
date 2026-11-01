---
id: datalab-to/chandra-ocr-2
name: Chandra OCR 2
owned_by: datalab
type: llm
description: Chandra OCR 2 is Datalab's 2026 open-weight OCR model, a 5B Qwen3.5-architecture VLM that converts pages to Markdown, HTML or JSON in 90+ languages and scores 85.8 on olmOCR-bench.
context_length: 262144
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Modified OpenRAIL-M
release_date: "2026-03-18"
sources:
  - https://huggingface.co/datalab-to/chandra-ocr-2
  - https://huggingface.co/api/models/datalab-to/chandra-ocr-2
  - https://huggingface.co/datalab-to/chandra-ocr-2/raw/main/config.json
  - https://huggingface.co/datalab-to/chandra-ocr-2/raw/main/LICENSE
  - https://github.com/datalab-to/chandra
  - https://github.com/datalab-to/chandra/releases/tag/v0.2.0
  - https://huggingface.co/blog/lightonai/lightonocr-3
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Chandra OCR 2

## Overview
Datalab released Chandra OCR 2 on 2026-03-18 with chandra-ocr v0.2.0 (Hugging Face repo created 2026-03-16). OpenRouter does not list it; the id follows the Hugging Face repo `datalab-to/chandra-ocr-2`. The weights use Datalab's modified OpenRAIL-M licence and the code Apache 2.0. config.json shows the Qwen3.5 vision-language architecture (5.30B parameters, 262,144 positions); LightOn describes it as based on Qwen3.5-4B. Like Chandra 1 it outputs Markdown, HTML or JSON with layout, and Datalab reports gains in maths, tables, wide layouts, image captioning and language coverage (90+). The `chandra-ocr` package runs it through vLLM (recommended) or transformers.

## Strengths
- olmOCR-bench 85.8 ± 0.8 in Datalab's run, against 83.1 for Chandra 1 and 82.4 for olmOCR 2; 92.1 on tables and 93.7 on long tiny text.
- Average 77.8% on Datalab's 43-language benchmark (Chandra 1 69.4%, Gemini 2.5 Flash 67.6%) and 72.7% across 90 languages.
- 1.44 pages per second on one H100 with vLLM at 96 concurrent sequences on hard olmOCR-bench pages; Datalab estimates 2 pages per second on real documents.

## Limitations
- Free only for research, personal use and startups under $2M funding or revenue, and not for services competing with Datalab's API.
- LightOn's ParseBench run scores it 51.2 on visual grounding, and LightOnOCR-3-4B serves 21% more pages per second on the same base model.
- Weak on Urdu, Sanskrit and Telugu (43 to 59%); no OmniDocBench result published.

## Good for
- Multilingual documents, handwriting, forms and tables.
- Teams that can meet the licence terms or buy Datalab's commercial licence.
