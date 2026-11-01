---
id: minimax/minimax-h3-lite
name: MiniMax H3 Lite
owned_by: minimax
type: video
description: MiniMax H3 Lite is the lightweight, lowest-cost variant of MiniMax H3 on the V2 video API, generating 4-15 second clips at 480p or 768p from text, keyframes or image, video and audio references for $0.025-0.04 per second.
aliases: [MiniMax-H3-Lite]
capabilities: [vision]
architecture:
  input_modalities: [text, image, video, audio]
  output_modalities: [video]
open_weights: false
license: proprietary
sources:
  - https://platform.minimax.io/docs/api-reference/video-generation-v2-create
  - https://platform.minimax.io/docs/pricing/overview
  - https://platform.minimax.io/docs/faq/models
  - https://platform.minimax.io/docs/release-notes/models
  - https://platform.minimax.io/docs/guides/video-generation
  - https://platform.minimax.io/docs/guides/local-deploy-h3
  - https://openrouter.ai/api/v1/models?output_modalities=video
  - https://artificialanalysis.ai/video/leaderboard/text-to-video
  - https://artificialanalysis.ai/video/leaderboard/image-to-video
retrieved: "2026-11-01"
---

# MiniMax H3 Lite

## Overview
`MiniMax-H3-Lite` is the cheapest of the four `model` values on MiniMax's V2 video endpoint (`POST /v2/video_generation`), described there as the lightweight variant and on the pricing page as meant for creative exploration and batch generation. OpenRouter does not list it, so the id is the API id lower-cased under the `minimax/` prefix. Like H3 Highspeed, it is absent from MiniMax's model list and release notes, so there is no release date or technical description. It accepts text-to-video, image-to-video with a first and/or last frame, and reference-to-video with up to 9 images, 3 video clips and 3 audio clips, with a 7,000-character prompt limit. One documented difference: for reference-to-video it does not yet accept the `adaptive` ratio, so a concrete ratio must be given. Output is 480p or 768p for 4-15 seconds; 2K is reserved for H3. Pay-as-you-go pricing is $0.04 per output second at 768p and $0.025 at 480p; input video is billed at the same rate, the first five input images are free and further ones cost $0.02 each, and audio input is free. No weights are published; the open H3 release covers H3-Base only.

## Strengths
- Half H3's per-second price at 768p and the lowest H3-family rate at 480p.
- The full H3 input set, including reference video and audio.
- Same asynchronous task, query, list and cancel endpoints as H3.

## Limitations
- No 2K output, and no `adaptive` ratio for reference-to-video.
- MiniMax does not say whether it generates audio as H3 does.
- Not on Artificial Analysis's video leaderboards (read 2026-11-01), so there is no independent quality score.
- Absent from MiniMax's model list and release notes; lifecycle undocumented. Pay-as-you-go only.

## Good for
- Cheap previews and storyboard animatics at 480p.
- High-volume 768p clips where the budget rules out H3.
