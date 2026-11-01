---
id: mistralai/codestral-embed-2505
name: Codestral Embed 2505
owned_by: mistralai
type: embedding
description: Mistral AI's code embedding model (version 25.05) for code retrieval, with output dimensions of up to 3072 ordered by relevance and float, int8 and binary output types.
aliases: [codestral-embed-2505, codestral-embed, mistral/codestral-embed-2505, mistral/codestral-embed]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Mistral
open_weights: false
license: proprietary
release_date: "2025-05-28"
embedding_dimensions: 1536
pricing:
  input: 0.15
  output: 0
sources:
  - https://openrouter.ai/mistralai/codestral-embed-2505
  - https://openrouter.ai/api/v1/embeddings/models
  - https://docs.mistral.ai/models/codestral-embed-25-05
  - https://docs.mistral.ai/models
  - https://docs.mistral.ai/resources/changelogs
  - https://docs.mistral.ai/studio/knowledge-rag/embeddings/code_embeddings
  - https://docs.mistral.ai/inference/pricing
  - https://mistral.ai/news/codestral-embed
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Codestral Embed 2505

## Overview
Codestral Embed (version 25.05, API id `codestral-embed-2505`, alias `codestral-embed`) was released on 2025-05-28 as Mistral's first embedding model specialised for code. OpenRouter lists it in its embeddings catalogue at $0.15 per million input tokens. It embeds code and text over an 8,192-token context. `output_dimension` defaults to 1536 and accepts any integer up to 3072; dimensions are ordered by relevance, so keeping the first n trades quality for storage. `output_dtype` is float (default), int8, uint8, binary or ubinary, the last two bit-packed to one eighth of the dimension. Mistral serves it on `/v1/embeddings` and `/v1/batch` at $0.15 per million tokens, with a 50% batch discount. Mistral publishes no MTEB figure, so the card has no `mteb_score`.

## Strengths
- Mistral reports that it outperforms Voyage Code 3, Cohere Embed v4.0 and OpenAI's large embedding model on SWE-Bench Lite, Text2Code (GitHub), Text2SQL and algorithm retrieval; the launch post gives the results as charts, not figures.
- Mistral says 256 dimensions at int8 precision still beats those competitors, cutting storage.
- For retrieval Mistral recommends 3,000-character chunks with 1,000 characters of overlap.

## Limitations
- 8k-token input, so large files must be chunked.
- Benchmark results are Mistral's own charts; no independent numbers are published.
- Proprietary and API only; on-premises deployment goes through Mistral's sales team.

## Good for
- Semantic code search over repositories.
- Context retrieval for coding agents and code completion.
- Duplicate detection and clustering of similar code.
