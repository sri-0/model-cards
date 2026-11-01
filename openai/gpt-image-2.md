---
id: openai/gpt-image-2
name: GPT Image 2
owned_by: openai
type: image
description: GPT Image 2 is OpenAI's April 2026 image generation and editing model with flexible sizes up to 4K, always-high-fidelity image inputs and token-based pricing, now listed by OpenAI among its earlier GPT Image models.
aliases: [gpt-image-2, gpt-image-2-2026-04-21, azure/gpt-image-2, azure/gpt-image-2-2026-04-21, azure_ai/gpt-image-2, fal_ai/openai/gpt-image-2, databricks/databricks-gpt-image-2]
context_length: 400000
max_output_tokens: 360000
capabilities: [vision, structured_output]
supported_parameters: [max_tokens, response_format, seed, structured_outputs]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-04-21"
sources:
  - https://openrouter.ai/openai/gpt-image-2
  - https://openrouter.ai/api/v1/models?output_modalities=image
  - https://openrouter.ai/api/v1/images/models/openai/gpt-image-2/endpoints
  - https://developers.openai.com/api/docs/models/gpt-image-2
  - https://developers.openai.com/api/docs/guides/image-generation
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://artificialanalysis.ai/image/leaderboard/text-to-image
  - https://artificialanalysis.ai/image/leaderboard/editing
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Image 2

## Overview
GPT Image 2 was released on 2026-04-21 for image generation and editing, with flexible image sizes, high-fidelity image inputs, token-based pricing and Batch support at a 50% discount (OpenAI changelog). The default snapshot is gpt-image-2-2026-04-21. OpenRouter lists it on its Images API as openai/gpt-image-2. It runs on /v1/images/generations, /v1/images/edits and Batch, and as the Responses API image generation tool, with inpainting. Any size up to 3840 px per edge is accepted when both edges are multiples of 16, the ratio is at most 3:1 and the total is 655,360 to 8,294,400 pixels. Quality is low, medium, high or auto. Transparent backgrounds have been in preview since 2026-08-20. OpenAI charges $5 per million text input tokens ($1.25 cached), $8 per million image input tokens ($2 cached, Responses API only) and $30 per million image output tokens. OpenRouter's image endpoint lists the same rates, but its model listing gives $8 for both prompt and completion. OpenAI now lists it under earlier GPT Image models and points new work to GPT Image 2.5. OpenAI publishes no context window; the frontmatter's 400,000 and 360,000 are OpenRouter's.

## Strengths
- Artificial Analysis (read 2026-11-01), GPT Image 2 (high): Elo 1186 (95% interval 1175 to 1197, 12,835 samples) on AA-Image-T2I v2.1, rank 3, and 1136 on AA-Image-Editing v2.1, rank 8.
- 2K and 4K output.
- Every image input is processed at high fidelity, so edits keep detail.

## Limitations
- Behind GPT Image 2.5 Sunburst (1222) and Flare (1207) at the same token rates.
- No xhigh or max quality, which only GPT Image 2.5 offers.
- Always-high-fidelity inputs raise input-token costs for edits with reference images.
- Build-tier limits of 20 images and 250,000 tokens per minute.

## Good for
- Existing integrations pinned to gpt-image-2-2026-04-21.
- Large-format generation where 4K output matters.
