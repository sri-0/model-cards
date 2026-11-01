---
id: openai/code-search-ada-code-001
name: code-search-ada-code-001
owned_by: openai
type: embedding
description: code-search-ada-code-001 was the code model of OpenAI's first-generation Ada code search embeddings, returning 1024-dimensional vectors; released in January 2022, it was shut down on 4 January 2024.
aliases: [code-search-ada-code-001]
context_length: 2048
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
release_date: "2022-01-25"
embedding_dimensions: 1024
sources:
  - https://developers.openai.com/api/docs/deprecations
  - https://web.archive.org/web/2022/https://openai.com/blog/introducing-text-and-code-embeddings/
  - https://arxiv.org/abs/2201.10005
  - https://web.archive.org/web/2023/https://openai.com/blog/new-and-improved-embedding-model
  - https://github.com/MicrosoftDocs/azure-docs/blob/fa38b7af737af91fddad7911466e1024990d3830/articles/cognitive-services/openai/concepts/models.md
  - https://github.com/MicrosoftDocs/azure-docs/blob/66b43614bc301725230b0d49ee867b5ae54e409c/articles/cognitive-services/openai/concepts/models.md
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# code-search-ada-code-001

## Overview
Shut down: OpenAI retired `code-search-ada-code-001` on 4 January 2024 (announced 6 July 2023); its deprecations page now names text-embedding-3-small as the replacement. OpenRouter does not list it; the id is OpenAI's API id. It was the code half of the Ada pair in OpenAI's first-generation code search family, launched with the /embeddings endpoint on 25 January 2022 for code search. This model embeds the code snippets to be retrieved; its partner `code-search-ada-text-001` handles the natural-language queries. OpenAI's paper describes the code models as initialised from Codex and trained on docstring and implementation pairs. It returned 1024-dimensional vectors and, per OpenAI's December 2022 post, took inputs of up to 2,048 tokens. Azure OpenAI listed a 2,046-token limit and training data up to August 2020. OpenAI's last price was $4.00 per million tokens.

## Strengths
- 93.4% average over six languages on CodeSearchNet for the Ada code search pair (OpenAI's launch post), against a previous best of 77.4%.
- The paper reports a 20.8% relative improvement over prior best work on code search for its code embedding models.
- 0.1 points behind Babbage, at a lower price and half the vector size.

## Limitations
- No longer accessible, so stored vectors cannot be extended or refreshed with the same model.
- Superseded in December 2022 by text-embedding-ada-002, which OpenAI says beats all the old models on text search, code search and sentence similarity, with four times the context and a price 90% below old models of the same size.
- Designed to work with `code-search-ada-text-001`; OpenAI reported results for the pair, not for either model alone.
- Offered in Ada and Babbage sizes only.

## Good for
- Recognising the id in old code search indexes, configurations and logs holding 1024-dimensional code vectors.
- Planning a migration: Azure's docs note that moving between embedding models means generating new embeddings.
