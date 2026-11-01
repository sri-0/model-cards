---
id: voyageai/voyage-multimodal-3.5
name: voyage-multimodal-3.5
owned_by: voyageai
type: embedding
description: Voyage AI's multimodal embedding model for interleaved text, images and video frames such as PDF screenshots, slides and figures, with a 32,000-token input and 1024-dimensional default output.
aliases: [voyage-multimodal-3.5]
context_length: 32000
capabilities: [vision]
architecture:
  input_modalities: [text, image]
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
  - https://openrouter.ai/voyageai/voyage-multimodal-3.5
  - https://openrouter.ai/api/v1/embeddings/models
  - https://docs.voyageai.com/docs/multimodal-embeddings
  - https://docs.voyageai.com/docs/pricing
  - https://blog.voyageai.com/2026/01/15/voyage-multimodal-3-5/
retrieved: "2026-11-01"
---

# voyage-multimodal-3.5

## Overview
voyage-multimodal-3.5 is Voyage AI's multimodal embedding model, announced on 2026-01-15 as the successor to voyage-multimodal-3. One transformer encoder embeds interleaved text and visual content, such as PDF screenshots, slides, tables and figures, and it is the only Voyage model that accepts video, passed as a sequence of frames. OpenRouter lists text and image input at $0.12 per million tokens. Voyage charges $0.12 per million text tokens plus $0.60 per billion pixels, with 200 million tokens and 150 billion pixels free; an image costs between $0.00003 and $0.0012. Each input may hold 32,000 tokens (560 image pixels or 1,120 video pixels count as one token), and a request up to 1,000 inputs and 320,000 tokens; images are capped at 16 million pixels and 20 MB, videos at 20 MB. Output is 1024 dimensions by default, or 256, 512 or 2048, as float, int8, uint8 or binary.

## Strengths
- Voyage reports 4.56% higher accuracy than Cohere Embed v4 across 15 visual document datasets and 3.03% over voyage-multimodal-3.
- Video retrieval 4.65% ahead of Google's multimodalembedding@001 on MSR-VTT, YouCook2 and DiDeMo.
- On text retrieval (38 datasets) it comes within 0.29% of voyage-3-large and beats Cohere Embed v4 by 3.49%.

## Limitations
- Long videos must be split into scenes that fit 32,000 tokens.
- All margins are Voyage's own NDCG@10 comparisons; absolute scores are in charts only.
- OpenRouter's listing covers text and images, not video.

## Good for
- Search over documents as images, without text extraction.
- Video and slide retrieval for RAG.
- Mixed text-and-image corpora in one index.
