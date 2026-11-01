---
id: voyageai/voyage-code-3
name: voyage-code-3
owned_by: voyageai
type: embedding
description: Voyage AI's previous-generation code embedding model, with a 32,000-token input, 1024-dimensional default output and Matryoshka and quantised output options; still served but superseded by voyage-code-4.
aliases: [voyage-code-3, voyage/voyage-code-3]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
release_date: "2024-12-04"
embedding_dimensions: 1024
sources:
  - https://docs.voyageai.com/docs/embeddings
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2024/12/04/voyage-code-3/
  - https://blog.voyageai.com/2026/08/13/voyage-code-4/
  - https://openrouter.ai/api/v1/embeddings/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# voyage-code-3

## Overview
voyage-code-3 was announced on 2024-12-04 as Voyage AI's code retrieval embedding model. Voyage now lists it among earlier models that its API still serves, and voyage-code-4 (2026-08-13) is its successor. OpenRouter does not list it; the id is Voyage's API id under the voyageai prefix. Input is up to 32,000 tokens per text, against 8K for OpenAI's embeddings and 1K for CodeSage-large at launch, with up to 1,000 texts and 120K tokens per request. Output is 1024 dimensions by default, or 256, 512 or 2048, as float, int8, uint8, binary or ubinary; int8 saves four times the storage and binary 32 times. Voyage's pricing page lists it among older models at $0.18 per million tokens. Voyage published no MTEB score; its launch evaluation used 32 code retrieval datasets in five categories.

## Strengths
- Voyage reported average leads of 13.80% over OpenAI's text-embedding-3-large and 16.81% over CodeSage-large across the 32 datasets.
- At 1024 dimensions, a third of OpenAI's 3072, it kept the 13.80% lead; binary 256-dimension vectors, at 1/384 of the storage, still led by 4.81%.
- Binary rescoring improved on plain binary retrieval by up to 4.25%.

## Limitations
- voyage-code-4 beats it by 27.54% on agentic code retrieval and 13.98% on traditional code search, at a third lower price.
- Older-model pricing with no free tokens.
- Text and code only; proprietary.

## Good for
- Existing code search indexes built on voyage-code-3.
- Storage-constrained code retrieval with binary or int8 vectors.
- Comparison baselines for newer code embedders.
