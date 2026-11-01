---
id: openai/sora-2-pro
name: Sora 2 Pro
owned_by: openai
type: video
description: Sora 2 Pro was OpenAI's highest-quality video generation model with synced audio on the Videos API, offering up to 1080p, released at DevDay 2025 and shut down on 2026-09-24.
aliases: [sora-2-pro, sora-2-pro-2025-10-06, azure/sora-2-pro]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [video, audio]
open_weights: false
license: proprietary
release_date: "2025-10-06"
sources:
  - https://developers.openai.com/api/docs/models/sora-2-pro
  - https://developers.openai.com/api/docs/guides/video-generation
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://openrouter.ai/api/v1/models?output_modalities=video
  - https://artificialanalysis.ai/video/leaderboard/text-to-video
  - https://artificialanalysis.ai/video/leaderboard/image-to-video
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Sora 2 Pro

## Overview
OpenAI launched the Videos API (/v1/videos) with Sora 2 and Sora 2 Pro at DevDay on 2025-10-06 (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. OpenAI announced the deprecation on 2026-03-24 and shut down the Sora 2 models and the Videos API on 2026-09-24, with no one-to-one replacement; the docs remain for reference. OpenAI called Sora 2 Pro its most advanced media generation model, producing richly detailed clips with synced audio from natural language or images, slower and dearer than Sora 2 but more polished and stable for cinematic footage and marketing assets. Its only dated snapshot was sora-2-pro-2025-10-06. Prices per second of video were $0.30 at 1280x720 or 720x1280, $0.50 at 1792x1024 or 1024x1792 and $0.70 at 1920x1080 or 1080x1920, the last added on 2026-03-12 with 16- and 20-second clips, character references, video extensions and Batch support. Jobs were asynchronous: create, poll or receive a webhook, then download the MP4.

## Strengths
- The only Sora model with 1080p output.
- Synced audio and image-guided first frames.
- Reusable character references for consistent non-human subjects.

## Limitations
- Shut down on OpenAI's API; no current OpenAI route.
- Three times Sora 2's price at 720p ($0.30 against $0.10 per second) and longer render times.
- Rejected real people, copyrighted characters and music, input images with human faces, and content unsuitable for under-18 audiences.
- Build tier allowed 25 requests per minute.
- Artificial Analysis's AA-Video-T2V v2.1 and AA-Video-I2V v2.1 boards (read 2026-11-01) do not list it.

## Good for
- Interpreting archived Sora 2 Pro jobs and prices.
- Planning a migration away from the Videos API.
