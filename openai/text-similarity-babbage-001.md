---
id: openai/text-similarity-babbage-001
name: text-similarity-babbage-001
owned_by: openai
type: embedding
description: text-similarity-babbage-001 was the Babbage size of OpenAI's first-generation text similarity embeddings, returning 2048-dimensional vectors; released in January 2022, it was shut down on 4 January 2024.
aliases: [text-similarity-babbage-001]
context_length: 2048
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
release_date: "2022-01-25"
embedding_dimensions: 2048
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

# text-similarity-babbage-001

## Overview
Shut down: OpenAI retired `text-similarity-babbage-001` on 4 January 2024 (announced 6 July 2023); its deprecations page now names text-embedding-3-small as the replacement. OpenRouter does not list it; the id is OpenAI's API id. It was the Babbage size of the text similarity family, one of three embedding families OpenAI launched with the /embeddings endpoint on 25 January 2022. OpenAI pitched it for clustering, regression, anomaly detection, visualisation and classification; its paper describes contrastive pre-training on neighbouring Internet text, starting from GPT models. It returned 2048-dimensional vectors and, per OpenAI's December 2022 post, took inputs of up to 2,048 tokens. Azure OpenAI listed a 2,046-token limit and training data up to August 2020. OpenAI's last price was $5.00 per million tokens.

## Strengths
- 91.1% average linear-probe accuracy over seven SentEval datasets (OpenAI's launch post), against a previous best of 90.2%; sizes ranged from 89.3% (Ada) to 92.2% (Davinci).
- Similarity is a dot product of two vectors, giving a cosine similarity between -1 and 1, so embeddings could be precomputed and compared quickly.
- OpenAI's launch post plotted its embeddings of 100 DBpedia samples, which formed five clear clusters, one per category, after PCA reduced the 2048 dimensions to three.

## Limitations
- No longer accessible, so stored vectors cannot be extended or refreshed with the same model.
- Superseded in December 2022 by text-embedding-ada-002, which OpenAI says beats all the old models on text search, code search and sentence similarity, with four times the context and a price 90% below old models of the same size.

## Good for
- Recognising the id in old configurations, logs and vector stores holding 2048-dimensional vectors.
- Planning a migration: Azure's docs note that moving between embedding models means generating new embeddings.
