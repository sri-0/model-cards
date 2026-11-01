---
id: meta/muse-image
name: Muse Image
owned_by: meta
type: image
description: Muse Image is Meta's proprietary agentic image generation and editing model, which reasons and searches the web before it renders and costs $0.01 per image.
aliases: [muse-image-1.0, meta/muse-image-1.0]
context_length: 65536
max_output_tokens: 58982
capabilities: [vision]
supported_parameters: [max_tokens, repetition_penalty, temperature, top_k, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-08-25"
sources:
  - https://openrouter.ai/meta/muse-image
  - https://openrouter.ai/api/v1/models
  - https://dev.meta.ai/models/muse-image
  - https://dev.meta.ai/docs/image-generation
  - https://dev.meta.ai/docs/models
  - https://dev.meta.ai/docs/pricing-rate-limits
  - https://dev.meta.ai/resources/blog/build-with-muse-Image
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Muse Image

## Overview
Muse Image (API id `muse-image-1.0`) is Meta's image generation and editing model. Meta opened it to developers on Meta Model API on August 25, 2026, after using it in Meta AI since July. It takes text and optional reference images and returns an image: one model covers generation, targeted edits, multi-image composition and multi-turn refinement. It reasons before rendering and by default searches the web and images for references and current facts and runs code to lay out charts; each tool can be switched off per request. Meta serves it through the Responses API and OpenAI-compatible `/v1/images/generations` and `/v1/images/edits` endpoints; fal, Runway and OpenRouter (65,536-token context) also offer it. Output is up to 1600px in WebP (default), PNG or JPEG. Price: a flat $0.01 per generated image on Meta Model API and OpenRouter, including the built-in search and at any reasoning strength; images that fail or are removed by safety filtering are not billed.

## Strengths
- Edits change what was asked and keep the rest intact; reference images keep a character, style and setting consistent across a series.
- Search grounding for real landmarks, products, logos and current data at no extra cost.
- `reasoning_strength: "low"` returns after a single pass for faster results at the same price.

## Limitations
- Exact text rendering varies between runs; Meta advises short baked-in text and re-running unclear labels.
- Multi-input compositions may be rearranged and redrawn, and every call is non-deterministic.
- `size` sets only the aspect ratio. Masks, `input_fidelity` and partial images are rejected, as is any tool other than `image_generation`.
- Proprietary and API-only, and the grounding tools need internet access.

## Good for
- Catalogue, advertising and personalised imagery at scale.
- Infographics and charts that depend on current facts.
- Conversational, step-by-step image editing.
