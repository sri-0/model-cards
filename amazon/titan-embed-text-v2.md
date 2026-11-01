---
id: amazon/titan-embed-text-v2
name: Titan Text Embeddings V2
owned_by: amazon
type: embedding
description: Titan Text Embeddings V2 is Amazon's proprietary Bedrock text embedding model for retrieval, with an 8,192-token input, 1,024-dimensional vectors reducible to 512 or 256, optional binary output and English-first support for 100+ languages.
aliases: ["amazon.titan-embed-text-v2:0", amazon/Titan-text-embeddings-v2]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2024-04-30"
embedding_dimensions: 1024
pricing:
  input: 0.02
  output: 0
sources:
  - https://openrouter.ai/amazon/titan-embed-text-v2
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-titan-text-embeddings-v2.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html
  - https://aws.amazon.com/about-aws/whats-new/2024/04/amazon-titan-text-embeddings-v2-amazon-bedrock/
  - https://aws.amazon.com/blogs/aws/amazon-titan-text-v2-now-available-in-amazon-bedrock-optimized-for-improving-rag/
  - https://huggingface.co/amazon/Titan-text-embeddings-v2
  - https://huggingface.co/spaces/mteb/leaderboard
retrieved: "2026-11-01"
---

# Titan Text Embeddings V2

## Overview
Titan Text Embeddings V2 became generally available in Amazon Bedrock on 2024-04-30 as the second-generation Titan text embedder. OpenRouter serves it on its embeddings endpoint as `amazon/titan-embed-text-v2`; the Bedrock model id is `amazon.titan-embed-text-v2:0`. The weights are not released; a Hugging Face repo (`amazon/Titan-text-embeddings-v2`) holds only MTEB scores and usage examples. It takes a non-empty string of up to 8,192 tokens or 50,000 characters (about 4.7 characters per English token) and returns a 1,024-dimensional vector by default, or 512 or 256 on request. Output is normalised unless `normalize` is false, and `embeddingTypes` can add binary vectors. AWS says it was pre-trained on 100+ languages and code; Bedrock documents it as optimised for English with multilingual support. Bedrock lists it as Active, throttled by requests per minute.

## Strengths
- AWS reports about 99% of full retrieval accuracy at 512 dimensions and 97% at 256.
- Binary and float output, both supported as vector types in Bedrock Knowledge Bases.
- 8,192-token inputs, on-demand or Provisioned Throughput, with batch jobs for indexing.

## Limitations
- Proprietary and API-only; there are no weights to self-host.
- Cross-language queries (for example a Korean knowledge base queried in German) return sub-optimal results, per AWS.
- AWS recommends splitting long documents into paragraphs or sections despite the 8K limit.
- The MTEB leaderboard listed it without an overall mean on 2026-11-01, and AWS publishes no MTEB average in the docs.

## Good for
- RAG on AWS through Bedrock Knowledge Bases.
- English search where vector storage cost matters (256 dimensions or binary).
- Teams replacing Titan Embeddings G1 at a fifth of its OpenRouter price.
