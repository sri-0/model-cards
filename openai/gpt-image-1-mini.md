---
id: openai/gpt-image-1-mini
name: GPT Image 1 Mini
owned_by: openai
type: image
description: GPT Image 1 Mini is the cost-efficient version of OpenAI's GPT Image 1 for image generation and editing, released at DevDay 2025 and deprecated, shutting down on 2026-12-01.
aliases: [gpt-image-1-mini, azure/gpt-image-1-mini, databricks/databricks-gpt-image-1-mini]
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
release_date: "2025-10-06"
sources:
  - https://developers.openai.com/api/docs/models/gpt-image-1-mini
  - https://developers.openai.com/api/docs/guides/image-generation
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://openrouter.ai/openai/gpt-image-1-mini
  - https://openrouter.ai/api/v1/models?output_modalities=image
  - https://openrouter.ai/api/v1/images/models/openai/gpt-image-1-mini/endpoints
  - https://artificialanalysis.ai/image/leaderboard/text-to-image
  - https://artificialanalysis.ai/image/leaderboard/editing
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Image 1 Mini

## Overview
gpt-image-1-mini was released at OpenAI DevDay on 2025-10-06 for more cost-efficient image generation and editing (OpenAI changelog). The id follows OpenRouter's Images API, which lists openai/gpt-image-1-mini. OpenAI describes it as a natively multimodal language model that takes text and image input and produces images. It runs on /v1/images/generations, /v1/images/edits and Batch, but not Responses. Prices per million tokens are $2 for text input ($0.20 cached), $2.50 for image input ($0.25 cached) and $8 for image output, half that on Batch; OpenRouter's image endpoint lists the same rates, while its model listing gives $2.50 prompt, $2.50 completion and $8 image output. Per image that is $0.005, $0.011 or $0.036 at 1024x1024 for low, medium or high quality, and $0.006, $0.015 or $0.052 at 1024x1536 or 1536x1024. OpenAI announced its deprecation on 2026-06-02; it shuts down on 2026-12-01, replaced by gpt-image-2.5-sunburst or gpt-image-2.5-flare.

## Strengths
- Image output at a fifth of GPT Image 1's rate ($8 against $40 per million tokens).
- Artificial Analysis (read 2026-11-01), GPT Image 1 Mini (medium): Elo 936 (95% interval 919 to 953, 2,333 samples) on AA-Image-T2I v2.1 and 934 on AA-Image-Editing v2.1, at $11 per 1,000 images.
- Transparent backgrounds, up to 10 images per request and up to 16 reference images (OpenRouter).

## Limitations
- Deprecated; shuts down on 2026-12-01.
- Rank 71 on AA-Image-T2I v2.1, well behind GPT Image 1 (high) at 1013 and GPT Image 2.5 Sunburst (max) at 1222.
- OpenAI lists latency of up to two minutes for complex prompts, imprecise text placement and weak layout control for GPT Image models.
- Build-tier limits of 20 images and 250,000 tokens per minute.

## Good for
- High-volume image generation until December 2026 where cost matters more than fidelity.
- Batch API image jobs at half price.
