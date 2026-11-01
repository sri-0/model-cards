---
id: openai/gpt-image-2.5-flare
name: GPT Image 2.5 Flare
owned_by: openai
type: image
description: GPT Image 2.5 Flare is OpenAI's fastest model for high-quality everyday image generation and editing, released in September 2026 as the speed-oriented tier of GPT Image 2.5.
aliases: [gpt-image-2.5-flare, gpt-image-2.5-flare-2026-09-08, azure/gpt-image-2.5-flare, openai/gpt-image-2.5-flare-20260908]
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
release_date: "2026-09-08"
sources:
  - https://openrouter.ai/openai/gpt-image-2.5-flare
  - https://openrouter.ai/api/v1/models?output_modalities=image
  - https://openrouter.ai/api/v1/images/models/openai/gpt-image-2.5-flare/endpoints
  - https://developers.openai.com/api/docs/models/gpt-image-2.5-flare
  - https://developers.openai.com/api/docs/guides/image-generation
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://artificialanalysis.ai/image/leaderboard/text-to-image
  - https://artificialanalysis.ai/image/leaderboard/editing
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Image 2.5 Flare

## Overview
GPT Image 2.5 Flare was released on 2026-09-08 with GPT Image 2.5 Sunburst (OpenAI changelog). OpenAI calls it its fastest model for high-quality, everyday image generation; OpenRouter describes it as the speed-oriented tier of the series, suited to high-volume generation, creator content and rapid prototyping, and lists it on its Images API as openai/gpt-image-2.5-flare. The snapshot is gpt-image-2.5-flare-2026-09-08. It takes text and images, returns images, and runs on /v1/images/generations, /v1/images/edits, Batch and the Responses API image generation tool, with inpainting. Quality settings are low, medium, high, xhigh, max and auto; custom sizes run up to 3840 px per edge. OpenAI charges $5 per million text input tokens ($1.25 cached), $8 per million image input tokens ($2 cached, Responses API only) and $30 per million image output tokens ($15 on Batch); text output is not billed. OpenRouter's image endpoint lists the same rates, while its model listing gives $8 for both prompt and completion. OpenAI publishes no context window; the frontmatter's 400,000 and 360,000 are OpenRouter's.

## Strengths
- Artificial Analysis (read 2026-11-01), GPT Image 2.5 Flare (max): second on AA-Image-T2I v2.1 at Elo 1207 (95% interval 1197 to 1217, 12,364 samples) and third on AA-Image-Editing v2.1 at 1182.
- Ahead of GPT Image 2 (1186) at the same token rates.
- Transparent backgrounds and up to 16 reference images (OpenRouter).

## Limitations
- 15 Elo points behind Sunburst on text-to-image and 17 on editing.
- Artificial Analysis prices its max setting at $210.7 per 1,000 images, the same as Sunburst.
- Token use differs by model and quality setting, so equal rates do not mean equal cost per image.
- Build-tier limits of 20 images and 250,000 tokens per minute.

## Good for
- High-volume everyday image generation.
- Rapid prototyping and creator content.
