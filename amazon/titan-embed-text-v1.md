---
id: amazon/titan-embed-text-v1
name: Titan Embeddings G1 - Text
owned_by: amazon
type: embedding
description: Titan Embeddings G1 - Text is Amazon's first-generation proprietary Bedrock text embedding model, taking up to 8,192 tokens and returning fixed 1,536-dimensional float vectors.
aliases: [amazon.titan-embed-text-v1]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2023-09-28"
embedding_dimensions: 1536
pricing:
  input: 0.1
  output: 0
sources:
  - https://openrouter.ai/amazon/titan-embed-text-v1
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-titan-embeddings-g1---text.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html
  - https://aws.amazon.com/blogs/aws/amazon-titan-text-v2-now-available-in-amazon-bedrock-optimized-for-improving-rag/
retrieved: "2026-11-01"
---

# Titan Embeddings G1 - Text

## Overview
Titan Embeddings G1 - Text is Amazon's first Titan text embedding model; its Bedrock model card gives a launch date of 2023-09-28. OpenRouter serves it on its embeddings endpoint as `amazon/titan-embed-text-v1`; the Bedrock model id is `amazon.titan-embed-text-v1`. The weights are not released. It converts text into vectors for search, personalisation and clustering, accepts up to 8,192 tokens and always returns a 1,536-dimensional float vector. The request takes only `inputText`; there are no inference parameters, no dimension choice and no binary output. Bedrock lists it as Active and supports it in Knowledge Bases.

## Strengths
- Long 8,192-token inputs.
- A long-standing Bedrock default: AWS notes that knowledge bases built with the original Titan model keep working after V2's release.
- Simple request format with a token count in every response.

## Limitations
- Proprietary and API-only; there are no weights to self-host.
- Fixed 1,536 dimensions cost more storage than V2's 1,024, 512 or 256, with no binary option.
- Five times V2's OpenRouter price ($0.10 against $0.02 per million input tokens).
- AWS publishes no benchmark scores for it in the Bedrock docs, and it is not on the MTEB leaderboard tables.

## Good for
- Existing indexes that were built with G1 and must stay compatible.
- Bedrock Knowledge Bases already configured for 1,536-dimensional vectors.
- New projects should compare it with Titan Text Embeddings V2 first.
