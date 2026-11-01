---
id: minimax/minimax-hailuo-02
name: MiniMax Hailuo 02
owned_by: minimax
type: video
description: MiniMax Hailuo 02 is MiniMax's June 2025 video model on the legacy V1 API, the only Hailuo model with 512p image-to-video and first-and-last-frame generation, producing silent 6 or 10 second clips up to 1080p.
aliases: [MiniMax-Hailuo-02]
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [video]
open_weights: false
license: proprietary
release_date: "2025-06-18"
sources:
  - https://platform.minimax.io/docs/guides/models-intro
  - https://platform.minimax.io/docs/faq/models
  - https://platform.minimax.io/docs/release-notes/models
  - https://platform.minimax.io/docs/release-notes/apis
  - https://platform.minimax.io/docs/api-reference/video-generation-t2v
  - https://platform.minimax.io/docs/api-reference/video-generation-i2v
  - https://platform.minimax.io/docs/api-reference/video-generation-fl2v
  - https://platform.minimax.io/docs/pricing/overview
  - https://platform.minimax.io/docs/guides/rate-limits
  - https://www.minimax.io/news/minimax-hailuo-02
  - https://openrouter.ai/api/v1/models?output_modalities=video
  - https://artificialanalysis.ai/video/leaderboard/text-to-video
  - https://artificialanalysis.ai/video/leaderboard/image-to-video
retrieved: "2026-11-01"
---

# MiniMax Hailuo 02

## Overview
`MiniMax-Hailuo-02` was released on 2025-06-18 as the successor to Hailuo Video 01. OpenRouter does not list it, so the id is the API id lower-cased under the `minimax/` prefix. MiniMax's launch post describes a Noise-aware Compute Redistribution (NCR) architecture that is 2.5 times as efficient in training and inference at comparable scale, three times the parameters of its predecessor and four times the training data, and says an early version placed second on the Artificial Analysis Video Arena (no score given). It runs on the V1 endpoint (`POST /v1/video_generation`) in three modes: text-to-video at 768p (6 or 10 s) or 1080p (6 s); first-frame image-to-video, which since 2025-08-02 also offers 512p at 6 or 10 s; and first-and-last-frame generation at 768p or 1080p, which no other V1 model offers. Output is 24 fps without audio; prompts are capped at 2,000 characters and accept 15 bracketed camera commands. Pay-as-you-go pricing is per clip: $0.10 (512p, 6 s), $0.15 (512p, 10 s), $0.28 (768p, 6 s), $0.56 (768p, 10 s) and $0.49 (1080p, 6 s); video packages deduct 0.3 to 2 points. MiniMax now lists it among legacy models behind H3.

## Strengths
- The cheapest MiniMax video at $0.10 for a 512p, 6-second clip.
- Start-and-end-frame generation, which Hailuo 2.3 lacks.
- Explicit camera commands and a default prompt optimiser with a fast-pretreatment option.

## Limitations
- No audio and no reference inputs; 10-second clips are 512p or 768p only, and 512p is image-to-video only.
- Not on Artificial Analysis's AA-Video-T2V v2.1 or AA-Video-I2V v2.1 boards (read 2026-11-01), so the second-place claim cannot be checked today.
- Superseded twice (Hailuo 2.3, then H3); the V1 Hailuo series is limited to 20 requests per minute.

## Good for
- Low-cost 512p drafts and transitions between two keyframes.
- Existing V1 integrations that depend on the first-and-last-frame endpoint.
