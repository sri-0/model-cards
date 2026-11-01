---
id: cohere/embed-v4.0
name: Embed 4
owned_by: cohere
type: embedding
description: Cohere's fourth-generation multimodal embedding model for text, images and mixed text-and-image pages, with a 128K-token context, 100+ languages and 1536-dimensional default output.
aliases: [embed-v4.0, cohere.embed-v4:0, us.cohere.embed-v4:0, global.cohere.embed-v4:0, oci/cohere.embed-v4.0]
context_length: 128000
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
release_date: "2025-04-15"
embedding_dimensions: 1536
sources:
  - https://docs.cohere.com/docs/models
  - https://docs.cohere.com/docs/cohere-embed
  - https://docs.cohere.com/reference/embed
  - https://docs.cohere.com/docs/deprecations
  - https://cohere.com/blog/embed-4
  - https://cohere.com/pricing
  - https://openrouter.ai/api/v1/embeddings/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Embed 4

## Overview
Embed 4 (`embed-v4.0`) was announced on 2025-04-15 as Cohere's multimodal embedding model for enterprise retrieval. OpenRouter does not list it; the id is Cohere's API id. It embeds text, images and mixed text-and-image inputs such as PDF pages over a 128K-token context, in 100+ languages per Cohere's pricing page. `output_dimension` is one of 256, 512, 1024 or 1536 (the default), and embeddings come back as float, int8, uint8, binary, ubinary or base64. A call takes up to 96 texts or inputs; images have no count limit but must total 20 MB or less. An `input_type` (for example `search_document`) is required. Cohere's pricing page no longer shows a per-token price for Embed 4; LiteLLM's catalogue records $0.12 per million tokens and the Bedrock ids listed in the aliases. Cohere publishes no MTEB score for it, so the card has no `mteb_score`.

## Strengths
- One model embeds text, images and mixed text-and-image pages such as PDFs.
- 128K-token inputs cover long documents in one embedding.
- Smaller dimensions and int8 or binary output cut vector storage.

## Limitations
- Cohere now lists Embed 5 (`embed-v5.0-pro` and `embed-v5.0-fast`) as its most capable embedding models; Embed 4 is not deprecated.
- No published benchmark figures on Cohere's model pages.
- Proprietary; served by Cohere's API and cloud partners only.

## Good for
- Multimodal enterprise search over PDFs, slides and images.
- Existing Embed 4 indexes that are not yet worth re-embedding.
- Multilingual retrieval across 100+ languages.
