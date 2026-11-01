---
id: openai/text-search-davinci-doc-001
name: text-search-davinci-doc-001
owned_by: openai
type: embedding
description: text-search-davinci-doc-001 was the document model of OpenAI's first-generation Davinci text search embeddings, returning 12288-dimensional vectors; released in January 2022, it was shut down on 4 January 2024.
aliases: [text-search-davinci-doc-001]
context_length: 2048
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
release_date: "2022-01-25"
embedding_dimensions: 12288
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

# text-search-davinci-doc-001

## Overview
Shut down: OpenAI retired `text-search-davinci-doc-001` on 4 January 2024 (announced 6 July 2023); its deprecations page now names text-embedding-3-small as the replacement. OpenRouter does not list it; the id is OpenAI's API id. It was the document half of the Davinci pair in OpenAI's first-generation text search family, launched with the /embeddings endpoint on 25 January 2022 for semantic search and information retrieval. This model embeds the documents to be retrieved; its partner `text-search-davinci-query-001` handles the search queries, and the two vectors are compared by cosine similarity. It returned 12288-dimensional vectors and, per OpenAI's December 2022 post, took inputs of up to 2,048 tokens. Azure OpenAI listed a 2,046-token limit and training data up to August 2020. OpenAI's last price was $200.00 per million tokens.

## Strengths
- 52.8% average over 11 BEIR search tasks for the Davinci doc and query pair (OpenAI's launch post), against a previous best of 50.2%; sizes ranged from 49.0% (Ada) to 52.8% (Davinci).
- OpenAI says embedding search generalises better than keyword search because it is less sensitive to exact words.
- The highest BEIR result of the family.

## Limitations
- No longer accessible, so stored vectors cannot be extended or refreshed with the same model.
- Superseded in December 2022 by text-embedding-ada-002, which OpenAI says beats all the old models on text search, code search and sentence similarity, with four times the context and a price 90% below old models of the same size.
- Designed to work with `text-search-davinci-query-001`; OpenAI reported results for the pair, not for either model alone.
- The costliest pair, at $200.00 per million tokens, with vectors eight times ada-002's size.

## Good for
- Recognising the id in old search indexes, configurations and logs holding 12288-dimensional document vectors.
- Planning a migration: Azure's docs note that moving between embedding models means generating new embeddings.
