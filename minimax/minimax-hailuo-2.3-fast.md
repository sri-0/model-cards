---
id: minimax/minimax-hailuo-2.3-fast
name: MiniMax Hailuo 2.3 Fast
owned_by: minimax
type: video
description: MiniMax Hailuo 2.3 Fast is the image-to-video-only fast variant of Hailuo 2.3 on MiniMax's legacy V1 video API, animating a first frame into a silent 768p (6 or 10 s) or 1080p (6 s) clip at a lower per-clip price.
aliases: [MiniMax-Hailuo-2.3-Fast]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [video]
open_weights: false
license: proprietary
release_date: "2025-10-28"
sources:
  - https://platform.minimax.io/docs/guides/models-intro
  - https://platform.minimax.io/docs/faq/models
  - https://platform.minimax.io/docs/release-notes/models
  - https://platform.minimax.io/docs/release-notes/apis
  - https://platform.minimax.io/docs/api-reference/video-generation-i2v
  - https://platform.minimax.io/docs/pricing/overview
  - https://www.minimax.io/news/minimax-hailuo-23
  - https://hailuoai.video/pages/blog/introducing-hailuo-2-3-ai-video-generator
  - https://openrouter.ai/api/v1/models?output_modalities=video
  - https://artificialanalysis.ai/video/leaderboard/image-to-video
retrieved: "2026-11-01"
---

# MiniMax Hailuo 2.3 Fast

## Overview
`MiniMax-Hailuo-2.3-Fast` was added to MiniMax's video API on 2025-10-28 with Hailuo 2.3. OpenRouter does not list it, so the id is the API id lower-cased under the `minimax/` prefix. Only the image-to-video request (`POST /v1/video_generation` with `first_frame_image`) accepts it; there is no text-to-video or first-and-last-frame mode. Output is 768p at 6 or 10 seconds or 1080p at 6 seconds, 24 fps, without audio. The first frame is a JPG, PNG or WebP under 20 MB with a short edge over 300 px and a 2:5 to 5:2 ratio; the optional prompt is capped at 2,000 characters and takes the same 15 bracketed camera commands as Hailuo 2.3, with `prompt_optimizer` on by default and `fast_pretreatment` available. Pay-as-you-go pricing is per clip: $0.19 (768p, 6 s), $0.32 (768p, 10 s) and $0.33 (1080p, 6 s), against $0.28, $0.56 and $0.49 for Hailuo 2.3; video packages deduct 0.7, 1.1 and 1.3 points. MiniMax's launch post says it generates faster at a lower price and cuts batch-creation cost by up to 50%; the Hailuo blog pitches it for rapid image-to-video production such as social content and A/B tests. MiniMax now lists it among legacy models behind H3.

## Strengths
- The cheapest MiniMax route to a 1080p clip ($0.33 for 6 s).
- Covered by prepaid video packages, unlike the H3 family.
- Same camera-command syntax and image limits as Hailuo 2.3.

## Limitations
- Image-to-video only; a first frame is mandatory.
- No audio, no reference inputs, and 10-second clips at 768p only.
- Not on Artificial Analysis's AA-Video-I2V v2.1 board (read 2026-11-01).
- Legacy status; MiniMax points new work to H3.

## Good for
- Bulk animation of product shots or stills where cost per clip matters.
- Quick motion tests before paying for Hailuo 2.3 or H3.
