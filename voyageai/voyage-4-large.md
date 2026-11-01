---
id: voyageai/voyage-4-large
name: voyage-4-large
owned_by: voyageai
type: embedding
description: Voyage AI's flagship general-purpose and multilingual text embedding model, a mixture-of-experts model with a 32,000-token input, 1024-dimensional default output and an embedding space shared with the rest of the Voyage 4 family.
aliases: [voyage-4-large, voyage/voyage-4-large]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-01-15"
embedding_dimensions: 1024
pricing:
  input: 0.12
  output: 0
sources:
  - https://openrouter.ai/voyageai/voyage-4-large
  - https://openrouter.ai/api/v1/embeddings/models
  - https://docs.voyageai.com/docs/embeddings
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2026/01/15/voyage-4/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# voyage-4-large

## Overview
voyage-4-large is the top model of the Voyage 4 family that Voyage AI (a MongoDB company) announced on 2026-01-15. Voyage calls it the first production-grade embedding model with a mixture-of-experts architecture, with serving costs 40% lower than comparable dense models. OpenRouter lists it in its embeddings catalogue at $0.12 per million input tokens, matching Voyage's price; the first 200 million tokens are free, and Voyage's Batch API takes 33% off. Input is up to 32,000 tokens per text, with up to 1,000 texts and 120K tokens per request. Output is 1024 dimensions by default, or 256, 512 or 2048, as float, int8, uint8, binary or ubinary. All Voyage 4 models share one embedding space, and Voyage recommends embedding documents with voyage-4-large and queries with a smaller model. Voyage publishes no MTEB score; it evaluates on RTEB's 29 datasets with NDCG@10.

## Strengths
- Voyage reports average leads of 3.87% over Gemini Embedding 001, 8.20% over Cohere Embed v4 and 14.05% over OpenAI's text-embedding-3-large on RTEB.
- 1.87% ahead of voyage-4 and 4.80% ahead of voyage-4-lite.
- Better accuracy than voyage-3-large at a lower price ($0.12 against $0.18).

## Limitations
- Twice the price of voyage-4 and six times voyage-4-lite.
- Per-request token cap of 120K is lower than voyage-4's 320K.
- All margins are Voyage's own; absolute scores are only in charts and a spreadsheet.

## Good for
- Document-side embedding for high-quality search indexes.
- Asymmetric retrieval with voyage-4 or voyage-4-lite on the query side.
- Multilingual enterprise retrieval where quality matters most.
