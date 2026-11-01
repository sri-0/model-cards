---
id: google/gemini-embedding-2
name: Gemini Embedding 2
owned_by: google
type: embedding
description: Google's first multimodal embedding model, mapping text, images, video, audio and PDFs into one embedding space with 3072-dimensional output that can be shortened to 128.
aliases: [gemini-embedding-2, google/gemini-embedding-2:batch, gemini/gemini-embedding-2, vertex_ai/gemini-embedding-2, gemini-embedding-2-preview, google/gemini-embedding-2-preview, gemini/gemini-embedding-2-preview, vertex_ai/gemini-embedding-2-preview]
context_length: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image, file, audio, video]
  output_modalities: [embeddings]
  tokenizer: Gemini
open_weights: false
license: proprietary
release_date: "2026-04-22"
embedding_dimensions: 3072
pricing:
  input: 0.2
  output: 0
sources:
  - https://openrouter.ai/google/gemini-embedding-2
  - https://openrouter.ai/api/v1/embeddings/models
  - https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2
  - https://ai.google.dev/gemini-api/docs/embeddings
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/changelog
  - https://ai.google.dev/gemini-api/docs/deprecations
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Gemini Embedding 2

## Overview
Gemini Embedding 2 (`gemini-embedding-2`) became generally available on 2026-04-22, after `gemini-embedding-2-preview` launched on 2026-03-10; Google shut the preview down on 2026-08-10, and OpenRouter still lists both ids. It maps text, images, video, audio and PDFs into one embedding space within an 8,192-token input. Per request it takes up to six PNG or JPEG images, 180 seconds of MP3 or WAV audio, 120 seconds of video (up to 32 frames, audio track ignored) or one PDF of up to six pages. Output is 3072 dimensions by default, any size from 128 to 3072 (768, 1536 and 3072 recommended), and shortened vectors are normalised automatically. There is no `task_type` field; the task goes in the prompt as a prefix such as `task: search result | query: ...`. Several inputs in one request return one aggregated embedding. Google's price is $0.20 per million text tokens, $0.45 image, $6.50 audio and $12.00 video, halved on the Batch API; OpenRouter charges the same text rate.

## Strengths
- Cross-modal search over text, images, audio, video and documents in a single index.
- Matryoshka output from 128 to 3072 dimensions without manual renormalisation.
- No shutdown date announced; Google names it the replacement for `gemini-embedding-001` and `text-embedding-004`.

## Limitations
- Its vectors are incompatible with `gemini-embedding-001`, so upgrading means re-embedding all data.
- 8,192-token input shared across all modalities in a request.
- Google publishes MTEB scores only for `gemini-embedding-001`, so the card has no `mteb_score`.
- Proprietary and API only.

## Good for
- Multimodal retrieval-augmented generation and Gemini File Search over images.
- Recommendation and similarity search across mixed media.
- Teams already on the Gemini API or Vertex AI.
