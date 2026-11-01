---
id: voyageai/voyage-code-4
name: voyage-code-4
owned_by: voyageai
type: embedding
description: Voyage AI's code embedding model for coding agents and code search, trained on queries mined from issue-fixing pull requests, with a 32,000-token input and 1024-dimensional default output.
aliases: [voyage-code-4, voyage/voyage-code-4]
context_length: 32000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-08-13"
embedding_dimensions: 1024
pricing:
  input: 0.12
  output: 0
sources:
  - https://openrouter.ai/voyageai/voyage-code-4
  - https://openrouter.ai/api/v1/embeddings/models
  - https://docs.voyageai.com/docs/embeddings
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2026/08/13/voyage-code-4/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# voyage-code-4

## Overview
voyage-code-4 is Voyage AI's code embedding model, announced on 2026-08-13 as the successor to voyage-code-3, which Voyage now lists among its earlier models. OpenRouter lists it in its embeddings catalogue at $0.12 per million input tokens, matching Voyage's price, a third below voyage-code-3; the first 200 million tokens are free. It takes up to 32,000 tokens per input and returns 1024 dimensions by default, or 256, 512 or 2048 through Matryoshka learning, as float, int8, uint8 or binary. Voyage trained it on a new corpus of natural-language queries paired with code from completed issue-fixing pull requests, covering hundreds of programming languages and tens of thousands of repositories. Voyage publishes no MTEB score; its benchmarks are NDCG@10 on its own code retrieval suites.

## Strengths
- Agentic code retrieval (19 benchmarks from issue-fixing pull requests): Voyage reports average gains of 27.54% over voyage-code-3, 28.25% over Cohere Embed v4, 31.03% over Gemini Embedding 2 and 48.58% over OpenAI's text-embedding-3-large.
- Traditional code search (28 datasets): 13.98%, 19.21%, 16.01% and 40.06% over the same four models.
- Voyage recommends pairing it with grep: grep for known identifiers, voyage-code-4 for symptom-style queries such as bug reports.

## Limitations
- Text and code only.
- All margins are Voyage's own; absolute scores are only in charts and a spreadsheet.
- Twice the price of voyage-4 per token.

## Good for
- Retrieval tools for coding agents working from issue or bug descriptions.
- Semantic code search alongside full-text search.
- Code RAG over large multi-language repositories.
