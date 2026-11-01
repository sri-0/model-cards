---
id: cohere/embed-v5.0-pro
name: Embed 5 Pro
owned_by: cohere
type: embedding
description: Cohere's most capable embedding model (Embed 5 generation), a roughly 2.4B-parameter multimodal model for text, images and mixed pages with a 128K-token context, 100+ languages and 2048-dimensional default output.
aliases: [embed-v5.0-pro, Cohere-Embed-V5-Pro, azure_ai/Cohere-Embed-V5-Pro]
context_length: 128000
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
release_date: "2026-09-30"
embedding_dimensions: 2048
sources:
  - https://docs.cohere.com/docs/cohere-embed
  - https://docs.cohere.com/docs/models
  - https://docs.cohere.com/changelog/embed-v5
  - https://docs.cohere.com/reference/embed
  - https://cohere.com/blog/embed-5
  - https://cohere.com/pricing
  - https://openrouter.ai/api/v1/embeddings/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Embed 5 Pro

## Overview
Embed 5 Pro (`embed-v5.0-pro`) was announced on 2026-09-30 with the lighter `embed-v5.0-fast`; Cohere calls it its most capable embedding model. OpenRouter does not list it; the id is Cohere's API id. It has about 2.4B parameters and embeds text, images and mixed text-and-image inputs such as PDF pages in one vector, over a 128K-token context in 100+ languages. Output is Matryoshka embeddings of 256, 512, 768, 1024, 1536 or 2048 (default) dimensions, as float, int8 or binary. Pro and Fast share one embedding space; Cohere recommends indexing with Pro and querying with Fast. Cohere's launch price is $0.12 per million text tokens and $0.40 per million image tokens. It is served on Cohere's API, Model Vault, Microsoft Foundry and Amazon SageMaker, and can be self-hosted with vLLM. Cohere publishes no MTEB score, so the card has no `mteb_score`; its figures use ViDoRe V3 and its own suites.

## Strengths
- Cohere's ViDoRe V3 average: 85.8, against 84.5 for Embed 5 Fast, 83.7 for voyage-4-large, 83.2 for Gemini Embedding 2 and 77.0 for Embed 4.
- Finance: 80.1 on FinanceBench and 90.0 on FinQA; parsed PDFs average 84.8.
- Querying a Pro index with Fast keeps 98.4% of Pro-on-Pro quality in Cohere's test.

## Limitations
- Gemini Embedding 2 scores higher in Cohere's own table on Japanese, Korean, Arabic, Hindi, Telugu and Thai.
- 159.7 documents per second against 377.3 for Fast.
- Proprietary; all figures are Cohere's.

## Good for
- Offline indexing of visually rich enterprise documents.
- Financial filings and multilingual retrieval.
- An index queried by Embed 5 Fast for low latency.
