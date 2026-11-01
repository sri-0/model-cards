---
id: amazon/titan-embed-image-v1
name: Titan Multimodal Embeddings G1
owned_by: amazon
type: embedding
description: Titan Multimodal Embeddings G1 is Amazon's proprietary Bedrock model that embeds English text, images or both into one 1,024-dimensional space (384 or 256 on request) for multimodal search and recommendation, with fine-tuning on image-text pairs.
aliases: [amazon.titan-embed-image-v1]
context_length: 128
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [embeddings]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2023-11-29"
embedding_dimensions: 1024
pricing:
  input: 0.8
  output: 0
sources:
  - https://openrouter.ai/amazon/titan-embed-image-v1
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://docs.aws.amazon.com/bedrock/latest/userguide/titan-multiemb-models.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-mm.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-titan-multimodal-embeddings-g1.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html
  - https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-titan-multimodal-embeddings-model-bedrock/
retrieved: "2026-11-01"
---

# Titan Multimodal Embeddings G1

## Overview
Titan Multimodal Embeddings G1 became generally available in Amazon Bedrock on 2023-11-29. OpenRouter serves it on its embeddings endpoint as `amazon/titan-embed-image-v1`, listing a 128-token context; Bedrock documents 256 input text tokens. The Bedrock model id is `amazon.titan-embed-image-v1`, and the weights are not released. It maps text, an image or both into a shared semantic space, so images can be searched by text, by image or by a combination. Requests carry `inputText` and a base64 `inputImage` (up to 25 MB and 2,048 x 2,048 pixels), and `embeddingConfig.outputEmbeddingLength` picks 1,024 (default), 384 or 256 dimensions. Text input is English only. Bedrock lists it as Active.

## Strengths
- One vector space for text and images, aimed at search, recommendation and personalisation.
- Fine-tuning on Bedrock with 1,000 to 500,000 image-text pairs (PNG or JPEG, captions up to 128 tokens).
- Smaller 384- or 256-dimensional vectors speed up responses, per AWS.
- Supported as a vector source in Bedrock Knowledge Bases.

## Limitations
- Proprietary and API-only; there are no weights to self-host.
- English text only, and very short text inputs (256 tokens per Bedrock, 128 on OpenRouter).
- AWS publishes no benchmark scores for it in the Bedrock docs.
- Expensive per text token on OpenRouter ($0.80 per million input tokens).

## Good for
- Product and stock-image search by text or example image.
- Recommendation systems that mix captions and pictures.
- AWS workloads that want a managed, fine-tunable image embedder.
