---
id: openai/text-embedding-3-large
name: Text Embedding 3 Large
owned_by: openai
type: embedding
description: OpenAI's most capable third-generation text embedding model for English and non-English tasks, returning 3072-dimensional vectors that the dimensions parameter can shorten.
aliases: [text-embedding-3-large, openai/text-embedding-3-large:batch, azure/text-embedding-3-large]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2024-01-25"
embedding_dimensions: 3072
mteb_score: 64.6
pricing:
  input: 0.13
  output: 0
sources:
  - https://openrouter.ai/openai/text-embedding-3-large
  - https://openrouter.ai/api/v1/embeddings/models
  - https://developers.openai.com/api/docs/models/text-embedding-3-large
  - https://developers.openai.com/api/docs/guides/embeddings
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Text Embedding 3 Large

## Overview
text-embedding-3-large is the larger of OpenAI's two third-generation embedding models, which OpenAI's changelog records as released on 2024-01-25. OpenAI calls it its most capable embedding model for both English and non-English tasks. OpenRouter lists it in its embeddings catalogue at $0.13 per million input tokens, the same as OpenAI's list price; a `:batch` variant is also listed. It returns a 3072-dimensional vector by default. The `dimensions` parameter shortens it at creation time, and the embeddings guide notes that a vector cut to 256 dimensions still outperforms the unshortened 1536-dimension text-embedding-ada-002 on MTEB. Maximum input is 8,192 tokens (LiteLLM's catalogue records 8,191), counted with `cl100k_base`. The `mteb_score` is OpenAI's own figure from the embeddings guide, which does not name the MTEB version.

## Strengths
- 64.6% on MTEB in OpenAI's guide, the highest of its three listed embedding models.
- Shortening to 1024 dimensions fits vector stores with that limit, the example OpenAI's guide gives.
- The same id works on OpenAI, Azure OpenAI and OpenRouter.

## Limitations
- 6.5 times the price of text-embedding-3-small ($0.13 against $0.02 per million tokens), about 9,615 pages per dollar.
- Text only; no image or other multimodal input.
- No published knowledge cutoff or deprecation date.
- Free-tier limits are 100 requests and 40,000 tokens per minute.

## Good for
- Retrieval where quality matters more than embedding cost, including non-English corpora.
- Indexes that need a full 3072-dimension vector or a shortened one from the same model.
- Replacing text-embedding-ada-002 at a lower dimension and higher MTEB score.
