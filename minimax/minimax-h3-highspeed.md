---
id: minimax/minimax-h3-highspeed
name: MiniMax H3 Highspeed
owned_by: minimax
type: video
description: MiniMax H3 Highspeed is the quality-and-speed balanced variant of MiniMax H3 on the V2 video API, generating 4-15 second clips at 480p or 768p from text, keyframes or image, video and audio references for $0.04-0.06 per second.
aliases: [MiniMax-H3-Highspeed]
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

# MiniMax H3 Highspeed

## Overview
`MiniMax-H3-Highspeed` is one of four `model` values on MiniMax's V2 video endpoint (`POST /v2/video_generation`), described there as balancing generation quality and speed and on the pricing page as meant for everyday content creation. OpenRouter does not list it, so the id is the API id lower-cased under the `minimax/` prefix. MiniMax's model list and release notes name H3 and H3 Max but not this variant, so there is no release date or technical description. Requests take the H3 shape: text-to-video (a concrete ratio is required), image-to-video with a first and/or last frame, or reference-to-video with up to 9 images, 3 video clips and 3 audio clips, a 7,000-character prompt and a 64 MB request body. Output is 480p or 768p for 4-15 seconds; 2K is reserved for H3. Pay-as-you-go pricing is $0.06 per output second at 768p and $0.04 at 480p; input video is billed at the same rate, the first five input images are free and further ones cost $0.03 each, and audio input is free. No weights are published; the open H3 release covers H3-Base only.

## Strengths
- 25% cheaper per second than H3 at 768p, with a 480p tier.
- The full H3 input set, including reference video and audio.
- Same asynchronous task, query, list and cancel endpoints as H3.

## Limitations
- No 2K output; MiniMax's 2K regeneration only accepts H3's 768p output.
- MiniMax does not say whether it generates audio as H3 does.
- Not on Artificial Analysis's video leaderboards (read 2026-11-01), so there is no independent quality score.
- Absent from MiniMax's model list and release notes; lifecycle undocumented. Pay-as-you-go only.

## Good for
- Iterating on prompts and references before a final H3 render.
- Volume generation at 768p where cost matters more than peak quality.
