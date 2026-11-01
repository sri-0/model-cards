---
id: minimax/hailuo-2.3
name: MiniMax Hailuo 2.3
owned_by: minimax
type: video
description: MiniMax Hailuo 2.3 is MiniMax's legacy V1 video model, built on Hailuo 02, for silent text-to-video and image-to-video at 768p (6 or 10 s) or 1080p (6 s) with bracketed camera commands.
aliases: [MiniMax-Hailuo-2.3, hailuo-2.3]
capabilities: [vision]
supported_parameters: [max_tokens, temperature, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [video]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2025-10-28"
sources:
  - https://platform.minimax.io/docs/guides/models-intro
  - https://platform.minimax.io/docs/faq/models
  - https://platform.minimax.io/docs/release-notes/models
  - https://platform.minimax.io/docs/release-notes/apis
  - https://platform.minimax.io/docs/api-reference/video-generation-t2v
  - https://platform.minimax.io/docs/api-reference/video-generation-i2v
  - https://platform.minimax.io/docs/pricing/overview
  - https://platform.minimax.io/docs/guides/rate-limits
  - https://www.minimax.io/news/minimax-hailuo-23
  - https://hailuoai.video/pages/blog/introducing-hailuo-2-3-ai-video-generator
  - https://openrouter.ai/minimax/hailuo-2.3
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://artificialanalysis.ai/video/leaderboard/text-to-video
  - https://artificialanalysis.ai/video/leaderboard/image-to-video
retrieved: "2026-11-01"
---

# MiniMax Hailuo 2.3

## Overview
`MiniMax-Hailuo-2.3` was added to MiniMax's video API on 2025-10-28 alongside the image-to-video-only Hailuo 2.3 Fast. The id is OpenRouter's (listed 2026-04-20). MiniMax now files it under legacy models behind H3 but still serves it on the V1 endpoint (`POST /v1/video_generation`) for text-to-video and first-frame image-to-video. Output is 768p at 6 or 10 seconds or 1080p at 6 seconds, 24 fps, without audio. Prompts are capped at 2,000 characters and accept 15 bracketed camera commands such as `[Pan left]` or `[Static shot]`; `prompt_optimizer` is on by default and `fast_pretreatment` shortens it. First frames are JPG, PNG or WebP under 20 MB, short edge over 300 px, ratio 2:5 to 5:2. Pay-as-you-go pricing is per clip: $0.28 (768p, 6 s), $0.56 (768p, 10 s) and $0.49 (1080p, 6 s), the same as Hailuo 02; video packages deduct 1, 2 and 2 points. MiniMax's launch post claims gains over Hailuo 02 in body movement, lighting, stylised output (anime, illustration, ink wash, game CG), micro-expressions and object motion.

## Strengths
- Explicit camera control, with up to three moves combined in one bracket.
- 1080p at the Hailuo 02 price.
- Covered by prepaid video packages, unlike the H3 family.

## Limitations
- No audio, no reference inputs and no first-and-last-frame mode (that endpoint takes only Hailuo 02).
- 10-second clips are 768p only; the V1 Hailuo series is limited to 20 requests per minute.
- Not on Artificial Analysis's AA-Video-T2V v2.1 or AA-Video-I2V v2.1 boards (read 2026-11-01).
- Legacy status; MiniMax points new work to H3.

## Good for
- Silent 6-10 second shots with scripted camera moves.
- Existing V1 integrations moving up from Hailuo 02.
