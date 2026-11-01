---
id: mistralai/mistral-ocr-4-1
name: Mistral OCR 4.1
owned_by: mistralai
type: llm
description: Mistral OCR 4.1 is Mistral AI's current API-only document OCR model, returning Markdown with paragraph-level bounding boxes, block labels and confidence scores, priced per page.
aliases: [mistral-ocr-4-1, mistral-ocr-4, mistral-ocr-latest, mistral/mistral-ocr-4-1, mistral/mistral-ocr-4, mistral/mistral-ocr-latest, mistral-ocr-4-0, mistral/mistral-ocr-4-0, azure_ai/mistral-ocr-4-0, mistral-ocr-2505, mistral-ocr-2503]
capabilities: [vision]
architecture:
  input_modalities: [image, file]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2026-07-16"
sources:
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/ocr-4-1
  - https://docs.mistral.ai/models/ocr-4-0
  - https://docs.mistral.ai/models/ocr-2-25-05
  - https://docs.mistral.ai/models/ocr-25-03
  - https://docs.mistral.ai/studio/document-processing/overview
  - https://docs.mistral.ai/studio/document-processing/basic_ocr
  - https://docs.mistral.ai/inference/pricing
  - https://docs.mistral.ai/resources/languages
  - https://docs.mistral.ai/resources/changelogs
  - https://mistral.ai/news/ocr-4
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mistral OCR 4.1

## Overview
OCR 4.1 (API id mistral-ocr-4-1, aliases mistral-ocr-4 and mistral-ocr-latest) was released on 16 July 2026 and became generally available on 31 August 2026. OpenRouter does not list it; the id is Mistral's API id. It runs on /v1/ocr and powers Mistral's Document AI. It takes PDF, PPTX, DOCX and image files and returns per-page Markdown with images, hyperlinks, tables, headers and footers; include_blocks adds paragraph-level bounding boxes with 13 block labels (text, title, table, equation, signature and others) in reading order. Confidence scores come per page, block or word; block scores are what 4.1 added over OCR 4.0 (released 23 June 2026, retired 30 September 2026). Mistral names OCR 4.1 as the replacement for the retired OCR 4.0, OCR 2 (mistral-ocr-2505) and OCR 25.03 (mistral-ocr-2503), so their ids are aliases here. Mistral charges $4 per 1,000 pages ($2 with the batch discount) and $5 per 1,000 annotated pages.

## Strengths
- Mistral's OCR 4 announcement reports 85.20 on OlmOCRBench, 93.07 on OmniDocBench and 0.98 on its internal Crawl Multilingual set; human annotators preferred it over every system tested (72% average win rate).
- 170 languages per the announcement; the docs claim strong results in more than 40.
- JSON-schema annotations on the same endpoint, filled by mistral-small-2603 from the extraction.
- Served on Mistral Studio, Amazon SageMaker and Microsoft Foundry; enterprises can self-host it in one container.

## Limitations
- API-only for the public; no OpenRouter listing, token pricing or Artificial Analysis results.
- Mistral calls its benchmark scores directional; competitor figures are its own reproductions.
- Mistral rules out medical, legal, safety-critical and latency-sensitive use.

## Good for
- Turning PDFs and scans into Markdown or JSON for RAG and search.
- Form and invoice pipelines that use bounding boxes and confidence scores for human review.
- Multilingual archives, including low-resource languages.
