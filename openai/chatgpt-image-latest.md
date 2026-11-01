---
id: openai/chatgpt-image-latest
name: chatgpt-image-latest
owned_by: openai
type: image
description: chatgpt-image-latest is OpenAI's deprecated API alias for the image snapshot previously used in ChatGPT, priced like GPT Image 1.5 and shutting down on 2026-12-01.
aliases: [chatgpt-image-latest]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [image, text]
open_weights: false
license: proprietary
release_date: "2025-12-16"
sources:
  - https://developers.openai.com/api/docs/models/chatgpt-image-latest
  - https://developers.openai.com/api/docs/guides/image-generation
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://openrouter.ai/api/v1/models?output_modalities=image
  - https://artificialanalysis.ai/image/leaderboard/text-to-image
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# chatgpt-image-latest

## Overview
Deprecated: OpenAI announced on 2026-06-02 that chatgpt-image-latest shuts down on 2026-12-01, replaced by gpt-image-2.5-sunburst or gpt-image-2.5-flare; the model page recommends Sunburst for API use. OpenAI released it on 2025-12-16 alongside gpt-image-1.5 (OpenAI changelog) and describes it as pointing to the image snapshot previously used in ChatGPT; chatgpt-image-latest is its only listed snapshot. OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. It takes text and images, returns images and text, and runs on /v1/images/generations, /v1/images/edits and Batch (from 2026-02-10), with inpainting; it joined the Responses API image generation tool on 2025-12-19. Prices match gpt-image-1.5: per million tokens, $5 text input ($1.25 cached), $10 text output, $8 image input ($2 cached) and $32 image output, half on Batch. Per image that is $0.009, $0.034 or $0.133 at 1024x1024 for low, medium or high quality, and $0.013, $0.05 or $0.2 at 1024x1536 or 1536x1024.

## Strengths
- API access to the image snapshot previously used in ChatGPT.
- Inpainting with masks on the standard Image API.
- Batch processing at half price.

## Limitations
- Deprecated; shuts down on 2026-12-01.
- No dated snapshot to pin.
- Artificial Analysis's image boards (read 2026-11-01) do not list it.
- A 2026-01-09 fix was needed after edits used high input fidelity even when low was requested.
- Build-tier limits of 20 images and 250,000 tokens per minute.

## Good for
- Existing integrations built on it, until December 2026.
- Reproducing the style of the snapshot previously used in ChatGPT.
