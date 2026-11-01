---
id: mistralai/mistral-ocr-2512
name: Mistral OCR 3
owned_by: mistralai
type: llm
description: Mistral OCR 3 is Mistral AI's API-only document OCR model of December 2025, still generally available at $2 per 1,000 pages alongside the newer OCR 4.1.
aliases: [mistral-ocr-2512, mistral/mistral-ocr-2512, mistral/mistral-ocr-3, mistral/mistral-ocr-3-0, azure_ai/mistral-ocr-2512]
capabilities: [vision]
architecture:
  input_modalities: [image, file]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-12-18"
sources:
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/ocr-3-25-12
  - https://docs.mistral.ai/studio/document-processing/basic_ocr
  - https://docs.mistral.ai/inference/pricing
  - https://docs.mistral.ai/resources/languages
  - https://docs.mistral.ai/resources/changelogs
  - https://mistral.ai/news/mistral-ocr-3
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mistral OCR 3

## Overview
OCR 3 (version 25.12, API id mistral-ocr-2512) was released on 18 December 2025. OpenRouter does not list it and there are no public weights, so the id is the vendor API id under the vendor prefix. Mistral's models page lists it as a GA Premier model that "remains available for existing integrations and production workloads" now that OCR 4 exists; mistral-ocr-latest no longer points to it. It runs on /v1/ocr and the batch API, returning Markdown per page with extracted images, and introduced the table_format option (inline, separate Markdown or HTML tables with colspan and rowspan), header and footer extraction and hyperlink output. Mistral prices it at $2 per 1,000 pages, $1 with the batch discount, and $3 per 1,000 annotated pages. Mistral says it is fully backward compatible with OCR 2 and offers self-hosting to organisations with strict data privacy requirements.

## Strengths
- Mistral reports a 74% overall win rate over OCR 2 on forms, scanned documents, complex tables and handwriting, using fuzzy-match accuracy against ground truth on internal business documents.
- Half the per-page price of OCR 4.1.
- Multilingual: Mistral's docs list more than 40 languages across European, Middle Eastern, South Asian, Southeast Asian, East Asian and Central Asian groups.
- Structured annotations (document and image JSON schemas) through the same endpoint.

## Limitations
- No paragraph-level bounding boxes or block labels; include_blocks needs OCR 4 or newer.
- API-only; no OpenRouter listing, no token pricing and no Artificial Analysis results.
- Mistral's comparison uses internal benchmarks of customer documents, so it cannot be reproduced.

## Good for
- Cost-sensitive bulk conversion of PDFs and scans to Markdown.
- Existing OCR 2 and OCR 3 integrations that do not need block-level output.
- Handwritten and low-quality scanned forms.
