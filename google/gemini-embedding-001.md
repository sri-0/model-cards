---
id: google/gemini-embedding-001
name: Gemini Embedding 001
owned_by: google
type: embedding
description: Google's first Gemini text embedding model, covering 100+ languages with 3072-dimensional default output that can be shortened to 128, due to shut down on 2028-05-14 in favour of Gemini Embedding 2.
aliases: [gemini-embedding-001, gemini/gemini-embedding-001, gemini-embedding-exp-03-07, gemini-embedding-exp]
context_length: 20000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Gemini
open_weights: false
license: proprietary
release_date: "2025-07-14"
embedding_dimensions: 3072
mteb_score: 68.16
pricing:
  input: 0.15
  output: 0
sources:
  - https://openrouter.ai/google/gemini-embedding-001
  - https://openrouter.ai/api/v1/embeddings/models
  - https://ai.google.dev/gemini-api/docs/models/gemini-embedding-001
  - https://ai.google.dev/gemini-api/docs/embeddings
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/changelog
  - https://ai.google.dev/gemini-api/docs/deprecations
  - https://developers.googleblog.com/en/gemini-embedding-available-gemini-api/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Gemini Embedding 001

## Overview
gemini-embedding-001 became generally available on 2025-07-14 as the stable version of the experimental `gemini-embedding-exp-03-07` released in March 2025. Google's deprecations page sets its shutdown for 2028-05-14, with gemini-embedding-2 as the replacement. It is text only, in over 100 languages. Google's model page gives a 2,048-token input limit; OpenRouter lists a 20,000-token context, which the frontmatter follows. Output is 3072 dimensions by default and any size from 128 to 3072 through Matryoshka learning (768, 1536 and 3072 recommended); vectors below 3072 must be normalised by the caller. A `task_type` field selects one of eight tasks, such as `RETRIEVAL_QUERY`, `RETRIEVAL_DOCUMENT` and `CODE_RETRIEVAL_QUERY`. Google charges $0.15 per million tokens ($0.075 on the Batch API), the same as OpenRouter. The `mteb_score` is the 2048-dimension figure in Google's embeddings guide; Google gives none for 3072, and its launch post says the model led the MTEB Multilingual leaderboard.

## Strengths
- MTEB scores barely fall with size: 68.17 at 1536 dimensions, 67.99 at 768 and 66.19 at 256.
- Task types tune one model for search, classification, clustering, question answering, fact checking and code retrieval.
- Cheaper than gemini-embedding-2 for text: $0.15 against $0.20 per million tokens.

## Limitations
- Shut down on 2028-05-14; its vectors are incompatible with gemini-embedding-2, so migration means re-embedding.
- Google's 2,048-token input limit is far below OpenRouter's figure.
- Text only; no images or other media.

## Good for
- Existing text indexes built on Gemini embeddings.
- Multilingual retrieval with small vectors.
- Code retrieval through the dedicated task type.
