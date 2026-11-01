---
id: openai/gpt-image-1
name: GPT Image 1
owned_by: openai
type: image
description: GPT Image 1 is OpenAI's April 2025 natively multimodal image generation and editing model, shut down on OpenAI's API on 2026-10-23 but still listed on OpenRouter's Images API.
aliases: [gpt-image-1, azure/gpt-image-1, databricks/databricks-gpt-image-1]
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
release_date: "2025-04-23"
sources:
  - https://developers.openai.com/api/docs/models/gpt-image-1
  - https://developers.openai.com/api/docs/guides/image-generation
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://openrouter.ai/openai/gpt-image-1
  - https://openrouter.ai/api/v1/models?output_modalities=image
  - https://openrouter.ai/api/v1/images/models/openai/gpt-image-1/endpoints
  - https://artificialanalysis.ai/image/leaderboard/text-to-image
  - https://artificialanalysis.ai/image/leaderboard/editing
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Image 1

## Overview
gpt-image-1 was added to the Image Generation and Edit endpoints on 2025-04-23 (OpenAI changelog). The id follows OpenRouter's Images API, which still lists openai/gpt-image-1. OpenAI announced its deprecation on 2026-04-22 and shut it down on 2026-10-23, recommending gpt-image-2.5-sunburst or gpt-image-2.5-flare; the model page and prices remain for reference. It took text and image input, returned images, and ran on /v1/images/generations, /v1/images/edits, Responses and Batch, with mask-based inpainting. Prices per million tokens were $5 for text input ($1.25 cached), $10 for image input ($2.50 cached) and $40 for image output; OpenRouter's image endpoint lists the same rates, while its model listing gives $10 prompt, $10 completion and $40 image output. Per image that came to $0.011, $0.042 or $0.167 at 1024x1024 for low, medium or high quality, and $0.016, $0.063 or $0.25 at 1024x1536 or 1536x1024.

## Strengths
- Artificial Analysis (read 2026-11-01), GPT Image 1 (high): Elo 1013 (95% interval 1001 to 1025, 5,518 samples) on AA-Image-T2I v2.1, rank 42, and 995 on AA-Image-Editing v2.1.
- Transparent backgrounds and up to 16 reference images per edit (OpenRouter).
- Low, medium and high quality settings that scale output tokens from 272 to 4,160 for a square image.

## Limitations
- Shut down on OpenAI's API; only third-party routes such as OpenRouter may still serve it.
- Far behind current OpenAI models on the same boards: GPT Image 2.5 Sunburst (max) leads text-to-image at 1222.
- OpenAI lists latency of up to two minutes for complex prompts, imprecise text placement, inconsistent recurring characters and weak layout control.
- Build-tier limits were 20 images and 250,000 tokens per minute.

## Good for
- Reproducing results from existing GPT Image 1 pipelines.
- Edits that need transparent output through a route that still serves it.
