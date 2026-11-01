---
id: openai/dall-e-3
name: DALL·E 3
owned_by: openai
type: image
description: DALL·E 3 was OpenAI's text-to-image model in the Images API from November 2023, with standard and HD quality and wide or tall sizes, shut down on 12 May 2026.
aliases: [dall-e-3, aiml/dall-e-3]
architecture:
  input_modalities: [text]
  output_modalities: [image]
open_weights: false
license: proprietary
release_date: "2023-11-06"
sources:
  - https://developers.openai.com/api/docs/models/dall-e-3
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://openrouter.ai/api/v1/models
  - https://web.archive.org/web/20231231174614/https://openai.com/blog/new-models-and-developer-products-announced-at-devday
  - https://web.archive.org/web/20240302001121/https://openai.com/pricing
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# DALL·E 3

## Overview
Shut down: OpenAI told developers on 14 November 2025 that `dall-e-3` was deprecated and removed it from the API on 12 May 2026, recommending `gpt-image-2`, `gpt-image-1` or `gpt-image-1-mini`; its model page now points to GPT-Image-2.5 Sunburst. OpenRouter does not list it; the id is OpenAI's API id. OpenAI brought DALL·E 3 to the Images API at DevDay on 6 November 2023, after launching it to ChatGPT Plus and Enterprise users, with built-in moderation and a choice of formats and quality levels. It took a text prompt and returned an image through `v1/images/generations` only; OpenAI's model page lists no edits endpoint. OpenAI's March 2024 price list charged $0.040 per standard 1024×1024 image and $0.080 at 1024×1792 or 1792×1024, and $0.080 and $0.120 for the same sizes in HD.

## Strengths
- OpenAI's pricing page called it the highest-quality DALL·E model at the time.
- Wide and tall formats as well as square, and an HD quality setting.
- Built-in moderation, as with DALL·E 2.
- Used by Snap, Coca-Cola and Shutterstock for programmatic image and design generation, per OpenAI's DevDay post.

## Limitations
- Shut down; `dall-e-3` requests no longer succeed on OpenAI's API.
- Generation only: no edits, inpainting or image input.
- Twice DALL·E 2's price for a standard square image, and up to $0.120 per HD image.

## Good for
- Recognising the id in old code and logs and mapping it to a current GPT Image model.
- Historical comparison with the GPT Image models that replaced it.
