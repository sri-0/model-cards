---
id: openai/sora-2
name: Sora 2
owned_by: openai
type: video
description: Sora 2 was OpenAI's speed-oriented video generation model with synced audio on the Videos API, released at DevDay 2025 and shut down with that API on 2026-09-24.
aliases: [sora-2, sora-2-2025-12-08, sora-2-2025-10-06, azure/sora-2]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [video, audio]
open_weights: false
license: proprietary
release_date: "2025-10-06"
sources:
  - https://developers.openai.com/api/docs/models/sora-2
  - https://developers.openai.com/api/docs/guides/video-generation
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://openrouter.ai/api/v1/models?output_modalities=video
  - https://artificialanalysis.ai/video/leaderboard/text-to-video
  - https://artificialanalysis.ai/video/leaderboard/image-to-video
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Sora 2

## Overview
OpenAI launched the Videos API (/v1/videos) with Sora 2 and Sora 2 Pro at DevDay on 2025-10-06 (OpenAI changelog). OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix. OpenAI announced the deprecation on 2026-03-24 and shut down the Sora 2 models and the Videos API on 2026-09-24, with no one-to-one replacement; the docs remain for reference. OpenAI described Sora 2 as a media generation model that turns natural language or images into video with synced audio, designed for speed and flexibility in exploration, rough cuts and social content. Snapshots were sora-2-2025-10-06 and sora-2-2025-12-08, the default from 2026-01-13. It rendered 1280x720 or 720x1280 at $0.10 per second of video. Jobs were asynchronous: create, poll or receive a webhook, then download the MP4. From 2026-03-12 it gained 16- and 20-second clips, reusable character references, video extensions and Batch support.

## Strengths
- Synced audio generated with the video.
- An image input can set the first frame.
- A third of Sora 2 Pro's price at the same 720p sizes.
- Characters kept non-human subjects consistent across clips.

## Limitations
- Shut down on OpenAI's API; no current OpenAI route.
- 720p only; 1080p and 1792x1024 needed Sora 2 Pro.
- Rejected real people, copyrighted characters and music, input images with human faces, and content unsuitable for under-18 audiences.
- Renders could take several minutes; Build tier allowed 50 requests per minute.
- Artificial Analysis's AA-Video-T2V v2.1 and AA-Video-I2V v2.1 boards (read 2026-11-01) do not list it.

## Good for
- Interpreting archived Sora 2 jobs and prices.
- Planning a migration away from the Videos API.
