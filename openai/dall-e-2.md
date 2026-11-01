---
id: openai/dall-e-2
name: DALL·E 2
owned_by: openai
type: image
description: DALL·E 2 was OpenAI's second-generation image model, offered in the Images API from November 2022 for generation, masked edits and variations, and shut down on 12 May 2026.
aliases: [dall-e-2, aiml/dall-e-2]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
open_weights: false
license: proprietary
release_date: "2022-11-03"
sources:
  - https://developers.openai.com/api/docs/models/dall-e-2
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://openrouter.ai/api/v1/models
  - https://web.archive.org/web/20231226102905/https://openai.com/blog/dall-e-api-now-available-in-public-beta/
  - https://web.archive.org/web/20230603183535/https://platform.openai.com/docs/models/gpt-3
  - https://web.archive.org/web/20240302001121/https://openai.com/pricing
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# DALL·E 2

## Overview
Shut down: OpenAI told developers on 14 November 2025 that `dall-e-2` was deprecated and removed it from the API on 12 May 2026, recommending `gpt-image-2`, `gpt-image-1` or `gpt-image-1-mini`; its model page now points to GPT-Image-2.5 Sunburst. OpenRouter does not list it; the id is OpenAI's API id. The DALL·E API opened to all API customers in public beta on 3 November 2022. OpenAI's 2023 model docs called it the second iteration of DALL·E, with more realistic and accurate images at four times the resolution of the original, able to create an image from a prompt, edit an existing image or make variations of an uploaded one. It served `v1/images/generations` and `v1/images/edits` with mask-based inpainting. OpenAI's model page lists text as the only input modality; edits and variations also take an image. OpenAI's March 2024 price list charged $0.020 per 1024×1024 image, $0.018 at 512×512 and $0.016 at 256×256.

## Strengths
- Generation, masked editing and variations from one model.
- The lower-cost option of its time: OpenAI's pricing page said DALL·E 2 was optimised for cost, while DALL·E 3 started at $0.040 per image.
- Built-in moderation, including filters for hate symbols and gore, per the launch post.

## Limitations
- Shut down; `dall-e-2` requests no longer succeed on OpenAI's API.
- Only the three square sizes on OpenAI's price list, up to 1024×1024.
- OpenAI described DALL·E 3 as the higher-quality model.

## Good for
- Recognising the id in old code and logs and mapping it to a current GPT Image model.
- Historical comparison with OpenAI's later image models.
