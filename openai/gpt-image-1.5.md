---
id: openai/gpt-image-1.5
name: GPT Image 1.5
owned_by: openai
type: image
description: GPT Image 1.5 is OpenAI's December 2025 image generation and editing model with better instruction following than GPT Image 1, deprecated and shutting down on 2026-12-01.
aliases: [gpt-image-1.5, gpt-image-1.5-2025-12-16, azure/gpt-image-1.5, azure/gpt-image-1.5-2025-12-16, databricks/databricks-gpt-image-1-5]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [image, text]
open_weights: false
license: proprietary
release_date: "2025-12-16"
sources:
  - https://developers.openai.com/api/docs/models/gpt-image-1.5
  - https://developers.openai.com/api/docs/guides/image-generation
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://openrouter.ai/api/v1/models?output_modalities=image
  - https://artificialanalysis.ai/image/leaderboard/text-to-image
  - https://artificialanalysis.ai/image/leaderboard/editing
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Image 1.5

## Overview
Deprecated: OpenAI announced on 2026-06-02 that gpt-image-1.5 and its snapshot gpt-image-1.5-2025-12-16 shut down on 2026-12-01, replaced by gpt-image-2.5-sunburst or gpt-image-2.5-flare. It was released on 2025-12-16 with chatgpt-image-latest (OpenAI changelog), joined the Responses API image generation tool on 2025-12-19 and Batch on 2026-02-10. OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. OpenAI calls it its previous image generation model, with better instruction following and prompt adherence. It takes text and images, returns images and text, and runs on /v1/images/generations, /v1/images/edits and Batch, with inpainting. Prices per million tokens are $5 text input ($1.25 cached), $10 text output, $8 image input ($2 cached) and $32 image output, half on Batch. Per image that is $0.009, $0.034 or $0.133 at 1024x1024 for low, medium or high quality, and $0.013, $0.05 or $0.2 at 1024x1536 or 1536x1024.

## Strengths
- Artificial Analysis (read 2026-11-01), GPT Image 1.5 (high): Elo 1123 (95% interval 1112 to 1134, 12,830 samples) on AA-Image-T2I v2.1, rank 9, and 1119 on AA-Image-Editing v2.1.
- Cheaper per image than GPT Image 1 at every listed size and quality ($0.133 against $0.167 for a high-quality square).
- 110 Elo points above GPT Image 1 (high) on text-to-image.

## Limitations
- Deprecated; shuts down on 2026-12-01.
- Behind GPT Image 2 (1186) and GPT Image 2.5 Sunburst (1222) on the same board.
- A 2026-01-09 fix was needed after edits used high input fidelity even when low was requested.
- Build-tier limits of 20 images and 250,000 tokens per minute.

## Good for
- Existing GPT Image 1.5 pipelines until December 2026.
- Batch jobs that need its per-image pricing.
