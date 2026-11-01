---
id: cohere/embed-v5.0-fast
name: Embed 5 Fast
owned_by: cohere
type: embedding
description: Cohere's low-latency Embed 5 model, a roughly 1B-parameter multimodal embedder sharing Embed 5 Pro's embedding space, with a 128K-token context, 100+ languages and 2048-dimensional default output.
aliases: [embed-v5.0-fast, Cohere-Embed-V5-Fast, azure_ai/Cohere-Embed-V5-Fast]
context_length: 128000
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [embeddings]
open_weights: false
license: proprietary
release_date: "2026-09-30"
embedding_dimensions: 2048
sources:
  - https://docs.cohere.com/docs/cohere-embed
  - https://docs.cohere.com/docs/models
  - https://docs.cohere.com/changelog/embed-v5
  - https://docs.cohere.com/reference/embed
  - https://cohere.com/blog/embed-5
  - https://cohere.com/pricing
  - https://openrouter.ai/api/v1/embeddings/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Embed 5 Fast

## Overview
Embed 5 Fast (`embed-v5.0-fast`) was announced on 2026-09-30 as the faster, lighter tier of Cohere's Embed 5 family. OpenRouter does not list it; the id is Cohere's API id. It has about 1B parameters and takes the same inputs as Embed 5 Pro: text, images and mixed text-and-image inputs such as PDF pages, over a 128K-token context in 100+ languages. Output is Matryoshka embeddings of 256, 512, 768, 1024, 1536 or 2048 (default) dimensions, as float, int8 or binary. It shares Pro's embedding space, so it can query a corpus indexed with Pro; Cohere aims it at interactive search, agent loops and high-volume query traffic. Cohere's launch price is $0.08 per million text tokens and $0.40 per million image tokens. It is served on Cohere's API, Model Vault, Microsoft Foundry and Amazon SageMaker, and can be self-hosted with vLLM. Cohere publishes no MTEB score for it.

## Strengths
- Cohere's ViDoRe V3 average: 84.5, ahead of voyage-4-large (83.7), Gemini Embedding 2 (83.2) and Embed 4 (77.0).
- 377.3 documents per second, about 2.4 times Pro on average across context sizes.
- Fast queries over a Pro index keep 98.4% of Pro-on-Pro quality; Fast on Fast keeps 96.6%.

## Limitations
- Behind Pro on most of Cohere's benchmarks, for example 88.8 against 90.0 on FinQA and 73.2 against 77.0 on page-image retrieval.
- Several Asian languages trail Gemini Embedding 2 in Cohere's own multilingual table.
- Proprietary; all figures are Cohere's.

## Good for
- Query-side embedding against an Embed 5 Pro index.
- Agent loops and interactive search where latency matters.
- Lower-cost multimodal indexing.
