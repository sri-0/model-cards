---
id: qwen/qwen3.7-text-embedding-flash
name: Qwen3.7 Text Embedding Flash
owned_by: qwen
type: embedding
description: The lower-cost, lightweight version of Alibaba Cloud Model Studio's qwen3.7-text-embedding, keeping 201-language support and a 128K-token context without sparse vectors or other advanced features.
aliases: [qwen3.7-text-embedding-flash]
context_length: 128000
architecture:
  input_modalities: [text]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
sources:
  - https://www.alibabacloud.com/help/en/model-studio/embedding
  - https://www.alibabacloud.com/help/en/model-studio/text-embedding-synchronous-api
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/embeddings/models
retrieved: "2026-11-01"
---

# Qwen3.7 Text Embedding Flash

## Overview
qwen3.7-text-embedding-flash is named in Alibaba Cloud Model Studio's embedding guide as the lightweight version of qwen3.7-text-embedding, for cost-sensitive work that does not need sparse vectors or other advanced features. The guide says it keeps 201-language support and a 128K-token context "at a more cost-effective price", and lists it among the models that accept custom vector dimensions. OpenRouter does not list it; the id is the Model Studio API id. Neither the guide's model table, the text embedding API reference nor the pricing page lists it with dimensions, a region, batch limits or a price, so the card has no `embedding_dimensions` and gives no price. Alibaba publishes no release date or benchmark scores for it.

## Strengths
- Same 201-language coverage and 128K-token context as qwen3.7-text-embedding, per Alibaba.
- Custom output dimensions.
- Positioned below qwen3.7-text-embedding on price.

## Limitations
- No sparse vectors or the full model's other advanced features, such as task instructions.
- Model tables, limits and prices are not yet published.
- No benchmark figures; proprietary and API only.

## Good for
- Cost-sensitive multilingual embedding on Model Studio.
- Long-document embedding where dense vectors are enough.
- Trials before choosing between the flash and full qwen3.7 models.
